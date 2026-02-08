"""
Evidence-based analysis models for the Pressure Cooker framework.

These models provide transparent, quote-backed assessments for:
- Per-turn personality trait signals
- Per-turn reasoning quality
- Intent classification with evidence
- Competency scoring with evidence trails

All assessments include direct quotes from candidate responses as evidence.
"""

from enum import Enum
from typing import Literal, Optional
from pydantic import BaseModel, Field

from utils.models import (
    BigFiveTrait,
    IntentCategory,
    SpeakerRole,
    PersonalityVector,
)


# =============================================================================
# Enums for Analysis
# =============================================================================

class TraitDirection(str, Enum):
    """Direction of trait signal on the Big Five spectrum."""
    HIGH = "high"
    LOW = "low"
    NEUTRAL = "neutral"


class LogicalConnectionQuality(str, Enum):
    """Quality of logical reasoning in a response."""
    NONE = "none"          # No logical connection made
    WEAK = "weak"          # Tenuous or flawed logic
    MODERATE = "moderate"  # Sound but incomplete reasoning
    STRONG = "strong"      # Clear, well-supported reasoning


class ContributionType(str, Enum):
    """How a piece of evidence contributes to a score."""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class CompetencyDimension(str, Enum):
    """Competency dimensions being assessed."""
    COLLABORATION = "collaboration"
    LEADERSHIP = "leadership"
    STRESS_MANAGEMENT = "stress_management"
    COMMUNICATION = "communication"
    PROBLEM_SOLVING = "problem_solving"


# =============================================================================
# Per-Turn Analysis Components
# =============================================================================

class TraitSignal(BaseModel):
    """
    Evidence of a personality trait from a single statement.

    Each signal links a specific quote to a Big Five trait indication,
    providing transparency for personality inference.
    """
    trait: BigFiveTrait = Field(description="Which Big Five trait this signals")
    direction: TraitDirection = Field(description="High or low on the trait spectrum")
    signal_strength: float = Field(
        ge=0.0, le=1.0,
        description="How clearly this manifests the trait (0=weak, 1=strong)"
    )
    evidence_quote: str = Field(
        description="Exact words from the response demonstrating the trait"
    )
    reasoning: str = Field(
        description="Explanation of why this quote indicates this trait direction"
    )

    def to_summary(self) -> str:
        """Generate a brief summary of the trait signal."""
        return f"{self.trait.value} ({self.direction.value}): \"{self.evidence_quote[:50]}...\""


class ReasoningAssessment(BaseModel):
    """
    Logic and reasoning quality assessment for a single response.

    Evaluates whether the candidate made assumptions, used data effectively,
    and constructed logical arguments.
    """
    # Assumption tracking
    makes_assumption: bool = Field(
        default=False,
        description="Whether this response contains an assumption"
    )
    assumption_text: Optional[str] = Field(
        default=None,
        description="The specific assumption made, if any"
    )
    assumption_valid: Optional[bool] = Field(
        default=None,
        description="Whether the assumption is valid given available data"
    )
    assumption_evidence: Optional[str] = Field(
        default=None,
        description="Quote showing the assumption"
    )

    # Data usage tracking
    uses_data: bool = Field(
        default=False,
        description="Whether this response references or uses case data"
    )
    data_categories_referenced: list[str] = Field(
        default_factory=list,
        description="Which data categories were mentioned"
    )
    data_categories_used_effectively: list[str] = Field(
        default_factory=list,
        description="Which data categories were used with sound reasoning"
    )

    # Logical quality
    logical_connection_quality: LogicalConnectionQuality = Field(
        default=LogicalConnectionQuality.NONE,
        description="Quality of logical reasoning in this response"
    )
    logic_evidence_quote: Optional[str] = Field(
        default=None,
        description="Key quote demonstrating reasoning quality (good or bad)"
    )
    logic_explanation: Optional[str] = Field(
        default=None,
        description="Explanation of the logical quality assessment"
    )

    # Framework/structure usage
    uses_framework: bool = Field(
        default=False,
        description="Whether candidate applied a structured framework"
    )
    framework_name: Optional[str] = Field(
        default=None,
        description="Name of framework used (e.g., 'profitability tree', 'BCG matrix')"
    )


