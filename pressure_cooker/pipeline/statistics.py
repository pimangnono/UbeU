"""
Statistics Pipeline for Pressure Cooker Framework.
Calculates intent statistics and maps them to assessment scores.

This module provides both:
1. Legacy formula-based scoring (for backwards compatibility)
2. New evidence-based analysis (via TurnAnalyzer and AssessmentBuilder)

For transparent, evidence-based assessment, use:
    from pipeline.turn_analyzer import TurnAnalyzer
    from pipeline.assessment_builder import build_evidence_based_assessment
"""

from typing import TYPE_CHECKING, Optional

from utils.models import (
    Turn,
    SpeakerRole,
    IntentCategory,
    IntentStatistics,
    AssessmentMapping,
)

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient, LLMClient
    from utils.analysis_models import EvidenceBasedAssessment, TurnAnalysis


# Intent classification keywords/patterns for rule-based fallback
INTENT_KEYWORDS: dict[IntentCategory, list[str]] = {
    IntentCategory.ASSERTIVE: [
        "i think", "i believe", "we should", "my view", "i propose",
        "clearly", "obviously", "the right way", "i'm confident"
    ],
    IntentCategory.COOPERATIVE: [
        "let's work together", "we can find", "how about", "what if we",
        "i agree", "good point", "you're right", "together"
    ],
    IntentCategory.AVOIDANT: [
        "i'm not sure", "maybe", "it's fine", "doesn't matter",
        "whatever you think", "i'll go along", "i don't want to"
    ],
    IntentCategory.AGGRESSIVE: [
        "you're wrong", "that's ridiculous", "absolutely not",
        "you always", "you never", "this is your fault"
    ],
    IntentCategory.ANXIOUS: [
        "i'm worried", "what if", "are you sure", "i'm concerned",
        "this could go wrong", "i'm nervous", "scary"
    ],
    IntentCategory.ANALYTICAL: [
        "the data shows", "logically", "if we consider", "statistically",
        "the evidence", "based on", "let's analyze"
    ],
    IntentCategory.CREATIVE: [
        "what about trying", "imagine if", "a new approach",
        "out of the box", "innovative", "creative solution"
    ],
    IntentCategory.EMPATHETIC: [
        "i understand", "i hear you", "that must be", "i can see why",
        "your feelings", "how you feel", "i appreciate"
    ],
    IntentCategory.DEFENSIVE: [
        "that's not fair", "i didn't mean", "you misunderstood",
        "that's not what i said", "i was just", "let me explain"
    ],
    IntentCategory.NEUTRAL: [
        "okay", "i see", "alright", "noted", "understood"
    ],
}


def classify_intent_rule_based(content: str) -> IntentCategory:
    """
    Rule-based intent classification using keyword matching.
    Used as fallback when LLM classification is not available.

    Args:
        content: The turn content to classify.

    Returns:
        Classified intent category.
    """
    content_lower = content.lower()

    scores: dict[IntentCategory, int] = {cat: 0 for cat in IntentCategory}

    for category, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in content_lower:
                scores[category] += 1

    # Return category with highest score, or NEUTRAL if no matches
    max_score = max(scores.values())
    if max_score == 0:
        return IntentCategory.NEUTRAL

    for category, score in scores.items():
        if score == max_score:
            return category

    return IntentCategory.NEUTRAL


async def classify_intent_llm(
    content: str,
    client: "GeminiClient | MockGeminiClient",
    context: str = "",
) -> IntentCategory:
    """
    LLM-based intent classification for more nuanced analysis.

    Args:
        content: The turn content to classify.
        client: LLM client for classification.
        context: Optional context about the conversation.

    Returns:
        Classified intent category.
    """
    from clients.llm_client import ModelTier

    categories = [cat.value for cat in IntentCategory]

    prompt = f"""Classify the following statement into one of these intent categories:
{', '.join(categories)}

Statement: "{content}"

{f'Context: {context}' if context else ''}

Respond with ONLY the category name, nothing else."""

    try:
        response = await client.generate(
            prompt=prompt,
            tier=ModelTier.FLASH,
            temperature=0.1,
            max_tokens=32,
        )

        response_clean = response.strip().lower()

        for category in IntentCategory:
            if category.value in response_clean:
                return category

        return classify_intent_rule_based(content)

    except Exception:
        return classify_intent_rule_based(content)


