#!/usr/bin/env python3
"""
Test script for the SmartLiveEngine integration.

Tests:
1. SmartLiveEngine initialization
2. Discussion phase tracking
3. Competency coverage tracking
4. Smart speaker selection
5. Evidence-based analysis generation

Run from project root:
    python pressure_cooker/scripts/test_smart_live_engine.py
"""

import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from clients.llm_client import MockLLMClient
from utils.models import ScenarioConfig
from step2.case_data import CaseStudy, CaseDataItem
from step2.live_engine import SmartLiveEngine, LiveEngine
from step2.models import SessionState


def create_test_scenario() -> ScenarioConfig:
    """Create a test scenario config."""
    return ScenarioConfig(
        id="test_techflow",
        name="TechFlow Case Study",
        description="B2B SaaS profitability analysis",
        context="TechFlow is a B2B SaaS company with $12M ARR facing declining margins.",
        conflict_point="The team needs to identify ways to improve profitability.",
        provoker_goal="Challenge assumptions and demand data-backed reasoning.",
        mediator_goal="Support the candidate while advancing the discussion.",
        escalation_triggers=["Surface-level analysis", "Ignoring data"],
        resolution_paths=["Data-driven recommendation", "Clear implementation plan"],
        min_turns=10,
    )


def create_test_case_study() -> CaseStudy:
    """Create a test case study."""
    return CaseStudy(
        id="techflow",
        company_name="TechFlow",
        industry="B2B SaaS",
        problem_statement="$12M ARR company facing declining margins. How to improve profitability by 5 percentage points?",
        data_items=[
            CaseDataItem(
                category="costs",
                label="Cost Structure",
                detail="Engineering 37%, Sales & Marketing 32%, Customer Success 18%, G&A 13%",
                keywords=["cost", "expense", "spending", "opex", "cogs"],
            ),
            CaseDataItem(
                category="customer_segments",
                label="Customer Segments",
                detail="Enterprise (50 accounts, $150K ACV, 95% retention), Mid-market (200 accounts, $25K ACV, 85% retention), SMB (800 accounts, $3K ACV, 65% retention)",
                keywords=["customer", "segment", "enterprise", "smb", "mid-market"],
            ),
            CaseDataItem(
                category="unit_economics",
                label="Unit Economics",
                detail="Enterprise LTV:CAC 10x, Mid-market 4.2x, SMB 2.6x. Enterprise CAC payback 3.6 months, SMB 8 months.",
                keywords=["ltv", "cac", "unit economics", "payback", "ratio"],
            ),
        ],
    )


async def test_smart_engine_init():
    """Test SmartLiveEngine initialization."""
    print("\n" + "=" * 60)
    print("TEST: SmartLiveEngine Initialization")
    print("=" * 60)

    client = MockLLMClient()
    scenario = create_test_scenario()
    case_study = create_test_case_study()

    # Create smart engine
    engine = SmartLiveEngine(
        client=client,
        scenario=scenario,
        participant_name="Jin",
        case_study=case_study,
        use_smart_agents=True,
    )

    print("\n--- Engine State ---")
    print(f"  Session ID: {engine.session_id}")
    print(f"  State: {engine.state.value}")
    print(f"  Participant: {engine.participant_name}")
    print(f"  Use smart agents: {engine.use_smart_agents}")

    print("\n--- Smart Agents ---")
    from agents.smart_agents import SmartProvokerAgent, ActiveMediatorAgent, SmartSystemManager
    print(f"  Provoker type: {type(engine.provoker).__name__}")
    print(f"  Mediator type: {type(engine.mediator).__name__}")
    print(f"  System Manager type: {type(engine.system_manager).__name__}")

    assert isinstance(engine.provoker, SmartProvokerAgent), "Provoker should be SmartProvokerAgent"
    assert isinstance(engine.mediator, ActiveMediatorAgent), "Mediator should be ActiveMediatorAgent"

    print("\n--- Discussion Context ---")
    print(f"  Phase: {engine.get_discussion_phase()}")
    print(f"  Guidance: {engine.get_phase_guidance()}")

    print("\n✓ SmartLiveEngine initialized successfully")
    return engine


