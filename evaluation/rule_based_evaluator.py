"""
Rule-Based OCEAN Evaluator: Deterministic personality scoring from behavioral features.

Provides an independent, non-LLM evaluation layer to cross-validate LLM ensemble
judgments. Uses sigmoid-normalized weighted feature combinations to produce
OCEAN scores (0.0-1.0).

This addresses the LLM-evaluates-LLM circularity concern by offering a fully
deterministic scoring method based on psycholinguistic feature-trait mappings.
"""

import math
from experiment.behavioral_features import BehavioralFeatures


# =============================================================================
# SIGMOID NORMALIZATION
# =============================================================================

def sigmoid_normalize(x: float, midpoint: float, steepness: float = 1.0) -> float:
    """
    Map raw feature value to 0.0-1.0 via sigmoid.

    Args:
        x: Raw feature value.
        midpoint: Value that maps to 0.5 (median from pilot data).
        steepness: Controls how quickly the function approaches 0/1.

    Returns:
        Normalized score in [0.0, 1.0].
    """
    z = steepness * (x - midpoint)
    # Clamp to prevent overflow
    z = max(-20.0, min(20.0, z))
    return 1.0 / (1.0 + math.exp(-z))


# =============================================================================
# CALIBRATION PARAMETERS (derived from pilot data, 4 sessions)
# =============================================================================
# midpoint = approximate median across pilot sessions
# steepness tuned so extreme profiles map to ~0.8/0.2

CALIBRATION = {
    # Feature: (midpoint, steepness)
    # --- Original 22 features ---
    "avg_words_per_turn":       (30.0,  0.06),
    "max_words_in_turn":        (50,    0.04),
    "min_words_in_turn":        (8,     0.15),
    "word_count_variance":      (12.0,  0.08),
    "question_ratio":           (0.3,   4.0),
    "exclamation_ratio":        (0.15,  6.0),
    "hedge_count":              (3.0,   0.5),
    "certainty_count":          (2.0,   0.6),
    "first_person_ratio":       (0.06,  20.0),
    "inclusive_pronoun_ratio":   (0.02,  40.0),
    "disagreement_count":       (2.0,   0.5),
    "acknowledgment_count":     (3.0,   0.4),
    "idea_count":               (2.0,   0.5),
    "name_mention_count":       (3.0,   0.4),
    "conditional_ratio":        (0.15,  6.0),
    "planning_count":           (2.0,   0.5),
    "emotional_word_count":     (1.5,   0.7),
    "positive_emotion_count":   (1.5,   0.7),
    "turn_initiation_ratio":    (0.2,   5.0),
    "avg_response_latency_rank":(1.5,   -1.5),  # Lower rank = more extraverted (inverted)
    "unique_word_ratio":        (0.55,  5.0),
    "long_sentence_ratio":      (0.15,  6.0),
    # --- 8 new features (Critiques 2 & 3) ---
    "structure_marker_count":   (2.0,   0.5),
    "reference_back_count":     (1.5,   0.6),
    "action_item_count":        (1.0,   0.7),
    "hypothetical_count":       (1.5,   0.6),
    "apology_count":            (1.0,   0.8),
    "self_doubt_count":         (0.5,   1.0),
    "reassurance_seeking_count":(1.0,   0.7),
    "negation_count":           (5.0,   0.2),
}


def _norm(feature_name: str, value: float) -> float:
    """Normalize a feature value using its calibration parameters."""
    midpoint, steepness = CALIBRATION[feature_name]
    return sigmoid_normalize(value, midpoint, steepness)


def _inv(score: float) -> float:
    """Invert a normalized score (for negative signals)."""
    return 1.0 - score


# =============================================================================
# TRAIT FORMULAS
# =============================================================================

