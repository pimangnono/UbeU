"""
Group Engine: Mode 2 - 1-to-Many Group Discussion for Personality Assessment.

V4: Thin wrapper around A2A Moderator. Session lifecycle, timer, and stats
remain here. AI turn generation delegated to Moderator agent.

Key Features:
- 3 AI agents with fixed personality profiles (Alex, Jordan, Riley)
- A2A Moderator orchestrates turn-taking and trait coverage
- Phase-based discussion flow
- Per-turn Supabase persistence (crash recovery)
"""

import time
import logging
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from engines.base_engine import BaseEngine
from agents.group_agents import create_group_agents
from agents.moderator import Moderator
from agents.registry import AgentRegistry
from agents.trait_selector import TraitElicitationSelector
from utils.models import (
    Turn,
    SpeakerRole,
    SessionState,
    InterviewMode,
    SessionOutput,
    GroupScenario,
    GroupSessionStats,
    DiscussionPhase,
    BigFiveTrait,
)

if TYPE_CHECKING:
    from clients.llm_client import LLMClient

logger = logging.getLogger(__name__)


class GroupEngine(BaseEngine):
    """
    Engine for 1-to-many group discussions (Mode 2).

    The candidate interacts with three AI agents orchestrated by the Moderator:
    - Alex: Assertive Challenger (High E, Low A)
    - Jordan: Supportive Collaborator (High A, High E)
    - Riley: Quiet Skeptic (Low E, Low O)
    """

    def __init__(
        self,
        client: "LLMClient",
        participant_id: str,
        participant_name: str,
        scenario: GroupScenario,
    ):
        super().__init__(
            client=client,
            participant_id=participant_id,
            participant_name=participant_name,
            mode=InterviewMode.GROUP_DISCUSSION,
        )
        self.scenario = scenario

        # Create AI agents with scenario context
        self.agents = create_group_agents(client, scenario.brief)
        self.agent_names = ["Alex", "Jordan", "Riley"]

        # A2A infrastructure
        self.trait_selector = TraitElicitationSelector(client=client)
        self.registry = AgentRegistry()
        self.moderator = Moderator(
            agents=self.agents,
            trait_selector=self.trait_selector,
            registry=self.registry,
            scenario_brief=scenario.brief,
            client=client,
        )

        # Phase tracking
        self.current_phase_index = 0
        self.turns_in_current_phase = 0

        # Behavioral statistics
        self._candidate_word_count = 0
        self._name_mentions = 0
        self._questions_asked = 0
        self._disagreements = 0
        self._acknowledgments = 0
        self._new_ideas = 0

    @property
    def current_phase(self) -> DiscussionPhase:
        """Get the current discussion phase."""
        if self.current_phase_index < len(self.scenario.phases):
            phase_name = self.scenario.phases[self.current_phase_index].name
            try:
                return DiscussionPhase[phase_name]
            except KeyError:
                return DiscussionPhase.EXPLORATION
        return DiscussionPhase.CLOSING

    @property
    def current_phase_config(self):
        """Get the current phase configuration."""
        if self.current_phase_index < len(self.scenario.phases):
            return self.scenario.phases[self.current_phase_index]
        return self.scenario.phases[-1]

    async def generate_opening(self) -> list[Turn]:
        """Generate the group discussion introduction (Jordan opens)."""
        self.start_session()
        opening_turns = []

        jordan = self.agents["Jordan"]
        context = f"""This is the start of a group discussion. Introduce the scenario to the group:

{self.scenario.brief}

Keep it brief (2-3 sentences). Welcome everyone and set a collaborative tone.
Mention the key decision the group needs to make."""

        opening = await jordan.generate_response(context, "neutral")
        turn = self._create_turn(SpeakerRole.JORDAN, "Jordan", opening)
        self.turns.append(turn)
        opening_turns.append(turn)

        self._sync_agent_histories()
        self.mark_active()
        return opening_turns

    async def submit_candidate_turn(self, content: str) -> None:
        """Record the candidate's response and extract behavioral signals."""
        turn = self._create_turn(
            SpeakerRole.CANDIDATE,
            self.participant_name,
            content,
        )
        self.turns.append(turn)

        # Track behavioral statistics
        self._analyze_candidate_turn(content)

        # Update quality metrics
        self.moderator.record_candidate_turn(content)

        # Extract trait signals via LLM (keyword fallback) and update coverage
        await self.moderator.analyze_candidate_traits(content)

        self._sync_agent_histories()
        self._check_phase_progression()

    def _analyze_candidate_turn(self, content: str):
        """Analyze candidate turn for behavioral statistics."""
        content_lower = content.lower()
        word_count = len(content.split())
        self._candidate_word_count += word_count

        for name in ["alex", "jordan", "riley"]:
            if name in content_lower:
                self._name_mentions += 1

        if "?" in content:
            self._questions_asked += 1

        disagreement_phrases = ["i disagree", "i don't think", "that won't work", "no,", "but actually"]
        if any(phrase in content_lower for phrase in disagreement_phrases):
            self._disagreements += 1

        acknowledgment_phrases = ["good point", "i agree", "that's right", "exactly", "i like that"]
        if any(phrase in content_lower for phrase in acknowledgment_phrases):
            self._acknowledgments += 1

        idea_phrases = ["what if", "we could", "how about", "another option", "alternatively"]
        if any(phrase in content_lower for phrase in idea_phrases):
            self._new_ideas += 1

    def _check_phase_progression(self):
        """Check if we should advance to the next phase."""
        self.turns_in_current_phase += 1
        current_config = self.current_phase_config
        if self.turns_in_current_phase >= current_config.turns:
            if self.current_phase_index < len(self.scenario.phases) - 1:
                self.current_phase_index += 1
                self.turns_in_current_phase = 0

    async def generate_ai_response(self) -> list[Turn]:
        """
        Generate AI agent response(s) via A2A Moderator dispatch.

        Moderator selects speaker based on trait coverage, dispatches task,
        agent generates independently.
        """
        ai_turns = []

        # Time warnings
        if self.should_warn_time:
            minutes_left = int(self.remaining_seconds / 60)
            warning = f"Just a heads up, we have about {minutes_left} minutes left. We should start wrapping up our discussion."
            turn = self._create_turn(SpeakerRole.JORDAN, "Jordan", warning)
            self.turns.append(turn)
            ai_turns.append(turn)
            self.mark_warned()

        # Wrap-up
        if self.should_wrap_up:
            closing = await self._generate_closing_turn()
            self.turns.append(closing)
            ai_turns.append(closing)
            self.mark_wrapping_up()
            return ai_turns

        # Time expired
        if self.is_time_expired:
            self.end_session()
            return ai_turns

        # Delegate to Moderator (A2A dispatch)
        phase_config = self.current_phase_config
        speaker_name, response_text, latency = await self.moderator.dispatch_turn(
            turns=self.turns,
            current_phase=self.current_phase,
            phase_style=phase_config.style,
            phase_goal=phase_config.goal,
        )

        # Compensate for LLM latency
        self.add_llm_wait_time(latency)

        # Create turn
        role = SpeakerRole[speaker_name.upper()]
        turn = self._create_turn(role, speaker_name, response_text)
        self.turns.append(turn)
        ai_turns.append(turn)
        self._sync_agent_histories()

        # Check for second response (Moderator decides)
        second_speaker = self.moderator.should_add_second_response(
            speaker_name, self.turns, phase_config.style,
        )
        if second_speaker:
            # Sync history before second agent generates
            self._sync_agent_histories()
            second_response, second_latency = await self.moderator.dispatch_second_turn(
                second_speaker, self.turns,
            )
            if second_response:
                self.add_llm_wait_time(second_latency)
                second_role = SpeakerRole[second_speaker.upper()]
                second_turn = self._create_turn(second_role, second_speaker, second_response)
                self.turns.append(second_turn)
                ai_turns.append(second_turn)
                self._sync_agent_histories()

        return ai_turns

    async def _generate_closing_turn(self) -> Turn:
        """Generate a closing turn from Jordan."""
        jordan = self.agents["Jordan"]
        context = """Time is almost up. Summarize what the group has discussed and try to
capture any consensus or remaining disagreements. Keep it brief (2-3 sentences)."""
        closing = await jordan.generate_response(context, "consensus")
        return self._create_turn(SpeakerRole.JORDAN, "Jordan", closing)

    def _sync_agent_histories(self):
        """Sync conversation history to all agents."""
        for agent in self.agents.values():
            agent.update_history(self.turns)

    def compute_session_stats(self) -> GroupSessionStats:
        """Compute behavioral statistics for the session."""
        candidate_turns = self.get_candidate_turns()
        candidate_turn_count = len(candidate_turns)
        avg_words = self._candidate_word_count / candidate_turn_count if candidate_turn_count else 0

        phase_engagement = {}
        for phase in self.scenario.phases:
            phase_engagement[phase.name] = "medium"

        return GroupSessionStats(
            total_duration_seconds=int(self.elapsed_seconds),
            total_turns=len(self.turns),
            candidate_turns=candidate_turn_count,
            candidate_word_count=self._candidate_word_count,
            candidate_avg_words_per_turn=avg_words,
            times_addressed_others_by_name=self._name_mentions,
            times_asked_questions=self._questions_asked,
            times_expressed_disagreement=self._disagreements,
            times_acknowledged_others=self._acknowledgments,
            times_proposed_new_ideas=self._new_ideas,
            phase_engagement=phase_engagement,
        )

    def to_session_output(self) -> SessionOutput:
        """Convert session to output format."""
        output = SessionOutput(
            session_id=self.session_id,
            participant_id=self.participant_id,
            participant_name=self.participant_name,
            mode=InterviewMode.GROUP_DISCUSSION,
            start_time=datetime.fromtimestamp(self.start_time) if self.start_time else datetime.now(),
            end_time=datetime.now(),
            duration_seconds=int(self.elapsed_seconds),
            turns=self.turns,
            group_stats=self.compute_session_stats(),
        )
        # Attach quality flags from moderator
        output.quality_flags = self.moderator.get_quality_flags()
        return output

    def get_trait_coverage(self) -> dict[str, float]:
        """Get current trait coverage from the selector."""
        return self.trait_selector.get_coverage_summary()

    def get_speaker_distribution(self) -> dict[str, int]:
        """Get count of turns per speaker."""
        distribution = {"Candidate": 0, "Alex": 0, "Jordan": 0, "Riley": 0}
        for turn in self.turns:
            if turn.speaker_role == SpeakerRole.CANDIDATE:
                distribution["Candidate"] += 1
            elif turn.speaker_name in distribution:
                distribution[turn.speaker_name] += 1
        return distribution
