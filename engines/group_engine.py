"""
Group Engine: Mode 2 - 1-to-Many Group Discussion for Personality Assessment.

Implements an AI-simulated Leaderless Group Discussion (LGD), a well-established
Assessment Center method for observing interpersonal behavior.

Key Features:
- 3 AI agents with fixed, known personality profiles (Alex, Jordan, Riley)
- Phase-based discussion flow (DialogLab-inspired snippets)
- Trait-elicitation-driven speaker selection
- Real-time behavioral signal tracking

What Mode 2 Assesses:
- Openness (engagement with novel ideas)
- Conscientiousness (organization, follow-through)
- Extraversion (initiation, elaboration)
- Agreeableness (conflict handling, accommodation)
- Neuroticism (stress response, composure)

What Mode 2 Does NOT Assess:
- Logical reasoning (delegated to Mode 1)
- Quantitative ability (delegated to Mode 1)
"""

import time
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from engines.base_engine import BaseEngine
from agents.group_agents import create_group_agents, GroupAgent
from agents.trait_selector import (
    TraitElicitationSelector,
    analyze_turn_for_traits,
)
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


class GroupEngine(BaseEngine):
    """
    Engine for 1-to-many group discussions (Mode 2).

    The candidate interacts with three AI agents:
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

        # Trait elicitation selector
        self.trait_selector = TraitElicitationSelector()

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
        """
        Generate the group discussion introduction.

        Jordan (supportive) typically opens by introducing the scenario
        and inviting everyone to share their thoughts.
        """
        self.start_session()
        opening_turns = []

        # Jordan introduces the scenario
        jordan = self.agents["Jordan"]
        context = f"""This is the start of a group discussion. Introduce the scenario to the group:

{self.scenario.brief}

