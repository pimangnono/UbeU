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
from agents.smart_agents import SmartProvokerAgent, ActiveMediatorAgent, SmartSystemManager
from agents.discussion_orchestrator import DiscussionPhase, DiscussionContext
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
SESSION_MAX_SECONDS = 2 * 60     # 2 minutes hard stop (change to 15 * 60 for production)
WARN_AT_SECONDS = 1 * 60         # 1 minute: facilitator warns
WRAPUP_AT_SECONDS = 90           # 1.5 minutes: facilitator starts wrapping up

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
        self._last_newly_revealed: set[str] = set()
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
            # Case study opening: present the case briefing only
            intro_context = (
                f"Present this case briefing in 3-4 sentences. The team is "
                f"{self.participant_name}, Jordan, and Sam.\n"
                f"Company: {self.case_study.company_name} ({self.case_study.industry})\n"
                f"Problem: {self.case_study.problem_statement}\n"
                f"State the company and problem clearly. "
                f"Do NOT ask any questions. Do NOT end with a question mark. "
                f"Do NOT invite discussion. Do NOT suggest what to do next. "
                f"Do NOT share detailed data yet. Just present the problem and stop."
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

        # For case studies: human starts the discussion (no provoker opening)
        # For legacy scenarios: provoker sets the stage
        if not self.case_study:
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
            # Track which categories were NEWLY revealed (for smart routing)
            self._last_newly_revealed = newly_matched - self.revealed_categories
            self.revealed_categories.update(newly_matched)
        else:
            self._last_newly_revealed = set()

        # Track analytical questions
        if self._detect_questions(content):
            self.human_question_count += 1

        return turn

    async def generate_ai_turns_until_human(
        self,
        target_speaker: Optional[str] = None,
    ) -> list[Turn]:
        """
        Generate AI turns until the SystemManager decides the human
        should speak next (or session ends).

        Args:
            target_speaker: If set, generate a response only from this
                speaker and return immediately. Bypasses decide_next_speaker().

        Returns:
            List of AI turns generated in this step.
        """
        if self.state == SessionState.ENDED:
            return []

        ai_turns: list[Turn] = []

        # --- Targeted-speaker bypass ---
        if target_speaker and target_speaker in self.ai_agents:
            # Still run time checks and sync history
            time_turns = await self._check_time_events()
            ai_turns.extend(time_turns)
            if self.state == SessionState.ENDED:
                return ai_turns

            self._sync_agent_histories()
            tension = await self._get_tension()
            gated_context = self._build_gated_context() if self.case_study else ""

            agent = self.ai_agents[target_speaker]
            if isinstance(agent, SystemManagerAgent):
                response = await agent.generate_response(gated_context if gated_context else "")
            else:
                case_context = (
                    "IMPORTANT: This is a consulting case study. The human candidate must "
                    "lead the analysis. Do NOT propose frameworks, structure, or analytical "
                    "approaches. Only react to what the candidate says — challenge weak "
                    "reasoning, ask for clarification, or support good points. Never suggest "
                    "what to look at next or how to break down the problem."
                ) if self.case_study else ""
                response = await agent.generate_response(
                    context=case_context, tension_level=tension
                )

            turn = self._create_turn(agent.role, target_speaker, response)
            self.turns.append(turn)
            ai_turns.append(turn)
            self._sync_agent_histories()

            # Check engagement after targeted turn
            engagement_turn = self._check_engagement()
            if engagement_turn is not None:
                ai_turns.append(engagement_turn)

            return ai_turns

        max_consecutive_ai = 5  # Safety limit

        # Case study fast path: skip tension/intervention/decide overhead.
        # All data is shown upfront in the UI data panel, so no facilitator responses needed.
        if self.case_study:
            time_turns = await self._check_time_events()
            ai_turns.extend(time_turns)
            if self.state == SessionState.ENDED:
                return ai_turns

            self._sync_agent_histories()
            tension = self.tension_history[-1] if self.tension_history else 0.3

            # Build case data context for agents
            case_data_context = self._build_case_data_context()

            # Both Jordan and Sam respond to create more dynamic discussion
            # First responder alternates to keep variety
            first_speaker = "Jordan" if len(self.turns) % 2 == 0 else "Sam"
            second_speaker = "Sam" if first_speaker == "Jordan" else "Jordan"

            # First response (more critical/challenging)
            agent1 = self.ai_agents[first_speaker]
            context1 = (
                "IMPORTANT: This is a consulting case study. The human candidate leads the analysis. "
                f"{case_data_context}"
                "Keep your response SHORT (1-2 sentences max). "
                "React to what the candidate just said. You can challenge, question, or support. "
                "If the candidate asks about specific data, reference the relevant numbers from the case data above and help them interpret it. "
                "Do NOT propose frameworks. Let the candidate lead. "
                "NEVER address the Facilitator. NEVER ask the Facilitator for data or questions."
            )
            response1 = await agent1.generate_response(context=context1, tension_level=tension)
            turn1 = self._create_turn(agent1.role, first_speaker, response1)
            self.turns.append(turn1)
            ai_turns.append(turn1)
            self._sync_agent_histories()

            # Second response (adds different perspective)
            agent2 = self.ai_agents[second_speaker]
            context2 = (
                "IMPORTANT: Your colleague just responded. Add a DIFFERENT perspective briefly. "
                f"{case_data_context}"
                "Keep it SHORT (1-2 sentences max). "
                "If they challenged, you can support. If they supported, add nuance or a question. "
                "If the candidate asks about data, cite specific numbers from the case data and offer analysis. "
                "Do NOT repeat what was said. Do NOT propose frameworks. Be concise. "
                "NEVER address the Facilitator. NEVER ask the Facilitator for data or questions."
            )
            response2 = await agent2.generate_response(context=context2, tension_level=tension)
            turn2 = self._create_turn(agent2.role, second_speaker, response2)
            self.turns.append(turn2)
            ai_turns.append(turn2)
            self._sync_agent_histories()

            return ai_turns

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
            gated_context = ""

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
                case_context = (
                    "IMPORTANT: This is a consulting case study. The human candidate must "
                    "lead the analysis. Do NOT propose frameworks, structure, or analytical "
                    "approaches. Only react to what the candidate says — challenge weak "
                    "reasoning, ask for clarification, or support good points. Never suggest "
                    "what to look at next or how to break down the problem."
                ) if self.case_study else ""
                response = await agent.generate_response(
                    context=case_context, tension_level=tension
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
        Async version of to_session_output that also classifies intents,
        computes statistics, and runs multi-model OCEAN personality inference.
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

        # Run multi-model OCEAN personality inference
        try:
            from pipeline.ensemble_detector import detect_personality_ensemble
            ensemble_result = await detect_personality_ensemble(
                turns=self.turns,
                candidate_name=self.participant_name,
                client=self.client,
            )
            output.personality_inference = ensemble_result.to_dict()
        except Exception as e:
            # Don't fail session output if personality inference fails
            output.personality_inference = {"error": str(e)}

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
            "'That specific data isn't available for this case.'"
        )

        parts.append(
            "\n## ABSOLUTE RULES — VIOLATING THESE IS FORBIDDEN:"
            "\n"
            "\n### WHAT YOU MUST DO:"
            "\n- State ONLY the requested data/numbers."
            "\n- Format: 'Here is [category]: [data]' then STOP."
            "\n- Use bullet points for multiple items, then STOP."
            "\n"
            "\n### WHAT YOU MUST NEVER DO:"
            "\n- NEVER use names (Jordan, Sam, Morgan, etc.) in your response."
            "\n- NEVER ask questions or end with '?'"
            "\n- NEVER say 'let's', 'we should', 'how do you', 'what do you think'"
            "\n- NEVER say 'discuss', 'focus on', 'consider', 'analyze'"
            "\n- NEVER offer opinions, commentary, or analysis"
            "\n- NEVER suggest next steps or actions"
            "\n- NEVER add concluding remarks after the data"
            "\n- NEVER hand off to others ('Over to you', 'What does X think')"
            "\n- NEVER facilitate or moderate in ANY way"
            "\n"
            "\n### EXAMPLE OF CORRECT RESPONSE:"
            "\n'Here is the cost breakdown: Engineering 40%, Sales 25%, Support 20%, G&A 15%.'"
            "\n"
            "\n### EXAMPLE OF WRONG RESPONSE (DO NOT DO THIS):"
            "\n'Here is the cost breakdown... Jordan and Sam, what are your thoughts on this?'"
        )

        return "\n".join(parts)

    def _detect_questions(self, text: str) -> bool:
        """Check if text contains analytical questions."""
        return bool(QUESTION_PATTERNS.search(text))

    def _build_case_data_context(self) -> str:
        """
        Build context string with all case data for AI agents.

        Returns a formatted string with all data items so agents can
        reference the data in their responses.
        """
        if not self.case_study:
            return ""

        data_parts = [
            f"\n--- CASE DATA (you have access to this) ---\n"
            f"Company: {self.case_study.company_name} ({self.case_study.industry})\n"
            f"Problem: {self.case_study.problem_statement}\n"
        ]

        for item in self.case_study.data_items:
            data_parts.append(f"\n{item.label}:\n{item.detail}\n")

        data_parts.append("--- END CASE DATA ---\n\n")

        return "".join(data_parts)

    def _is_data_request(self, text: str) -> bool:
        """
        Check if text is asking the Facilitator for data.

        Detects common patterns like:
        - "can we get..." / "could we see..."
        - "what is the..." / "what are the..."
        - "facilitator, ..." / "@facilitator"
        - "do we have data on..."
        - "show me..." / "tell me about..."
        """
        text = text.lower()

        # Direct facilitator address
        if "facilitator" in text:
            return True

        # Common data request patterns
        data_patterns = [
            r"\bcan (we|you|i) (get|see|have|look at)\b",
            r"\bcould (we|you|i) (get|see|have|look at)\b",
            r"\bdo (we|you) have (data|numbers|info|information)\b",
            r"\bwhat (is|are|about) the\b.*\?",
            r"\bshow (me|us)\b",
            r"\btell (me|us) about\b",
            r"\bgive (me|us)\b.*\b(data|numbers|breakdown)\b",
            r"\bi('d| would) like to (see|know|understand)\b",
            r"\bwhat('s| is) (the|our)\b.*\b(margin|cost|revenue|rate|ratio|percentage)\b",
            r"\bhow (much|many)\b.*\?",
            r"\bbreakdown\b.*\?",
            r"\bcan you (share|provide|walk us through)\b",
        ]

        import re
        for pattern in data_patterns:
            if re.search(pattern, text):
                return True

        return False

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

        # Sam models analytical thinking (without asking facilitator)
        target = unrevealed[0]
        nudge_content = (
            f"I think we should consider the {target.label.lower()} more carefully. "
            f"It might give us important insights into the situation."
        )

        turn = self._create_turn(SpeakerRole.MEDIATOR, "Sam", nudge_content)
        self.turns.append(turn)

        # This also reveals the category so the facilitator can respond
        self.revealed_categories.add(target.category)

        return turn


# =============================================================================
# Smart Live Engine with Evidence-Based Analysis
# =============================================================================

class SmartLiveEngine(LiveEngine):
    """
    Enhanced LiveEngine with:
    - Smart agents (competency-targeted provoker, active mediator)
    - Discussion phase management
    - Competency coverage tracking
    - Evidence-based analysis output

    Use this engine for interviews where you want transparent,
    evidence-backed assessments.
    """

    def __init__(
        self,
        client: "GeminiClient | MockGeminiClient",
        scenario: ScenarioConfig,
        participant_name: str,
        case_study: Optional[CaseStudy] = None,
        use_smart_agents: bool = True,
    ):
        """
        Initialize smart live engine.

        Args:
            client: LLM client.
            scenario: Scenario configuration.
            participant_name: Human participant's name.
            case_study: Optional case study for consulting scenarios.
            use_smart_agents: If True, use smart agents; else fall back to basic agents.
        """
        # Initialize parent
        super().__init__(client, scenario, participant_name, case_study)

        self.use_smart_agents = use_smart_agents

        # Create shared discussion context
        self.discussion_context = DiscussionContext()

        if use_smart_agents:
            # Replace agents with smart versions
            self.provoker = SmartProvokerAgent(
                name="Jordan",
                client=client,
                scenario=scenario,
                context=self.discussion_context,
            )
            self.mediator = ActiveMediatorAgent(
                name="Sam",
                client=client,
                scenario=scenario,
                context=self.discussion_context,
            )
            self.system_manager = SmartSystemManager(
                name="Facilitator",
                client=client,
                scenario=scenario,
                context=self.discussion_context,
            )

            self.ai_agents = {
                "Jordan": self.provoker,
                "Sam": self.mediator,
                "Facilitator": self.system_manager,
            }

        # Evidence-based analysis storage
        self._turn_analyses: list = []
        self._evidence_assessment = None

    def _record_turn_to_context(self, turn: Turn) -> None:
        """Record a turn to the discussion context and detect competency behaviors."""
        self.discussion_context.record_turn(turn)

        # Track revealed data
        if turn.speaker == SpeakerRole.CANDIDATE:
            self.discussion_context.data_requested.update(self.revealed_categories)

        # Check for phase advancement
        if self.discussion_context.should_advance_phase():
            old_phase = self.discussion_context.current_phase
            self.discussion_context.advance_phase()
            new_phase = self.discussion_context.current_phase
            # Log phase transition (could emit an event here)
            if old_phase != new_phase:
                pass  # Phase advanced from {old_phase} to {new_phase}

    def submit_human_turn(self, content: str) -> Turn:
        """
        Record human turn and update discussion context.

        Extends parent to also:
        - Update discussion context
        - Detect competency behaviors
        - Check for phase advancement
        """
        turn = super().submit_human_turn(content)

        # Record to discussion context
        self._record_turn_to_context(turn)

        # Track data usage
        if self.case_study:
            self.discussion_context.data_revealed.update(self.revealed_categories)

        return turn

    async def generate_ai_turns_until_human(
        self,
        target_speaker: Optional[str] = None,
    ) -> list[Turn]:
        """
        Generate AI turns with smart agent behavior.

        Enhancements over parent:
        - Uses competency-targeted challenges
        - Active mediator advancement
        - Phase-aware speaker selection
        - Records all turns to discussion context
        """
        if self.state == SessionState.ENDED:
            return []

        ai_turns: list[Turn] = []

        # Time checks
        time_turns = await self._check_time_events()
        ai_turns.extend(time_turns)
        if self.state == SessionState.ENDED:
            return ai_turns

        self._sync_agent_histories()

        # Get candidate's last turn for context
        candidate_last_turn = None
        for t in reversed(self.turns):
            if t.speaker == SpeakerRole.CANDIDATE:
                candidate_last_turn = t
                break

        # Update tension
        tension = await self._get_tension()
        self.discussion_context.tension_level = tension

        # --- Targeted speaker bypass ---
        if target_speaker and target_speaker in self.ai_agents:
            agent = self.ai_agents[target_speaker]
            response = await self._generate_smart_response(
                agent, target_speaker, tension, candidate_last_turn
            )
            turn = self._create_turn(agent.role, target_speaker, response)
            self.turns.append(turn)
            ai_turns.append(turn)
            self._record_turn_to_context(turn)
            self._sync_agent_histories()
            return ai_turns

        # --- Case study smart flow ---
        if self.case_study:
            human_message = candidate_last_turn.content.lower() if candidate_last_turn else ""

            # Check if human requested data
            newly_revealed = getattr(self, '_last_newly_revealed', set())
            is_data_question = bool(newly_revealed) or self._is_data_request(human_message)

            if is_data_question:
                # Facilitator provides data
                gated_context = self._build_gated_context()
                fac_response = await self.system_manager.generate_response(gated_context)
                fac_turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", fac_response)
                self.turns.append(fac_turn)
                ai_turns.append(fac_turn)
                self._record_turn_to_context(fac_turn)
                self._sync_agent_histories()

                # Track that data was revealed
                self.discussion_context.data_revealed.update(self.revealed_categories)

                # Colleague reaction (brief)
                if len(fac_response) < 200 and self.use_smart_agents:
                    # Use smart speaker selection
                    next_speaker = self._select_smart_speaker()
                    agent = self.ai_agents[next_speaker]
                    response = await self._generate_smart_response(
                        agent, next_speaker, tension, candidate_last_turn,
                        context="The Facilitator just shared data. React briefly (1-2 sentences) if you have specific insight."
                    )
                    turn = self._create_turn(agent.role, next_speaker, response)
                    self.turns.append(turn)
                    ai_turns.append(turn)
                    self._record_turn_to_context(turn)
                    self._sync_agent_histories()
            else:
                # No data question - colleague responds
                next_speaker = self._select_smart_speaker()
                agent = self.ai_agents[next_speaker]
                response = await self._generate_smart_response(
                    agent, next_speaker, tension, candidate_last_turn
                )
                turn = self._create_turn(agent.role, next_speaker, response)
                self.turns.append(turn)
                ai_turns.append(turn)
                self._record_turn_to_context(turn)
                self._sync_agent_histories()

            # Check engagement
            engagement_turn = self._check_engagement()
            if engagement_turn is not None:
                ai_turns.append(engagement_turn)
                self._record_turn_to_context(engagement_turn)

            return ai_turns

        # --- Non-case-study flow (original behavior with smart agents) ---
        max_consecutive_ai = 5

        for _ in range(max_consecutive_ai):
            time_turns = await self._check_time_events()
            ai_turns.extend(time_turns)
            if self.state == SessionState.ENDED:
                break

            self._sync_agent_histories()
            tension = await self._get_tension()

            # Check for intervention
            should_intervene, reason = await self.system_manager.should_intervene(self.turns)
            if should_intervene:
                response = await self.system_manager.generate_response(reason)
                turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", response)
                self.turns.append(turn)
                ai_turns.append(turn)
                self._record_turn_to_context(turn)
                self._sync_agent_histories()

            # Smart speaker selection
            next_speaker = self._select_smart_speaker()

            if next_speaker == self.participant_name:
                break

            agent = self.ai_agents.get(next_speaker)
            if agent is None:
                break

            response = await self._generate_smart_response(
                agent, next_speaker, tension, candidate_last_turn
            )
            turn = self._create_turn(agent.role, next_speaker, response)
            self.turns.append(turn)
            ai_turns.append(turn)
            self._record_turn_to_context(turn)
            self._sync_agent_histories()

            # Check resolution
            if len(self.turns) >= self.scenario.min_turns:
                resolved, summary = await self.system_manager.check_resolution(
                    self.turns, self.scenario.min_turns
                )
                if resolved:
                    closing = await self.system_manager.generate_response(
                        f"The discussion has reached a natural conclusion: {summary}. "
                        f"Thank everyone and wrap up."
                    )
                    close_turn = self._create_turn(SpeakerRole.SYSTEM, "Facilitator", closing)
                    self.turns.append(close_turn)
                    ai_turns.append(close_turn)
                    self._record_turn_to_context(close_turn)
                    self.state = SessionState.ENDED
                    break

        return ai_turns

    def _select_smart_speaker(self, ai_only: bool = True) -> str:
        """
        Select next speaker using smart logic.

        Args:
            ai_only: If True, only return AI agent names (Jordan/Sam).
                     If False, may return participant name.
        """
        if self.use_smart_agents and isinstance(self.system_manager, SmartSystemManager):
            selected = self.system_manager.decide_next_speaker_strategic(
                self.turns,
                provoker_name="Jordan",
                mediator_name="Sam",
                candidate_name=self.participant_name,
            )
            # If ai_only and selected is human, fall back to alternating AI
            if ai_only and selected == self.participant_name:
                return "Jordan" if len(self.turns) % 2 == 0 else "Sam"
            return selected
        else:
            # Fallback to alternating
            return "Jordan" if len(self.turns) % 2 == 0 else "Sam"

    async def _generate_smart_response(
        self,
        agent,
        speaker_name: str,
        tension: float,
        candidate_last_turn: Optional[Turn],
        context: str = "",
    ) -> str:
        """Generate response from smart agent with appropriate parameters."""
        if isinstance(agent, SmartProvokerAgent):
            return await agent.generate_response(
                context=context or self._get_case_context(),
                tension_level=tension,
                candidate_last_turn=candidate_last_turn,
            )
        elif isinstance(agent, ActiveMediatorAgent):
            # Determine if should advance
            should_advance = self.discussion_context.turns_in_phase >= 3
            return await agent.generate_response(
                context=context or self._get_case_context(),
                tension_level=tension,
                should_advance=should_advance,
            )
        elif isinstance(agent, SmartSystemManager):
            return await agent.generate_response(context)
        else:
            # Fallback for basic agents
            return await agent.generate_response(
                context=context or self._get_case_context(),
                tension_level=tension,
            )

    def _get_case_context(self) -> str:
        """Get case study context instruction for agents."""
        if not self.case_study:
            return ""
        return (
            "IMPORTANT: This is a consulting case study. The human candidate must "
            "lead the analysis. Do NOT propose frameworks, structure, or analytical "
            "approaches. Only react to what the candidate says — challenge weak "
            "reasoning, ask for clarification, or support good points."
        )

    async def finalize_session_output(
        self,
        participant_id: str,
        profile: Optional[PersonalityProfile] = None,
    ) -> SessionOutput:
        """
        Finalize session with optional evidence-based analysis.

        Returns standard SessionOutput for backwards compatibility,
        but also generates evidence-based assessment internally.
        """
        # Get standard output
        output = await super().finalize_session_output(participant_id, profile)

        # Generate evidence-based analysis if smart agents were used
        if self.use_smart_agents:
            try:
                await self._generate_evidence_based_analysis(participant_id)
            except Exception as e:
                # Log error but don't fail the session
                print(f"Warning: Evidence-based analysis failed: {e}")

        return output

    async def _generate_evidence_based_analysis(self, participant_id: str) -> None:
        """Generate evidence-based analysis using the new pipeline."""
        try:
            from pipeline.turn_analyzer import TurnAnalyzer
            from pipeline.assessment_builder import build_evidence_based_assessment

            # Create analyzer
            case_context = ""
            if self.case_study:
                case_context = f"{self.case_study.company_name} ({self.case_study.industry}): {self.case_study.problem_statement}"

            analyzer = TurnAnalyzer(
                client=self.client,
                case_context=case_context,
                candidate_name=self.participant_name,
            )

            # Build revealed data by turn
            revealed_by_turn = {}
            revealed_so_far = set()
            for turn in self.turns:
                if turn.speaker == SpeakerRole.CANDIDATE:
                    # Check what was revealed after this turn
                    if self.case_study:
                        matched = self.case_study.match_categories(turn.content)
                        revealed_so_far.update(matched)
                    revealed_by_turn[turn.turn_number] = list(revealed_so_far)

            # Analyze all turns
            self._turn_analyses = await analyzer.analyze_conversation(
                turns=self.turns,
                revealed_data_by_turn=revealed_by_turn,
            )

            # Build assessment
            self._evidence_assessment = build_evidence_based_assessment(
                session_id=self.session_id,
                candidate_name=self.participant_name,
                turn_analyses=self._turn_analyses,
            )

        except ImportError:
            # Analysis modules not available
            pass

    def get_evidence_assessment(self):
        """Get the evidence-based assessment if available."""
        return self._evidence_assessment

    def get_competency_coverage(self) -> dict:
        """Get current competency coverage summary."""
        return self.discussion_context.competency_tracker.get_coverage_summary()

    def get_discussion_phase(self) -> str:
        """Get current discussion phase."""
        return self.discussion_context.current_phase.value

    def get_phase_guidance(self) -> str:
        """Get guidance for current phase."""
        return self.discussion_context.get_phase_guidance()

    def get_targeting_info(self) -> dict:
        """Get info about what competencies are being targeted."""
        if isinstance(self.provoker, SmartProvokerAgent):
            return self.provoker.get_targeting_summary()
        return {}

    def to_state_dict(self) -> dict:
        """Serialize engine state including discussion context."""
        state = super().to_state_dict()

        # Add discussion context state
        state["discussion_context"] = {
            "current_phase": self.discussion_context.current_phase.value,
            "turns_in_phase": self.discussion_context.turns_in_phase,
            "total_turns": self.discussion_context.total_turns,
            "candidate_turns": self.discussion_context.candidate_turns,
            "tension_level": self.discussion_context.tension_level,
            "data_revealed": list(self.discussion_context.data_revealed),
            "data_requested": list(self.discussion_context.data_requested),
            "hypotheses_stated": self.discussion_context.hypotheses_stated,
            "has_recommendation": self.discussion_context.has_recommendation,
        }

        # Add competency coverage
        state["competency_coverage"] = self.get_competency_coverage()

        return state

    def restore_from_state(self, state: dict) -> None:
        """Restore engine state including discussion context."""
        super().restore_from_state(state)

        # Restore discussion context
        if "discussion_context" in state:
            ctx = state["discussion_context"]
            self.discussion_context.current_phase = DiscussionPhase(ctx.get("current_phase", "opening"))
            self.discussion_context.turns_in_phase = ctx.get("turns_in_phase", 0)
            self.discussion_context.total_turns = ctx.get("total_turns", 0)
            self.discussion_context.candidate_turns = ctx.get("candidate_turns", 0)
            self.discussion_context.tension_level = ctx.get("tension_level", 0.3)
            self.discussion_context.data_revealed = set(ctx.get("data_revealed", []))
            self.discussion_context.data_requested = set(ctx.get("data_requested", []))
            self.discussion_context.hypotheses_stated = ctx.get("hypotheses_stated", [])
            self.discussion_context.has_recommendation = ctx.get("has_recommendation", False)

        # Update smart agents with context
        if self.use_smart_agents:
            if isinstance(self.provoker, SmartProvokerAgent):
                self.provoker.set_context(self.discussion_context)
            if isinstance(self.mediator, ActiveMediatorAgent):
                self.mediator.set_context(self.discussion_context)
            if isinstance(self.system_manager, SmartSystemManager):
                self.system_manager.set_context(self.discussion_context)
