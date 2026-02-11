"""
Pydantic data models for the Pressure Cooker framework.
Defines all core data structures for personality profiles, scenarios,
conversation turns, and session outputs.
"""

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class BigFiveTrait(str, Enum):
    """Big Five personality traits."""
    OPENNESS = "openness"
    CONSCIENTIOUSNESS = "conscientiousness"
    EXTRAVERSION = "extraversion"
    AGREEABLENESS = "agreeableness"
    NEUROTICISM = "neuroticism"


class SpeakerRole(str, Enum):
    """Roles in the simulation."""
    CANDIDATE = "candidate"
    PROVOKER = "provoker"
    MEDIATOR = "mediator"
    SYSTEM = "system"


class IntentCategory(str, Enum):
    """Intent categories for turn classification."""
    ASSERTIVE = "assertive"
    COOPERATIVE = "cooperative"
    AVOIDANT = "avoidant"
    AGGRESSIVE = "aggressive"
    ANXIOUS = "anxious"
    ANALYTICAL = "analytical"
    CREATIVE = "creative"
    EMPATHETIC = "empathetic"
    DEFENSIVE = "defensive"
    NEUTRAL = "neutral"


class PersonalityVector(BaseModel):
    """Big Five personality scores (0.0 - 1.0 scale)."""
    openness: float = Field(ge=0.0, le=1.0, description="Openness to experience")
    conscientiousness: float = Field(ge=0.0, le=1.0, description="Conscientiousness")
    extraversion: float = Field(ge=0.0, le=1.0, description="Extraversion")
    agreeableness: float = Field(ge=0.0, le=1.0, description="Agreeableness")
    neuroticism: float = Field(ge=0.0, le=1.0, description="Neuroticism")

    def to_dict(self) -> dict[str, float]:
        return {
            "O": self.openness,
            "C": self.conscientiousness,
            "E": self.extraversion,
            "A": self.agreeableness,
            "N": self.neuroticism,
        }

    def to_description(self) -> str:
        """Generate natural language description of personality."""
        descriptions = []

        if self.openness >= 0.7:
            descriptions.append("highly open to new experiences and ideas")
        elif self.openness <= 0.3:
            descriptions.append("preferring familiar and conventional approaches")

        if self.conscientiousness >= 0.7:
            descriptions.append("very organized and detail-oriented")
        elif self.conscientiousness <= 0.3:
            descriptions.append("flexible and spontaneous in approach")

        if self.extraversion >= 0.7:
            descriptions.append("outgoing and energized by social interaction")
        elif self.extraversion <= 0.3:
            descriptions.append("reserved and preferring solitary work")

        if self.agreeableness >= 0.7:
            descriptions.append("cooperative and prioritizing harmony")
        elif self.agreeableness <= 0.3:
            descriptions.append("competitive and direct in expressing views")

        if self.neuroticism >= 0.7:
            descriptions.append("sensitive to stress and emotionally reactive")
        elif self.neuroticism <= 0.3:
            descriptions.append("calm and emotionally stable under pressure")

        return ", ".join(descriptions) if descriptions else "balanced across all traits"


class PersonalityProfile(BaseModel):
    """Complete personality profile with metadata."""
    id: str = Field(description="Unique profile identifier")
    name: str = Field(description="Display name for the profile")
    description: str = Field(description="Brief description of the personality type")
    vector: PersonalityVector = Field(description="Big Five scores")
    behavioral_tendencies: list[str] = Field(
        default_factory=list,
        description="Expected behavioral patterns in conversations"
    )
    communication_style: str = Field(
        default="",
        description="Typical communication style"
    )

    def get_system_prompt_injection(self) -> str:
        """Generate personality injection for LLM system prompt."""
        return f"""You embody a person with the following personality traits:
- Openness: {self.vector.openness:.1f}/1.0 - {self._trait_description('openness', self.vector.openness)}
- Conscientiousness: {self.vector.conscientiousness:.1f}/1.0 - {self._trait_description('conscientiousness', self.vector.conscientiousness)}
- Extraversion: {self.vector.extraversion:.1f}/1.0 - {self._trait_description('extraversion', self.vector.extraversion)}
- Agreeableness: {self.vector.agreeableness:.1f}/1.0 - {self._trait_description('agreeableness', self.vector.agreeableness)}
- Neuroticism: {self.vector.neuroticism:.1f}/1.0 - {self._trait_description('neuroticism', self.vector.neuroticism)}

Communication style: {self.communication_style}

Your responses should naturally reflect these personality traits through:
- Word choice and tone
- How you handle disagreements
- Your emotional reactions
- Your problem-solving approach
- Your interaction with others"""

    @staticmethod
    def _trait_description(trait: str, value: float) -> str:
        """Get description for a trait level."""
        descriptions = {
            "openness": {
                "high": "curious, creative, embraces novelty",
                "medium": "moderately open to new ideas",
                "low": "practical, conventional, prefers routine"
            },
            "conscientiousness": {
                "high": "organized, disciplined, goal-oriented",
                "medium": "reasonably organized and reliable",
                "low": "flexible, spontaneous, adaptable"
            },
            "extraversion": {
                "high": "energetic, talkative, seeks social engagement",
                "medium": "comfortable in both social and solo settings",
                "low": "reserved, reflective, prefers solitude"
            },
            "agreeableness": {
                "high": "cooperative, trusting, conflict-avoidant",
                "medium": "balanced between cooperation and assertion",
                "low": "competitive, skeptical, direct"
            },
            "neuroticism": {
                "high": "emotionally sensitive, prone to stress",
                "medium": "moderate emotional reactivity",
                "low": "calm, resilient, emotionally stable"
            }
        }

        if value >= 0.7:
            level = "high"
        elif value <= 0.3:
            level = "low"
        else:
            level = "medium"

        return descriptions.get(trait, {}).get(level, "")


