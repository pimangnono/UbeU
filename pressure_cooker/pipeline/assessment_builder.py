"""
Assessment Builder for Evidence-Based Scoring.

Aggregates per-turn analyses into final competency scores with full evidence trails.
Replaces opaque formula-based scoring with transparent, quote-backed assessments.
"""

from typing import Optional

from utils.models import (
    Turn,
    SpeakerRole,
    IntentCategory,
    BigFiveTrait,
    PersonalityVector,
)
from utils.analysis_models import (
    TurnAnalysis,
    TraitSignal,
    TraitDirection,
    ReasoningAssessment,
    LogicalConnectionQuality,
    ScoringEvidence,
    TraitEvidence,
    ContributionType,
    CompetencyDimension,
    CompetencyScore,
    PersonalityInference,
    LogicalAssessmentEvidence,
    EvidenceBasedAssessment,
)
from pipeline.turn_analyzer import (
    aggregate_trait_signals,
    infer_trait_score,
)


# =============================================================================
# Competency Scoring Rules
# =============================================================================

# Intent to competency contribution mappings
INTENT_COMPETENCY_MAPPING = {
    CompetencyDimension.COLLABORATION: {
        IntentCategory.COOPERATIVE: (ContributionType.POSITIVE, 0.15, "Showed cooperative intent"),
        IntentCategory.EMPATHETIC: (ContributionType.POSITIVE, 0.12, "Demonstrated empathy"),
        IntentCategory.AGGRESSIVE: (ContributionType.NEGATIVE, 0.15, "Showed aggressive behavior"),
        IntentCategory.DEFENSIVE: (ContributionType.NEGATIVE, 0.08, "Was defensive"),
    },
    CompetencyDimension.LEADERSHIP: {
        IntentCategory.ASSERTIVE: (ContributionType.POSITIVE, 0.15, "Took assertive stance"),
        IntentCategory.ANALYTICAL: (ContributionType.POSITIVE, 0.10, "Led with analytical approach"),
        IntentCategory.CREATIVE: (ContributionType.POSITIVE, 0.08, "Proposed creative solutions"),
        IntentCategory.AVOIDANT: (ContributionType.NEGATIVE, 0.12, "Avoided taking position"),
    },
    CompetencyDimension.STRESS_MANAGEMENT: {
        IntentCategory.ANXIOUS: (ContributionType.NEGATIVE, 0.15, "Showed anxiety"),
        IntentCategory.DEFENSIVE: (ContributionType.NEGATIVE, 0.10, "Became defensive under pressure"),
        IntentCategory.AGGRESSIVE: (ContributionType.NEGATIVE, 0.12, "Lost composure, became aggressive"),
        IntentCategory.COOPERATIVE: (ContributionType.POSITIVE, 0.05, "Maintained cooperative stance"),
        IntentCategory.ANALYTICAL: (ContributionType.POSITIVE, 0.08, "Stayed analytical under pressure"),
    },
    CompetencyDimension.COMMUNICATION: {
        IntentCategory.ASSERTIVE: (ContributionType.POSITIVE, 0.10, "Clear, assertive communication"),
        IntentCategory.EMPATHETIC: (ContributionType.POSITIVE, 0.10, "Empathetic communication"),
        IntentCategory.ANALYTICAL: (ContributionType.POSITIVE, 0.08, "Structured analytical communication"),
        IntentCategory.AVOIDANT: (ContributionType.NEGATIVE, 0.10, "Unclear, avoidant communication"),
    },
    CompetencyDimension.PROBLEM_SOLVING: {
        IntentCategory.ANALYTICAL: (ContributionType.POSITIVE, 0.15, "Applied analytical thinking"),
        IntentCategory.CREATIVE: (ContributionType.POSITIVE, 0.12, "Generated creative solutions"),
        IntentCategory.ASSERTIVE: (ContributionType.POSITIVE, 0.08, "Drove toward solutions"),
        IntentCategory.AVOIDANT: (ContributionType.NEGATIVE, 0.10, "Avoided problem engagement"),
    },
}

