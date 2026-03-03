"""
Live Demo: AI Candidate through Streamlit UI.

This script creates a participant and sends AI-generated responses
through the HTTP API, so you can watch the conversation live in Streamlit.

Usage:
    1. Start the backend: uvicorn step2.server:app --port 8000
    2. Start Streamlit: streamlit run step2/ui/app.py
    3. Run this script: python scripts/live_demo.py --persona fluent_expert
    4. Watch the Streamlit UI at http://localhost:8501

The script will:
    - Create a participant
    - Auto-submit consent
    - Auto-complete BFI-44
    - Create a session
    - Send AI-generated responses every few seconds
"""

import argparse
import asyncio
import sys
import time
from pathlib import Path

import httpx

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.test_candidate_agent import AITestCandidate
from clients.llm_client import LLMClient
from config.test_personas import get_test_persona, get_all_test_persona_ids
from step2.consulting_scenarios import get_consulting_scenario
from config.scenarios import SCENARIOS

API_BASE = "http://localhost:8000"
TURN_DELAY = 3  # seconds between AI candidate responses


async def run_live_demo(
    persona_id: str = "fluent_expert",
    scenario_id: str = "techflow",
    max_turns: int = 20,
):
    """Run a live demo with AI candidate through the API."""

    print(f"\n{'='*60}")
    print(f"LIVE DEMO: {persona_id} on {scenario_id}")
    print(f"Watch at: http://localhost:8501")
    print(f"{'='*60}\n")

    persona = get_test_persona(persona_id)
    case_study = get_consulting_scenario(scenario_id)
    scenario_config = SCENARIOS.get("resource_conflict", list(SCENARIOS.values())[0])

    # Create LLM client for AI candidate
    client = LLMClient()

    # Create AI test candidate
    ai_candidate = AITestCandidate(
        client=client,
        scenario=scenario_config,
        persona=persona,
        case_study=case_study,
    )

    async with httpx.AsyncClient(timeout=180.0) as http:
        # 1. Create participant
        print("1. Creating participant...")
        resp = await http.post(
            f"{API_BASE}/participant",
            json={"name": f"AI_{persona.display_name}"}
        )
        resp.raise_for_status()
        data = resp.json()
        pid = data["participant_id"]
        print(f"   Participant ID: {pid}")

        # 2. Submit consent
        print("2. Submitting consent...")
        resp = await http.post(
            f"{API_BASE}/participant/{pid}/consent",
            json={"consent": True}
        )
        resp.raise_for_status()

        # 3. Submit BFI-44 (auto-generate based on persona)
        print("3. Submitting BFI-44...")
        bfi_responses = _generate_bfi44_from_persona(persona)
        resp = await http.post(
            f"{API_BASE}/participant/{pid}/bfi44",
            json={"responses": bfi_responses, "duration_seconds": 120}
        )
        resp.raise_for_status()

        # 4. Create session
        print("4. Creating session...")
        resp = await http.post(
            f"{API_BASE}/session/create",
            json={"participant_id": pid}
        )
        resp.raise_for_status()
        data = resp.json()
        sid = data["session_id"]
        opening = data["opening_messages"]
        print(f"   Session ID: {sid}")

        # Show opening messages
        print("\n--- Opening ---")
        conversation_context = []
        for msg in opening:
            print(f"[{msg['speaker']}]: {msg['content'][:80]}...")
            conversation_context.append(f"[{msg['speaker']}]: {msg['content']}")

        # Wait for user to see the opening in Streamlit
        print(f"\n⏳ Waiting 10 seconds for Streamlit to show opening...")
        print(f"   Open http://localhost:8501 and complete consent/BFI-44 for participant {pid}")
        await asyncio.sleep(10)

        # 5. Send AI responses turn by turn
        print("\n--- Starting AI Candidate Responses ---")
        revealed_categories = set()

        for turn in range(max_turns):
            # Get current session status
            status_resp = await http.get(f"{API_BASE}/session/{sid}/status")
            if status_resp.status_code == 404:
                print("Session not found - may need to create via Streamlit first")
                break
            status_resp.raise_for_status()
            status = status_resp.json()

            if status["state"] == "ended":
                print("\n✅ Session ended")
                break

            # Get last message for context
            conversation = status.get("conversation", [])
            context = ""
            if conversation:
                last = conversation[-1]
                context = f"{last['speaker']} said: '{last['content']}'"

            # Generate AI candidate response
            ai_candidate.update_revealed_categories(revealed_categories)

            # Build context from recent conversation
            full_context = "\n".join(conversation_context[-10:])  # Last 10 messages
            if context:
                full_context += f"\n\nMost recent: {context}"

            response = await ai_candidate.generate_response(full_context)

            print(f"\n[Turn {turn + 1}] [{persona.display_name}]: {response}")

            # Send to API
            try:
                msg_resp = await http.post(
                    f"{API_BASE}/session/{sid}/message",
                    json={"content": response, "target_speaker": None}
                )
                msg_resp.raise_for_status()
                msg_data = msg_resp.json()

                # Add candidate's own message to context
                conversation_context.append(f"[{persona.display_name}]: {response}")

                # Show AI colleague responses
                for ai_turn in msg_data.get("ai_turns", []):
                    print(f"  [{ai_turn['speaker']}]: {ai_turn['content'][:80]}...")
                    # Update conversation context
                    conversation_context.append(f"[{ai_turn['speaker']}]: {ai_turn['content']}")
                    # Track revealed categories from facilitator
                    if ai_turn["speaker"] == "Facilitator":
                        revealed_categories.update(
                            case_study.match_categories(response)
                        )

                if msg_data.get("session_state") == "ended":
                    print("\n✅ Session ended")
                    break

            except httpx.HTTPStatusError as e:
                print(f"  Error: {e.response.text}")
                if "ended" in str(e.response.text).lower():
                    break

            # Wait before next turn
            print(f"  ⏳ Waiting {TURN_DELAY}s...")
            await asyncio.sleep(TURN_DELAY)

        print(f"\n{'='*60}")
        print(f"Demo complete! Check Streamlit for the full conversation.")
        print(f"{'='*60}\n")


