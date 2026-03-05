"""
Fidelity Controller: Runtime behavioral deviation check and correction for BCFC.

BCFC v1.1 removes regeneration. Instead:
1. Fidelity Monitor (every N candidate turns): Checks incremental features
   against contract targets, generates corrective nudge for system prompt.
2. Hard Constraint Checker: Evaluates violations for scoring penalties only.

Monitoring is zero-cost (deterministic). Control is achieved via BoN reranking.
"""

import logging
import re
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from experiment.persona_compiler import BehaviorContract
from experiment.incremental_features import extract_incremental_features
from experiment.behavioral_features import (
    DISAGREEMENT_PHRASES,
    ACKNOWLEDGMENT_PHRASES,
    PLANNING_PHRASES,
    STRUCTURE_MARKER_PATTERNS,
    ACTION_ITEM_PHRASES,
    IDEA_PHRASES,
    HYPOTHETICAL_PHRASES,
    HEDGE_PHRASES,
    SELF_DOUBT_PHRASES,
    REASSURANCE_SEEKING_PHRASES,
)
from experiment.bcfc_config import DEFAULT_CONFIG, CONSTRAINT_PENALTIES

if TYPE_CHECKING:
    from utils.models import Turn

logger = logging.getLogger(__name__)


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class DeviationReport:
    """Report of feature deviations from behavior contract targets."""
    turn_number: int
    deviations: list
    nudge_text: str
    violation_rate: float  # 0.0-1.0, proportion of features outside range
    distance: float  # weighted distance
    delta: float  # composite drift

    def to_dict(self) -> dict:
        return {
            "turn_number": self.turn_number,
            "deviations": self.deviations,
            "nudge_text": self.nudge_text,
            "violation_rate": round(self.violation_rate, 3),
            "distance": round(self.distance, 3),
            "delta": round(self.delta, 3),
        }


@dataclass
class ConstraintViolation:
    """Record of a hard constraint violation."""
    turn_number: int
    constraint: str
    violation_type: str
    original_text: str
    retry_count: int = 0
    final_text: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "turn_number": self.turn_number,
            "constraint": self.constraint,
            "violation_type": self.violation_type,
            "original_text": self.original_text,
            "retry_count": self.retry_count,
            "final_text": self.final_text,
        }


@dataclass
class ControllerLog:
    """Complete log of all controller interventions in a session."""
    session_key: str
    deviation_reports: list = field(default_factory=list)
    constraint_violations: list = field(default_factory=list)
    total_nudges: int = 0
    total_regenerations: int = 0
    total_candidate_turns: int = 0
    total_hard_violations: int = 0
    drift_reports: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "session_key": self.session_key,
            "deviation_reports": [d.to_dict() for d in self.deviation_reports],
            "constraint_violations": [v.to_dict() for v in self.constraint_violations],
            "total_nudges": self.total_nudges,
            "total_regenerations": self.total_regenerations,
            "total_candidate_turns": self.total_candidate_turns,
            "total_hard_violations": self.total_hard_violations,
            "drift_reports": [d.to_dict() for d in self.drift_reports],
            "nudge_rate": round(
                self.total_nudges / max(self.total_candidate_turns, 1), 3
            ),
            "regeneration_rate": round(
                self.total_regenerations / max(self.total_candidate_turns, 1), 3
            ),
            "hard_violation_rate": round(
                self.total_hard_violations / max(self.total_candidate_turns, 1), 3
            ),
        }


# Expected candidate turns in a full session (for scaling window targets)
EXPECTED_TOTAL_TURNS = 17


# =============================================================================
# FIDELITY CONTROLLER
# =============================================================================

