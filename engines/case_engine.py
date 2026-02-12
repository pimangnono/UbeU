"""
Case Engine: Mode 1 - 1-on-1 Case Study Interview for Logical Assessment.

Implements a faithful simulation of a management consulting case interview.
The candidate works 1-on-1 with an AI facilitator who plays the role of a
data clerk holding case information.

Key Features:
- Data gating: Information revealed only when candidate asks
- No guidance: Facilitator never suggests approaches or evaluates reasoning
- Evidence tracking: All turns captured for post-session evaluation

What Mode 1 Assesses:
- Problem Structuring
- Hypothesis-Driven Thinking
- Quantitative Reasoning
- Data Synthesis
- Recommendation Quality
- Communication Clarity

What Mode 1 Does NOT Assess:
- Personality traits (delegated to Mode 2)
- Collaboration skills (no group dynamics)
"""

import time
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from engines.base_engine import BaseEngine
from agents.facilitator_agent import FacilitatorAgent
from utils.models import (
    Turn,
    SpeakerRole,
    SessionState,
    InterviewMode,
    SessionOutput,
    CaseStudyData,
    CaseSessionStats,
)

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


class CaseEngine(BaseEngine):
    """
    Engine for 1-on-1 case study interviews (Mode 1).

    The candidate interacts only with a single Facilitator agent who:
    - Presents the case brief
    - Provides data when asked specific questions
    - Never guides, suggests, or evaluates
    """

    def __init__(
        self,
        client: "LLMClient",
        participant_id: str,
        participant_name: str,
        case_study: CaseStudyData,
    ):
        super().__init__(
            client=client,
            participant_id=participant_id,
            participant_name=participant_name,
            mode=InterviewMode.CASE_STUDY,
        )
        self.case_study = case_study
        self.facilitator = FacilitatorAgent(client, case_study)

        # Session statistics tracking
        self._first_data_request_time: Optional[float] = None
        self._first_hypothesis_time: Optional[float] = None
        self._hypothesis_count = 0
        self._question_count = 0
        self._quantitative_statement_count = 0
        self._framework_mention_count = 0
        self._synthesis_start_time: Optional[float] = None

    async def generate_opening(self) -> list[Turn]:
        """
        Generate the case study introduction.

        The facilitator presents the company, industry, and problem statement
        without revealing any hidden data.
        """
        self.start_session()
        opening_turns = []

        # Facilitator introduces the case
        intro = await self.facilitator.generate_opening()
        turn = self._create_turn(SpeakerRole.FACILITATOR, "Facilitator", intro)
        self.turns.append(turn)
        opening_turns.append(turn)

        # Update facilitator's history
        self.facilitator.update_history(self.turns)

        self.mark_active()
        return opening_turns

    async def submit_candidate_turn(self, content: str) -> None:
        """
        Record the candidate's response.

        Also tracks statistics:
        - First data request timing
        - First hypothesis timing
        - Question count
        - Quantitative statements
        - Framework mentions
        """
        turn = self._create_turn(
            SpeakerRole.CANDIDATE,
            self.participant_name,
            content,
        )
        self.turns.append(turn)

        # Track statistics
        self._analyze_candidate_turn(content)

        # Update facilitator's history
        self.facilitator.update_history(self.turns)

    def _analyze_candidate_turn(self, content: str):
        """Analyze candidate turn for statistics tracking."""
        content_lower = content.lower()

        # Track questions (data requests)
        if "?" in content:
            self._question_count += 1
            if self._first_data_request_time is None:
                self._first_data_request_time = self.elapsed_seconds

        # Track hypothesis statements
        hypothesis_phrases = [
            "i hypothesize", "my hypothesis", "i think this is because",
            "my theory is", "i believe the issue is", "the root cause is",
            "i suspect", "this suggests that", "my assumption is"
        ]
        if any(phrase in content_lower for phrase in hypothesis_phrases):
            self._hypothesis_count += 1
            if self._first_hypothesis_time is None:
                self._first_hypothesis_time = self.elapsed_seconds

        # Track quantitative statements (numbers, calculations)
        import re
        numbers = re.findall(r'\d+(?:\.\d+)?(?:%|percent|million|billion|k)?', content_lower)
        calculation_phrases = ["divided by", "multiplied", "equals", "times", "plus", "minus", "="]
        if numbers or any(phrase in content_lower for phrase in calculation_phrases):
            self._quantitative_statement_count += 1

        # Track framework mentions
        framework_phrases = [
            "profit", "revenue", "cost", "market size", "market share",
            "4p", "swot", "porter", "framework", "structure", "first,", "second,",
            "let me break this down", "let me structure", "categories"
        ]
        if any(phrase in content_lower for phrase in framework_phrases):
            self._framework_mention_count += 1

        # Track synthesis phase
        synthesis_phrases = [
            "in conclusion", "to summarize", "putting this together",
            "based on all of this", "my recommendation is", "overall"
        ]
        if any(phrase in content_lower for phrase in synthesis_phrases):
            if self._synthesis_start_time is None:
                self._synthesis_start_time = self.elapsed_seconds

    async def generate_ai_response(self) -> list[Turn]:
        """
        Generate the facilitator's response.

        The facilitator will:
        - Provide data if the candidate asked about a matching category
        - Ask for clarification if the question is vague
        - Never guide or evaluate
        """
        ai_turns = []

        # Check for time warnings first
        if self.should_warn_time:
            minutes_left = int(self.remaining_seconds / 60)
            warning = await self.facilitator.generate_time_warning(minutes_left)
            turn = self._create_turn(SpeakerRole.FACILITATOR, "Facilitator", warning)
            self.turns.append(turn)
            ai_turns.append(turn)
            self.mark_warned()

        # Check for wrap-up
        if self.should_wrap_up:
            closing = await self.facilitator.generate_closing()
            turn = self._create_turn(SpeakerRole.FACILITATOR, "Facilitator", closing)
            self.turns.append(turn)
            ai_turns.append(turn)
            self.mark_wrapping_up()
            return ai_turns

        # Check if time expired
        if self.is_time_expired:
            self.end_session()
            return ai_turns

        # Get the candidate's last turn
        candidate_turns = self.get_candidate_turns()
        if not candidate_turns:
            return ai_turns

        last_candidate_turn = candidate_turns[-1].content

        # Track LLM latency
        start_time = time.time()

        # Generate facilitator response
        response = await self.facilitator.generate_response(last_candidate_turn)

        # Compensate for latency
        latency = time.time() - start_time
        self.add_llm_wait_time(latency)

        turn = self._create_turn(SpeakerRole.FACILITATOR, "Facilitator", response)
        self.turns.append(turn)
        ai_turns.append(turn)

        # Update facilitator's history
        self.facilitator.update_history(self.turns)

        return ai_turns

    def compute_session_stats(self) -> CaseSessionStats:
        """Compute behavioral statistics for the session."""
        candidate_turns = self.get_candidate_turns()
        total_words = sum(t.word_count for t in candidate_turns)
        avg_words = total_words / len(candidate_turns) if candidate_turns else 0

        revealed, total = self.facilitator.get_data_coverage()

        # Count signposting
        signposting_phrases = [
            "first,", "second,", "third,", "finally,", "next,",
            "moving on", "now let's", "to summarize", "in conclusion"
        ]
        signposting_count = sum(
            1 for t in candidate_turns
            for phrase in signposting_phrases
            if phrase in t.content.lower()
        )

        return CaseSessionStats(
            total_duration_seconds=int(self.elapsed_seconds),
            time_to_first_data_request=int(self._first_data_request_time or 0),
            time_to_first_hypothesis=int(self._first_hypothesis_time or 0),
            time_spent_in_synthesis=int(
                self.elapsed_seconds - self._synthesis_start_time
                if self._synthesis_start_time else 0
            ),
            data_categories_requested=revealed,
            data_categories_available=total,
            data_coverage_ratio=revealed / total if total > 0 else 0,
            data_requests_before_hypothesis=self._question_count if self._first_hypothesis_time is None
                else sum(1 for t in candidate_turns[:self._get_hypothesis_turn_index()] if "?" in t.content),
            total_candidate_turns=len(candidate_turns),
            avg_words_per_turn=avg_words,
            questions_asked=self._question_count,
            quantitative_statements=self._quantitative_statement_count,
            framework_mentions=self._framework_mention_count,
            signposting_count=signposting_count,
            hypothesis_statements=self._hypothesis_count,
            synthesis_statements=sum(
                1 for t in candidate_turns
                if any(p in t.content.lower() for p in ["to summarize", "in conclusion", "my recommendation"])
            ),
        )

    def _get_hypothesis_turn_index(self) -> int:
        """Get the turn index where first hypothesis was made."""
        candidate_turns = self.get_candidate_turns()
        hypothesis_phrases = [
            "i hypothesize", "my hypothesis", "i think this is because",
            "my theory is", "i believe the issue is"
        ]
        for i, turn in enumerate(candidate_turns):
            if any(phrase in turn.content.lower() for phrase in hypothesis_phrases):
                return i
        return len(candidate_turns)

    def to_session_output(self) -> SessionOutput:
        """Convert session to output format."""
        return SessionOutput(
            session_id=self.session_id,
            participant_id=self.participant_id,
            participant_name=self.participant_name,
            mode=InterviewMode.CASE_STUDY,
            start_time=datetime.fromtimestamp(self.start_time) if self.start_time else datetime.now(),
            end_time=datetime.now(),
            duration_seconds=int(self.elapsed_seconds),
            turns=self.turns,
            case_stats=self.compute_session_stats(),
        )

    def get_revealed_data(self) -> dict[str, str]:
        """Get all data that was revealed during the session."""
        return self.facilitator.get_revealed_data_summary()

    def get_unrevealed_categories(self) -> list[str]:
        """Get categories that were never requested."""
        all_categories = set(self.case_study.data_categories.keys())
        revealed = self.facilitator.revealed_categories
        return list(all_categories - revealed)