class IntentAnalysis(BaseModel):
    """
    Intent classification with supporting evidence.

    Provides transparency for why a particular intent was assigned.
    """
    primary_intent: IntentCategory = Field(
        description="Primary classified intent of this turn"
    )
    primary_confidence: float = Field(
        ge=0.0, le=1.0,
        description="Confidence in primary intent classification"
    )
    primary_evidence: str = Field(
        description="Quote supporting the primary intent classification"
    )
    primary_reasoning: str = Field(
        description="Explanation of why this intent was classified"
    )

    secondary_intent: Optional[IntentCategory] = Field(
        default=None,
        description="Secondary intent if response shows mixed signals"
    )
    secondary_confidence: Optional[float] = Field(
        default=None,
        ge=0.0, le=1.0,
        description="Confidence in secondary intent"
    )
    secondary_evidence: Optional[str] = Field(
        default=None,
        description="Quote supporting secondary intent"
    )


class TurnAnalysis(BaseModel):
    """
    Rich evidence-based analysis of a single candidate turn.

    This is the core model for transparent assessment. Each candidate
    response is analyzed for:
    - Intent (with evidence)
    - Personality trait signals (with quotes)
    - Reasoning quality (with evidence)
    - Contextual factors

    This replaces the simple Turn.intent field with full evidence trails.
    """
    # Core turn identification
    turn_number: int = Field(ge=0, description="Sequential turn number")
    speaker: SpeakerRole = Field(description="Who is speaking")
    speaker_name: str = Field(description="Display name of speaker")
    content: str = Field(description="The full response text")

    # Response characteristics
    word_count: int = Field(ge=0, description="Number of words in response")
    sentence_count: int = Field(ge=0, description="Number of sentences")

    # Intent analysis with evidence
    intent_analysis: IntentAnalysis = Field(
        description="Intent classification with supporting evidence"
    )

    # Personality trait signals with evidence
    trait_signals: list[TraitSignal] = Field(
        default_factory=list,
        description="Personality trait indicators found in this response"
    )

    # Reasoning/logic assessment
    reasoning_assessment: Optional[ReasoningAssessment] = Field(
        default=None,
        description="Assessment of logical reasoning quality"
    )

    # Contextual factors
    responding_to_turn: Optional[int] = Field(
        default=None,
        description="Turn number this response is primarily addressing"
    )
    responding_to_speaker: Optional[str] = Field(
        default=None,
        description="Who the candidate is primarily responding to"
    )

    # Data interaction
    data_requested: list[str] = Field(
        default_factory=list,
        description="Data categories explicitly requested in this turn"
    )
    data_received_this_turn: list[str] = Field(
        default_factory=list,
        description="Data categories provided to candidate before this turn"
    )

    # Tension/emotion
    tension_level: float = Field(
        default=0.3,
        ge=0.0, le=1.0,
        description="Current tension level (0=calm, 1=heated)"
    )
    emotional_tone: Optional[str] = Field(
        default=None,
        description="Detected emotional tone (e.g., 'frustrated', 'confident', 'anxious')"
    )

    # Competency signals (for later aggregation)
    competency_signals: dict[str, list[str]] = Field(
        default_factory=dict,
        description="Mapping of competency dimension to evidence quotes"
    )

    def get_trait_signals_for(self, trait: BigFiveTrait) -> list[TraitSignal]:
        """Get all trait signals for a specific Big Five trait."""
        return [s for s in self.trait_signals if s.trait == trait]

    def get_dominant_trait_direction(self, trait: BigFiveTrait) -> Optional[TraitDirection]:
        """Get the dominant direction for a trait based on signals."""
        signals = self.get_trait_signals_for(trait)
        if not signals:
            return None

        high_weight = sum(s.signal_strength for s in signals if s.direction == TraitDirection.HIGH)
        low_weight = sum(s.signal_strength for s in signals if s.direction == TraitDirection.LOW)

        if high_weight > low_weight:
            return TraitDirection.HIGH
        elif low_weight > high_weight:
            return TraitDirection.LOW
        return TraitDirection.NEUTRAL

    def has_strong_reasoning(self) -> bool:
        """Check if this turn demonstrates strong logical reasoning."""
        if not self.reasoning_assessment:
            return False
        return self.reasoning_assessment.logical_connection_quality in [
            LogicalConnectionQuality.STRONG,
            LogicalConnectionQuality.MODERATE
        ]


# =============================================================================
# Evidence-Based Scoring Models
# =============================================================================