class ScenarioConfig(BaseModel):
    """Configuration for a conflict scenario."""
    id: str = Field(description="Unique scenario identifier")
    name: str = Field(description="Display name")
    description: str = Field(description="Scenario description")
    context: str = Field(description="Workplace context and setup")
    conflict_point: str = Field(description="Main source of conflict")
    provoker_goal: str = Field(description="What the provoker is trying to achieve")
    mediator_goal: str = Field(description="What the mediator is trying to achieve")
    escalation_triggers: list[str] = Field(
        default_factory=list,
        description="Events that can escalate tension"
    )
    resolution_paths: list[str] = Field(
        default_factory=list,
        description="Possible ways to resolve the conflict"
    )
    turn_limit: int = Field(default=30, ge=10, le=50, description="Maximum turns")
    min_turns: int = Field(default=15, ge=5, description="Minimum turns before resolution")


class Turn(BaseModel):
    """A single conversation turn."""
    turn_number: int = Field(ge=0, description="Sequential turn number")
    speaker: SpeakerRole = Field(description="Who is speaking")
    speaker_name: str = Field(description="Display name of speaker")
    content: str = Field(description="The actual dialogue")
    intent: Optional[IntentCategory] = Field(
        default=None,
        description="Classified intent of this turn"
    )
    emotion: Optional[str] = Field(
        default=None,
        description="Detected emotion in this turn"
    )
    tension_level: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Current tension level (0=calm, 1=heated)"
    )
    metadata: dict = Field(
        default_factory=dict,
        description="Additional metadata"
    )


class IntentStatistics(BaseModel):
    """Statistics about intent distribution in a session."""
    total_turns: int = Field(description="Total candidate turns analyzed")
    intent_counts: dict[str, int] = Field(description="Count per intent category")
    intent_percentages: dict[str, float] = Field(description="Percentage per category")
    dominant_intent: str = Field(description="Most frequent intent")
    secondary_intent: Optional[str] = Field(default=None, description="Second most frequent")


class AssessmentMapping(BaseModel):
    """Mapping from intent statistics to assessment scores."""
    collaboration_score: float = Field(ge=0.0, le=1.0)
    leadership_score: float = Field(ge=0.0, le=1.0)
    stress_management_score: float = Field(ge=0.0, le=1.0)
    communication_score: float = Field(ge=0.0, le=1.0)
    problem_solving_score: float = Field(ge=0.0, le=1.0)


class SessionMetadata(BaseModel):
    """Metadata for a simulation session."""
    session_id: str = Field(description="Unique session identifier")
    profile_id: str = Field(description="Personality profile used")
    scenario_id: str = Field(description="Scenario used")
    timestamp: datetime = Field(default_factory=datetime.now)
    total_turns: int = Field(default=0, description="Total turns in session")
    duration_seconds: Optional[float] = Field(default=None)
    api_calls: int = Field(default=0, description="Number of API calls made")
    model_used: str = Field(default="", description="LLM model used")


class SessionOutput(BaseModel):
    """Complete output of a simulation session."""
    metadata: SessionMetadata
    profile: PersonalityProfile
    scenario: ScenarioConfig
    conversation: list[Turn] = Field(default_factory=list)
    intent_statistics: Optional[IntentStatistics] = Field(default=None)
    assessment_mapping: Optional[AssessmentMapping] = Field(default=None)
    validation_results: Optional[dict] = Field(default=None)
    # Multi-model OCEAN personality inference
    personality_inference: Optional[dict] = Field(
        default=None,
        description="Ensemble OCEAN inference from multiple models with individual and average scores"
    )

    def to_json(self) -> str:
        """Serialize to JSON string."""
        return self.model_dump_json(indent=2)

    def get_candidate_turns(self) -> list[Turn]:
        """Get only candidate turns."""
        return [t for t in self.conversation if t.speaker == SpeakerRole.CANDIDATE]


class ValidationResult(BaseModel):
    """Result of validation process."""
    session_id: str
    validation_type: str = Field(description="reverse_inference, baseline, human")
    inferred_profile: Optional[PersonalityVector] = Field(default=None)
    ground_truth_profile: PersonalityVector
    accuracy_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Per-trait accuracy"
    )
    overall_accuracy: float = Field(ge=0.0, le=1.0)
    notes: str = Field(default="")


class BatchConfig(BaseModel):
    """Configuration for batch generation."""
    profiles: list[str] = Field(description="Profile IDs to use")
    scenarios: list[str] = Field(description="Scenario IDs to use")
    sessions_per_combination: int = Field(default=1, ge=1)
    turn_limit: int = Field(default=30, ge=10, le=50)
    output_dir: str = Field(default="outputs/batches")


class BatchResult(BaseModel):
    """Summary of batch generation."""
    batch_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    config: BatchConfig
    total_sessions: int
    successful_sessions: int
    failed_sessions: int
    session_ids: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
