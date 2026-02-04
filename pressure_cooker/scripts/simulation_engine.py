"""
Simulation Engine for Pressure Cooker Framework.
Orchestrates the multi-agent conversation simulation.
"""

import asyncio
import time
import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from agents.candidate_agent import CandidateAgent
from agents.colleague_agents import ProvokerAgent, MediatorAgent
from agents.system_manager import SystemManagerAgent
from pipeline.statistics import (
    calculate_intent_statistics,
    map_to_assessment,
    classify_all_turns,
)
from utils.models import (
    PersonalityProfile,
    ScenarioConfig,
    Turn,
    SpeakerRole,
    SessionMetadata,
    SessionOutput,
)

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient


class SimulationEngine:
    """
    Main simulation engine that orchestrates multi-agent conversations.

    Manages turn-taking, tension tracking, and conversation flow
    to generate personality-revealing dialogue.
    """

    def __init__(
        self,
        client: "GeminiClient | MockGeminiClient",
        profile: PersonalityProfile,
        scenario: ScenarioConfig,
        turn_limit: Optional[int] = None,
        min_turns: Optional[int] = None,
    ):
        """
        Initialize simulation engine.

        Args:
            client: LLM client for all agents.
            profile: Personality profile for the candidate.
            scenario: Scenario configuration.
            turn_limit: Override scenario turn limit.
            min_turns: Override scenario minimum turns.
        """
        self.client = client
        self.profile = profile
        self.scenario = scenario
        self.turn_limit = turn_limit or scenario.turn_limit
        self.min_turns = min_turns or scenario.min_turns

        # Create agents
        self.candidate = CandidateAgent(
            name="Alex",  # Candidate name
            client=client,
            scenario=scenario,
            profile=profile,
        )

        self.provoker = ProvokerAgent(
            name="Jordan",  # Provoker name
            client=client,
            scenario=scenario,
            aggression_level=0.7,
        )

        self.mediator = MediatorAgent(
            name="Sam",  # Mediator name
            client=client,
            scenario=scenario,
            diplomacy_level=0.7,
        )

        self.system_manager = SystemManagerAgent(
            name="Facilitator",
            client=client,
            scenario=scenario,
        )

        self.agents = {
            "Alex": self.candidate,
            "Jordan": self.provoker,
            "Sam": self.mediator,
            "Facilitator": self.system_manager,
        }

        # Conversation state
        self.turns: list[Turn] = []
        self.tension_history: list[float] = []
        self.session_id = str(uuid.uuid4())[:8]

    async def run(self, verbose: bool = False) -> SessionOutput:
        """
        Run the complete simulation.

        Args:
            verbose: If True, print progress during simulation.

        Returns:
            SessionOutput with complete conversation and analysis.
        """
        start_time = time.time()

        if verbose:
            print(f"\n{'='*60}")
            print(f"Starting simulation: {self.session_id}")
            print(f"Profile: {self.profile.name}")
            print(f"Scenario: {self.scenario.name}")
            print(f"{'='*60}\n")

        # Run conversation loop
        turn_number = 0

        while turn_number < self.turn_limit:
            # Update all agents with current history
            for agent in self.agents.values():
                agent.update_history(self.turns)

            # Get current tension
            if len(self.turns) >= 3:
                tension = await self.system_manager.assess_tension(self.turns)
                self.tension_history.append(tension)
            else:
                tension = 0.3

            # Check for facilitator intervention
            should_intervene, reason = await self.system_manager.should_intervene(self.turns)

            if should_intervene and turn_number > 0:
                # Facilitator speaks
                response = await self.system_manager.generate_response(reason)
                turn = self._create_turn(
                    SpeakerRole.SYSTEM,
                    "Facilitator",
                    response,
                    turn_number,
                    tension,
                )
                self.turns.append(turn)
                turn_number += 1

                if verbose:
                    print(f"[Turn {turn_number}] Facilitator: {response}\n")

                if turn_number >= self.turn_limit:
                    break

            # Determine next speaker (not facilitator)
            available = ["Alex", "Jordan", "Sam"]
            next_speaker = await self.system_manager.decide_next_speaker(
                self.turns,
                available,
            )

            # Generate response
            agent = self.agents[next_speaker]
            context = f"Current tension level: {tension:.1f}"

            if isinstance(agent, CandidateAgent):
                response = await agent.generate_response(context)
            else:
                response = await agent.generate_response(context, tension)

            # Create and store turn
            turn = self._create_turn(
                agent.role,
                next_speaker,
                response,
                turn_number,
                tension,
            )
            self.turns.append(turn)
            turn_number += 1

            if verbose:
                role_label = agent.role.value.upper()
                print(f"[Turn {turn_number}] {next_speaker} ({role_label}): {response}\n")

            # Check for natural resolution (after minimum turns)
            if turn_number >= self.min_turns:
                resolved, summary = await self.system_manager.check_resolution(
                    self.turns,
                    self.min_turns,
                )
                if resolved:
                    if verbose:
                        print(f"\n[Resolution detected: {summary}]")
                    break

        # Calculate duration
        duration = time.time() - start_time

        # Classify intents
        self.turns = await classify_all_turns(self.turns, self.client, use_llm=False)

        # Calculate statistics
        intent_stats = calculate_intent_statistics(self.turns, candidate_only=True)

        # Calculate average tension
        avg_tension = sum(self.tension_history) / len(self.tension_history) if self.tension_history else 0.5

        # Map to assessment
        assessment = map_to_assessment(intent_stats, avg_tension)

        # Build output
        metadata = SessionMetadata(
            session_id=self.session_id,
            profile_id=self.profile.id,
            scenario_id=self.scenario.id,
            timestamp=datetime.now(),
            total_turns=len(self.turns),
            duration_seconds=duration,
            api_calls=self.client.total_requests,
            model_used=self.client.pro_model_name if hasattr(self.client, "pro_model_name") else "mock",
        )

        output = SessionOutput(
            metadata=metadata,
            profile=self.profile,
            scenario=self.scenario,
            conversation=self.turns,
            intent_statistics=intent_stats,
            assessment_mapping=assessment,
        )

        if verbose:
            print(f"\n{'='*60}")
            print(f"Simulation complete!")
            print(f"Total turns: {len(self.turns)}")
            print(f"Duration: {duration:.1f}s")
            print(f"API calls: {self.client.total_requests}")
            print(f"Dominant intent: {intent_stats.dominant_intent}")
            print(f"{'='*60}")

        return output

    def _create_turn(
        self,
        role: SpeakerRole,
        name: str,
        content: str,
        turn_number: int,
        tension: float,
    ) -> Turn:
        """Create a Turn object with metadata."""
        return Turn(
            turn_number=turn_number,
            speaker=role,
            speaker_name=name,
            content=content,
            tension_level=tension,
            metadata={"session_id": self.session_id},
        )


async def run_simulation(
    profile_id: str,
    scenario_id: str,
    client: "GeminiClient | MockGeminiClient",
    turn_limit: Optional[int] = None,
    verbose: bool = False,
) -> SessionOutput:
    """
    Convenience function to run a single simulation.

    Args:
        profile_id: ID of the personality profile to use.
        scenario_id: ID of the scenario to use.
        client: LLM client.
        turn_limit: Optional turn limit override.
        verbose: Print progress during simulation.

    Returns:
        SessionOutput with complete results.
    """
    from config.personality_profiles import get_profile
    from config.scenarios import get_scenario

    profile = get_profile(profile_id)
    scenario = get_scenario(scenario_id)

    engine = SimulationEngine(
        client=client,
        profile=profile,
        scenario=scenario,
        turn_limit=turn_limit,
    )

    return await engine.run(verbose=verbose)
