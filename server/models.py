"""
Pydantic models for V3 Server API.

Supports dual-mode study flow:
- Mode 1: Case Study Interview (logical assessment)
- Mode 2: Group Discussion (personality assessment)
- Within-subject design: participants complete both modes (counterbalanced)
"""

from datetime import datetime
from enum import Enum
from typing import Optional, Any

from pydantic import BaseModel, Field

from utils.models import (
    PersonalityVector,
    InterviewMode,
    SessionState,
    LogicAssessment,
    PersonalityAssessment,
    CaseSessionStats,
    GroupSessionStats,
)


# =============================================================================
# STUDY FLOW ENUMS
# =============================================================================

class StudyCondition(str, Enum):
    """Counterbalanced study condition."""
    CASE_FIRST = "case_first"    # Mode 1 → Mode 2
    GROUP_FIRST = "group_first"  # Mode 2 → Mode 1


class StudyPhase(str, Enum):
    """Current phase in the study flow."""
    CONSENT = "consent"
    BFI44 = "bfi44"
    MODE_1_INTERVIEW = "mode_1_interview"
    MODE_1_COMPLETE = "mode_1_complete"
    MODE_2_INTERVIEW = "mode_2_interview"
    MODE_2_COMPLETE = "mode_2_complete"
    SURVEY = "survey"
    COMPLETE = "complete"


# =============================================================================
# PARTICIPANT MODELS
# =============================================================================

class BFI44Response(BaseModel):
    """Raw BFI-44 questionnaire submission."""
    responses: dict[int, int] = Field(
        description="Item number (1-44) -> Likert value (1-5)"
    )
    duration_seconds: Optional[float] = None


class PostSessionSurvey(BaseModel):
    """Post-session experience survey."""
    # Mode 1 ratings
    case_naturalness: int = Field(ge=1, le=5)
    case_challenge: int = Field(ge=1, le=5)
    case_fairness: int = Field(ge=1, le=5)

    # Mode 2 ratings
    group_naturalness: int = Field(ge=1, le=5)
    group_authenticity: int = Field(ge=1, le=5)
    group_engagement: int = Field(ge=1, le=5)

    # Overall
    overall_recommendation: int = Field(ge=1, le=5)
    preferred_mode: str = Field(default="")  # "case", "group", "both", "neither"
    open_feedback: str = Field(default="")

    def mean_case_score(self) -> float:
        return (self.case_naturalness + self.case_challenge + self.case_fairness) / 3.0

    def mean_group_score(self) -> float:
        return (self.group_naturalness + self.group_authenticity + self.group_engagement) / 3.0


class ParticipantRecord(BaseModel):
    """Complete record for a study participant (within-subject design)."""
    participant_id: str
    name: str = ""
    email: Optional[str] = None

    # Consent
    consent_given: bool = False
    consent_timestamp: Optional[datetime] = None

    # Study condition (counterbalanced)
    condition: StudyCondition = StudyCondition.CASE_FIRST
    current_phase: StudyPhase = StudyPhase.CONSENT

    # BFI-44 ground truth
    bfi44_raw: Optional[dict[int, int]] = None
    bfi44_scores: Optional[PersonalityVector] = None
    bfi44_duration_seconds: Optional[float] = None

    # Mode 1: Case Study
    case_scenario_id: Optional[str] = None
    case_session_id: Optional[str] = None
    case_completed: bool = False
    case_assessment: Optional[LogicAssessment] = None
    case_stats: Optional[CaseSessionStats] = None

    # Mode 2: Group Discussion
    group_scenario_id: Optional[str] = None
    group_session_id: Optional[str] = None
    group_completed: bool = False
    group_assessment: Optional[PersonalityAssessment] = None
    group_stats: Optional[GroupSessionStats] = None

    # Post-study
    survey: Optional[PostSessionSurvey] = None
    created_at: datetime = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

    def get_next_mode(self) -> Optional[InterviewMode]:
        """Get the next interview mode based on condition and progress."""
        if self.condition == StudyCondition.CASE_FIRST:
            if not self.case_completed:
                return InterviewMode.CASE_STUDY
            elif not self.group_completed:
                return InterviewMode.GROUP_DISCUSSION
        else:
            if not self.group_completed:
                return InterviewMode.GROUP_DISCUSSION
            elif not self.case_completed:
                return InterviewMode.CASE_STUDY
        return None


