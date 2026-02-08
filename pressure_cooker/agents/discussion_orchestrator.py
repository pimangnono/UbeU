"""
Discussion Orchestrator for Strategic Group Discussion Management.

Provides:
- Discussion phases (problem framing → synthesis → recommendation)
- Competency coverage tracking
- Strategic speaker selection
- Context management for AI agents

This module enables structured, competency-targeted discussions
that systematically assess candidates across all dimensions.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from utils.models import Turn, SpeakerRole, IntentCategory


# =============================================================================
# Discussion Phases
# =============================================================================

class DiscussionPhase(str, Enum):
    """
    Phases of a structured case discussion.

    The discussion progresses through these phases to ensure
    comprehensive assessment of candidate capabilities.
    """
    OPENING = "opening"                   # Facilitator introduces the case
    PROBLEM_FRAMING = "problem_framing"   # Candidate structures the problem
    HYPOTHESIS_GENERATION = "hypothesis"  # Candidate proposes hypotheses
    DATA_GATHERING = "data_gathering"     # Candidate requests and analyzes data
    SYNTHESIS = "synthesis"               # Candidate synthesizes findings
    RECOMMENDATION = "recommendation"     # Candidate proposes recommendations
    STRESS_TEST = "stress_test"           # Provoker challenges the recommendation
    CLOSING = "closing"                   # Wrap up and conclusion


# Phase transitions and triggers
PHASE_TRIGGERS = {
    DiscussionPhase.OPENING: {
        "next_phase": DiscussionPhase.PROBLEM_FRAMING,
        "trigger_conditions": ["facilitator_introduced_case"],
        "min_turns": 1,
    },
    DiscussionPhase.PROBLEM_FRAMING: {
        "next_phase": DiscussionPhase.HYPOTHESIS_GENERATION,
        "trigger_conditions": ["candidate_asked_initial_question", "candidate_proposed_structure"],
        "min_turns": 2,
    },
    DiscussionPhase.HYPOTHESIS_GENERATION: {
        "next_phase": DiscussionPhase.DATA_GATHERING,
        "trigger_conditions": ["candidate_stated_hypothesis", "candidate_requested_data"],
        "min_turns": 2,
    },
    DiscussionPhase.DATA_GATHERING: {
        "next_phase": DiscussionPhase.SYNTHESIS,
        "trigger_conditions": ["multiple_data_revealed", "candidate_connected_data"],
        "min_turns": 4,
    },
    DiscussionPhase.SYNTHESIS: {
        "next_phase": DiscussionPhase.RECOMMENDATION,
        "trigger_conditions": ["candidate_synthesized_findings"],
        "min_turns": 2,
    },
    DiscussionPhase.RECOMMENDATION: {
        "next_phase": DiscussionPhase.STRESS_TEST,
        "trigger_conditions": ["candidate_made_recommendation"],
        "min_turns": 2,
    },
    DiscussionPhase.STRESS_TEST: {
        "next_phase": DiscussionPhase.CLOSING,
        "trigger_conditions": ["recommendation_defended", "time_limit_near"],
        "min_turns": 3,
    },
}


# =============================================================================
# Competency Tracking
# =============================================================================

@dataclass
class CompetencyBehavior:
    """A specific behavior that demonstrates a competency."""
    behavior_id: str
    description: str
    example_indicators: list[str]
    observed: bool = False
    evidence_turns: list[int] = field(default_factory=list)
    evidence_quotes: list[str] = field(default_factory=list)


@dataclass
class CompetencyDimension:
    """A competency dimension with its component behaviors."""
    name: str
    description: str
    behaviors: list[CompetencyBehavior]

    @property
    def coverage(self) -> float:
        """Percentage of behaviors observed."""
        if not self.behaviors:
            return 0.0
        observed = sum(1 for b in self.behaviors if b.observed)
        return observed / len(self.behaviors)

    @property
    def untested_behaviors(self) -> list[CompetencyBehavior]:
        """Behaviors not yet observed."""
        return [b for b in self.behaviors if not b.observed]


class CompetencyCoverageTracker:
    """
    Tracks which competencies have been tested during a discussion.

    Ensures the discussion covers all assessment dimensions and
    provides guidance on which competencies need more probing.
    """

    def __init__(self):
        """Initialize with all competency dimensions."""
        self.dimensions = self._initialize_dimensions()
        self.phase_competency_focus = self._initialize_phase_focus()

    def _initialize_dimensions(self) -> dict[str, CompetencyDimension]:
        """Set up all competency dimensions with their behaviors."""
        return {
            "collaboration": CompetencyDimension(
                name="Collaboration",
                description="Working effectively with others",
                behaviors=[
                    CompetencyBehavior(
                        behavior_id="acknowledged_others",
                        description="Acknowledged others' points before responding",
                        example_indicators=["I hear you", "That's a good point", "I understand Jordan's concern"],
                    ),
                    CompetencyBehavior(
                        behavior_id="built_on_ideas",
                        description="Built on or extended colleagues' ideas",
                        example_indicators=["Building on what Sam said", "To add to that", "Expanding on Jordan's point"],
                    ),
                    CompetencyBehavior(
                        behavior_id="sought_input",
                        description="Actively sought input from others",
                        example_indicators=["What do you think?", "Jordan, your perspective?", "Sam, how do you see this?"],
                    ),
                    CompetencyBehavior(
                        behavior_id="resolved_conflict",
                        description="Helped resolve disagreements constructively",
                        example_indicators=["Perhaps we can find middle ground", "Let's focus on what we agree on"],
                    ),
                ],
            ),
            "leadership": CompetencyDimension(
                name="Leadership",
                description="Taking initiative and guiding the discussion",
                behaviors=[
                    CompetencyBehavior(
                        behavior_id="set_direction",
                        description="Set direction or proposed a structure",
                        example_indicators=["Let me propose a framework", "I suggest we start with", "First, we should"],
                    ),
                    CompetencyBehavior(
                        behavior_id="made_decisions",
                        description="Made clear decisions when needed",
                        example_indicators=["I think we should", "My recommendation is", "Let's go with"],
                    ),
                    CompetencyBehavior(
                        behavior_id="took_initiative",
                        description="Took initiative to move discussion forward",
                        example_indicators=["Let me", "I'll take the lead on", "Moving forward"],
                    ),
                    CompetencyBehavior(
                        behavior_id="delegated",
                        description="Appropriately involved others in the work",
                        example_indicators=["Jordan, could you", "Sam, what if you", "Let's divide this"],
                    ),
                ],
            ),
            "problem_solving": CompetencyDimension(
                name="Problem Solving",
                description="Analytical thinking and structured problem-solving",
                behaviors=[
                    CompetencyBehavior(
                        behavior_id="framed_problem",
                        description="Clearly framed or structured the problem",
                        example_indicators=["The core issue is", "Let me break this down", "The key questions are"],
                    ),
                    CompetencyBehavior(
                        behavior_id="generated_hypotheses",
                        description="Generated hypotheses to test",
                        example_indicators=["I hypothesize", "My hypothesis is", "I suspect that"],
                    ),
                    CompetencyBehavior(
                        behavior_id="used_data",
                        description="Used data effectively in analysis",
                        example_indicators=["The data shows", "Based on the numbers", "Looking at the 37%"],
                    ),
                    CompetencyBehavior(
                        behavior_id="identified_root_cause",
                        description="Identified root causes, not just symptoms",
                        example_indicators=["The root cause is", "This is because", "The underlying issue"],
                    ),
                    CompetencyBehavior(
                        behavior_id="used_framework",
                        description="Applied a structured analytical framework",
                        example_indicators=["profitability tree", "BCG matrix", "Porter's forces", "segment analysis"],
                    ),
                ],
            ),
            "communication": CompetencyDimension(
                name="Communication",
                description="Clear, effective communication",
                behaviors=[
                    CompetencyBehavior(
                        behavior_id="clear_explanations",
                        description="Explained complex ideas clearly",
                        example_indicators=["In other words", "Simply put", "To clarify"],
                    ),
                    CompetencyBehavior(
                        behavior_id="structured_responses",
                        description="Used structured, organized responses",
                        example_indicators=["First... Second... Third", "1) 2) 3)", "There are three parts"],
                    ),
                    CompetencyBehavior(
                        behavior_id="asked_good_questions",
                        description="Asked probing, insightful questions",
                        example_indicators=["What if", "How does", "Can we get data on"],
                    ),
                    CompetencyBehavior(
                        behavior_id="summarized",
                        description="Summarized or synthesized discussion points",
                        example_indicators=["To summarize", "So far we've identified", "The key takeaways are"],
                    ),
                ],
            ),
            "stress_management": CompetencyDimension(
                name="Stress Management",
                description="Handling pressure and challenges",
                behaviors=[
                    CompetencyBehavior(
                        behavior_id="handled_pushback",
                        description="Responded constructively to pushback",
                        example_indicators=["I see your point, but", "That's fair, however", "Let me address that"],
                    ),
                    CompetencyBehavior(
                        behavior_id="maintained_composure",
                        description="Maintained composure under pressure",
                        example_indicators=["calm tone", "non-defensive", "measured response"],
                    ),
                    CompetencyBehavior(
                        behavior_id="adapted_approach",
                        description="Adapted approach when challenged",
                        example_indicators=["Let me refine my approach", "Good point, let's consider", "I'll adjust"],
                    ),
                    CompetencyBehavior(
                        behavior_id="stayed_on_track",
                        description="Stayed focused on the goal despite distractions",
                        example_indicators=["Back to the main issue", "The key point remains", "Focusing on our goal"],
                    ),
                ],
            ),
        }

    def _initialize_phase_focus(self) -> dict[DiscussionPhase, list[str]]:
        """Map phases to primary competencies to assess."""
        return {
            DiscussionPhase.OPENING: [],
            DiscussionPhase.PROBLEM_FRAMING: ["problem_solving", "communication"],
            DiscussionPhase.HYPOTHESIS_GENERATION: ["problem_solving", "leadership"],
            DiscussionPhase.DATA_GATHERING: ["problem_solving", "communication"],
            DiscussionPhase.SYNTHESIS: ["problem_solving", "communication", "leadership"],
            DiscussionPhase.RECOMMENDATION: ["leadership", "communication", "problem_solving"],
            DiscussionPhase.STRESS_TEST: ["stress_management", "collaboration", "leadership"],
            DiscussionPhase.CLOSING: [],
        }

    def get_untested_competencies(self, threshold: float = 0.5) -> list[str]:
        """Get competencies with coverage below threshold."""
        return [
            name for name, dim in self.dimensions.items()
            if dim.coverage < threshold
        ]

    def get_priority_competency(self, current_phase: DiscussionPhase) -> Optional[str]:
        """
        Get the highest priority competency to test in current phase.

        Prioritizes competencies that are:
        1. Relevant to the current phase
        2. Haven't been tested yet
        """
        phase_competencies = self.phase_competency_focus.get(current_phase, [])

        # Find least-covered competency relevant to this phase
        candidates = [
            (name, self.dimensions[name].coverage)
            for name in phase_competencies
            if name in self.dimensions
        ]

        if not candidates:
            # Fall back to any untested competency
            candidates = [(name, dim.coverage) for name, dim in self.dimensions.items()]

        if candidates:
            candidates.sort(key=lambda x: x[1])
            return candidates[0][0]

        return None

    def get_untested_behavior(self, competency: str) -> Optional[CompetencyBehavior]:
        """Get a specific untested behavior from a competency."""
        if competency not in self.dimensions:
            return None

        untested = self.dimensions[competency].untested_behaviors
        return untested[0] if untested else None

    def mark_behavior_observed(
        self,
        competency: str,
        behavior_id: str,
        turn_number: int,
        evidence_quote: str,
    ) -> None:
        """Mark a behavior as observed with evidence."""
        if competency not in self.dimensions:
            return

        for behavior in self.dimensions[competency].behaviors:
            if behavior.behavior_id == behavior_id:
                behavior.observed = True
                behavior.evidence_turns.append(turn_number)
                behavior.evidence_quotes.append(evidence_quote)
                break

    def detect_behaviors(self, turn: Turn) -> list[tuple[str, str, str]]:
        """
        Detect behaviors demonstrated in a turn.

        Returns list of (competency, behavior_id, evidence_quote) tuples.
        """
        if turn.speaker != SpeakerRole.CANDIDATE:
            return []

        detected = []
        content_lower = turn.content.lower()

        for comp_name, dimension in self.dimensions.items():
            for behavior in dimension.behaviors:
                if behavior.observed:
                    continue

                # Check for indicator phrases
                for indicator in behavior.example_indicators:
                    if indicator.lower() in content_lower:
                        detected.append((comp_name, behavior.behavior_id, turn.content[:100]))
                        break

        return detected

    def get_coverage_summary(self) -> dict[str, dict]:
        """Get summary of competency coverage."""
        return {
            name: {
                "coverage": dim.coverage,
                "tested": sum(1 for b in dim.behaviors if b.observed),
                "total": len(dim.behaviors),
                "untested_behaviors": [b.behavior_id for b in dim.untested_behaviors],
            }
            for name, dim in self.dimensions.items()
        }


# =============================================================================
# Discussion Context
# =============================================================================

@dataclass
class DiscussionContext:
    """
    Tracks the full state of a discussion for strategic decision-making.

    Used by agents to understand:
    - Current phase and progress
    - What competencies need testing
    - Conversation dynamics
    - Data revealed and used
    """
    # Phase tracking
    current_phase: DiscussionPhase = DiscussionPhase.OPENING
    turns_in_phase: int = 0
    phase_history: list[tuple[DiscussionPhase, int]] = field(default_factory=list)

    # Conversation state
    total_turns: int = 0
    candidate_turns: int = 0
    tension_level: float = 0.3
    tension_history: list[float] = field(default_factory=list)

    # Data tracking
    data_revealed: set[str] = field(default_factory=set)
    data_requested: set[str] = field(default_factory=set)
    data_used_effectively: set[str] = field(default_factory=set)

    # Hypothesis tracking
    hypotheses_stated: list[str] = field(default_factory=list)

    # Recommendation tracking
    has_recommendation: bool = False
    recommendation_defended: bool = False

    # Competency tracking
    competency_tracker: CompetencyCoverageTracker = field(
        default_factory=CompetencyCoverageTracker
    )

    # Recent speakers
    recent_speakers: list[str] = field(default_factory=list)

    def advance_phase(self) -> None:
        """Advance to the next discussion phase."""
        if self.current_phase in PHASE_TRIGGERS:
            next_phase = PHASE_TRIGGERS[self.current_phase]["next_phase"]
            self.phase_history.append((self.current_phase, self.turns_in_phase))
            self.current_phase = next_phase
            self.turns_in_phase = 0

    def should_advance_phase(self) -> bool:
        """Check if conditions are met to advance to next phase."""
        if self.current_phase not in PHASE_TRIGGERS:
            return False

        config = PHASE_TRIGGERS[self.current_phase]

        # Must meet minimum turns
        if self.turns_in_phase < config["min_turns"]:
            return False

        # Check trigger conditions based on phase
        if self.current_phase == DiscussionPhase.PROBLEM_FRAMING:
            return len(self.data_requested) > 0 or self.candidate_turns >= 2

        elif self.current_phase == DiscussionPhase.HYPOTHESIS_GENERATION:
            return len(self.hypotheses_stated) > 0 or self.candidate_turns >= 3

        elif self.current_phase == DiscussionPhase.DATA_GATHERING:
            return len(self.data_revealed) >= 3 or self.turns_in_phase >= 6

        elif self.current_phase == DiscussionPhase.SYNTHESIS:
            return len(self.data_used_effectively) >= 2 or self.turns_in_phase >= 4

        elif self.current_phase == DiscussionPhase.RECOMMENDATION:
            return self.has_recommendation

        elif self.current_phase == DiscussionPhase.STRESS_TEST:
            return self.recommendation_defended or self.turns_in_phase >= 4

        return self.turns_in_phase >= config["min_turns"] + 2

    def record_turn(self, turn: Turn) -> None:
        """Record a turn and update context state."""
        self.total_turns += 1
        self.turns_in_phase += 1
        self.tension_history.append(self.tension_level)

        # Track speaker
        self.recent_speakers.append(turn.speaker_name)
        if len(self.recent_speakers) > 5:
            self.recent_speakers.pop(0)

        if turn.speaker == SpeakerRole.CANDIDATE:
            self.candidate_turns += 1

            # Detect competency behaviors
            behaviors = self.competency_tracker.detect_behaviors(turn)
            for comp, behavior_id, quote in behaviors:
                self.competency_tracker.mark_behavior_observed(
                    comp, behavior_id, turn.turn_number, quote
                )

            # Check for hypothesis
            content_lower = turn.content.lower()
            if any(word in content_lower for word in ["hypothesize", "hypothesis", "suspect", "believe"]):
                self.hypotheses_stated.append(turn.content[:100])

            # Check for recommendation
            if any(word in content_lower for word in ["recommend", "recommendation", "propose", "suggest we"]):
                self.has_recommendation = True

    def get_phase_guidance(self) -> str:
        """Get guidance string for current phase."""
        guidance = {
            DiscussionPhase.OPENING: "Introduce the case and set the scene.",
            DiscussionPhase.PROBLEM_FRAMING: "Guide candidate to structure the problem and identify key questions.",
            DiscussionPhase.HYPOTHESIS_GENERATION: "Encourage candidate to form testable hypotheses.",
            DiscussionPhase.DATA_GATHERING: "Provide data when requested, prompt for deeper analysis.",
            DiscussionPhase.SYNTHESIS: "Guide candidate to connect findings across data categories.",
            DiscussionPhase.RECOMMENDATION: "Push candidate to commit to a specific recommendation.",
            DiscussionPhase.STRESS_TEST: "Challenge the recommendation and test the candidate's conviction.",
            DiscussionPhase.CLOSING: "Summarize and conclude the discussion.",
        }
        return guidance.get(self.current_phase, "")

    def get_untested_competency_prompt(self) -> Optional[str]:
        """Get a prompt to test an untested competency."""
        priority = self.competency_tracker.get_priority_competency(self.current_phase)
        if not priority:
            return None

        behavior = self.competency_tracker.get_untested_behavior(priority)
        if not behavior:
            return None

        prompts = {
            # Collaboration behaviors
            "acknowledged_others": "Create an opportunity for the candidate to acknowledge a colleague's point.",
            "built_on_ideas": "Have a colleague make a partial point the candidate could build on.",
            "sought_input": "Create a moment where seeking input would be appropriate.",
            "resolved_conflict": "Create a disagreement between provoker and mediator for candidate to help resolve.",

            # Leadership behaviors
            "set_direction": "Ask the candidate what approach they'd recommend.",
            "made_decisions": "Present a choice point requiring a decision.",
            "took_initiative": "Create a pause allowing candidate to take initiative.",
            "delegated": "Create a complex task that could be divided.",

            # Problem solving behaviors
            "framed_problem": "Ask how the candidate would structure this problem.",
            "generated_hypotheses": "Ask what the candidate thinks might be causing the issue.",
            "used_data": "Provide data and see if candidate uses it effectively.",
            "identified_root_cause": "Challenge surface-level analysis to push for root causes.",
            "used_framework": "See if candidate applies a structured analytical approach.",

            # Communication behaviors
            "clear_explanations": "Ask candidate to explain their reasoning.",
            "structured_responses": "Request a multi-part response.",
            "asked_good_questions": "Create an information gap requiring good questions.",
            "summarized": "After discussion, see if candidate synthesizes key points.",

            # Stress management behaviors
            "handled_pushback": "Have provoker strongly challenge the candidate's position.",
            "maintained_composure": "Increase tension and observe candidate's response.",
            "adapted_approach": "Point out a flaw requiring the candidate to adapt.",
            "stayed_on_track": "Introduce a tangent to see if candidate refocuses.",
        }

        return prompts.get(behavior.behavior_id)
