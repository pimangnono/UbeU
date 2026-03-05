"""
Persona Compiler: Deterministic behavior contract generation from OCEAN vectors.

Inverts the rule-based evaluator's feature-trait weights to produce target
feature ranges, action policies, and hard constraints. Module 1 of BCFC.

Fully deterministic — no API calls. Runs once per profile before a session.
"""

import math
from dataclasses import dataclass, field, asdict
from evaluation.rule_based_evaluator import CALIBRATION
from experiment.bcfc_config import get_feature_reliability


# =============================================================================
# SIGMOID INVERSION
# =============================================================================

def invert_sigmoid(target_score: float, midpoint: float, steepness: float) -> float:
    """
    Given a target normalized score (0-1), compute the raw feature value
    that would produce it via sigmoid normalization.

    Inverse of: sigmoid(x, mid, steep) = 1/(1+exp(-steep*(x-mid)))
    Solution:   x = mid - ln(1/s - 1) / steep
    """
    target_score = max(0.02, min(0.98, target_score))
    if abs(steepness) < 1e-6:
        return midpoint
    return midpoint - math.log(1.0 / target_score - 1.0) / steepness


# =============================================================================
# FEATURE-TRAIT MAPPINGS (mirrors rule_based_evaluator.py formulas exactly)
# =============================================================================
# Each entry: (feature_name, weight, inverted)
# inverted=True means the feature contributes via 1 - norm(x)

TRAIT_FEATURE_MAP = {
    "O": [
        ("unique_word_ratio", 0.20, False),
        ("idea_count", 0.25, False),
        ("hypothetical_count", 0.15, False),
        ("word_count_variance", 0.15, False),
        ("long_sentence_ratio", 0.15, False),
        ("question_ratio", 0.10, False),
    ],
    "C": [
        ("planning_count", 0.20, False),
        ("structure_marker_count", 0.20, False),
        ("conditional_ratio", 0.20, False),
        ("reference_back_count", 0.15, False),
        ("action_item_count", 0.10, False),
        ("emotional_word_count", 0.15, True),
    ],
    "E": [
        ("avg_words_per_turn", 0.30, False),
        ("question_ratio", 0.15, False),
        ("exclamation_ratio", 0.10, False),
        ("name_mention_count", 0.15, False),
        ("certainty_count", 0.10, False),
        ("turn_initiation_ratio", 0.10, False),
        ("hedge_count", 0.10, True),
    ],
    "A": [
        ("acknowledgment_count", 0.25, False),
        ("disagreement_count", 0.20, True),
        ("inclusive_pronoun_ratio", 0.15, False),
        ("positive_emotion_count", 0.15, False),
        ("name_mention_count", 0.10, False),
        ("negation_count", 0.15, True),
    ],
    "N": [
        ("hedge_count", 0.15, False),
        ("emotional_word_count", 0.15, False),
        ("apology_count", 0.10, False),
        ("self_doubt_count", 0.10, False),
        ("reassurance_seeking_count", 0.10, False),
        ("first_person_ratio", 0.15, False),
        ("word_count_variance", 0.10, False),
        ("certainty_count", 0.10, True),
        ("positive_emotion_count", 0.05, True),
    ],
}

# =============================================================================
# FEATURE TYPE HINTS (for range construction)
# =============================================================================

RATIO_SUFFIX = "_ratio"
COUNT_SUFFIX = "_count"

# Non-negative continuous features (not *_count but should never be < 0)
NONNEGATIVE_FEATURES = {
    "avg_words_per_turn",
    "max_words_in_turn",
    "word_count_variance",
}

# Minimum range widths by type (prevents degenerate ranges)
MIN_WIDTH = {
    "ratio": 0.05,
    "count": 0.5,
    "nonneg": 0.5,
    "signed": 0.5,
}


def _feature_type(feature_name: str) -> str:
    if feature_name.endswith(RATIO_SUFFIX):
        return "ratio"
    if feature_name.endswith(COUNT_SUFFIX):
        return "count"
    if feature_name in NONNEGATIVE_FEATURES:
        return "nonneg"
    return "signed"


# =============================================================================
# ACTION POLICIES (per-turn behavioral mandates by trait level)
# =============================================================================