Keep it brief (2-3 sentences). Welcome everyone and set a collaborative tone.
Mention the key decision the group needs to make."""

        opening = await jordan.generate_response(context, "neutral")
        turn = self._create_turn(SpeakerRole.JORDAN, "Jordan", opening)
        self.turns.append(turn)
        opening_turns.append(turn)

        # Update all agents with the opening
        self._sync_agent_histories()

        self.mark_active()
        return opening_turns

    async def submit_candidate_turn(self, content: str) -> None:
        """
        Record the candidate's response.

        Also extracts behavioral signals for real-time trait coverage tracking.
        """
        turn = self._create_turn(
            SpeakerRole.CANDIDATE,
            self.participant_name,
            content,
        )
        self.turns.append(turn)

        # Track behavioral statistics
        self._analyze_candidate_turn(content)

        # Extract trait signals and update coverage
        signals = analyze_turn_for_traits(content)
        for trait, confidence in signals:
            self.trait_selector.update_coverage(trait, confidence)

        # Update all agents with the new turn
        self._sync_agent_histories()

        # Check phase progression
        self._check_phase_progression()

    def _analyze_candidate_turn(self, content: str):
        """Analyze candidate turn for behavioral statistics."""
        content_lower = content.lower()
        word_count = len(content.split())
        self._candidate_word_count += word_count

        # Track name mentions
        for name in ["alex", "jordan", "riley"]:
            if name in content_lower:
                self._name_mentions += 1

        # Track questions
        if "?" in content:
            self._questions_asked += 1

        # Track disagreement
        disagreement_phrases = ["i disagree", "i don't think", "that won't work", "no,", "but actually"]
        if any(phrase in content_lower for phrase in disagreement_phrases):
            self._disagreements += 1

        # Track acknowledgments
        acknowledgment_phrases = ["good point", "i agree", "that's right", "exactly", "i like that"]
        if any(phrase in content_lower for phrase in acknowledgment_phrases):
            self._acknowledgments += 1

        # Track new ideas
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
        Generate AI agent response(s).

        The trait elicitation selector chooses which agent speaks based on
        which personality traits have been insufficiently observed.
        """
        ai_turns = []

        # Check for time warnings
        if self.should_warn_time:
            minutes_left = int(self.remaining_seconds / 60)
            # Jordan delivers time warning (more natural)
            warning = f"Just a heads up, we have about {minutes_left} minutes left. We should start wrapping up our discussion."
            turn = self._create_turn(SpeakerRole.JORDAN, "Jordan", warning)
            self.turns.append(turn)
            ai_turns.append(turn)
            self.mark_warned()

        # Check for wrap-up
        if self.should_wrap_up:
            closing = await self._generate_closing_turn()
            self.turns.append(closing)
            ai_turns.append(closing)
            self.mark_wrapping_up()
            return ai_turns

        # Check if time expired
        if self.is_time_expired:
            self.end_session()
            return ai_turns

        # Get candidate's last turn for context
        candidate_turns = self.get_candidate_turns()
        last_content = candidate_turns[-1].content if candidate_turns else ""

        # Select next speaker based on trait coverage needs
        next_speaker = self.trait_selector.select_next_speaker(
            self.current_phase,
            last_content,
        )

        # Track LLM latency
        start_time = time.time()

        # Generate response from selected agent
        agent = self.agents[next_speaker]
        phase_style = self.current_phase_config.style

        # Build context for the agent
        context = self._build_agent_context(next_speaker, last_content)
        response = await agent.generate_response(context, phase_style)

        # Compensate for latency
        latency = time.time() - start_time
        self.add_llm_wait_time(latency)

        # Create turn with appropriate role
        role = SpeakerRole[next_speaker.upper()]
        turn = self._create_turn(role, next_speaker, response)
        self.turns.append(turn)
        ai_turns.append(turn)

        # Update all agents
        self._sync_agent_histories()

        # Sometimes add a second response (especially from Riley if they haven't spoken)
        if self._should_add_second_response(next_speaker):
            second_turn = await self._generate_second_response(next_speaker)
            if second_turn:
                self.turns.append(second_turn)
                ai_turns.append(second_turn)
                self._sync_agent_histories()

        return ai_turns

    def _build_agent_context(self, speaker: str, last_candidate_content: str) -> str:
        """Build context for the AI agent response."""
        phase_config = self.current_phase_config
        context_parts = []

        if last_candidate_content:
            context_parts.append(f"The candidate just said: \"{last_candidate_content}\"")

        if phase_config.goal:
            context_parts.append(f"Current goal: {phase_config.goal}")

        # Add phase-specific triggers
        if phase_config.trigger and self.current_phase.value == "conflict":
            context_parts.append(f"Trigger: {phase_config.trigger}")

        return "\n".join(context_parts) if context_parts else ""

    def _should_add_second_response(self, first_speaker: str) -> bool:
        """Decide if we should add a second AI response."""
        # Don't chain too many AI responses
        recent_ai_turns = sum(
            1 for t in self.turns[-5:]
            if t.speaker_role != SpeakerRole.CANDIDATE
        )
        if recent_ai_turns >= 2:
            return False

        # If first speaker was Alex (challenging), Jordan might support candidate
        if first_speaker == "Alex" and self.current_phase_config.style == "disagreement":
            return True

        # If Riley hasn't spoken much, include them
        riley_turns = sum(1 for t in self.turns if t.speaker_name == "Riley")
        total_ai_turns = sum(1 for t in self.turns if t.speaker_role != SpeakerRole.CANDIDATE)
        if total_ai_turns > 6 and riley_turns < 2:
            return True

        return False

    async def _generate_second_response(self, first_speaker: str) -> Optional[Turn]:
        """Generate a second AI response."""
        # Pick a different speaker
        if first_speaker == "Alex":
            second_speaker = "Jordan"
        elif first_speaker == "Jordan":
            second_speaker = "Riley"
        else:
            second_speaker = "Jordan"

        agent = self.agents[second_speaker]
        context = "Add a brief comment or reaction to the ongoing discussion."
        response = await agent.generate_response(context, "neutral")

        role = SpeakerRole[second_speaker.upper()]
        return self._create_turn(role, second_speaker, response)

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

        # Calculate phase engagement
        phase_engagement = {}
        for phase in self.scenario.phases:
            # Simple heuristic: check candidate activity in each phase
            phase_engagement[phase.name] = "medium"  # Default

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
        return SessionOutput(
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
