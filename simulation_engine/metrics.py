"""Deterministic metrics for stakeholder-simulation stability evaluation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from experiment.behavioral_features import extract_features
from experiment.memory_backend import Commitment, detect_commitment_contradiction

from .runtime import RuntimeTurnView, StakeholderSimulationRuntime
from .script import StakeholderActorSpec

TRAIT_KEYS = ("O", "C", "E", "A", "N")
RELATION_SENTIMENT_SCORE = {
    "negative": -1.0,
    "challenging": -0.3,
    "neutral": 0.0,
    "positive": 1.0,
}


def _clip_unit(value: float) -> float:
    return max(0.0, min(1.0, round(float(value), 4)))


def estimate_actor_traits_from_turns(
    turns: list[RuntimeTurnView],
    actor_name: str,
) -> dict[str, float]:
    """Estimate OCEAN expression using existing behavioral feature extraction."""
    features = extract_features(turns=turns, candidate_name=actor_name)

    openness = _clip_unit(
        0.25
        + 0.10 * min(features.idea_count, 4)
        + 0.10 * min(features.hypothetical_count, 3)
        + 0.90 * min(features.unique_word_ratio, 0.20)
    )
    conscientiousness = _clip_unit(
        0.20
        + 0.08 * min(features.planning_count, 4)
        + 0.10 * min(features.structure_marker_count, 3)
        + 0.08 * min(features.reference_back_count, 3)
        + 0.10 * min(features.action_item_count, 3)
    )
    extraversion = _clip_unit(
        0.20
        + min(features.avg_words_per_turn, 80.0) / 120.0
        + 0.08 * min(features.name_mention_count, 3)
        + 0.12 * min(features.question_ratio, 1.0)
        + 0.10 * min(features.turn_initiation_ratio, 1.0)
    )
    agreeableness = _clip_unit(
        0.45
        + 0.10 * min(features.acknowledgment_count, 4)
        - 0.10 * min(features.disagreement_count, 4)
        - 0.02 * min(features.negation_count, 6)
    )
    neuroticism = _clip_unit(
        0.18
        + 0.08 * min(features.hedge_count, 4)
        + 0.10 * min(features.self_doubt_count, 3)
        + 0.08 * min(features.reassurance_seeking_count, 3)
        + 0.06 * min(features.apology_count, 2)
        + 0.04 * min(features.emotional_word_count, 3)
    )

    return {
        "O": openness,
        "C": conscientiousness,
        "E": extraversion,
        "A": agreeableness,
        "N": neuroticism,
    }


def persona_drift_mae(
    personality_prior: dict[str, float],
    inferred_traits: dict[str, float],
) -> float:
    return round(
        sum(abs(inferred_traits[trait] - personality_prior[trait]) for trait in TRAIT_KEYS) / 5.0,
        4,
    )


def trait_absolute_errors(
    personality_prior: dict[str, float],
    inferred_traits: dict[str, float],
) -> dict[str, float]:
    return {
        trait: round(abs(inferred_traits[trait] - personality_prior[trait]), 4)
        for trait in TRAIT_KEYS
    }


def envelope_violation_count(
    actor_spec: StakeholderActorSpec,
    inferred_traits: dict[str, float],
) -> int:
    violations = 0
    for trait, value in inferred_traits.items():
        low, high = actor_spec.personality_envelope[trait]
        if value < low or value > high:
            violations += 1
    return violations


def relationship_inconsistency_rate(runtime: StakeholderSimulationRuntime) -> float:
    events = [event for event in runtime.ledger.relationship_events if event.get("sentiment") != "neutral"]
    if len(events) < 2:
        return 0.0

    by_edge: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for event in events:
        key = (event["source_actor_id"], event["target_actor_id"])
        by_edge.setdefault(key, []).append(event)

    edge_scores: list[float] = []
    for edge_events in by_edge.values():
        if len(edge_events) < 2:
            continue
        ordered = sorted(edge_events, key=lambda item: item["turn_index"])
        step_scores: list[float] = []
        for prior, current in zip(ordered, ordered[1:]):
            prior_score = RELATION_SENTIMENT_SCORE.get(prior["sentiment"], 0.0)
            current_score = RELATION_SENTIMENT_SCORE.get(current["sentiment"], 0.0)
            score_swing = abs(current_score - prior_score)
            trust_swing = abs(float(current["trust"]) - float(prior["trust"]))
            tension_swing = abs(float(current["tension"]) - float(prior["tension"]))

            step = 0.0
            if (prior_score > 0.35 and current_score < -0.35) or (prior_score < -0.35 and current_score > 0.35):
                step += 0.75
            elif score_swing >= 0.7:
                step += 0.45
            elif score_swing >= 0.3:
                step += 0.18

            step += max(0.0, trust_swing - 0.12) * 1.6
            step += max(0.0, tension_swing - 0.12) * 1.8

            if prior["sentiment"] == "positive" and current["sentiment"] == "challenging":
                step += 0.10
            if prior["sentiment"] == "challenging" and current["sentiment"] == "negative":
                step += 0.10

            step_scores.append(min(1.0, step))
        if step_scores:
            edge_scores.append(sum(step_scores) / len(step_scores))

    if not edge_scores:
        return 0.0
    return round(sum(edge_scores) / len(edge_scores), 4)


def commitment_contradiction_rate(runtime: StakeholderSimulationRuntime) -> float:
    contradictions = 0
    eligible_turns = 0

    by_actor: dict[str, list[Commitment]] = {
        actor_id: []
        for actor_id in runtime.actors
    }
    for turn in runtime.ledger.turns:
        open_commitments = [c for c in by_actor[turn.actor_id] if c.status == "open"]
        if open_commitments:
            eligible_turns += 1
            if detect_commitment_contradiction(turn.content, open_commitments):
                contradictions += 1
        for commitment in runtime.ledger.commitments_by_actor.get(turn.actor_id, []):
            if commitment.created_turn == turn.turn_index:
                by_actor[turn.actor_id].append(commitment)

    return round(contradictions / max(eligible_turns, 1), 4)


@dataclass
class BenchmarkRunMetrics:
    persona_drift_mae: float
    relationship_inconsistency: float
    commitment_contradiction_rate: float
    envelope_violations: int
    per_trait_error_mean: dict[str, float]
    actor_labels: dict[str, str]
    actor_display_names: dict[str, str]
    actor_trait_estimates: dict[str, dict[str, float]]
    actor_trait_errors: dict[str, dict[str, float]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "persona_drift_mae": self.persona_drift_mae,
            "relationship_inconsistency": self.relationship_inconsistency,
            "commitment_contradiction_rate": self.commitment_contradiction_rate,
            "envelope_violations": self.envelope_violations,
            "per_trait_error_mean": self.per_trait_error_mean,
            "actor_labels": self.actor_labels,
            "actor_display_names": self.actor_display_names,
            "actor_trait_estimates": self.actor_trait_estimates,
            "actor_trait_errors": self.actor_trait_errors,
        }


def compute_runtime_metrics(runtime: StakeholderSimulationRuntime) -> BenchmarkRunMetrics:
    actor_trait_estimates: dict[str, dict[str, float]] = {}
    actor_trait_errors: dict[str, dict[str, float]] = {}
    drift_values: list[float] = []
    envelope_violations = 0
    per_trait_buckets: dict[str, list[float]] = {trait: [] for trait in TRAIT_KEYS}

    for actor_id, actor in runtime.actors.items():
        turns = runtime.visible_turns_for_actor(actor_id, max_turns=999)
        inferred = estimate_actor_traits_from_turns(turns, actor.display_name)
        errors = trait_absolute_errors(actor.actor_spec.personality_prior, inferred)
        actor_trait_estimates[actor_id] = inferred
        actor_trait_errors[actor_id] = errors
        drift_values.append(persona_drift_mae(actor.actor_spec.personality_prior, inferred))
        envelope_violations += envelope_violation_count(actor.actor_spec, inferred)
        for trait, error in errors.items():
            per_trait_buckets[trait].append(error)

    return BenchmarkRunMetrics(
        persona_drift_mae=round(sum(drift_values) / max(len(drift_values), 1), 4),
        relationship_inconsistency=relationship_inconsistency_rate(runtime),
        commitment_contradiction_rate=commitment_contradiction_rate(runtime),
        envelope_violations=envelope_violations,
        per_trait_error_mean={
            trait: round(sum(values) / max(len(values), 1), 4)
            for trait, values in per_trait_buckets.items()
        },
        actor_labels=dict(runtime.script.actor_analysis_label_map),
        actor_display_names=dict(runtime.script.actor_display_name_map),
        actor_trait_estimates=actor_trait_estimates,
        actor_trait_errors=actor_trait_errors,
    )