# =============================================================================
# API REQUEST/RESPONSE MODELS
# =============================================================================

class CreateParticipantRequest(BaseModel):
    """Request to create a new participant."""
    name: str
    email: Optional[str] = None


class CreateParticipantResponse(BaseModel):
    """Response after creating a participant."""
    participant_id: str
    condition: StudyCondition
    first_mode: str  # "case" or "group"


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
    next_phase: StudyPhase


class CreateSessionRequest(BaseModel):
    """Request to create an interview session."""
    participant_id: str
    mode: InterviewMode


class CreateSessionResponse(BaseModel):
    """Response after session creation."""
    session_id: str
    mode: InterviewMode
    opening_messages: list[dict]
    # Mode 1 specific
    case_data: list[dict] = []
    problem_statement: str = ""
    company_name: str = ""
    # Mode 2 specific
    scenario_brief: str = ""
    agents: list[str] = []


class SessionStatusResponse(BaseModel):
    """Current status of a session."""
    session_id: str
    mode: InterviewMode
    state: SessionState
    conversation: list[dict]
    elapsed_seconds: float
    remaining_seconds: float
    # Mode-specific
    revealed_data: dict = {}  # Mode 1: revealed case data
    trait_coverage: dict = {}  # Mode 2: trait observation coverage


class SubmitMessageRequest(BaseModel):
    """Request to submit participant message."""
    content: str
    target_speaker: Optional[str] = None  # Mode 2: @mention


class SubmitMessageResponse(BaseModel):
    """Response with AI-generated turns."""
    ai_turns: list[dict]
    session_state: SessionState
    elapsed_seconds: float
    remaining_seconds: float


class EndSessionRequest(BaseModel):
    """Request to end a session."""
    session_id: str


class EndSessionResponse(BaseModel):
    """Response after ending session."""
    session_id: str
    mode: InterviewMode
    next_phase: StudyPhase
    # Assessment preview (full assessment in participant record)
    summary: dict = {}


class SurveySubmitRequest(BaseModel):
    """Request to submit post-study survey."""
    case_naturalness: int = Field(ge=1, le=5)
    case_challenge: int = Field(ge=1, le=5)
    case_fairness: int = Field(ge=1, le=5)
    group_naturalness: int = Field(ge=1, le=5)
    group_authenticity: int = Field(ge=1, le=5)
    group_engagement: int = Field(ge=1, le=5)
    overall_recommendation: int = Field(ge=1, le=5)
    preferred_mode: str = ""
    open_feedback: str = ""


# =============================================================================
# HR DASHBOARD MODELS
# =============================================================================

class CandidateSummary(BaseModel):
    """Summary view of a candidate for HR dashboard."""
    participant_id: str
    name: str
    completed_at: Optional[datetime] = None

    # Mode 1 summary
    logic_overall_score: Optional[float] = None
    logic_strengths: list[str] = []
    logic_weaknesses: list[str] = []

    # Mode 2 summary
    personality_vector: Optional[PersonalityVector] = None
    personality_strengths: list[str] = []
    personality_areas: list[str] = []

    # Combined
    overall_fit_score: Optional[float] = None


class CandidateComparison(BaseModel):
    """Multi-candidate comparison view."""
    candidates: list[CandidateSummary]
    dimension_rankings: dict[str, list[str]] = {}  # dimension -> [pid, pid, ...]


class CandidateReport(BaseModel):
    """Full candidate report for PDF export."""
    participant_id: str
    name: str
    assessment_date: datetime

    # BFI-44 ground truth
    bfi44_scores: Optional[PersonalityVector] = None

    # Mode 1 full assessment
    logic_assessment: Optional[LogicAssessment] = None
    case_stats: Optional[CaseSessionStats] = None

    # Mode 2 full assessment
    personality_assessment: Optional[PersonalityAssessment] = None
    group_stats: Optional[GroupSessionStats] = None

    # Validation metrics (Mode 2 vs BFI-44)
    personality_accuracy: Optional[dict] = None

    # Survey feedback
    survey: Optional[PostSessionSurvey] = None