# Reasoning quality to competency contribution
REASONING_COMPETENCY_CONTRIBUTION = {
    LogicalConnectionQuality.STRONG: (ContributionType.POSITIVE, 0.15),
    LogicalConnectionQuality.MODERATE: (ContributionType.POSITIVE, 0.08),
    LogicalConnectionQuality.WEAK: (ContributionType.NEGATIVE, 0.05),
    LogicalConnectionQuality.NONE: (ContributionType.NEUTRAL, 0.0),
}


# =============================================================================
# Assessment Builder Class
# =============================================================================

class AssessmentBuilder:
    """
    Builds evidence-based assessments from turn analyses.

    Aggregates per-turn evidence into:
    - Competency scores with full evidence trails
    - Personality inference with trait evidence
    - Logical assessment with quote-backed analysis
    """

    def __init__(
        self,
        session_id: str,
        candidate_name: str,
    ):
        """
        Initialize the assessment builder.

        Args:
            session_id: Session identifier.
            candidate_name: Name of the candidate.
        """
        self.session_id = session_id
        self.candidate_name = candidate_name

    def build_assessment(
        self,
        turn_analyses: list[TurnAnalysis],
        logical_validation: Optional[dict] = None,
    ) -> EvidenceBasedAssessment:
        """
        Build complete evidence-based assessment from turn analyses.

        Args:
            turn_analyses: List of analyzed candidate turns.
            logical_validation: Optional validator output to incorporate.

        Returns:
            Complete EvidenceBasedAssessment with all evidence trails.
        """
        # Build competency scores
        competency_scores = self._build_competency_scores(turn_analyses)

        # Build personality inference
        personality_inference = self._build_personality_inference(turn_analyses)

        # Build logical assessment
        logical_assessment = self._build_logical_assessment(
            turn_analyses, logical_validation
        )

        # Generate summaries
        overall_summary, strengths, development = self._generate_summaries(
            turn_analyses, competency_scores, personality_inference
        )

        return EvidenceBasedAssessment(
            session_id=self.session_id,
            candidate_name=self.candidate_name,
            total_turns_analyzed=len(turn_analyses),
            competency_scores=competency_scores,
            personality_inference=personality_inference,
            logical_assessment=logical_assessment,
            turn_analyses=turn_analyses,
            overall_summary=overall_summary,
            key_strengths=strengths,
            areas_for_development=development,
        )

    def _build_competency_scores(
        self,
        analyses: list[TurnAnalysis],
    ) -> list[CompetencyScore]:
        """Build competency scores with evidence from all turns."""
        scores = []

        for dimension in CompetencyDimension:
            evidence = self._collect_competency_evidence(analyses, dimension)
            score_value = self._calculate_competency_score(evidence)

            positive = sum(1 for e in evidence if e.contribution == ContributionType.POSITIVE)
            negative = sum(1 for e in evidence if e.contribution == ContributionType.NEGATIVE)

            summary = self._generate_competency_summary(dimension, score_value, evidence)

            scores.append(CompetencyScore(
                dimension=dimension,
                score=score_value,
                evidence=evidence,
                summary=summary,
                positive_contributions=positive,
                negative_contributions=negative,
            ))

        return scores

    def _collect_competency_evidence(
        self,
        analyses: list[TurnAnalysis],
        dimension: CompetencyDimension,
    ) -> list[ScoringEvidence]:
        """Collect all evidence for a competency dimension."""
        evidence = []

        for analysis in analyses:
            # Evidence from intent
            intent = analysis.intent_analysis.primary_intent
            if intent in INTENT_COMPETENCY_MAPPING.get(dimension, {}):
                contrib_type, weight, reason = INTENT_COMPETENCY_MAPPING[dimension][intent]
                evidence.append(ScoringEvidence(
                    turn_number=analysis.turn_number,
                    quote=analysis.intent_analysis.primary_evidence,
                    contribution=contrib_type,
                    weight=weight * analysis.intent_analysis.primary_confidence,
                    explanation=f"{reason}: {analysis.intent_analysis.primary_reasoning[:100]}",
                    behavior_demonstrated=intent.value,
                ))

            # Evidence from direct competency signals
            quotes = analysis.competency_signals.get(dimension.value, [])
            for quote in quotes:
                if quote:
                    evidence.append(ScoringEvidence(
                        turn_number=analysis.turn_number,
                        quote=quote,
                        contribution=ContributionType.POSITIVE,
                        weight=0.10,
                        explanation=f"Directly demonstrated {dimension.value.replace('_', ' ')}",
                    ))

            # Evidence from reasoning (for problem-solving and leadership)
            if dimension in [CompetencyDimension.PROBLEM_SOLVING, CompetencyDimension.LEADERSHIP]:
                if analysis.reasoning_assessment:
                    ra = analysis.reasoning_assessment
                    contrib, weight = REASONING_COMPETENCY_CONTRIBUTION.get(
                        ra.logical_connection_quality,
                        (ContributionType.NEUTRAL, 0.0)
                    )
                    if contrib != ContributionType.NEUTRAL and ra.logic_evidence_quote:
                        evidence.append(ScoringEvidence(
                            turn_number=analysis.turn_number,
                            quote=ra.logic_evidence_quote,
                            contribution=contrib,
                            weight=weight,
                            explanation=f"Reasoning quality ({ra.logical_connection_quality.value}): {ra.logic_explanation or ''}",
                            behavior_demonstrated="logical_reasoning",
                        ))

                    # Framework usage is positive for problem-solving
                    if ra.uses_framework and ra.framework_name and dimension == CompetencyDimension.PROBLEM_SOLVING:
                        evidence.append(ScoringEvidence(
                            turn_number=analysis.turn_number,
                            quote=f"Applied {ra.framework_name}",
                            contribution=ContributionType.POSITIVE,
                            weight=0.12,
                            explanation=f"Used structured framework: {ra.framework_name}",
                            behavior_demonstrated="framework_usage",
                        ))

            # Evidence from tension for stress management
            if dimension == CompetencyDimension.STRESS_MANAGEMENT:
                if analysis.tension_level > 0.6:
                    # High tension - check if maintained composure
                    if analysis.intent_analysis.primary_intent not in [
                        IntentCategory.ANXIOUS, IntentCategory.AGGRESSIVE, IntentCategory.DEFENSIVE
                    ]:
                        evidence.append(ScoringEvidence(
                            turn_number=analysis.turn_number,
                            quote=analysis.content[:80],
                            contribution=ContributionType.POSITIVE,
                            weight=0.10,
                            explanation="Maintained composure under high tension",
                            behavior_demonstrated="composure_under_pressure",
                        ))

        return evidence

    def _calculate_competency_score(self, evidence: list[ScoringEvidence]) -> float:
        """Calculate competency score from evidence."""
        if not evidence:
            return 0.5  # Default neutral score

        positive_weight = sum(
            e.weight for e in evidence if e.contribution == ContributionType.POSITIVE
        )
        negative_weight = sum(
            e.weight for e in evidence if e.contribution == ContributionType.NEGATIVE
        )

        # Base score of 0.5, modified by evidence
        base = 0.5
        max_shift = 0.5  # Can go from 0.0 to 1.0

        net_weight = positive_weight - negative_weight
        total_weight = positive_weight + negative_weight

        if total_weight > 0:
            # Normalize and apply
            shift = (net_weight / max(total_weight, 1.0)) * max_shift
            score = base + shift
        else:
            score = base

        return max(0.0, min(1.0, round(score, 3)))

    def _generate_competency_summary(
        self,
        dimension: CompetencyDimension,
        score: float,
        evidence: list[ScoringEvidence],
    ) -> str:
        """Generate brief summary for a competency score."""
        level = "strong" if score >= 0.7 else "moderate" if score >= 0.4 else "developing"
        positive = sum(1 for e in evidence if e.contribution == ContributionType.POSITIVE)
        negative = sum(1 for e in evidence if e.contribution == ContributionType.NEGATIVE)

        dimension_name = dimension.value.replace("_", " ").title()
        return f"{level.title()} {dimension_name} ({positive} positive, {negative} negative signals across {len(evidence)} evidence points)"

    def _build_personality_inference(
        self,
        analyses: list[TurnAnalysis],
    ) -> PersonalityInference:
        """Build personality inference from trait signals."""
        # Aggregate signals by trait
        aggregated = aggregate_trait_signals(analyses)

        # Infer scores for each trait
        trait_scores = {}
        trait_evidence = {}
        confidences = []

        for trait in BigFiveTrait:
            signals = aggregated[trait.value]
            score, confidence = infer_trait_score(signals)
            trait_scores[trait.value] = score
            confidences.append(confidence)

            # Convert signals to evidence
            trait_evidence[trait.value] = [
                TraitEvidence(
                    turn_number=0,  # We don't have turn number in TraitSignal
                    quote=s.evidence_quote,
                    trait_signal=s.direction,
                    signal_strength=s.signal_strength,
                    explanation=s.reasoning,
                )
                for s in signals
            ]

        # Build personality vector
        vector = PersonalityVector(
            openness=trait_scores.get("openness", 0.5),
            conscientiousness=trait_scores.get("conscientiousness", 0.5),
            extraversion=trait_scores.get("extraversion", 0.5),
            agreeableness=trait_scores.get("agreeableness", 0.5),
            neuroticism=trait_scores.get("neuroticism", 0.5),
        )

        overall_confidence = sum(confidences) / len(confidences) if confidences else 0.0

        return PersonalityInference(
            inferred_vector=vector,
            trait_evidence=trait_evidence,
            confidence=overall_confidence,
        )

    def _build_logical_assessment(
        self,
        analyses: list[TurnAnalysis],
        validation: Optional[dict] = None,
    ) -> LogicalAssessmentEvidence:
        """Build logical assessment from reasoning assessments."""
        # Collect assumptions
        assumptions = []
        for analysis in analyses:
            if analysis.reasoning_assessment and analysis.reasoning_assessment.makes_assumption:
                ra = analysis.reasoning_assessment
                assumptions.append({
                    "assumption": ra.assumption_text,
                    "valid": ra.assumption_valid,
                    "quote": ra.assumption_evidence,
                    "turn_number": analysis.turn_number,
                    "explanation": f"Assumption {'validated' if ra.assumption_valid else 'not validated'} by data",
                })

        # Collect logical gaps
        logical_gaps = []
        for analysis in analyses:
            if analysis.reasoning_assessment:
                ra = analysis.reasoning_assessment
                if ra.logical_connection_quality in [LogicalConnectionQuality.WEAK, LogicalConnectionQuality.NONE]:
                    logical_gaps.append({
                        "gap_description": ra.logic_explanation or "Weak or missing logical connection",
                        "turn_number": analysis.turn_number,
                        "quote": ra.logic_evidence_quote or analysis.content[:80],
                        "severity": "high" if ra.logical_connection_quality == LogicalConnectionQuality.NONE else "medium",
                    })

        # Calculate analytical depth from reasoning quality distribution
        quality_counts = {q: 0 for q in LogicalConnectionQuality}
        for analysis in analyses:
            if analysis.reasoning_assessment:
                quality_counts[analysis.reasoning_assessment.logical_connection_quality] += 1

        total = sum(quality_counts.values()) or 1
        strong_pct = quality_counts[LogicalConnectionQuality.STRONG] / total
        moderate_pct = quality_counts[LogicalConnectionQuality.MODERATE] / total

        if strong_pct >= 0.5:
            analytical_depth = 5
        elif strong_pct >= 0.3 or (strong_pct + moderate_pct) >= 0.6:
            analytical_depth = 4
        elif moderate_pct >= 0.3:
            analytical_depth = 3
        elif moderate_pct > 0:
            analytical_depth = 2
        else:
            analytical_depth = 1

        # Build analytical depth evidence
        depth_evidence = []
        for analysis in analyses:
            if analysis.reasoning_assessment and analysis.reasoning_assessment.logical_connection_quality == LogicalConnectionQuality.STRONG:
                depth_evidence.append(ScoringEvidence(
                    turn_number=analysis.turn_number,
                    quote=analysis.reasoning_assessment.logic_evidence_quote or "",
                    contribution=ContributionType.POSITIVE,
                    weight=0.15,
                    explanation=analysis.reasoning_assessment.logic_explanation or "Strong logical reasoning",
                ))

        # Build data utilization tracking
        data_util = {}
        for analysis in analyses:
            if analysis.reasoning_assessment:
                for cat in analysis.reasoning_assessment.data_categories_used_effectively:
                    if cat not in data_util:
                        data_util[cat] = {"status": "used_effectively", "evidence_quotes": [], "turn_numbers": []}
                    data_util[cat]["turn_numbers"].append(analysis.turn_number)

                for cat in analysis.reasoning_assessment.data_categories_referenced:
                    if cat not in data_util:
                        data_util[cat] = {"status": "mentioned", "evidence_quotes": [], "turn_numbers": []}
                    if cat not in analysis.reasoning_assessment.data_categories_used_effectively:
                        data_util[cat]["turn_numbers"].append(analysis.turn_number)

        # Use validation data if provided
        rec_quality = 3  # Default moderate
        rec_evidence = []
        summary = "Assessment based on turn-by-turn analysis"

        if validation:
            if "recommendation_quality" in validation:
                rec_quality = validation["recommendation_quality"]
            if "summary" in validation:
                summary = validation["summary"]
            if "analytical_depth" in validation:
                analytical_depth = validation["analytical_depth"]

        return LogicalAssessmentEvidence(
            assumptions=assumptions,
            logical_gaps=logical_gaps,
            analytical_depth=analytical_depth,
            analytical_depth_evidence=depth_evidence,
            recommendation_quality=rec_quality,
            recommendation_evidence=rec_evidence,
            data_utilization=data_util,
            summary=summary,
        )

    def _generate_summaries(
        self,
        analyses: list[TurnAnalysis],
        scores: list[CompetencyScore],
        personality: PersonalityInference,
    ) -> tuple[str, list[str], list[str]]:
        """Generate overall summary, strengths, and development areas."""
        # Find top scores
        sorted_scores = sorted(scores, key=lambda s: s.score, reverse=True)
        top_competencies = [s for s in sorted_scores[:2] if s.score >= 0.6]
        weak_competencies = [s for s in sorted_scores[-2:] if s.score < 0.5]

        # Build strengths
        strengths = []
        for score in top_competencies:
            top_evidence = score.get_top_evidence(1)
            if top_evidence:
                strengths.append(
                    f"{score.dimension.value.replace('_', ' ').title()}: \"{top_evidence[0].quote[:50]}...\""
                )

        # Build development areas
        development = []
        for score in weak_competencies:
            neg_evidence = [e for e in score.evidence if e.contribution == ContributionType.NEGATIVE]
            if neg_evidence:
                development.append(
                    f"{score.dimension.value.replace('_', ' ').title()}: {neg_evidence[0].explanation[:80]}"
                )

        # Overall summary
        avg_score = sum(s.score for s in scores) / len(scores) if scores else 0.5
        level = "strong" if avg_score >= 0.65 else "solid" if avg_score >= 0.5 else "developing"

        personality_desc = personality.inferred_vector.to_description()
        summary = (
            f"Candidate demonstrated {level} overall performance across {len(analyses)} turns. "
            f"Personality profile: {personality_desc}. "
            f"Top competencies: {', '.join(s.dimension.value for s in top_competencies) or 'N/A'}."
        )

        return summary, strengths, development


# =============================================================================
# Convenience Function
# =============================================================================

def build_evidence_based_assessment(
    session_id: str,
    candidate_name: str,
    turn_analyses: list[TurnAnalysis],
    logical_validation: Optional[dict] = None,
) -> EvidenceBasedAssessment:
    """
    Convenience function to build an evidence-based assessment.

    Args:
        session_id: Session identifier.
        candidate_name: Name of the candidate.
        turn_analyses: List of analyzed candidate turns.
        logical_validation: Optional validator output.

    Returns:
        Complete EvidenceBasedAssessment.
    """
    builder = AssessmentBuilder(session_id, candidate_name)
    return builder.build_assessment(turn_analyses, logical_validation)