def calculate_intent_statistics(
    turns: list[Turn],
    candidate_only: bool = True,
) -> IntentStatistics:
    """
    Calculate intent distribution statistics for a conversation.

    Args:
        turns: List of conversation turns.
        candidate_only: If True, only analyze candidate turns.

    Returns:
        IntentStatistics with counts and percentages.
    """
    relevant_turns = [
        t for t in turns
        if not candidate_only or t.speaker == SpeakerRole.CANDIDATE
    ]

    if not relevant_turns:
        return IntentStatistics(
            total_turns=0,
            intent_counts={cat.value: 0 for cat in IntentCategory},
            intent_percentages={cat.value: 0.0 for cat in IntentCategory},
            dominant_intent=IntentCategory.NEUTRAL.value,
            secondary_intent=None,
        )

    # Count intents
    intent_counts: dict[str, int] = {cat.value: 0 for cat in IntentCategory}

    for turn in relevant_turns:
        if turn.intent:
            intent_counts[turn.intent.value] += 1
        else:
            # Classify if not already classified
            intent = classify_intent_rule_based(turn.content)
            intent_counts[intent.value] += 1

    total = sum(intent_counts.values())

    # Calculate percentages
    intent_percentages = {
        cat: (count / total * 100) if total > 0 else 0.0
        for cat, count in intent_counts.items()
    }

    # Find dominant and secondary intents
    sorted_intents = sorted(intent_counts.items(), key=lambda x: x[1], reverse=True)
    dominant = sorted_intents[0][0] if sorted_intents else IntentCategory.NEUTRAL.value
    secondary = sorted_intents[1][0] if len(sorted_intents) > 1 and sorted_intents[1][1] > 0 else None

    return IntentStatistics(
        total_turns=len(relevant_turns),
        intent_counts=intent_counts,
        intent_percentages=intent_percentages,
        dominant_intent=dominant,
        secondary_intent=secondary,
    )


def map_to_assessment(
    intent_stats: IntentStatistics,
    tension_avg: float = 0.5,
) -> AssessmentMapping:
    """
    Map intent statistics to assessment scores.

    This creates a mapping from conversation behavior to
    workplace competency scores.

    Args:
        intent_stats: Calculated intent statistics.
        tension_avg: Average tension level during conversation.

    Returns:
        AssessmentMapping with competency scores.
    """
    pcts = intent_stats.intent_percentages

    # Collaboration score: cooperative, empathetic, less aggressive
    collaboration = (
        pcts.get(IntentCategory.COOPERATIVE.value, 0) * 0.4 +
        pcts.get(IntentCategory.EMPATHETIC.value, 0) * 0.3 +
        (100 - pcts.get(IntentCategory.AGGRESSIVE.value, 0)) * 0.003  # Inverse
    )
    collaboration = min(1.0, collaboration / 100)

    # Leadership score: assertive, analytical, less avoidant
    leadership = (
        pcts.get(IntentCategory.ASSERTIVE.value, 0) * 0.35 +
        pcts.get(IntentCategory.ANALYTICAL.value, 0) * 0.25 +
        pcts.get(IntentCategory.CREATIVE.value, 0) * 0.2 +
        (100 - pcts.get(IntentCategory.AVOIDANT.value, 0)) * 0.002
    )
    leadership = min(1.0, leadership / 100)

    # Stress management: low anxiety, low defensiveness, calm under tension
    stress_factor = 1.0 - (tension_avg * 0.5)  # Higher tension hurts score
    stress_management = (
        (100 - pcts.get(IntentCategory.ANXIOUS.value, 0)) * 0.004 +
        (100 - pcts.get(IntentCategory.DEFENSIVE.value, 0)) * 0.003 +
        (100 - pcts.get(IntentCategory.AGGRESSIVE.value, 0)) * 0.003
    ) * stress_factor
    stress_management = min(1.0, max(0.0, stress_management))

    # Communication score: balance of assertive, empathetic, analytical
    communication = (
        pcts.get(IntentCategory.ASSERTIVE.value, 0) * 0.25 +
        pcts.get(IntentCategory.EMPATHETIC.value, 0) * 0.25 +
        pcts.get(IntentCategory.ANALYTICAL.value, 0) * 0.2 +
        pcts.get(IntentCategory.COOPERATIVE.value, 0) * 0.15 +
        (100 - pcts.get(IntentCategory.AVOIDANT.value, 0)) * 0.0015
    )
    communication = min(1.0, communication / 100)

    # Problem-solving: analytical, creative, assertive
    problem_solving = (
        pcts.get(IntentCategory.ANALYTICAL.value, 0) * 0.35 +
        pcts.get(IntentCategory.CREATIVE.value, 0) * 0.3 +
        pcts.get(IntentCategory.ASSERTIVE.value, 0) * 0.2 +
        pcts.get(IntentCategory.COOPERATIVE.value, 0) * 0.15
    )
    problem_solving = min(1.0, problem_solving / 100)

    return AssessmentMapping(
        collaboration_score=round(collaboration, 3),
        leadership_score=round(leadership, 3),
        stress_management_score=round(stress_management, 3),
        communication_score=round(communication, 3),
        problem_solving_score=round(problem_solving, 3),
    )


