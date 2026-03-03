"""
Moderator Agent: Orchestrates A2A turn-taking in group discussions.

V4: Adaptive dispatch with elicitation goals and quality gates.

Responsibilities:
- Selects next speaker based on trait coverage gaps
- Creates A2A Tasks with elicitation goals and dispatches to participant agents
- Manages turn order and prevents agent domination
- Tracks session quality in real-time
- Delegates actual response generation to individual agents

This is the central orchestrator in the Hybrid A2A architecture.
GroupEngine delegates to Moderator for AI turn generation.
"""

import logging
import time
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from agents.registry import AgentRegistry
from agents.trait_selector import (
    TraitElicitationSelector,
    analyze_turn_for_traits,
    analyze_turn_with_llm,
)
from utils.models import (
    Turn,
    SpeakerRole,
    DiscussionPhase,
    BigFiveTrait,
)

if TYPE_CHECKING:
    from agents.group_agents import GroupAgent
    from clients.llm_client import LLMClient

logger = logging.getLogger(__name__)


@dataclass
class A2ATask:
    """Task dispatched from Moderator to a Participant Agent."""
    task_id: str
    task_type: str = "respond_in_discussion"
    input: dict = field(default_factory=dict)


@dataclass
class A2ATaskResult:
    """Result returned from a Participant Agent to Moderator."""
    task_id: str
    status: str = "completed"  # completed, failed
    output: dict = field(default_factory=dict)


@dataclass
class QualityMetrics:
    """Real-time session quality tracking."""
    candidate_turns: int = 0
    candidate_total_words: int = 0
    trait_coverage_at_check: float = 0.0

    @property
    def avg_words_per_turn(self) -> float:
        return self.candidate_total_words / self.candidate_turns if self.candidate_turns else 0.0

    @property
    def is_low_engagement(self) -> bool:
        """Candidate is under-engaged if avg words < 15 after 3+ turns."""
        return self.candidate_turns >= 3 and self.avg_words_per_turn < 15

    @property
    def is_low_coverage(self) -> bool:
        """Trait coverage is low if mean < 0.3 after 5+ candidate turns."""
        return self.candidate_turns >= 5 and self.trait_coverage_at_check < 0.3

    def get_quality_flags(self) -> list[str]:
        """Return list of quality concern flags."""
        flags = []
        if self.is_low_engagement:
            flags.append("low_engagement")
        if self.is_low_coverage:
            flags.append("low_trait_coverage")
        if self.candidate_turns >= 3 and self.avg_words_per_turn > 150:
            flags.append("verbose_responses")
        return flags