async def test_opening_and_turns(engine: SmartLiveEngine):
    """Test opening generation and turn submission."""
    print("\n" + "=" * 60)
    print("TEST: Opening and Turn Submission")
    print("=" * 60)

    # Generate opening
    print("\n--- Generating Opening ---")
    opening_turns = await engine.generate_opening()
    print(f"  Opening turns: {len(opening_turns)}")
    for turn in opening_turns:
        print(f"    [{turn.speaker_name}]: {turn.content[:60]}...")

    print(f"\n  State after opening: {engine.state.value}")
    print(f"  Phase: {engine.get_discussion_phase()}")

    # Submit human turn
    print("\n--- Submitting Human Turn ---")
    human_response = "Let me structure this using a profitability framework. First, I'd like to understand the cost breakdown - can we see the costs?"

    turn = engine.submit_human_turn(human_response)
    print(f"  Turn {turn.turn_number}: {turn.content[:60]}...")
    print(f"  Phase after: {engine.get_discussion_phase()}")
    print(f"  Revealed categories: {engine.revealed_categories}")

    # Check competency detection
    coverage = engine.get_competency_coverage()
    print("\n--- Competency Coverage ---")
    for name, data in coverage.items():
        if data['tested'] > 0:
            print(f"  ✓ {name}: {data['tested']}/{data['total']}")

    print("\n✓ Opening and turn submission working")
    return engine


async def test_ai_turn_generation(engine: SmartLiveEngine):
    """Test AI turn generation with smart agents."""
    print("\n" + "=" * 60)
    print("TEST: AI Turn Generation")
    print("=" * 60)

    print("\n--- Generating AI Response ---")
    ai_turns = await engine.generate_ai_turns_until_human()

    print(f"  AI turns generated: {len(ai_turns)}")
    for turn in ai_turns:
        print(f"    [{turn.speaker_name}]: {turn.content[:60]}...")

    print(f"\n  Phase: {engine.get_discussion_phase()}")
    print(f"  Total turns: {len(engine.turns)}")

    # Check targeting info
    targeting = engine.get_targeting_info()
    if targeting:
        print("\n--- Provoker Targeting ---")
        print(f"  Target competency: {targeting.get('target_competency')}")
        print(f"  Target behavior: {targeting.get('target_behavior')}")
        print(f"  Phase: {targeting.get('phase')}")

    print("\n✓ AI turn generation working")
    return engine


async def test_multi_turn_flow(engine: SmartLiveEngine):
    """Test multiple turns and phase advancement."""
    print("\n" + "=" * 60)
    print("TEST: Multi-Turn Flow")
    print("=" * 60)

    # Simulate a few more turns
    human_turns = [
        "I understand Jordan's concern. Let me refine - could we see customer segments by revenue contribution?",
        "I hypothesize we have a customer mix problem. The SMB segment seems to be consuming too many resources. What's the LTV:CAC by segment?",
        "Based on the data, I'd recommend focusing on Enterprise and Mid-market while restructuring SMB pricing.",
    ]

    print("\n--- Simulating Multi-Turn Discussion ---")

    for i, human_content in enumerate(human_turns):
        print(f"\n  Turn {i+1}:")

        # Human turn
        turn = engine.submit_human_turn(human_content)
        print(f"    [Jin]: {turn.content[:50]}...")

        # AI response
        ai_turns = await engine.generate_ai_turns_until_human()
        for at in ai_turns:
            print(f"    [{at.speaker_name}]: {at.content[:50]}...")

        # Phase status
        print(f"    Phase: {engine.get_discussion_phase()}")

    # Final coverage
    print("\n--- Final Competency Coverage ---")
    coverage = engine.get_competency_coverage()
    total_tested = sum(d['tested'] for d in coverage.values())
    total_behaviors = sum(d['total'] for d in coverage.values())
    print(f"  Overall: {total_tested}/{total_behaviors} behaviors observed")
    for name, data in coverage.items():
        status = "✓" if data['coverage'] >= 0.5 else "○"
        print(f"  {status} {name}: {data['tested']}/{data['total']} ({data['coverage']*100:.0f}%)")

    print("\n✓ Multi-turn flow working")
    return engine