async def classify_all_turns(
    turns: list[Turn],
    client: "GeminiClient | MockGeminiClient",
    use_llm: bool = False,
) -> list[Turn]:
    """
    Classify intent for all turns in a conversation.

    Args:
        turns: List of turns to classify.
        client: LLM client (used if use_llm=True).
        use_llm: Whether to use LLM for classification.

    Returns:
        Turns with intent field populated.
    """
    classified_turns = []

    for turn in turns:
        if turn.intent is None:
            if use_llm:
                intent = await classify_intent_llm(turn.content, client)
            else:
                intent = classify_intent_rule_based(turn.content)

            classified_turn = turn.model_copy(update={"intent": intent})
            classified_turns.append(classified_turn)
        else:
            classified_turns.append(turn)

    return classified_turns


# =============================================================================
# Evidence-Based Analysis (New System)
# =============================================================================

async def analyze_conversation_with_evidence(
    turns: list[Turn],
    client: "LLMClient",
    session_id: str,
    candidate_name: str,
    case_context: str = "",
    revealed_data_by_turn: Optional[dict[int, list[str]]] = None,
    logical_validation: Optional[dict] = None,
) -> "EvidenceBasedAssessment":
    """
    Analyze a conversation using the new evidence-based system.

    This provides transparent, quote-backed assessments instead of
    opaque formula-based scores.

    Args:
        turns: All turns in the conversation.
        client: LLM client for analysis.
        session_id: Session identifier.
        candidate_name: Name of the candidate.
        case_context: Brief description of the case study.
        revealed_data_by_turn: Mapping of turn number to revealed data.
        logical_validation: Optional validator output to incorporate.

    Returns:
        EvidenceBasedAssessment with full evidence trails.

    Example:
        >>> from clients.llm_client import LLMClient
        >>> client = LLMClient()
        >>> assessment = await analyze_conversation_with_evidence(
        ...     turns=conversation,
        ...     client=client,
        ...     session_id="abc123",
        ...     candidate_name="Jin",
        ...     case_context="TechFlow profitability case",
        ... )
        >>> print(assessment.get_score_value(CompetencyDimension.LEADERSHIP))
        0.72
        >>> for evidence in assessment.get_competency_score(CompetencyDimension.LEADERSHIP).evidence[:3]:
        ...     print(f"Turn {evidence.turn_number}: \"{evidence.quote[:50]}...\"")
    """
    from pipeline.turn_analyzer import TurnAnalyzer
    from pipeline.assessment_builder import build_evidence_based_assessment

    # Create analyzer
    analyzer = TurnAnalyzer(
        client=client,
        case_context=case_context,
        candidate_name=candidate_name,
    )

    # Start session
    analyzer.start_session(session_id)

    # Analyze all candidate turns
    turn_analyses = await analyzer.analyze_conversation(
        turns=turns,
        revealed_data_by_turn=revealed_data_by_turn,
    )

    # Build final assessment
    assessment = build_evidence_based_assessment(
        session_id=session_id,
        candidate_name=candidate_name,
        turn_analyses=turn_analyses,
        logical_validation=logical_validation,
    )

    return assessment


async def analyze_single_turn_with_evidence(
    turn: Turn,
    client: "LLMClient",
    previous_turn: Optional[Turn] = None,
    case_context: str = "",
    revealed_data: Optional[list[str]] = None,
) -> "TurnAnalysis":
    """
    Analyze a single turn using the evidence-based system.

    Useful for real-time analysis during a live session.

    Args:
        turn: The turn to analyze.
        client: LLM client.
        previous_turn: The turn being responded to.
        case_context: Brief case description.
        revealed_data: Data categories revealed so far.

    Returns:
        TurnAnalysis with evidence-based assessments.
    """
    from pipeline.turn_analyzer import TurnAnalyzer

    analyzer = TurnAnalyzer(
        client=client,
        case_context=case_context,
        candidate_name=turn.speaker_name,
    )

    return await analyzer.analyze_turn(
        turn=turn,
        previous_turn=previous_turn,
        revealed_data=revealed_data,
    )