class ScoringEvidence(BaseModel):
    """
    Single piece of evidence contributing to a competency score.

    Links a specific quote to its contribution to a competency dimension,
    enabling transparent and auditable scoring.
    """
    turn_number: int = Field(description="Which turn this evidence is from")
    quote: str = Field(description="Exact words from candidate")
    contribution: ContributionType = Field(
        description="Whether this positively or negatively affects the score"
    )
    weight: float = Field(
        ge=0.0, le=1.0,
        description="How much this evidence affects the score"
    )
    explanation: str = Field(
        description="Why this quote contributes to this competency"
    )

    # Optional: link to specific behavior
    behavior_demonstrated: Optional[str] = Field(
        default=None,
        description="Specific behavior this evidences (e.g., 'took_initiative', 'built_on_ideas')"
    )


class TraitEvidence(BaseModel):
    """
    Evidence for personality trait inference aggregated across turns.

    Used in the final assessment to show how personality was inferred.
    """
    turn_number: int = Field(description="Which turn this evidence is from")
    quote: str = Field(description="Exact words demonstrating the trait")
    trait_signal: TraitDirection = Field(description="High or low indication")
    signal_strength: float = Field(
        ge=0.0, le=1.0,
        description="How strongly this evidences the trait"
    )
    explanation: str = Field(description="Why this quote indicates this trait level")


class CompetencyScore(BaseModel):
    """
    A single competency score with full evidence trail.
    """
    dimension: CompetencyDimension = Field(description="Which competency")
    score: float = Field(ge=0.0, le=1.0, description="Final score (0-1)")
    evidence: list[ScoringEvidence] = Field(
        default_factory=list,
        description="All evidence contributing to this score"
    )
    summary: str = Field(
        default="",
        description="Brief explanation of the score"
    )

    # Breakdown
    positive_contributions: int = Field(
        default=0,
        description="Number of positive evidence pieces"
    )
    negative_contributions: int = Field(
        default=0,
        description="Number of negative evidence pieces"
    )

    def get_top_evidence(self, n: int = 3) -> list[ScoringEvidence]:
        """Get the top N most impactful evidence pieces."""
        sorted_evidence = sorted(self.evidence, key=lambda e: e.weight, reverse=True)
        return sorted_evidence[:n]


class PersonalityInference(BaseModel):
    """
    Inferred personality with evidence for each trait.
    """
    inferred_vector: PersonalityVector = Field(
        description="The inferred Big Five personality vector"
    )
    trait_evidence: dict[str, list[TraitEvidence]] = Field(
        default_factory=dict,
        description="Evidence for each trait (keyed by trait name)"
    )
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="Overall confidence in the personality inference"
    )

    def get_evidence_for_trait(self, trait: BigFiveTrait) -> list[TraitEvidence]:
        """Get all evidence for a specific trait."""
        return self.trait_evidence.get(trait.value, [])

    def get_trait_confidence(self, trait: BigFiveTrait) -> float:
        """Get confidence for a specific trait based on evidence quantity and strength."""
        evidence = self.get_evidence_for_trait(trait)
        if not evidence:
            return 0.0
        avg_strength = sum(e.signal_strength for e in evidence) / len(evidence)
        quantity_factor = min(1.0, len(evidence) / 5)  # Max confidence at 5+ pieces
        return avg_strength * quantity_factor


class LogicalAssessmentEvidence(BaseModel):
    """
    Evidence-based logical/analytical assessment.

    Extends the validator output with quote-based evidence.
    """
    # Assumptions with evidence
    assumptions: list[dict] = Field(
        default_factory=list,
        description="Assumptions made: [{assumption, valid, quote, turn_number, explanation}]"
    )

    # Logical gaps with evidence
    logical_gaps: list[dict] = Field(
        default_factory=list,
        description="Logical gaps: [{gap_description, turn_number, quote, severity}]"
    )

    # Scores with evidence
    analytical_depth: int = Field(ge=1, le=5, description="Analytical depth score (1-5)")
    analytical_depth_evidence: list[ScoringEvidence] = Field(
        default_factory=list,
        description="Evidence supporting the analytical depth score"
    )

    recommendation_quality: int = Field(ge=1, le=5, description="Recommendation quality (1-5)")
    recommendation_evidence: list[ScoringEvidence] = Field(
        default_factory=list,
        description="Evidence for recommendation quality score"
    )

    # Data utilization with evidence
    data_utilization: dict = Field(
        default_factory=dict,
        description="Data usage: {category: {status, evidence_quotes, turn_numbers}}"
    )

    summary: str = Field(default="", description="Overall assessment summary")