def _score_openness(f: BehavioralFeatures) -> float:
    """Openness: vocabulary diversity, novel ideas, hypotheticals, complex expression, curiosity."""
    return (
        0.20 * _norm("unique_word_ratio", f.unique_word_ratio)
        + 0.25 * _norm("idea_count", f.idea_count)
        + 0.15 * _norm("hypothetical_count", f.hypothetical_count)
        + 0.15 * _norm("word_count_variance", f.word_count_variance)
        + 0.15 * _norm("long_sentence_ratio", f.long_sentence_ratio)
        + 0.10 * _norm("question_ratio", f.question_ratio)
    )


def _score_conscientiousness(f: BehavioralFeatures) -> float:
    """Conscientiousness: planning, structure markers, backward references, action items, thoroughness."""
    return (
        0.20 * _norm("planning_count", f.planning_count)
        + 0.20 * _norm("structure_marker_count", f.structure_marker_count)
        + 0.20 * _norm("conditional_ratio", f.conditional_ratio)
        + 0.15 * _norm("reference_back_count", f.reference_back_count)
        + 0.10 * _norm("action_item_count", f.action_item_count)
        + 0.15 * _inv(_norm("emotional_word_count", f.emotional_word_count))
    )


def _score_extraversion(f: BehavioralFeatures) -> float:
    """Extraversion: verbosity, social engagement, assertiveness, initiative."""
    return (
        0.30 * _norm("avg_words_per_turn", f.avg_words_per_turn)
        + 0.15 * _norm("question_ratio", f.question_ratio)
        + 0.10 * _norm("exclamation_ratio", f.exclamation_ratio)
        + 0.15 * _norm("name_mention_count", f.name_mention_count)
        + 0.10 * _norm("certainty_count", f.certainty_count)
        + 0.10 * _norm("turn_initiation_ratio", f.turn_initiation_ratio)
        + 0.10 * _inv(_norm("hedge_count", f.hedge_count))
    )


def _score_agreeableness(f: BehavioralFeatures) -> float:
    """Agreeableness: cooperation, warmth, social attentiveness vs. conflict and negation."""
    return (
        0.25 * _norm("acknowledgment_count", f.acknowledgment_count)
        + 0.20 * _inv(_norm("disagreement_count", f.disagreement_count))
        + 0.15 * _norm("inclusive_pronoun_ratio", f.inclusive_pronoun_ratio)
        + 0.15 * _norm("positive_emotion_count", f.positive_emotion_count)
        + 0.10 * _norm("name_mention_count", f.name_mention_count)
        + 0.15 * _inv(_norm("negation_count", f.negation_count))
    )


def _score_neuroticism(f: BehavioralFeatures) -> float:
    """Neuroticism: uncertainty, apology, self-doubt, reassurance seeking, negative affect."""
    return (
        0.15 * _norm("hedge_count", f.hedge_count)
        + 0.15 * _norm("emotional_word_count", f.emotional_word_count)
        + 0.10 * _norm("apology_count", f.apology_count)
        + 0.10 * _norm("self_doubt_count", f.self_doubt_count)
        + 0.10 * _norm("reassurance_seeking_count", f.reassurance_seeking_count)
        + 0.15 * _norm("first_person_ratio", f.first_person_ratio)
        + 0.10 * _norm("word_count_variance", f.word_count_variance)
        + 0.10 * _inv(_norm("certainty_count", f.certainty_count))
        + 0.05 * _inv(_norm("positive_emotion_count", f.positive_emotion_count))
    )


# =============================================================================
# PUBLIC API
# =============================================================================

def evaluate_rule_based(features: BehavioralFeatures) -> dict[str, float]:
    """
    Return OCEAN dict with scores 0.0-1.0, purely from behavioral features.

    This is fully deterministic — no LLM involved. Provides an independent
    validation layer against the LLM ensemble evaluation.

    Args:
        features: Extracted behavioral features from a session.

    Returns:
        Dict with keys "O", "C", "E", "A", "N" mapping to scores 0.0-1.0.
    """
    return {
        "O": round(_score_openness(features), 4),
        "C": round(_score_conscientiousness(features), 4),
        "E": round(_score_extraversion(features), 4),
        "A": round(_score_agreeableness(features), 4),
        "N": round(_score_neuroticism(features), 4),
    }
