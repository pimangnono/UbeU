"""
Base Engine: Shared infrastructure for both interview modes.

Provides:
- Session management (state, timing, turn tracking)
- LLM client integration
- Common turn creation utilities
"""

import time
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from utils.models import (
    Turn,
    SessionState,
    SpeakerRole,
    InterviewMode,
    SessionOutput,
)

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


# Timer constants (seconds)
SESSION_MAX_SECONDS = 15 * 60   # 15 minutes hard stop
WARN_AT_SECONDS = 12 * 60       # 12 minutes: facilitator warns
WRAPUP_AT_SECONDS = 14 * 60     # 14 minutes: start wrapping up


class BaseEngine(ABC):
    """
    Abstract base class for interview engines.

    Provides shared functionality for:
    - Mode 1 (CaseEngine): 1-on-1 case study interview
    - Mode 2 (GroupEngine): 1-to-many group discussion
    """

    def __init__(
        self,
        client: "LLMClient",
        participant_id: str,
        participant_name: str,
        mode: InterviewMode,
    ):
        self.client = client
        self.participant_id = participant_id
        self.participant_name = participant_name
        self.mode = mode
        self.session_id = str(uuid.uuid4())[:8]

        # Session state
        self.turns: list[Turn] = []
        self.state = SessionState.CREATED
        self.start_time: Optional[float] = None
        self._turn_counter = 0
        self._warned_time = False
        self._wrapping_up = False

        # LLM latency compensation (accumulated time spent waiting for API)
        self._llm_wait_time = 0.0

    # =========================================================================
    # TIMING PROPERTIES
    # =========================================================================

    @property
    def elapsed_seconds(self) -> float:
        """Seconds since session started (excluding LLM wait time)."""
        if self.start_time is None:
            return 0.0
        raw_elapsed = time.time() - self.start_time
        return max(0.0, raw_elapsed - self._llm_wait_time)

    @property
    def remaining_seconds(self) -> float:
        """Seconds remaining before hard stop."""
        return max(0.0, SESSION_MAX_SECONDS - self.elapsed_seconds)

    @property
    def is_time_expired(self) -> bool:
        """Whether the session has exceeded the time limit."""
        return self.elapsed_seconds >= SESSION_MAX_SECONDS

    @property
    def should_warn_time(self) -> bool:
        """Whether to warn about remaining time."""
        return not self._warned_time and self.elapsed_seconds >= WARN_AT_SECONDS

    @property
    def should_wrap_up(self) -> bool:
        """Whether to start wrapping up the session."""
        return not self._wrapping_up and self.elapsed_seconds >= WRAPUP_AT_SECONDS

    def add_llm_wait_time(self, seconds: float):
        """Add time spent waiting for LLM response (for latency compensation)."""
        self._llm_wait_time += seconds

    # =========================================================================
    # TURN MANAGEMENT
    # =========================================================================

    def _create_turn(
        self,
        speaker_role: SpeakerRole,
        speaker_name: str,
        content: str,
    ) -> Turn:
        """Create a new turn with auto-incrementing turn number."""
        self._turn_counter += 1
        return Turn(
            turn_number=self._turn_counter,
            speaker_role=speaker_role,
            speaker_name=speaker_name,
            content=content,
            timestamp=datetime.now(),
        )

    def get_conversation_history(self, max_turns: Optional[int] = None) -> str:
        """Format conversation history for prompts."""
        turns_to_format = self.turns
        if max_turns:
            turns_to_format = self.turns[-max_turns:]

        lines = []
        for turn in turns_to_format:
            lines.append(f"[Turn {turn.turn_number}] {turn.speaker_name}: {turn.content}")
        return "\n".join(lines)

    def get_candidate_turns(self) -> list[Turn]:
        """Get only the candidate's turns."""
        return [t for t in self.turns if t.speaker_role == SpeakerRole.CANDIDATE]

    # =========================================================================
    # ABSTRACT METHODS (implemented by subclasses)
    # =========================================================================

    @abstractmethod
    async def generate_opening(self) -> list[Turn]:
        """Generate the opening of the interview."""
        pass

    @abstractmethod
    async def submit_candidate_turn(self, content: str) -> None:
        """Record the candidate's response."""
        pass

    @abstractmethod
    async def generate_ai_response(self) -> list[Turn]:
        """Generate AI response(s) to the candidate."""
        pass

    @abstractmethod
    def to_session_output(self) -> SessionOutput:
        """Convert session to output format."""
        pass

    # =========================================================================
    # SESSION LIFECYCLE
    # =========================================================================

    def start_session(self):
        """Mark session as started."""
        self.start_time = time.time()
        self.state = SessionState.OPENING

    def end_session(self):
        """Mark session as ended."""
        self.state = SessionState.ENDED

    def mark_active(self):
        """Transition to active state after opening."""
        self.state = SessionState.ACTIVE

    def mark_wrapping_up(self):
        """Transition to wrapping up state."""
        self._wrapping_up = True
        self.state = SessionState.WRAPPING_UP

    def mark_warned(self):
        """Mark that time warning has been given."""
        self._warned_time = True
