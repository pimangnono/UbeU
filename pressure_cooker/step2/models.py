"""
Pydantic models for Step 2: Live Interview Platform.
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.models import PersonalityVector, SessionOutput


class SessionState(str, Enum):
    """States for a live interview session."""
    CREATED = "created"
    OPENING = "opening"
    ACTIVE = "active"
    WRAPPING_UP = "wrapping_up"
    ENDED = "ended"


class BFI44Response(BaseModel):
    """Raw BFI-44 questionnaire submission."""
    participant_id: str
    responses: dict[int, int] = Field(
        description="Item number (1-44) -> Likert value (1-5)"
    )
    timestamp: datetime = Field(default_factory=datetime.now)
    duration_seconds: Optional[float] = Field(
        default=None,
        description="Time spent on questionnaire in seconds",
    )


class PostSessionSurvey(BaseModel):
    """Post-session experience survey (5 Likert items + open feedback)."""
    participant_id: str
    naturalness: int = Field(ge=1, le=5, description="How natural did the conversation feel?")
    authenticity: int = Field(ge=1, le=5, description="How authentic did the AI characters seem?")
    realism: int = Field(ge=1, le=5, description="How realistic was the workplace scenario?")
    engagement: int = Field(ge=1, le=5, description="How engaged were you in the discussion?")
    recommendation: int = Field(ge=1, le=5, description="Would you recommend this experience?")
    open_feedback: str = Field(default="", description="Free-text feedback")
    timestamp: datetime = Field(default_factory=datetime.now)

    def mean_score(self) -> float:
        """Average of all 5 Likert items."""
        return (
            self.naturalness + self.authenticity + self.realism
            + self.engagement + self.recommendation
        ) / 5.0


class ParticipantRecord(BaseModel):
    """Complete record for a study participant."""
    participant_id: str
    name: str = Field(default="", description="Participant's display name for the interview")
    consent_given: bool = Field(default=False)
    consent_timestamp: Optional[datetime] = Field(default=None)
    bfi44_raw: Optional[dict[int, int]] = Field(default=None)
    bfi44_scores: Optional[PersonalityVector] = Field(default=None)
    bfi44_duration_seconds: Optional[float] = Field(default=None)
    assigned_scenario: Optional[str] = Field(default=None)
    session_id: Optional[str] = Field(default=None)
    survey: Optional[PostSessionSurvey] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)


class Step2SessionOutput(BaseModel):
    """Wraps SessionOutput with Step 2-specific ground truth."""
    session_output: SessionOutput
    participant_id: str
    participant_name: str = Field(default="")
    bfi44_ground_truth: PersonalityVector
    survey: Optional[PostSessionSurvey] = Field(default=None)


# --- API request/response models ---

class CreateParticipantRequest(BaseModel):
    """Request to create a new participant."""
    name: str = Field(description="Participant's first name for the interview")


class CreateParticipantResponse(BaseModel):
    """Response after creating a participant."""
    participant_id: str
    assigned_scenario: str


class ConsentRequest(BaseModel):
    """Request to record consent."""
    consent: bool


class BFI44SubmitRequest(BaseModel):
    """Request to submit BFI-44 responses."""
    responses: dict[int, int]
    duration_seconds: Optional[float] = None


class BFI44SubmitResponse(BaseModel):
    """Response after BFI-44 scoring."""
    participant_id: str
    scores_computed: bool


class CreateSessionRequest(BaseModel):
    """Request to create a live interview session."""
    participant_id: str


class CreateSessionResponse(BaseModel):
    """Response after session creation."""
    session_id: str
    opening_messages: list[dict]  # list of {"speaker": str, "content": str}


class SessionStatusResponse(BaseModel):
    """Current status of a session."""
    session_id: str
    state: SessionState
    conversation: list[dict]  # list of {"speaker": str, "speaker_role": str, "content": str}
    elapsed_seconds: float
    remaining_seconds: float


class SubmitMessageRequest(BaseModel):
    """Request to submit a human message."""
    content: str


class SubmitMessageResponse(BaseModel):
    """Response with AI-generated turns after human input."""
    ai_turns: list[dict]  # list of {"speaker": str, "content": str}
    session_state: SessionState
    elapsed_seconds: float
    remaining_seconds: float


class SurveySubmitRequest(BaseModel):
    """Request to submit post-session survey."""
    naturalness: int = Field(ge=1, le=5)
    authenticity: int = Field(ge=1, le=5)
    realism: int = Field(ge=1, le=5)
    engagement: int = Field(ge=1, le=5)
    recommendation: int = Field(ge=1, le=5)
    open_feedback: str = Field(default="")