def _generate_bfi44_from_persona(persona) -> dict:
    """Generate BFI-44 responses that match the persona's personality vector."""
    import random
    from step2.bfi44 import BFI44_ITEMS

    vector = persona.personality.vector
    responses = {}

    # Map trait codes to persona vector values
    trait_map = {
        "O": vector.openness,
        "C": vector.conscientiousness,
        "E": vector.extraversion,
        "A": vector.agreeableness,
        "N": vector.neuroticism,
    }

    for item in BFI44_ITEMS:
        base_value = trait_map.get(item.trait, 0.5)

        # Convert 0-1 scale to 1-5 Likert
        if item.reverse:
            score = int(5 - (base_value * 4) + 0.5)
        else:
            score = int(1 + (base_value * 4) + 0.5)

        # Add some noise
        noise = random.choice([-1, 0, 0, 0, 1])
        score = max(1, min(5, score + noise))

        responses[str(item.number)] = score

    return responses


async def main():
    parser = argparse.ArgumentParser(description="Run live AI candidate demo")
    parser.add_argument(
        "--persona",
        type=str,
        choices=get_all_test_persona_ids(),
        default="fluent_expert",
        help="Persona to use (default: fluent_expert)",
    )
    parser.add_argument(
        "--scenario",
        type=str,
        default="techflow",
        help="Scenario to use (default: techflow)",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=20,
        help="Maximum turns (default: 20)",
    )

    args = parser.parse_args()
    await run_live_demo(args.persona, args.scenario, args.max_turns)


if __name__ == "__main__":
    asyncio.run(main())