class EvidenceBasedAssessment(BaseModel):
    """
    Complete transparent assessment with full evidence trails.

    This is the top-level output model that replaces the opaque
    AssessmentMapping with fully traceable scores.
    """
    # Session identification
    session_id: str = Field(description="Session this assessment is for")
    candidate_name: str = Field(description="Name of the candidate assessed")
    total_turns_analyzed: int = Field(description="Number of candidate turns analyzed")

    # Competency scores with evidence
    competency_scores: list[CompetencyScore] = Field(
        default_factory=list,
        description="All competency scores with evidence"
    )

    # Personality inference with evidence
    personality_inference: Optional[PersonalityInference] = Field(
        default=None,
        description="Inferred personality with trait evidence"
    )

    # Logical assessment with evidence
    logical_assessment: Optional[LogicalAssessmentEvidence] = Field(
        default=None,
        description="Logical/analytical assessment with evidence"
    )

    # Per-turn analyses (the raw data)
    turn_analyses: list[TurnAnalysis] = Field(
        default_factory=list,
        description="Detailed analysis of each candidate turn"
    )

    # Summary
    overall_summary: str = Field(
        default="",
        description="High-level summary of candidate performance"
    )
    key_strengths: list[str] = Field(
        default_factory=list,
        description="Key strengths identified with evidence references"
    )
    areas_for_development: list[str] = Field(
        default_factory=list,
        description="Areas for development with evidence references"
    )

    def get_competency_score(self, dimension: CompetencyDimension) -> Optional[CompetencyScore]:
        """Get the score for a specific competency dimension."""
        for score in self.competency_scores:
            if score.dimension == dimension:
                return score
        return None

    def get_score_value(self, dimension: CompetencyDimension) -> float:
        """Get just the numeric score for a competency."""
        score = self.get_competency_score(dimension)
        return score.score if score else 0.0

    def to_legacy_assessment_mapping(self) -> dict:
        """
        Convert to legacy AssessmentMapping format for backwards compatibility.
        """
        return {
            "collaboration_score": self.get_score_value(CompetencyDimension.COLLABORATION),
            "leadership_score": self.get_score_value(CompetencyDimension.LEADERSHIP),
            "stress_management_score": self.get_score_value(CompetencyDimension.STRESS_MANAGEMENT),
            "communication_score": self.get_score_value(CompetencyDimension.COMMUNICATION),
            "problem_solving_score": self.get_score_value(CompetencyDimension.PROBLEM_SOLVING),
        }


# =============================================================================
# Analysis Session State
# =============================================================================

class AnalysisSession(BaseModel):
    """
    Container for tracking analysis state during a session.

    Used by the TurnAnalyzer to accumulate evidence across turns.
    """
    session_id: str
    candidate_name: str

    # Accumulated analyses
    turn_analyses: list[TurnAnalysis] = Field(default_factory=list)

    # Running trait signal accumulator
    accumulated_trait_signals: dict[str, list[TraitSignal]] = Field(
        default_factory=lambda: {trait.value: [] for trait in BigFiveTrait}
    )

    # Running competency evidence accumulator
    accumulated_competency_evidence: dict[str, list[ScoringEvidence]] = Field(
        default_factory=lambda: {dim.value: [] for dim in CompetencyDimension}
    )

    # Data tracking
    data_revealed: set[str] = Field(default_factory=set)
    data_requested: set[str] = Field(default_factory=set)
    data_used_effectively: set[str] = Field(default_factory=set)

    # Assumption tracking
    assumptions_made: list[dict] = Field(default_factory=list)

    def add_turn_analysis(self, analysis: TurnAnalysis) -> None:
        """Add a turn analysis and update accumulators."""
        self.turn_analyses.append(analysis)

        # Accumulate trait signals
        for signal in analysis.trait_signals:
            self.accumulated_trait_signals[signal.trait.value].append(signal)

        # Track data requests
        self.data_requested.update(analysis.data_requested)

        # Track effective data usage
        if analysis.reasoning_assessment:
            self.data_used_effectively.update(
                analysis.reasoning_assessment.data_categories_used_effectively
            )

    def get_trait_signal_count(self, trait: BigFiveTrait) -> int:
        """Get number of signals for a trait."""
        return len(self.accumulated_trait_signals.get(trait.value, []))