ACTION_POLICIES = {
    "O": {
        "High": [
            "Propose an alternative approach to the current suggestion",
            "Connect the current topic to a different domain or analogy",
            "Challenge an underlying assumption in someone's argument",
        ],
        "Low": [
            "Advocate for the conventional, proven approach",
            "Question unproven ideas by asking about track records",
        ],
    },
    "C": {
        "High": [
            "Recap a decision or commitment from earlier in the discussion",
            "Assign ownership for the next action item",
            "Break down a complex proposal into numbered steps",
        ],
        "Low": [
            "Respond intuitively without structured organization",
            "Resist when others try to impose rigid processes",
        ],
    },
    "E": {
        "High": [
            "Address another participant by name",
            "Ask an engaging follow-up question",
            "Elaborate on a point beyond the minimum needed",
        ],
        "Low": [
            "Keep response under 40 words",
            "Wait to be addressed rather than volunteering",
        ],
    },
    "A": {
        "High": [
            "Find common ground with the last speaker's position",
            "Validate something specific about another's contribution",
        ],
        "Low": [
            "Identify a weakness or flaw in the current proposal",
            "State a clear opposing position on a point of disagreement",
        ],
    },
    "N": {
        "High": [
            "Express concern about a potential negative outcome",
            "Qualify a statement with uncertainty language",
        ],
        "Low": [
            "Reframe a problem as a solvable challenge",
            "State a position with confident, steady language",
        ],
    },
}


# =============================================================================
# HARD CONSTRAINTS (binary rules for generate-check-regenerate)
# =============================================================================

HARD_CONSTRAINTS = {
    ("A", "Low"): (
        "Never agree with a proposal without first identifying at least one "
        "weakness, concern, or area that needs improvement."
    ),
    ("A", "High"): (
        "Never directly criticize another participant's idea without first "
        "acknowledging what is valuable about it."
    ),
    ("C", "High"): (
        "In responses longer than one sentence, include at least one concrete "
        "organizational element: a deadline, an owner, a next step, or a "
        "reference to a prior commitment."
    ),
    ("C", "Low"): (
        "Do not impose numbered lists, deadlines, or structured processes "
        "unless directly asked to do so."
    ),
    ("O", "High"): (
        "When someone suggests a standard solution, offer at least one "
        "alternative angle or creative variation before accepting it."
    ),
    ("N", "Low"): (
        "Never express self-doubt, seek reassurance, or use apologetic "
        "language about your own contributions."
    ),
    ("N", "High"): (
        "When challenged or under pressure, include at least one qualifier, "
        "hedge, or expression of uncertainty in your response."
    ),
    ("E", "Low"): (
        "Keep responses under 50 words unless directly asked to elaborate."
    ),
    ("E", "High"): (
        "Address at least one other participant by name in every response."
    ),
}

# Constraint conflict pairs: when both traits are extreme, the first
# constraint is demoted to soft (nudge-only, no regeneration).
# Format: ((trait1, level1), (trait2, level2)) → demoted key
CONSTRAINT_CONFLICTS = [
    # High C (org elements → longer) conflicts with Low E (brevity)
    (("C", "High"), ("E", "Low"), ("C", "High")),
    # High C (org elements) conflicts with High N (hedging → already adds length)
    (("C", "High"), ("N", "High"), ("C", "High")),
]


# =============================================================================
# BEHAVIOR CONTRACT
# =============================================================================

@dataclass
class BehaviorContract:
    """
    Complete behavioral specification for a personality profile.

    Produced by the Persona Compiler from an OCEAN vector.
    Consumed by the Fidelity Controller at runtime.
    """
    profile_id: str
    ocean_vector: dict
    target_features: dict  # feature_name -> {target, min, max, trait, weight, inverted, reliability}
    action_policies: list  # action strings to cycle through
    hard_constraints: list  # never-violate rules (penalized in BoN scoring)
    soft_constraints: list = field(default_factory=list)  # nudge-only (no regeneration)
    invalid_features: list = field(default_factory=list)  # range construction failures
    pressure_rule: str = (
        "If challenged, first acknowledge the specific concern raised, "
        "then execute your trait-consistent action."
    )
    continuity_rule: str = (
        "Reference at least one open item, prior decision, or earlier "
        "discussion point from the conversation so far."
    )

    def to_dict(self) -> dict:
        return asdict(self)


# =============================================================================
# COMPILER
# =============================================================================

def _get_trait_level(value: float) -> str:
    """Map trait value to level (same logic as ExperimentProfile)."""
    if value >= 0.7:
        return "High"
    elif value >= 0.6:
        return "Moderate-High"
    elif value >= 0.4:
        return "Moderate"
    elif value >= 0.31:
        return "Moderate-Low"
    else:
        return "Low"


