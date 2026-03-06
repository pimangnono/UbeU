"""
BCFC v1.1 Configuration

Centralizes tunable parameters that must be frozen after the Stage-1 pilot.
All defaults here should be treated as frozen for the main run.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
from typing import Dict, List


# -------------------------------
# Model pricing (optional)
# -------------------------------
# Optional override via env MODEL_PRICES_JSON (per-1M tokens):
# {"model_name": {"prompt": 1.0, "completion": 1.0}}

def _load_model_prices() -> dict:
    raw = os.getenv("MODEL_PRICES_JSON")
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


MODEL_PRICES_PER_1M = _load_model_prices()


# -------------------------------
# Feature reliability weights
# -------------------------------
# Based on validation correlations in prior analysis. Values are frozen after
# Stage-1 pilot. Any missing feature defaults to 0.5.

FEATURE_RELIABILITY: Dict[str, float] = {
    # Strong / stable
    "planning_count": 1.0,
    "structure_marker_count": 1.0,
    "action_item_count": 1.0,
    "avg_words_per_turn": 1.0,
    "max_words_in_turn": 1.0,
    "negation_count": 1.0,
    "hedge_count": 1.0,
    "emotional_word_count": 1.0,

    # Moderate
    "acknowledgment_count": 0.5,
    "disagreement_count": 0.5,
    "positive_emotion_count": 0.5,
    "name_mention_count": 0.5,
    "unique_word_ratio": 0.5,
    "long_sentence_ratio": 0.5,
    "question_ratio": 0.5,
    "exclamation_ratio": 0.5,
    "first_person_ratio": 0.5,
    "inclusive_pronoun_ratio": 0.5,
    "conditional_ratio": 0.5,
    "reference_back_count": 0.5,
    "hypothetical_count": 0.5,

    # Weak / unstable
    "idea_count": 0.1,
    "word_count_variance": 0.1,
    "apology_count": 0.1,
    "self_doubt_count": 0.1,
    "reassurance_seeking_count": 0.1,
}


# -------------------------------
# Constraint penalties
# -------------------------------
# Penalties are applied in the BoN adequacy component.

CONSTRAINT_PENALTIES: Dict[str, float] = {
    "agreed_without_concern": 0.4,
    "criticized_without_acknowledgment": 0.4,
    "no_organizational_element": 0.3,
    "imposed_unsolicited_structure": 0.3,
    "accepted_without_alternative": 0.3,
    "expressed_self_doubt": 0.3,
    "no_hedge_under_pressure": 0.3,
    "response_too_long": 0.2,
    "no_name_mention": 0.2,
}


@dataclass
class BCFCConfig:
    # Best-of-N
    bon_n: int = 4
    bon_weights: dict = field(default_factory=lambda: {
        "contract": 0.65,
        "relevance": 0.20,
        "adequacy": 0.10,
        "redundancy": 0.05,
    })

    # Drift / controller
    drift_alpha: float = 0.5
    drift_threshold: float = 0.30
    drift_window_size: int = 4
    nudge_check_every: int = 2
    distance_clip: float = 3.0

    # Escalation triggers
    escalation_confidence_threshold: float = 0.5
    escalation_model_range_threshold: float = 0.20
    escalation_uncertain_only: bool = True

    # Staged execution sizes
    freeze_pilot_profiles: list = field(default_factory=lambda: [
        "anxious_perfectionist",
        "creative_rebel",
        "neutral_observer",
    ])
    freeze_pilot_scenario: str = "crisis_management"
    mid_check_size: int = 20
    mid_check_seed: int = 42

    # Compute-control subset
    bon_random_scenario: str = "resource_conflict"
    bon_random_reps: int = 2

    # Low-pressure manipulation
    low_pressure_scenario: str = "crisis_management_low"

    # Trajectory judge
    trajectory_context_turns: int = 6

    # Feature reliability
    feature_reliability: Dict[str, float] = field(default_factory=lambda: FEATURE_RELIABILITY)

    # BCFC v3 (mini experiment) - best-of-styles + phase-conditioned scoring
    v3_style_slots: list = field(default_factory=lambda: [
        "ideator",
        "planner",
        "challenger",
        "integrator",
    ])
    v3_global_contract_weight: float = 0.3
    v3_phase_trait_weights: dict = field(default_factory=lambda: {
        "FRAMING": {"O": 0.4, "C": 0.1, "E": 0.2, "A": 0.2, "N": 0.1},
        "ALTERNATIVES": {"O": 0.6, "C": 0.1, "E": 0.1, "A": 0.1, "N": 0.1},
        "DECISION": {"O": 0.1, "C": 0.6, "E": 0.1, "A": 0.1, "N": 0.1},
        "REVISION": {"O": 0.2, "C": 0.2, "E": 0.1, "A": 0.3, "N": 0.2},
    })

    # BCFC v4 (policy + phase-conditioned scoring)
    v4_style_slots: list = field(default_factory=lambda: [
        "ideator",
        "planner",
        "challenger",
        "integrator",
    ])
    v4_phase_slots: dict = field(default_factory=lambda: {
        "FRAMING": ["ideator", "integrator"],
        "ALTERNATIVES": ["ideator", "challenger", "integrator"],
        "DECISION": ["planner", "integrator"],
        "REVISION": ["challenger", "integrator"],
        "CRISIS_REVEAL": ["challenger", "planner", "integrator"],
        "INITIAL_REACTION": ["challenger", "integrator"],
        "PROBLEM_SOLVING": ["planner", "integrator"],
        "STRESS_TEST": ["challenger", "integrator"],
        "CLOSING": ["integrator", "planner"],
    })
    v4_score_weights: dict = field(default_factory=lambda: {
        "policy_match": 0.30,
        "situational_adequacy": 0.20,
        "commitment_continuity": 0.20,
        "trait_evidence": 0.15,
        "relationship_consistency": 0.10,
        "redundancy_penalty": 0.05,
    })

    # BCFC v5 (opportunity-gated trait execution)
    # Positive components sum to 0.95; redundancy is subtractive.
    v5_score_weights: dict = field(default_factory=lambda: {
        "policy_match": 0.30,
        "situational_adequacy": 0.17,
        "commitment_continuity": 0.17,
        "trait_evidence": 0.11,
        "relationship_consistency": 0.07,
        "trait_execution": 0.13,
        "redundancy_penalty": 0.05,
    })
    v5_phase_slots: dict = field(default_factory=lambda: {
        "FRAMING": ["ideator", "integrator"],
        "ALTERNATIVES": ["ideator", "challenger", "integrator"],
        "DECISION": ["planner", "integrator"],
        "REVISION": ["challenger", "integrator"],
        "CRISIS_REVEAL": ["challenger", "planner", "integrator"],
        "INITIAL_REACTION": ["challenger", "integrator"],
        "PROBLEM_SOLVING": ["planner", "integrator"],
        "STRESS_TEST": ["challenger", "integrator"],
        "CLOSING": ["integrator", "planner"],
    })
    v5_opportunity_gate_threshold: float = 0.35
    v5_activation_floor: float = 0.15
    v5_hard_activation_threshold: float = 0.55
    v5_adequacy_threshold: float = 0.55
    v5_tie_delta: float = 0.08
    v5_policy_tie_weight: float = 0.25
    v5_required_signal_counts: dict = field(default_factory=lambda: {
        "O": 1,
        "C": 1,
    })
    v5_opportunity_cue_map: dict = field(default_factory=lambda: {
        "O": [
            "ambiguity",
            "problem_reframing",
            "option_generation",
            "tradeoff_comparison",
            "reframe_request",
            "novelty",
            "ideation",
            "opportunity",
            "strategy_pivot",
        ],
        "C": [
            "owner_deadline_dependency",
            "structured_planning",
            "sequencing",
            "triage",
            "plan_under_pressure",
            "coordination",
            "commitment",
            "follow_up",
            "execution",
        ],
    })
    v5_context_keyword_map: dict = field(default_factory=lambda: {
        "O": [
            "unknown", "uncertain", "no data", "pivot", "alternative",
            "new approach", "reframe", "option", "experiment", "hypothesis",
        ],
        "C": [
            "owner", "responsible", "deadline", "due", "by when", "timeline",
            "sequence", "next step", "follow up", "contingency", "handoff",
        ],
    })
    # Signal categories used by the trait execution layer (coverage-based scoring).
    v5_trait_signal_keywords: dict = field(default_factory=lambda: {
        "O": {
            "alternative_generation": [
                "what if", "alternative", "another option", "another way",
                "we could", "new approach", "third option",
            ],
            "reframing_or_analogy": [
                "reframe", "different lens", "another way to look",
                "similar to", "as if", "analogy",
            ],
            "tradeoff_exploration": [
                "tradeoff", "upside", "downside", "pros and cons",
                "cost-benefit", "risk", "benefit",
            ],
        },
        "C": {
            "owner_assignment": [
                "owner", "assigned", "responsible", "ownership", "who will",
            ],
            "deadline_commitment": [
                "deadline", "due", "by ", "eod", "end of day", "timeline",
            ],
            "sequence_structure": [
                "first", "second", "next", "then", "after that", "step",
                "phase",
            ],
            "follow_up_or_contingency": [
                "follow up", "check in", "contingency", "fallback",
                "backup plan", "if", "in case",
            ],
        },
    })

    # Reporting sets: probe highlights detectability; robustness is the primary endpoint.
    probe_scenario_ids: list = field(default_factory=lambda: [
        "strategy_pivot",
        "release_recovery",
    ])
    robustness_scenario_ids: list = field(default_factory=lambda: [
        "resource_conflict",
        "creative_brainstorm",
        "crisis_management",
        "new_member_integration",
        "crisis_management_low",
    ])


def get_feature_reliability(feature_name: str) -> float:
    return FEATURE_RELIABILITY.get(feature_name, 0.5)


DEFAULT_CONFIG = BCFCConfig()