class Moderator:
    """
    A2A Moderator: Orchestrates group discussion turn-taking.

    V4 additions:
    - Elicitation goals passed to agents via A2A Tasks
    - Quality gates track engagement and coverage in real-time
    - Adaptive urgency: agents prompt more directly when quality is low

    Usage (from GroupEngine):
        moderator = Moderator(agents, trait_selector, registry)
        speaker, response, latency = await moderator.dispatch_turn(
            turns, current_phase, phase_style, phase_goal
        )
    """

    def __init__(
        self,
        agents: dict[str, "GroupAgent"],
        trait_selector: TraitElicitationSelector,
        registry: AgentRegistry,
        scenario_brief: str = "",
        client: "LLMClient | None" = None,
    ):
        self.agents = agents
        self.trait_selector = trait_selector
        self.registry = registry
        self.scenario_brief = scenario_brief
        self.client = client  # For LLM-based trait analysis
        self._turn_counter = 0
        self.quality = QualityMetrics()

    def record_candidate_turn(self, content: str):
        """Update quality metrics when candidate speaks."""
        self.quality.candidate_turns += 1
        self.quality.candidate_total_words += len(content.split())
        self.quality.trait_coverage_at_check = self.trait_selector.coverage.mean_coverage()

    async def analyze_candidate_traits(self, content: str):
        """
        Analyze candidate turn for trait signals using LLM (keyword fallback).
        Updates trait coverage automatically.
        """
        if self.client:
            signals = await analyze_turn_with_llm(self.client, content)
        else:
            signals = analyze_turn_for_traits(content)

        for trait, confidence in signals:
            self.trait_selector.update_coverage(trait, confidence)

        return signals

    async def dispatch_turn(
        self,
        turns: list[Turn],
        current_phase: DiscussionPhase,
        phase_style: str = "neutral",
        phase_goal: str = "",
    ) -> tuple[str, str, float]:
        """
        Select next speaker and dispatch A2A task with elicitation goal.

        Returns:
            (speaker_name, response_text, llm_latency_seconds)
        """
        # Get candidate's last turn for context
        candidate_turns = [t for t in turns if t.speaker_role == SpeakerRole.CANDIDATE]
        last_candidate_content = candidate_turns[-1].content if candidate_turns else ""

        # Select next speaker via trait coverage analysis
        next_speaker = self.trait_selector.select_next_speaker(
            current_phase,
            last_candidate_content,
        )

        # Get elicitation goal for this speaker
        elicitation_goal = self.trait_selector.get_elicitation_goal(next_speaker)

        # Adjust urgency based on quality gates
        urgency = self._compute_urgency()

        # Build A2A task
        self._turn_counter += 1
        task = A2ATask(
            task_id=f"turn_{self._turn_counter:03d}_{next_speaker.lower()}",
            task_type="respond_in_discussion",
            input={
                "scenario_context": self.scenario_brief,
                "goal": phase_goal or "continue_discussion",
                "phase_style": phase_style,
                "last_candidate_message": last_candidate_content,
                "elicitation_goal": elicitation_goal,
                "urgency": urgency,
            },
        )

        # Dispatch to agent
        start_time = time.time()
        result = await self._dispatch_to_agent(next_speaker, task, phase_style)
        latency = time.time() - start_time

        response_text = result.output.get("response_text", "")

        return next_speaker, response_text, latency

    def _compute_urgency(self) -> str:
        """
        Determine urgency level based on quality gates.

        Returns:
            "normal", "elevated", or "high"
        """
        flags = self.quality.get_quality_flags()
        if "low_trait_coverage" in flags and "low_engagement" in flags:
            return "high"
        elif flags:
            return "elevated"
        return "normal"

    async def _dispatch_to_agent(
        self,
        speaker_name: str,
        task: A2ATask,
        phase_style: str,
    ) -> A2ATaskResult:
        """Dispatch an A2A task to a specific agent."""
        agent = self.agents.get(speaker_name)
        if agent is None:
            logger.error(f"Agent '{speaker_name}' not found")
            return A2ATaskResult(
                task_id=task.task_id,
                status="failed",
                output={"error": f"Agent {speaker_name} not found"},
            )

        try:
            # Build context from task input
            context_parts = []
            last_msg = task.input.get("last_candidate_message", "")
            if last_msg:
                context_parts.append(f'The candidate just said: "{last_msg}"')

            goal = task.input.get("goal", "")
            if goal and goal != "continue_discussion":
                context_parts.append(f"Current goal: {goal}")

            context = "\n".join(context_parts) if context_parts else ""

            # Extract elicitation goal and urgency from task
            elicitation_goal = task.input.get("elicitation_goal")
            urgency = task.input.get("urgency", "normal")

            # Agent generates response with elicitation goal
            response = await agent.generate_response(
                context,
                phase_style,
                elicitation_goal=elicitation_goal,
                urgency=urgency,
            )

            return A2ATaskResult(
                task_id=task.task_id,
                status="completed",
                output={"response_text": response},
            )

        except Exception as e:
            logger.error(f"Agent {speaker_name} failed: {e}")
            return A2ATaskResult(
                task_id=task.task_id,
                status="failed",
                output={"error": str(e)},
            )

    def should_add_second_response(
        self,
        first_speaker: str,
        turns: list[Turn],
        phase_style: str,
    ) -> Optional[str]:
        """
        Decide if a second agent should respond.

        Returns:
            Name of second speaker, or None
        """
        # Don't chain too many AI responses
        recent_ai_turns = sum(
            1 for t in turns[-5:]
            if t.speaker_role != SpeakerRole.CANDIDATE
        )
        if recent_ai_turns >= 2:
            return None

        # If first speaker was Alex (challenging), Jordan might support candidate
        if first_speaker == "Alex" and phase_style == "disagreement":
            return "Jordan"

        # If Riley hasn't spoken much, include them
        riley_turns = sum(1 for t in turns if t.speaker_name == "Riley")
        total_ai_turns = sum(1 for t in turns if t.speaker_role != SpeakerRole.CANDIDATE)
        if total_ai_turns > 6 and riley_turns < 2:
            return "Riley"

        return None

    async def dispatch_second_turn(
        self,
        speaker_name: str,
        turns: list[Turn],
    ) -> tuple[str, float]:
        """
        Generate a second AI response (brief reaction).

        Returns:
            (response_text, llm_latency_seconds)
        """
        self._turn_counter += 1
        task = A2ATask(
            task_id=f"turn_{self._turn_counter:03d}_{speaker_name.lower()}_follow",
            task_type="respond_in_discussion",
            input={
                "goal": "brief_reaction",
                "last_candidate_message": "",
                "elicitation_goal": None,
                "urgency": "normal",
            },
        )

        start_time = time.time()
        agent = self.agents.get(speaker_name)
        if agent is None:
            return "", 0.0

        try:
            response = await agent.generate_response(
                "Add a brief comment or reaction to the ongoing discussion.",
                "neutral",
            )
            latency = time.time() - start_time
            return response, latency
        except Exception as e:
            logger.error(f"Second response from {speaker_name} failed: {e}")
            return "", time.time() - start_time

    def get_quality_flags(self) -> list[str]:
        """Get current quality flags for session metadata."""
        return self.quality.get_quality_flags()

    def get_quality_summary(self) -> dict:
        """Get quality metrics summary."""
        return {
            "candidate_turns": self.quality.candidate_turns,
            "avg_words_per_turn": round(self.quality.avg_words_per_turn, 1),
            "trait_coverage": round(self.quality.trait_coverage_at_check, 3),
            "flags": self.quality.get_quality_flags(),
        }