def compile_contract(profile_id: str, ocean_vector: dict) -> BehaviorContract:
    """
    Compile an OCEAN vector into a BehaviorContract.

    Deterministic — no API calls. Inverts the sigmoid normalizations in
    rule_based_evaluator.py to compute target raw feature values.

    Args:
        profile_id: Identifier for the profile (for logging).
        ocean_vector: Dict {"O", "C", "E", "A", "N"} with values 0.0-1.0.

    Returns:
        BehaviorContract with target features, actions, and constraints.
    """
    target_features: dict[str, dict] = {}
    invalid_features: list[dict] = []
    actions: list[str] = []
    all_constraint_keys: list[tuple[str, str]] = []

    for trait_key, feature_specs in TRAIT_FEATURE_MAP.items():
        trait_score = ocean_vector[trait_key]
        trait_level = _get_trait_level(trait_score)

        # Compute target feature ranges by inverting sigmoid
        for feature_name, weight, inverted in feature_specs:
            if feature_name not in CALIBRATION:
                continue

            midpoint, steepness = CALIBRATION[feature_name]

            # Target normalized score for this feature
            target_norm = (1.0 - trait_score) if inverted else trait_score

            # Invert sigmoid to get target raw value
            target_raw = invert_sigmoid(target_norm, midpoint, steepness)

            # Compute range with type-aware constraints
            ftype = _feature_type(feature_name)
            if ftype == "ratio":
                margin = max(abs(target_raw * 0.3), MIN_WIDTH["ratio"])
                min_raw = max(0.0, target_raw - margin)
                max_raw = min(1.0, target_raw + margin)
                if (max_raw - min_raw) < MIN_WIDTH["ratio"]:
                    expand = (MIN_WIDTH["ratio"] - (max_raw - min_raw)) / 2
                    min_raw = max(0.0, min_raw - expand)
                    max_raw = min(1.0, max_raw + expand)
            elif ftype == "count":
                margin = max(abs(target_raw * 0.3), 1.0)
                min_raw = max(0.0, target_raw - margin)
                max_raw = max(target_raw + margin, min_raw + MIN_WIDTH["count"], 0.0)
            elif ftype == "nonneg":
                margin = max(abs(target_raw * 0.3), MIN_WIDTH["nonneg"])
                min_raw = max(0.0, target_raw - margin)
                max_raw = max(target_raw + margin, min_raw + MIN_WIDTH["nonneg"], 0.0)
            else:
                margin = max(abs(target_raw * 0.3), MIN_WIDTH["signed"])
                min_raw = target_raw - margin
                max_raw = target_raw + margin

            # Validate range; skip invalid features to avoid exploding distances
            if max_raw <= min_raw:
                invalid_features.append({
                    "feature": feature_name,
                    "target_raw": round(target_raw, 4),
                    "min_raw": round(min_raw, 4),
                    "max_raw": round(max_raw, 4),
                    "type": ftype,
                })
                continue

            # Keep the feature with highest weight if it appears in multiple traits
            if feature_name in target_features:
                if weight <= target_features[feature_name].get("weight", 0):
                    continue

            target_features[feature_name] = {
                "target": round(target_raw, 2),
                "min": round(min_raw, 2),
                "max": round(max_raw, 2),
                "trait": trait_key,
                "weight": round(weight, 2),
                "inverted": inverted,
                "reliability": round(get_feature_reliability(feature_name), 2),
            }

        # Collect action policies for extreme traits
        if trait_level in ("High", "Low"):
            policy_list = ACTION_POLICIES.get(trait_key, {}).get(trait_level, [])
            actions.extend(policy_list)

        # Collect constraint keys for extreme traits
        constraint_key = (trait_key, trait_level)
        if constraint_key in HARD_CONSTRAINTS:
            all_constraint_keys.append(constraint_key)

    # Detect conflicting constraints and demote the specified one to soft
    demoted_keys: set[tuple[str, str]] = set()
    active_key_set = set(all_constraint_keys)
    for key_a, key_b, demote_key in CONSTRAINT_CONFLICTS:
        if key_a in active_key_set and key_b in active_key_set:
            demoted_keys.add(demote_key)

    hard_constraints = []
    soft_constraints = []
    for ck in all_constraint_keys:
        text = HARD_CONSTRAINTS[ck]
        if ck in demoted_keys:
            soft_constraints.append(text)
        else:
            hard_constraints.append(text)

    return BehaviorContract(
        profile_id=profile_id,
        ocean_vector=ocean_vector,
        target_features=target_features,
        action_policies=actions,
        hard_constraints=hard_constraints,
        soft_constraints=soft_constraints,
        invalid_features=invalid_features,
    )
