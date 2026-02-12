"""
V3 Core Data Models

Defines all shared data structures for the dual-mode interview platform:
- Mode 1: Case Study Interview (logical assessment)
- Mode 2: Group Discussion (personality assessment)
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import datetime


# =============================================================================
# ENUMS
# =============================================================================

class InterviewMode(Enum):
    """The two assessment modes in V3."""
    CASE_STUDY = "case_study"       # Mode 1: 1-on-1 logical assessment
    GROUP_DISCUSSION = "group"       # Mode 2: 1-to-many personality assessment


class SessionState(Enum):
    """State machine for interview sessions."""
    CREATED = "created"
    OPENING = "opening"
    ACTIVE = "active"
    WRAPPING_UP = "wrapping_up"
    ENDED = "ended"


class SpeakerRole(Enum):
    """Role of each speaker in the conversation."""
    CANDIDATE = "candidate"          # Human participant
    FACILITATOR = "facilitator"      # Mode 1: Data clerk / Mode 2: Not used
    ALEX = "alex"                    # Mode 2: Assertive Challenger
    JORDAN = "jordan"                # Mode 2: Supportive Collaborator
    RILEY = "riley"                  # Mode 2: Quiet Skeptic


class DiscussionPhase(Enum):
    """Phases of a group discussion (Mode 2)."""
    INTRODUCTION = "introduction"
    EXPLORATION = "exploration"
    CONFLICT = "conflict"
    RESOLUTION = "resolution"
    CLOSING = "closing"


class BigFiveTrait(Enum):
    """Big Five personality traits (OCEAN)."""
    OPENNESS = "openness"
    CONSCIENTIOUSNESS = "conscientiousness"
    EXTRAVERSION = "extraversion"
    AGREEABLENESS = "agreeableness"
    NEUROTICISM = "neuroticism"


# =============================================================================
# DATA CLASSES - SHARED
# =============================================================================

@dataclass
class PersonalityVector:
    """Big Five personality scores (0.0 - 1.0 scale)."""
    O: float = 0.5  # Openness
    C: float = 0.5  # Conscientiousness
    E: float = 0.5  # Extraversion
    A: float = 0.5  # Agreeableness
    N: float = 0.5  # Neuroticism

    def to_dict(self) -> dict[str, float]:
        return {"O": self.O, "C": self.C, "E": self.E, "A": self.A, "N": self.N}

    @classmethod
    def from_dict(cls, d: dict[str, float]) -> "PersonalityVector":
        return cls(O=d.get("O", 0.5), C=d.get("C", 0.5), E=d.get("E", 0.5),
                   A=d.get("A", 0.5), N=d.get("N", 0.5))


@dataclass
class Turn:
    """A single conversation turn."""
    turn_number: int
    speaker_role: SpeakerRole
    speaker_name: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)

    # Optional metadata
    word_count: int = 0
    is_question: bool = False

    def __post_init__(self):
        if self.word_count == 0:
            self.word_count = len(self.content.split())
        if not self.is_question:
            self.is_question = "?" in self.content


@dataclass
class Evidence:
    """A piece of evidence (quote) supporting an assessment score."""
    quote: str
    turn_number: int
    demonstrates: str  # What behavior/skill this quote demonstrates
    signal_direction: str = "neutral"  # "high", "low", "neutral"
    signal_strength: str = "moderate"  # "weak", "moderate", "strong"


# =============================================================================
# DATA CLASSES - MODE 1: CASE STUDY
# =============================================================================

@dataclass
class CaseStudyData:
    """Case study with gated information categories."""
    id: str
    company_name: str
    industry: str
    problem_statement: str
    data_categories: dict[str, dict]  # category_id -> {keywords, data, revealed}

    def match_categories(self, query: str) -> list[str]:
        """Find categories matching keywords in the query."""
        query_lower = query.lower()
        matched = []
        for cat_id, cat_info in self.data_categories.items():
            if cat_info.get("revealed", False):
                continue
            for keyword in cat_info.get("keywords", []):
                if keyword.lower() in query_lower:
                    matched.append(cat_id)
                    break
        return matched

    def reveal_category(self, category_id: str) -> Optional[str]:
        """Reveal a category and return its data."""
        if category_id in self.data_categories:
            self.data_categories[category_id]["revealed"] = True
            return self.data_categories[category_id].get("data", "")
        return None

    def get_revealed_data(self) -> dict[str, str]:
        """Get all revealed data categories."""
        return {
            cat_id: cat_info["data"]
            for cat_id, cat_info in self.data_categories.items()
            if cat_info.get("revealed", False)
        }


@dataclass
class LogicDimensionScore:
    """Score for one logical assessment dimension with evidence."""
    dimension: str
    score: int  # 1-5
    confidence: float  # 0.0-1.0
    evidence: list[Evidence] = field(default_factory=list)
    absent_behaviors: list[str] = field(default_factory=list)
    rubric_justification: str = ""


@dataclass
class LogicAssessment:
    """Complete logical assessment for Mode 1."""
    problem_structuring: LogicDimensionScore
    hypothesis_thinking: LogicDimensionScore
    quantitative_reasoning: LogicDimensionScore
    data_synthesis: LogicDimensionScore
    recommendation_quality: LogicDimensionScore
    communication_clarity: LogicDimensionScore

    overall_score: float = 0.0  # Average of 6 dimensions
    strengths: list[str] = field(default_factory=list)
    development_areas: list[str] = field(default_factory=list)

    def __post_init__(self):
        scores = [
            self.problem_structuring.score,
            self.hypothesis_thinking.score,
            self.quantitative_reasoning.score,
            self.data_synthesis.score,
            self.recommendation_quality.score,
            self.communication_clarity.score,
        ]
        self.overall_score = sum(scores) / len(scores)


@dataclass
class CaseSessionStats:
    """Behavioral statistics computed from a case study session."""
    total_duration_seconds: int = 0
    time_to_first_data_request: int = 0
    time_to_first_hypothesis: int = 0
    time_spent_in_synthesis: int = 0

    data_categories_requested: int = 0
    data_categories_available: int = 0
    data_coverage_ratio: float = 0.0
    data_requests_before_hypothesis: int = 0

    total_candidate_turns: int = 0
    avg_words_per_turn: float = 0.0
    questions_asked: int = 0
    quantitative_statements: int = 0
    framework_mentions: int = 0

    signposting_count: int = 0
    hypothesis_statements: int = 0
    synthesis_statements: int = 0


# =============================================================================
# DATA CLASSES - MODE 2: GROUP DISCUSSION
# =============================================================================

@dataclass
class AgentProfile:
    """Profile for an AI agent in group discussions."""
    name: str
    role: str
    personality: PersonalityVector
    purpose: str  # What traits this agent is designed to elicit
    behavioral_instructions: str
    voice_settings: dict = field(default_factory=lambda: {"pitch": 1.0, "rate": 1.0})


@dataclass
class GroupScenarioPhase:
    """A phase within a group discussion scenario."""
    name: str
    turns: int
    style: str  # "neutral", "agreement", "disagreement", "consensus"
    goal: str = ""
    trigger: str = ""


@dataclass
class GroupScenario:
    """A behavioral scenario for group discussion."""
    id: str
    title: str
    brief: str
    primary_traits_elicited: list[str]
    secondary_traits_elicited: list[str]
    phases: list[GroupScenarioPhase]


@dataclass
class TraitFacetScore:
    """Score for a specific facet of a Big Five trait."""
    facet_name: str
    score: float  # 0.0-1.0
    evidence: list[Evidence] = field(default_factory=list)


@dataclass
class TraitScore:
    """Score for one Big Five trait with facets and evidence."""
    trait: BigFiveTrait
    score: float  # 0.0-1.0
    confidence: float  # 0.0-1.0 (inter-judge agreement)
    facets: list[TraitFacetScore] = field(default_factory=list)
    evidence: list[Evidence] = field(default_factory=list)


@dataclass
class PersonalityAssessment:
    """Complete personality assessment for Mode 2."""
    openness: TraitScore
    conscientiousness: TraitScore
    extraversion: TraitScore
    agreeableness: TraitScore
    neuroticism: TraitScore

    overall_confidence: float = 0.0
    behavioral_summary: str = ""
    strengths: list[str] = field(default_factory=list)
    development_areas: list[str] = field(default_factory=list)

    def to_vector(self) -> PersonalityVector:
        return PersonalityVector(
            O=self.openness.score,
            C=self.conscientiousness.score,
            E=self.extraversion.score,
            A=self.agreeableness.score,
            N=self.neuroticism.score,
        )


@dataclass
class GroupSessionStats:
    """Discussion dynamics statistics for Mode 2."""
    total_duration_seconds: int = 0
    total_turns: int = 0

    # Speaking distribution
    candidate_turns: int = 0
    candidate_word_count: int = 0
    candidate_avg_words_per_turn: float = 0.0

    # Interaction patterns
    times_addressed_others_by_name: int = 0
    times_asked_questions: int = 0
    times_expressed_disagreement: int = 0
    times_acknowledged_others: int = 0
    times_proposed_new_ideas: int = 0

    # Phase engagement
    phase_engagement: dict[str, str] = field(default_factory=dict)  # phase -> "low"/"med"/"high"


# =============================================================================
# SESSION OUTPUT
# =============================================================================

@dataclass
class SessionOutput:
    """Complete output from an interview session (either mode)."""
    session_id: str
    participant_id: str
    participant_name: str
    mode: InterviewMode

    # Timing
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_seconds: int = 0

    # Conversation
    turns: list[Turn] = field(default_factory=list)

    # Mode-specific assessment
    logic_assessment: Optional[LogicAssessment] = None  # Mode 1
    personality_assessment: Optional[PersonalityAssessment] = None  # Mode 2

    # Mode-specific stats
    case_stats: Optional[CaseSessionStats] = None  # Mode 1
    group_stats: Optional[GroupSessionStats] = None  # Mode 2

    # Ground truth (from BFI-44)
    bfi44_ground_truth: Optional[PersonalityVector] = None