class FidelityController:
    """
    Runtime controller that monitors and corrects personality drift.

    Usage:
        controller = FidelityController(contract, session_key)

        # Every 2 candidate turns:
        nudge = controller.check_and_nudge(turns, candidate_turn_count)
        if nudge:
            candidate.update_nudge(nudge)

        # Every candidate turn (before submission):
        violations = controller.check_hard_constraints(response_text, turns)
        # Violations are penalized in BoN scoring (no regeneration).
    """

    def __init__(self, contract: BehaviorContract, session_key: str):
        self.contract = contract
        self.log = ControllerLog(session_key=session_key)
        self._current_nudge: Optional[str] = None
        self.config = DEFAULT_CONFIG

    def check_and_nudge(
        self,
        turns: list["Turn"],
        candidate_turn_count: int,
        candidate_name: str = "Candidate",
    ) -> Optional[str]:
        """
        Check behavioral features against contract and generate nudge if needed.

        Called every 2 candidate turns. Returns nudge text to inject into
        system prompt, or None if behavior is within acceptable range.

        Also includes soft constraint reminders (demoted from hard constraints
        due to inter-trait conflicts).
        """
        self.log.total_candidate_turns = candidate_turn_count

        # Only check every N turns, starting from turn N
        if candidate_turn_count < self.config.nudge_check_every or \
           candidate_turn_count % self.config.nudge_check_every != 0:
            return self._current_nudge

        # Extract features from recent window
        features = extract_incremental_features(
            turns, candidate_name, window_size=self.config.drift_window_size
        )

        # Compare against contract targets
        deviations = self._compute_deviations(features, candidate_turn_count)

        # Compute drift
        violation_rate, distance, delta = self._compute_drift(features)

        # Record drift even if no nudge
        drift_report = DeviationReport(
            turn_number=candidate_turn_count,
            deviations=deviations,
            nudge_text="",
            violation_rate=violation_rate,
            distance=distance,
            delta=delta,
        )
        self.log.drift_reports.append(drift_report)

        if delta < self.config.drift_threshold:
            self._current_nudge = None
            return None

        # Include soft constraints as nudge guidance (not hard-enforced)
        soft_parts = []
        if self.contract.soft_constraints:
            soft_parts = [f"Aim to: {c}" for c in self.contract.soft_constraints]

        if not deviations and not soft_parts:
            self._current_nudge = None
            return None

        # Generate nudge from deviations + soft constraints
        nudge = self._generate_nudge(deviations, soft_parts)

        drift_report.nudge_text = nudge
        self.log.deviation_reports.append(drift_report)
        self.log.total_nudges += 1

        self._current_nudge = nudge
        return nudge

    def _compute_deviations(
        self, features, turn_number: int, window_size: Optional[int] = None
    ) -> list[dict]:
        """Compare extracted features against contract targets."""
        deviations = []
        features_dict = features.to_dict()

        # Scale factor for count features (window vs full session)
        window_size = window_size or self.config.drift_window_size
        scale = window_size / EXPECTED_TOTAL_TURNS

        for feature_name, spec in self.contract.target_features.items():
            actual = features_dict.get(feature_name)
            if actual is None:
                continue

            target_min = spec["min"]
            target_max = spec["max"]

            # Scale count-based targets for the window size
            if feature_name.endswith("_count"):
                target_min *= scale
                target_max *= scale

            if target_max <= target_min:
                continue

            reliability = spec.get("reliability", 0.5)

            if actual < target_min:
                deviations.append({
                    "feature": feature_name,
                    "actual": round(actual, 2) if isinstance(actual, float) else actual,
                    "target_min": round(target_min, 2),
                    "target_max": round(target_max, 2),
                    "trait": spec["trait"],
                    "direction": "below",
                    "reliability": reliability,
                })
            elif actual > target_max:
                deviations.append({
                    "feature": feature_name,
                    "actual": round(actual, 2) if isinstance(actual, float) else actual,
                    "target_min": round(target_min, 2),
                    "target_max": round(target_max, 2),
                    "trait": spec["trait"],
                    "direction": "above",
                    "reliability": reliability,
                })

        return deviations

    def _compute_drift(self, features) -> tuple[float, float, float]:
        """Compute violation rate, weighted distance, and composite drift."""
        features_dict = features.to_dict()

        violations = 0
        total = 0
        weighted_dist = 0.0
        weight_sum = 0.0

        window_size = self.config.drift_window_size
        scale = window_size / EXPECTED_TOTAL_TURNS

        for feature_name, spec in self.contract.target_features.items():
            actual = features_dict.get(feature_name)
            if actual is None:
                continue

            target_min = spec["min"]
            target_max = spec["max"]
            if feature_name.endswith("_count"):
                target_min *= scale
                target_max *= scale

            denom = target_max - target_min
            if denom <= 0:
                continue
            total += 1
            if actual < target_min or actual > target_max:
                violations += 1

            # Normalized distance
            if actual < target_min:
                dist = (target_min - actual) / denom
            elif actual > target_max:
                dist = (actual - target_max) / denom
            else:
                dist = 0.0

            dist = min(dist, self.config.distance_clip)

            rel = spec.get("reliability", 0.5)
            weighted_dist += rel * dist
            weight_sum += rel

        violation_rate = violations / max(total, 1)
        distance = weighted_dist / max(weight_sum, 1e-6)
        delta = self.config.drift_alpha * violation_rate + (1 - self.config.drift_alpha) * distance
        return round(violation_rate, 4), round(distance, 4), round(delta, 4)

    def _generate_nudge(self, deviations: list[dict], soft_parts: list[str] = None) -> str:
        """Generate a corrective nudge from deviations and soft constraints."""
        # Group deviations by trait
        trait_devs: dict[str, list[dict]] = {}
        for d in deviations:
            trait_devs.setdefault(d["trait"], []).append(d)

        nudge_parts = ["[FIDELITY NOTE:"]

        for trait, devs in trait_devs.items():
            corrections = []
            for d in devs:
                feature = d["feature"].replace("_", " ")
                if d["direction"] == "below":
                    corrections.append(f"your {feature} is below target")
                else:
                    corrections.append(f"your {feature} is above target")

            action = self._get_trait_action(trait, devs)
            if action:
                corrections.append(action)

            nudge_parts.append(f"{trait}: {'; '.join(corrections)}.")

        # Append soft constraint reminders
        if soft_parts:
            for sp in soft_parts:
                nudge_parts.append(sp)

        nudge_parts.append("]")
        return " ".join(nudge_parts)

    def _get_trait_action(self, trait: str, deviations: list[dict]) -> str:
        """Get a specific action suggestion for a trait's deviations."""
        below_count = sum(1 for d in deviations if d["direction"] == "below")
        above_count = sum(1 for d in deviations if d["direction"] == "above")

        actions = {
            "C": {
                "increase": "Include a concrete action item with an owner or reference a prior commitment.",
                "decrease": "Be more spontaneous and avoid over-organizing.",
            },
            "O": {
                "increase": "Propose an alternative approach or ask a speculative question.",
                "decrease": "Focus on practical, proven solutions.",
            },
            "E": {
                "increase": "Address someone by name and elaborate more.",
                "decrease": "Keep it brief and let others lead.",
            },
            "A": {
                "increase": "Validate someone's contribution or find common ground.",
                "decrease": "Identify a flaw in the current proposal and push back.",
            },
            "N": {
                "increase": "Express a concern or qualify your statement with uncertainty.",
                "decrease": "Project calm confidence without hedging.",
            },
        }

        if trait in actions:
            direction = "increase" if below_count >= above_count else "decrease"
            return actions[trait][direction]
        return ""

    # =========================================================================
    # BEST-OF-N SCORING
    # =========================================================================

    _STOPWORDS = {
        "the", "a", "an", "and", "or", "but", "if", "then", "than", "to", "of",
        "in", "on", "for", "with", "at", "by", "from", "that", "this", "it",
        "we", "i", "you", "he", "she", "they", "them", "our", "your", "their",
        "is", "are", "was", "were", "be", "been", "being", "as", "so", "just",
        "not", "no", "yes", "do", "does", "did", "can", "could", "should",
    }

    _VIOLATION_FEATURE_MAP = {
        "no_organizational_element": "structure_marker_count",
        "imposed_unsolicited_structure": "structure_marker_count",
        "agreed_without_concern": "disagreement_count",
        "criticized_without_acknowledgment": "acknowledgment_count",
        "accepted_without_alternative": "idea_count",
        "expressed_self_doubt": "self_doubt_count",
        "no_hedge_under_pressure": "hedge_count",
        "response_too_long": "avg_words_per_turn",
        "no_name_mention": "name_mention_count",
    }

    def score_candidates(
        self,
        turns: list["Turn"],
        candidates: list[str],
        candidate_name: str = "Candidate",
    ) -> list[dict]:
        """Score a candidate pool for Best-of-N selection."""
        scored = []
        for text in candidates:
            violations = self.check_hard_constraints(text, turns, candidate_name)
            features = self._features_for_candidate(turns, text, candidate_name)
            contract_distance = self._compute_weighted_distance(features)

            relevance_penalty = self._relevance_penalty(text, turns)
            redundancy_penalty = self._redundancy_penalty(text, turns, candidate_name)

            adequacy_penalty, adequacy_flags = self._adequacy_penalty(
                text, turns, violations, candidate_name
            )

            weights = self.config.bon_weights
            total_penalty = (
                weights["contract"] * contract_distance
                + weights["relevance"] * relevance_penalty
                + weights["adequacy"] * adequacy_penalty
                + weights["redundancy"] * redundancy_penalty
            )
            total_score = round(1.0 - total_penalty, 4)

            scored.append({
                "text": text,
                "score": total_score,
                "contract_distance": round(contract_distance, 4),
                "relevance_penalty": round(relevance_penalty, 4),
                "adequacy_penalty": round(adequacy_penalty, 4),
                "redundancy_penalty": round(redundancy_penalty, 4),
                "adequacy_flags": adequacy_flags,
                "violations": [v.to_dict() for v in violations],
                "violation_types": [v.violation_type for v in violations],
            })

        return scored

    def score_candidates_phase(
        self,
        turns: list["Turn"],
        candidates: list[str],
        phase_name: str,
        candidate_name: str = "Candidate",
    ) -> list[dict]:
        """Score candidate pool with phase-conditioned trait weights (BCFC v3)."""
        trait_weights = self.config.v3_phase_trait_weights.get(phase_name, {})
        scored = []
        for text in candidates:
            violations = self.check_hard_constraints(text, turns, candidate_name)
            features = self._features_for_candidate(turns, text, candidate_name)

            full_distance = self._compute_weighted_distance(features)
            phase_distance = self._compute_weighted_distance(features, trait_weights=trait_weights)
            global_w = self.config.v3_global_contract_weight
            contract_distance = (global_w * full_distance) + ((1 - global_w) * phase_distance)

            relevance_penalty = self._relevance_penalty(text, turns)
            redundancy_penalty = self._redundancy_penalty(text, turns, candidate_name)
            adequacy_penalty, adequacy_flags = self._adequacy_penalty(
                text, turns, violations, candidate_name
            )

            weights = self.config.bon_weights
            total_penalty = (
                weights["contract"] * contract_distance
                + weights["relevance"] * relevance_penalty
                + weights["adequacy"] * adequacy_penalty
                + weights["redundancy"] * redundancy_penalty
            )
            total_score = round(1.0 - total_penalty, 4)

            scored.append({
                "text": text,
                "score": total_score,
                "contract_distance": round(contract_distance, 4),
                "full_contract_distance": round(full_distance, 4),
                "phase_contract_distance": round(phase_distance, 4),
                "phase_name": phase_name,
                "phase_trait_weights": trait_weights,
                "relevance_penalty": round(relevance_penalty, 4),
                "adequacy_penalty": round(adequacy_penalty, 4),
                "redundancy_penalty": round(redundancy_penalty, 4),
                "adequacy_flags": adequacy_flags,
                "violations": [v.to_dict() for v in violations],
                "violation_types": [v.violation_type for v in violations],
            })
        return scored

    def _features_for_candidate(
        self,
        turns: list["Turn"],
        candidate_text: str,
        candidate_name: str,
    ):
        """Compute incremental features including a candidate response."""
        from utils.models import Turn, SpeakerRole
        turn_number = len([t for t in turns if t.speaker_name == candidate_name]) + 1
        temp_turn = Turn(
            turn_number=turn_number,
            speaker_role=SpeakerRole.CANDIDATE,
            speaker_name=candidate_name,
            content=candidate_text,
        )
        temp_turns = turns + [temp_turn]
        return extract_incremental_features(
            temp_turns, candidate_name, window_size=self.config.drift_window_size
        )

    def _compute_weighted_distance(self, features, trait_weights: Optional[dict] = None) -> float:
        """Compute weighted normalized distance from contract ranges."""
        features_dict = features.to_dict()
        window_size = self.config.drift_window_size
        scale = window_size / EXPECTED_TOTAL_TURNS

        total = 0.0
        weight_sum = 0.0
        trait_weights = trait_weights or {}

        for feature_name, spec in self.contract.target_features.items():
            actual = features_dict.get(feature_name)
            if actual is None:
                continue

            target_min = spec["min"]
            target_max = spec["max"]
            if feature_name.endswith("_count"):
                target_min *= scale
                target_max *= scale

            denom = target_max - target_min
            if denom <= 0:
                continue
            if actual < target_min:
                dist = (target_min - actual) / denom
            elif actual > target_max:
                dist = (actual - target_max) / denom
            else:
                dist = 0.0

            dist = min(dist, self.config.distance_clip)

            rel = spec.get("reliability", 0.5)
            trait = spec.get("trait")
            trait_w = trait_weights.get(trait, 1.0)
            total += rel * trait_w * dist
            weight_sum += rel * trait_w

        return total / max(weight_sum, 1e-6)

    def _relevance_penalty(self, text: str, turns: list["Turn"]) -> float:
        """Penalize if response is weakly related to the last non-candidate turn."""
        last_other = None
        for t in reversed(turns):
            if t.speaker_name != "Candidate":
                last_other = t
                break
        if not last_other:
            return 0.0

        def tokenize(s: str) -> set[str]:
            tokens = [w.strip(".,!?;:()[]").lower() for w in s.split()]
            return {t for t in tokens if t and t not in self._STOPWORDS}

        a = tokenize(text)
        b = tokenize(last_other.content)
        if not b:
            return 0.0
        overlap = len(a & b) / max(len(b), 1)
        if overlap >= 0.08:
            return 0.0
        return round(0.25 - overlap, 4)

    def _redundancy_penalty(self, text: str, turns: list["Turn"], candidate_name: str) -> float:
        """Penalize if response repeats candidate's prior turn heavily."""
        last_candidate = None
        for t in reversed(turns):
            if t.speaker_name == candidate_name:
                last_candidate = t
                break
        if not last_candidate:
            return 0.0

        def tokenize(s: str) -> set[str]:
            tokens = [w.strip(".,!?;:()[]").lower() for w in s.split()]
            return {t for t in tokens if t and t not in self._STOPWORDS}

        a = tokenize(text)
        b = tokenize(last_candidate.content)
        if not a or not b:
            return 0.0
        overlap = len(a & b) / max(len(a), 1)
        if overlap < 0.4:
            return 0.0
        return min(1.0, (overlap - 0.4) * 1.5)

    def _adequacy_penalty(
        self,
        text: str,
        turns: list["Turn"],
        violations: list[ConstraintViolation],
        candidate_name: str,
    ) -> tuple[float, list[str]]:
        """Compute adequacy penalty and diagnostic flags."""
        penalty = 0.0
        flags: list[str] = []

        # Empty or too short
        if len(text.split()) < 6:
            penalty += 0.4
            flags.append("too_short")

        # Direct question not answered
        last_other = None
        for t in reversed(turns):
            if t.speaker_name != candidate_name:
                last_other = t
                break
        if last_other and "?" in last_other.content:
            if len(text.split()) < 8:
                penalty += 0.3
                flags.append("question_not_answered")

        # Unsolicited structure (heuristic)
        if any(re.search(p, text.lower()) for p in STRUCTURE_MARKER_PATTERNS):
            asked = False
            for t in (turns[-2:] if len(turns) >= 2 else turns):
                if any(w in t.content.lower() for w in ["list", "outline", "organize", "structure", "steps"]):
                    asked = True
                    break
            if not asked:
                penalty += 0.2
                flags.append("unsolicited_structure")

        # Over-verbosity
        if len(text.split()) > 90:
            penalty += 0.2
            flags.append("too_long")

        # Constraint violations (weighted)
        for v in violations:
            base = CONSTRAINT_PENALTIES.get(v.violation_type, 0.1)
            feature = self._VIOLATION_FEATURE_MAP.get(v.violation_type)
            reliability = 0.5
            if feature and feature in self.contract.target_features:
                reliability = self.contract.target_features[feature].get("reliability", 0.5)
            penalty += base * reliability
            flags.append(f"constraint:{v.violation_type}")

        return min(1.0, penalty), flags

    # =========================================================================
    # HARD CONSTRAINT CHECKING (Generate-Check-Regenerate)
    # =========================================================================

    def check_hard_constraints(
        self,
        response_text: str,
        turns: list["Turn"],
        candidate_name: str = "Candidate",
    ) -> list[ConstraintViolation]:
        """
        Check a candidate response against hard constraints before submission.

        Returns list of violations. Empty list = response passes all checks.
        """
        violations = []
        text_lower = response_text.lower()
        turn_number = sum(
            1 for t in turns if t.speaker_name == candidate_name
        ) + 1

        for constraint in self.contract.hard_constraints:
            violation = self._check_single_constraint(
                constraint, response_text, text_lower, turns, turn_number
            )
            if violation:
                # Only strong/reliable features remain hard-gated
                if self._is_hard_violation(violation):
                    violations.append(violation)

        return violations

    def _check_single_constraint(
        self,
        constraint: str,
        response_text: str,
        text_lower: str,
        turns: list["Turn"],
        turn_number: int,
    ) -> Optional[ConstraintViolation]:
        """Check a single hard constraint. Returns violation or None."""

        # Low A: "Never agree without first identifying a weakness"
        if "agree" in constraint and "weakness" in constraint:
            has_agreement = any(
                p in text_lower
                for p in [
                    "i agree", "good point", "you're right", "that's right",
                    "exactly", "makes sense", "great idea",
                ]
            )
            has_criticism = any(
                p in text_lower
                for p in [
                    "but", "however", "although", "concern", "problem",
                    "issue", "risk", "weakness", "flaw", "careful",
                    "i disagree", "not sure", "question whether",
                ]
            )
            if has_agreement and not has_criticism:
                return ConstraintViolation(
                    turn_number=turn_number,
                    constraint=constraint,
                    violation_type="agreed_without_concern",
                    original_text=response_text,
                )

        # High A: "Never criticize without acknowledging value"
        if "criticize" in constraint and "acknowledging" in constraint:
            has_criticism = any(p in text_lower for p in DISAGREEMENT_PHRASES[:8])
            has_ack = any(p in text_lower for p in ACKNOWLEDGMENT_PHRASES[:8])
            if has_criticism and not has_ack:
                return ConstraintViolation(
                    turn_number=turn_number,
                    constraint=constraint,
                    violation_type="criticized_without_acknowledgment",
                    original_text=response_text,
                )

        # High C: "Include organizational element in long responses"
        if "organizational element" in constraint:
            words = response_text.split()
            if len(words) > 25:
                has_org = any(
                    p in text_lower for p in PLANNING_PHRASES + ACTION_ITEM_PHRASES
                ) or any(
                    re.search(p, text_lower) for p in STRUCTURE_MARKER_PATTERNS
                )
                if not has_org:
                    return ConstraintViolation(
                        turn_number=turn_number,
                        constraint=constraint,
                        violation_type="no_organizational_element",
                        original_text=response_text,
                    )

        # Low C: "Do not impose structure unless asked"
        if "numbered lists" in constraint and "unless" in constraint:
            has_structure = any(
                re.search(p, text_lower) for p in STRUCTURE_MARKER_PATTERNS
            ) or any(p in text_lower for p in ACTION_ITEM_PHRASES)
            asked = False
            for t in (turns[-2:] if len(turns) >= 2 else turns):
                if any(w in t.content.lower() for w in [
                    "list", "outline", "organize", "structure", "steps"
                ]):
                    asked = True
                    break
            if has_structure and not asked:
                return ConstraintViolation(
                    turn_number=turn_number,
                    constraint=constraint,
                    violation_type="imposed_unsolicited_structure",
                    original_text=response_text,
                )

        # High O: "Offer alternative before accepting"
        if "alternative" in constraint and "standard solution" in constraint:
            if turns and turns[-1].speaker_name != "Candidate":
                has_accept = any(
                    p in text_lower
                    for p in ["sounds good", "let's go with", "i agree", "that works"]
                )
                has_alt = any(
                    p in text_lower
                    for p in IDEA_PHRASES + HYPOTHETICAL_PHRASES + [
                        "or we could", "alternatively", "another way"
                    ]
                )
                if has_accept and not has_alt:
                    return ConstraintViolation(
                        turn_number=turn_number,
                        constraint=constraint,
                        violation_type="accepted_without_alternative",
                        original_text=response_text,
                    )

        # Low N: "Never express self-doubt or seek reassurance"
        if "self-doubt" in constraint and "reassurance" in constraint:
            has_doubt = any(
                p in text_lower
                for p in SELF_DOUBT_PHRASES + REASSURANCE_SEEKING_PHRASES
            )
            if has_doubt:
                return ConstraintViolation(
                    turn_number=turn_number,
                    constraint=constraint,
                    violation_type="expressed_self_doubt",
                    original_text=response_text,
                )

        # High N: "Include qualifier under pressure"
        if "qualifier" in constraint and "hedge" in constraint:
            has_hedge = any(
                p in text_lower
                for p in HEDGE_PHRASES + ["but", "although", "however"]
            )
            if not has_hedge:
                recent = turns[-3:] if len(turns) >= 3 else turns
                has_pressure = any(
                    any(p in t.content.lower() for p in DISAGREEMENT_PHRASES[:5])
                    for t in recent
                    if t.speaker_name != "Candidate"
                )
                if has_pressure:
                    return ConstraintViolation(
                        turn_number=turn_number,
                        constraint=constraint,
                        violation_type="no_hedge_under_pressure",
                        original_text=response_text,
                    )

        # Low E: "Keep under 50 words"
        if "under 50 words" in constraint:
            word_count = len(response_text.split())
            asked_elaborate = False
            if turns and turns[-1].speaker_name != "Candidate":
                asked_elaborate = any(
                    w in turns[-1].content.lower()
                    for w in ["elaborate", "tell us more", "explain", "go on"]
                )
            if word_count > 50 and not asked_elaborate:
                return ConstraintViolation(
                    turn_number=turn_number,
                    constraint=constraint,
                    violation_type="response_too_long",
                    original_text=response_text,
                )

        # High E: "Address someone by name"
        if "by name" in constraint:
            agent_names = ["alex", "jordan", "riley"]
            if not any(name in text_lower for name in agent_names):
                return ConstraintViolation(
                    turn_number=turn_number,
                    constraint=constraint,
                    violation_type="no_name_mention",
                    original_text=response_text,
                )

        return None

    def _is_hard_violation(self, violation: ConstraintViolation) -> bool:
        """Return True if violation maps to a strong/reliable feature."""
        feature = self._VIOLATION_FEATURE_MAP.get(violation.violation_type)
        if not feature:
            return True
        reliability = self.contract.target_features.get(feature, {}).get("reliability", 0.5)
        return reliability >= 0.3

    def record_violation(self, violation: ConstraintViolation):
        """Record a violation to the controller log."""
        self.log.constraint_violations.append(violation)
        self.log.total_hard_violations += 1

    def get_current_nudge(self) -> Optional[str]:
        """Get the current active nudge text (if any)."""
        return self._current_nudge
