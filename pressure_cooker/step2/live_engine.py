"""
Live Engine: Step-by-step conversation engine for human participants.

Replaces SimulationEngine.run() with discrete steps:
  - submit_human_turn(): records human input as SpeakerRole.CANDIDATE
  - generate_ai_turns_until_human(): generates AI turns until the next
    speaker should be the human
  - to_session_output(): converts to existing SessionOutput format

The human fully replaces CandidateAgent — no AI candidate is created.

Supports consulting case studies with information gating:
  - CaseStudy data is hidden until the candidate asks about it
  - Facilitator context is rebuilt each turn with only revealed data
  - Engagement checks model analytical questioning if human is passive
"""

import asyncio
import re
import time
import uuid
from datetime import datetime
from typing import Optional, TYPE_CHECKING

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.colleague_agents import ProvokerAgent, MediatorAgent
from agents.system_manager import SystemManagerAgent
from pipeline.statistics import classify_all_turns, calculate_intent_statistics, map_to_assessment
from utils.models import (
    PersonalityProfile,
    PersonalityVector,
    ScenarioConfig,
    Turn,
    SpeakerRole,
    SessionMetadata,
    SessionOutput,
)
from step2.models import SessionState
from step2.case_data import CaseStudy

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient


# Timer constants (seconds)
SESSION_MAX_SECONDS = 15 * 60    # 15 minutes hard stop
WARN_AT_SECONDS = 12 * 60       # 12 minutes: facilitator warns
WRAPUP_AT_SECONDS = 14 * 60     # 14 minutes: facilitator starts wrapping up

# Engagement check constants
ENGAGEMENT_CHECK_TURN = 8       # Check engagement after this many total turns
QUESTION_PATTERNS = re.compile(
    r'\?|'
    r'\b(what|how|why|when|where|who|which|can you|could you|do you|is there|are there|tell me)\b',
    re.IGNORECASE,
)