async def test_state_persistence(engine: SmartLiveEngine):
    """Test state serialization and restoration."""
    print("\n" + "=" * 60)
    print("TEST: State Persistence")
    print("=" * 60)

    # Serialize state
    print("\n--- Serializing State ---")
    state = engine.to_state_dict()
    print(f"  Keys: {list(state.keys())}")
    print(f"  Turns: {len(state['turns'])}")
    print(f"  Discussion context: {list(state.get('discussion_context', {}).keys())}")
    print(f"  Competency coverage: {list(state.get('competency_coverage', {}).keys())}")

    # Create new engine and restore
    print("\n--- Restoring State ---")
    client = MockLLMClient()
    scenario = create_test_scenario()
    case_study = create_test_case_study()

    new_engine = SmartLiveEngine(
        client=client,
        scenario=scenario,
        participant_name="Jin",
        case_study=case_study,
    )

    new_engine.restore_from_state(state)

    print(f"  Restored turns: {len(new_engine.turns)}")
    print(f"  Restored phase: {new_engine.get_discussion_phase()}")
    print(f"  Restored state: {new_engine.state.value}")

    # Verify
    assert len(new_engine.turns) == len(engine.turns), "Turn count mismatch"
    assert new_engine.get_discussion_phase() == engine.get_discussion_phase(), "Phase mismatch"

    print("\n✓ State persistence working")


async def test_session_finalization():
    """Test session finalization with evidence-based analysis."""
    print("\n" + "=" * 60)
    print("TEST: Session Finalization")
    print("=" * 60)

    client = MockLLMClient()
    scenario = create_test_scenario()
    case_study = create_test_case_study()

    engine = SmartLiveEngine(
        client=client,
        scenario=scenario,
        participant_name="Jin",
        case_study=case_study,
    )

    # Quick session
    await engine.generate_opening()
    engine.submit_human_turn("Let me analyze the cost structure. Can we see the costs breakdown?")
    await engine.generate_ai_turns_until_human()
    engine.submit_human_turn("I recommend focusing on Enterprise segment given the superior unit economics.")
    await engine.generate_ai_turns_until_human()

    # Finalize
    print("\n--- Finalizing Session ---")
    output = await engine.finalize_session_output("P999")

    print(f"  Session ID: {output.metadata.session_id}")
    print(f"  Total turns: {output.metadata.total_turns}")
    print(f"  Duration: {output.metadata.duration_seconds:.1f}s")

    print("\n--- Intent Statistics ---")
    if output.intent_statistics:
        print(f"  Total candidate turns: {output.intent_statistics.total_turns}")
        print(f"  Dominant intent: {output.intent_statistics.dominant_intent}")

    print("\n--- Assessment Mapping ---")
    if output.assessment_mapping:
        print(f"  Collaboration: {output.assessment_mapping.collaboration_score:.3f}")
        print(f"  Leadership: {output.assessment_mapping.leadership_score:.3f}")
        print(f"  Problem Solving: {output.assessment_mapping.problem_solving_score:.3f}")

    print("\n--- Evidence Assessment ---")
    evidence = engine.get_evidence_assessment()
    if evidence:
        print(f"  Turns analyzed: {evidence.total_turns_analyzed}")
        print(f"  Competency scores: {len(evidence.competency_scores)}")
    else:
        print("  (Evidence analysis not generated - requires real LLM)")

    print("\n✓ Session finalization working")


async def test_backwards_compatibility():
    """Test that original LiveEngine still works."""
    print("\n" + "=" * 60)
    print("TEST: Backwards Compatibility (Original LiveEngine)")
    print("=" * 60)

    client = MockLLMClient()
    scenario = create_test_scenario()
    case_study = create_test_case_study()

    # Use original engine
    engine = LiveEngine(
        client=client,
        scenario=scenario,
        participant_name="Jin",
        case_study=case_study,
    )

    print("\n--- Original Engine ---")
    print(f"  Type: {type(engine).__name__}")
    print(f"  Provoker type: {type(engine.provoker).__name__}")

    # Basic operations
    await engine.generate_opening()
    engine.submit_human_turn("What are the costs?")
    await engine.generate_ai_turns_until_human()

    print(f"  Turns: {len(engine.turns)}")
    print(f"  State: {engine.state.value}")

    print("\n✓ Original LiveEngine still works")


async def main():
    """Run all tests."""
    print("=" * 60)
    print("SmartLiveEngine Integration Tests")
    print("=" * 60)

    # Test 1: Initialization
    engine = await test_smart_engine_init()

    # Test 2: Opening and turns
    engine = await test_opening_and_turns(engine)

    # Test 3: AI generation
    engine = await test_ai_turn_generation(engine)

    # Test 4: Multi-turn flow
    engine = await test_multi_turn_flow(engine)

    # Test 5: State persistence
    await test_state_persistence(engine)

    # Test 6: Session finalization
    await test_session_finalization()

    # Test 7: Backwards compatibility
    await test_backwards_compatibility()

    print("\n" + "=" * 60)
    print("All SmartLiveEngine tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