class LiveEngine:
    """
    Step-by-step conversation engine for live human interviews.

    Unlike SimulationEngine which runs a full loop autonomously, LiveEngine
    operates turn-by-turn with human input between AI generation steps.
    """

    def __init__(
        self,
        client: "GeminiClient | MockGeminiClient",
        scenario: ScenarioConfig,
        participant_name: str,
        case_study: Optional[CaseStudy] = None,
    ):
        self.client = client
        self.scenario = scenario
        self.participant_name = participant_name
        self.session_id = str(uuid.uuid4())[:8]
        self.case_study = case_study

        # Create AI agents (no CandidateAgent — human fills that role)
        self.provoker = ProvokerAgent(
            name="Jordan",
            client=client,
            scenario=scenario,
            aggression_level=0.7,
        )
        self.mediator = MediatorAgent(
            name="Sam",
            client=client,
            scenario=scenario,
            diplomacy_level=0.7,
        )
        self.system_manager = SystemManagerAgent(
            name="Facilitator",
            client=client,
            scenario=scenario,
        )

        self.ai_agents = {
            "Jordan": self.provoker,
            "Sam": self.mediator,
            "Facilitator": self.system_manager,
        }

        # Available speakers for the system manager to choose from
        # Uses participant's actual name as the candidate speaker
        self.speaker_names = [self.participant_name, "Jordan", "Sam"]

        # Conversation state
        self.turns: list[Turn] = []
        self.tension_history: list[float] = []
        self.state = SessionState.CREATED
        self.start_time: Optional[float] = None
        self._turn_counter = 0
        self._warned_time = False
        self._wrapping_up = False

        # Case study / information gating state
        self.revealed_categories: set[str] = set()
        self.human_question_count: int = 0
        self.engagement_nudge_sent: bool = False

    @property
    def elapsed_seconds(self) -> float:
        """Seconds since session started."""
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time

    @property
    def remaining_seconds(self) -> float:
        """Seconds remaining before hard stop."""
        return max(0.0, SESSION_MAX_SECONDS - self.elapsed_seconds)

    @property
    def is_time_expired(self) -> bool:
        """Whether the session has exceeded the time limit."""
        return self.elapsed_seconds >= SESSION_MAX_SECONDS

    async def generate_opening(self) -> list[Turn]:
        """
        Generate the opening of the conversation.

        For case studies: Facilitator introduces the company, industry, and
        problem statement (but NOT hidden data). Provoker makes initial
        skeptical observation.

        For legacy scenarios: Facilitator introduces the discussion topic,
        Provoker states their position.
        """
        self.start_time = time.time()
        self.state = SessionState.OPENING
        opening_turns = []

        if self.case_study:
            # Case study opening: introduce the case
            intro_context = (
                f"You are the facilitator for a consulting case discussion. "
                f"Introduce the case to the group. The participants are "
                f"{self.participant_name}, Jordan, and Sam.\n\n"
                f"Company: {self.case_study.company_name}\n"
                f"Industry: {self.case_study.industry}\n"
                f"Problem: {self.case_study.problem_statement}\n\n"
                f"Present the company and problem clearly. Invite the team to "
                f"analyze the problem and ask questions about the available data. "
                f"Do NOT share any detailed data yet — wait for them to ask."
            )
        else:
            # Legacy scenario opening
            intro_context = (
                f"Introduce the discussion topic to the group. The participants are "
                f"{self.participant_name}, Jordan, and Sam. Briefly explain the situation "
                f"and invite everyone to share their thoughts."
            )

        intro = await self.system_manager.generate_response(intro_context)
        turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", intro)
        self.turns.append(turn)
        opening_turns.append(turn)

        # Update agents with the intro
        self._sync_agent_histories()

        # Provoker sets the stage
        if self.case_study:
            provoker_context = (
                f"The facilitator just introduced a case about {self.case_study.company_name}. "
                f"Make a skeptical initial observation about the problem: "
                f"'{self.case_study.problem_statement}'. "
                f"Challenge whether the stated goal is realistic or ask what data "
                f"we'd need to even begin analyzing this."
            )
        else:
            provoker_context = "Open the discussion by stating your position on the issue."

        tension = 0.3
        provoker_response = await self.provoker.generate_response(
            provoker_context, tension
        )
        turn = self._create_turn(SpeakerRole.PROVOKER, "Jordan", provoker_response)
        self.turns.append(turn)
        opening_turns.append(turn)

        self.state = SessionState.ACTIVE
        return opening_turns

    def submit_human_turn(self, content: str) -> Turn:
        """
        Record a human participant's message as a CANDIDATE turn.

        Also performs:
        - Keyword matching against case study data categories
        - Question detection for engagement tracking

        Args:
            content: The human's message text.

        Returns:
            The created Turn object.
        """
        turn = self._create_turn(
            SpeakerRole.CANDIDATE,
            self.participant_name,
            content,
        )
        self.turns.append(turn)

        # Case study: match keywords to reveal data categories
        if self.case_study:
            newly_matched = self.case_study.match_categories(content)
            self.revealed_categories.update(newly_matched)

        # Track analytical questions
        if self._detect_questions(content):
            self.human_question_count += 1

        return turn

    async def generate_ai_turns_until_human(self) -> list[Turn]:
        """
        Generate AI turns until the SystemManager decides the human
        should speak next (or session ends).

        Returns:
            List of AI turns generated in this step.
        """
        if self.state == SessionState.ENDED:
            return []

        ai_turns: list[Turn] = []
        max_consecutive_ai = 5  # Safety limit

        for _ in range(max_consecutive_ai):
            # Check time-based events
            time_turns = await self._check_time_events()
            ai_turns.extend(time_turns)

            if self.state == SessionState.ENDED:
                break

            # Sync history to all agents
            self._sync_agent_histories()

            # Assess tension
            tension = await self._get_tension()

            # Check for facilitator intervention
            should_intervene, reason = await self.system_manager.should_intervene(
                self.turns
            )

            # Build gated context for facilitator if case study active
            gated_context = self._build_gated_context() if self.case_study else ""

            if should_intervene:
                context = f"{reason}\n\n{gated_context}" if gated_context else reason
                response = await self.system_manager.generate_response(context)
                turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", response)
                self.turns.append(turn)
                ai_turns.append(turn)
                self._sync_agent_histories()

            # Decide next speaker
            next_speaker = await self.system_manager.decide_next_speaker(
                self.turns, self.speaker_names
            )

            # If human is next, stop generating
            if next_speaker == self.participant_name:
                break

            # Generate AI response
            agent = self.ai_agents.get(next_speaker)
            if agent is None:
                # Fallback: if system manager returned the human's name variant
                break

            if isinstance(agent, SystemManagerAgent):
                context = gated_context if gated_context else ""
                response = await agent.generate_response(context)
            else:
                response = await agent.generate_response(
                    context="", tension_level=tension
                )

            turn = self._create_turn(agent.role, next_speaker, response)
            self.turns.append(turn)
            ai_turns.append(turn)

            self._sync_agent_histories()

            # Check for natural resolution after enough turns
            if len(self.turns) >= self.scenario.min_turns:
                resolved, summary = await self.system_manager.check_resolution(
                    self.turns, self.scenario.min_turns
                )
                if resolved:
                    # Add closing from facilitator
                    closing = await self.system_manager.generate_response(
                        f"The discussion has reached a natural conclusion: {summary}. "
                        f"Thank everyone and wrap up."
                    )
                    close_turn = self._create_turn(
                        SpeakerRole.SYSTEM, "Facilitator", closing
                    )
                    self.turns.append(close_turn)
                    ai_turns.append(close_turn)
                    self.state = SessionState.ENDED
                    break

        # Check engagement after AI turns
        engagement_turn = self._check_engagement()
        if engagement_turn is not None:
            ai_turns.append(engagement_turn)

        return ai_turns

    async def end_session(self) -> Optional[Turn]:
        """
        End the session with a facilitator closing statement.

        Returns:
            The closing Turn, or None if already ended.
        """
        if self.state == SessionState.ENDED:
            return None

        self.state = SessionState.ENDED
        self._sync_agent_histories()

        closing = await self.system_manager.generate_response(
            "The discussion time is up. Thank everyone for their contributions "
            "and summarize the key points discussed."
        )
        turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", closing)
        self.turns.append(turn)
        return turn

    def to_session_output(
        self,
        participant_id: str,
        profile: Optional[PersonalityProfile] = None,
    ) -> SessionOutput:
        """
        Convert the live session to a SessionOutput compatible with
        the existing evaluation pipeline.

        Args:
            participant_id: Participant ID for metadata.
            profile: Optional personality profile (for ground truth).
                     If not provided, uses a placeholder.

        Returns:
            SessionOutput with conversation and metadata.
        """
        duration = self.elapsed_seconds

        # Classify intents (synchronous rule-based)
        # Note: We do this synchronously since classify_all_turns with use_llm=False
        # is effectively synchronous but has an async signature
        classified_turns = self.turns  # Will be classified in the async wrapper

        # Build metadata
        metadata = SessionMetadata(
            session_id=self.session_id,
            profile_id=f"human_{participant_id}",
            scenario_id=self.scenario.id,
            timestamp=datetime.now(),
            total_turns=len(self.turns),
            duration_seconds=duration,
            api_calls=self.client.total_requests if hasattr(self.client, "total_requests") else 0,
            model_used=self.client.pro_model_name if hasattr(self.client, "pro_model_name") else "live",
        )

        # Use placeholder profile if none provided
        if profile is None:
            profile = PersonalityProfile(
                id=f"human_{participant_id}",
                name=self.participant_name,
                description="Human participant (no injected personality)",
                vector=PersonalityVector(
                    openness=0.5,
                    conscientiousness=0.5,
                    extraversion=0.5,
                    agreeableness=0.5,
                    neuroticism=0.5,
                ),
            )

        return SessionOutput(
            metadata=metadata,
            profile=profile,
            scenario=self.scenario,
            conversation=classified_turns,
        )

    async def finalize_session_output(
        self,
        participant_id: str,
        profile: Optional[PersonalityProfile] = None,
    ) -> SessionOutput:
        """
        Async version of to_session_output that also classifies intents
        and computes statistics.
        """
        output = self.to_session_output(participant_id, profile)

        # Classify intents
        output.conversation = await classify_all_turns(
            output.conversation, self.client, use_llm=False
        )

        # Compute statistics
        intent_stats = calculate_intent_statistics(output.conversation, candidate_only=True)
        output.intent_statistics = intent_stats

        avg_tension = (
            sum(self.tension_history) / len(self.tension_history)
            if self.tension_history
            else 0.5
        )
        output.assessment_mapping = map_to_assessment(intent_stats, avg_tension)

        return output

    def get_conversation_dicts(self) -> list[dict]:
        """Return conversation as list of dicts for API responses."""
        return [
            {
                "speaker": t.speaker_name,
                "speaker_role": t.speaker.value,
                "content": t.content,
            }
            for t in self.turns
        ]

    def to_state_dict(self) -> dict:
        """Serialize engine state for persistence."""
        return {
            "session_id": self.session_id,
            "scenario_id": self.scenario.id,
            "participant_name": self.participant_name,
            "state": self.state.value,
            "start_time": self.start_time,
            "turn_counter": self._turn_counter,
            "warned_time": self._warned_time,
            "wrapping_up": self._wrapping_up,
            "turns": [t.model_dump() for t in self.turns],
            "tension_history": self.tension_history,
            # Case study gating state
            "revealed_categories": list(self.revealed_categories),
            "human_question_count": self.human_question_count,
            "engagement_nudge_sent": self.engagement_nudge_sent,
        }

    def restore_from_state(self, state: dict) -> None:
        """Restore engine state from persisted dict."""
        self.state = SessionState(state["state"])
        self.start_time = state["start_time"]
        self._turn_counter = state["turn_counter"]
        self._warned_time = state["warned_time"]
        self._wrapping_up = state["wrapping_up"]
        self.turns = [Turn.model_validate(t) for t in state["turns"]]
        self.tension_history = state["tension_history"]
        # Restore case study gating state
        self.revealed_categories = set(state.get("revealed_categories", []))
        self.human_question_count = state.get("human_question_count", 0)
        self.engagement_nudge_sent = state.get("engagement_nudge_sent", False)
        self._sync_agent_histories()

    # --- Private helpers ---

    def _create_turn(
        self,
        role: SpeakerRole,
        name: str,
        content: str,
    ) -> Turn:
        """Create a Turn and increment counter."""
        turn = Turn(
            turn_number=self._turn_counter,
            speaker=role,
            speaker_name=name,
            content=content,
            tension_level=self.tension_history[-1] if self.tension_history else 0.3,
            metadata={"session_id": self.session_id},
        )
        self._turn_counter += 1
        return turn

    def _sync_agent_histories(self) -> None:
        """Push current conversation history to all agents."""
        for agent in self.ai_agents.values():
            agent.update_history(self.turns)

    async def _get_tension(self) -> float:
        """Assess current tension level."""
        if len(self.turns) >= 3:
            tension = await self.system_manager.assess_tension(self.turns)
            self.tension_history.append(tension)
            return tension
        return 0.3

    async def _check_time_events(self) -> list[Turn]:
        """Check for time-based facilitator interventions."""
        turns = []
        elapsed = self.elapsed_seconds

        # 12-minute warning
        if elapsed >= WARN_AT_SECONDS and not self._warned_time:
            self._warned_time = True
            self._sync_agent_histories()
            warning = await self.system_manager.generate_response(
                "We have about 3 minutes left. Let's start moving toward "
                "concluding thoughts or final decisions."
            )
            turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", warning)
            self.turns.append(turn)
            turns.append(turn)

        # 14-minute wrap-up
        if elapsed >= WRAPUP_AT_SECONDS and not self._wrapping_up:
            self._wrapping_up = True
            self.state = SessionState.WRAPPING_UP
            self._sync_agent_histories()
            wrapup = await self.system_manager.generate_response(
                "We have about 1 minute left. Please share any final thoughts."
            )
            turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", wrapup)
            self.turns.append(turn)
            turns.append(turn)

        # 15-minute hard stop
        if elapsed >= SESSION_MAX_SECONDS:
            self.state = SessionState.ENDED
            self._sync_agent_histories()
            closing = await self.system_manager.generate_response(
                "Time is up. Thank everyone and briefly summarize the discussion."
            )
            turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", closing)
            self.turns.append(turn)
            turns.append(turn)

        return turns

    def _build_gated_context(self) -> str:
        """
        Build facilitator context with only revealed data categories.

        Returns instruction string telling the facilitator what data
        has been unlocked and what to share.
        """
        if not self.case_study:
            return ""

        all_labels = self.case_study.get_all_category_labels()
        revealed_data = self.case_study.get_revealed_data(self.revealed_categories)
        unrevealed = [
            label for cat, label in all_labels.items()
            if cat not in self.revealed_categories
        ]

        parts = [
            f"You are the facilitator for the {self.case_study.company_name} case study.",
        ]

        if revealed_data:
            parts.append(
                f"\nThe candidate has asked about the following data. "
                f"You may share this information:\n\n{revealed_data}"
            )

        if unrevealed:
            unrevealed_str = ", ".join(unrevealed)
            parts.append(
                f"\nDo NOT proactively share data about: {unrevealed_str}. "
                f"Only share this data if the candidate specifically asks about it."
            )

        parts.append(
            "\nIf asked about data not listed here, respond: "
            "'That specific data isn't available for this case. "
            "Let me share what we do have about [nearest available category].'"
        )

        return "\n".join(parts)

    def _detect_questions(self, text: str) -> bool:
        """Check if text contains analytical questions."""
        return bool(QUESTION_PATTERNS.search(text))

    def _check_engagement(self) -> Optional[Turn]:
        """
        Check if the human needs an engagement nudge.

        At turn ~8+, if the human hasn't asked any analytical questions,
        Sam models the behavior by asking about a key data category.
        """
        if self.engagement_nudge_sent:
            return None
        if len(self.turns) < ENGAGEMENT_CHECK_TURN:
            return None
        if self.human_question_count > 0:
            return None
        if not self.case_study:
            return None

        self.engagement_nudge_sent = True

        # Pick a data category to ask about
        unrevealed = [
            item for item in self.case_study.data_items
            if item.category not in self.revealed_categories
        ]
        if not unrevealed:
            return None

        # Sam models analytical questioning
        target = unrevealed[0]
        nudge_content = (
            f"Before we dive deeper, I think we should understand the "
            f"{target.label.lower()} better. Facilitator, can you walk us "
            f"through the {target.label.lower()}?"
        )

        turn = self._create_turn(SpeakerRole.MEDIATOR, "Sam", nudge_content)
        self.turns.append(turn)

        # This also reveals the category so the facilitator can respond
        self.revealed_categories.add(target.category)

        return turn
