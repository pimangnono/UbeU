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
from typing import Optional, TYPE_CHECKING, Any

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
from experiment.memory_backend import (
    score_commitment_continuity,
    score_relationship_consistency,
    detect_commitment_contradiction,
)

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
    selection_audit: list = field(default_factory=list)

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
            "selection_audit": self.selection_audit,
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
        # Per-phase policy-act tracking for v5 facet-level execution control.
        self._phase_policy_state: dict[str, dict[str, set[str]]] = {}

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
    _VIOLATION_TRAIT_MAP = {
        "no_organizational_element": "C",
        "imposed_unsolicited_structure": "C",
        "accepted_without_alternative": "O",
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

    def score_candidates_policy(
        self,
        turns: list["Turn"],
        candidates: list[str],
        policy_plan: dict,
        phase_context: dict,
        memory_context: dict,
        candidate_name: str = "Candidate",
        scoring_version: str = "v4",
    ) -> list[dict]:
        """Score candidate pool with policy + phase-conditioned scoring (BCFC v4)."""
        scored: list[dict] = []
        target_traits = phase_context.get("target_traits") or []
        phase_style = phase_context.get("phase_style") or ""
        use_v5 = scoring_version.lower() == "v5"
        weights = self.config.v5_score_weights if use_v5 else self.config.v4_score_weights
        opportunities = self._trait_opportunity_scores(turns, phase_context) if use_v5 else {}
        activation_mask = (
            self._build_activation_mask(
                opportunities=opportunities,
                target_traits=target_traits,
                apply_floor=True,
            )
            if use_v5
            else {}
        )
        phase_name = str(phase_context.get("phase_name") or "UNKNOWN")
        required_policy_acts = (
            self._derive_required_policy_acts(policy_plan, phase_context, opportunities)
            if use_v5
            else set()
        )
        phase_state = self._phase_policy_state.setdefault(
            phase_name,
            {"required_acts": set(), "completed_acts": set()},
        )
        if use_v5:
            phase_state["required_acts"].update(required_policy_acts)

        for text in candidates:
            violations = self.check_hard_constraints(
                text,
                turns,
                candidate_name,
                phase_context=phase_context if use_v5 else None,
                scoring_version=scoring_version,
            )
            features = self._features_for_candidate(turns, text, candidate_name)

            # Hard-fail on commitment contradictions if detected
            commitments = memory_context.get("commitments") or []
            if detect_commitment_contradiction(text, commitments):
                scored.append({
                    "text": text,
                    "score": 0.0,
                    "hard_fail_reason": "commitment_contradiction",
                    "policy_match": 0.0,
                    "situational_adequacy": 0.0,
                    "commitment_continuity": 0.0,
                    "trait_evidence": 0.0,
                    "relationship_consistency": 0.0,
                    "trait_execution": 0.0 if use_v5 else None,
                    "redundancy_penalty": 1.0,
                    "phase_target_traits": target_traits,
                    "phase_style": phase_style,
                    "scoring_version": scoring_version,
                    "violations": [v.to_dict() for v in violations],
                    "violation_types": [v.violation_type for v in violations],
                })
                continue

            policy_match_base = self._policy_match_score(policy_plan, text)
            if use_v5:
                policy_match = self._policy_match_score_v5(
                    policy_plan,
                    text,
                    phase_context=phase_context,
                    turns=turns,
                )
            else:
                policy_match = policy_match_base
            situational_adequacy = self._situational_adequacy_score(text, turns, violations, candidate_name)
            commitment_continuity = score_commitment_continuity(text, commitments)
            trait_evidence = self._trait_evidence_score(features, target_traits)
            relationship_consistency = score_relationship_consistency(
                text, memory_context.get("relationships") or []
            )
            trait_execution = 0.5
            trait_execution_details: dict[str, Any] = {}
            trait_opportunities: dict[str, float] = {}
            policy_act_completion = 0.5
            policy_act_matches: list[str] = []
            policy_act_missing: list[str] = []
            policy_act_required: list[str] = []
            activation_weighted_contract_distance = self._compute_weighted_distance(features)
            if use_v5:
                trait_execution, trait_execution_details, trait_opportunities = self._trait_execution_score(
                    text=text,
                    turns=turns,
                    phase_context=phase_context,
                    opportunities=opportunities,
                )
                (
                    policy_act_completion,
                    policy_act_matches,
                    policy_act_missing,
                    policy_act_required,
                ) = self._policy_act_completion_score(
                    text=text,
                    policy_plan=policy_plan,
                    phase_state=phase_state,
                    opportunities=opportunities,
                    trait_execution_details=trait_execution_details,
                )
                activation_weighted_contract_distance = self._compute_weighted_distance(
                    features,
                    activation_mask=activation_mask,
                )
            redundancy_penalty = self._redundancy_penalty(text, turns, candidate_name)

            total_score = (
                weights["policy_match"] * policy_match
                + weights["situational_adequacy"] * situational_adequacy
                + weights["commitment_continuity"] * commitment_continuity
                + weights["trait_evidence"] * trait_evidence
                + weights["relationship_consistency"] * relationship_consistency
                + weights.get("trait_execution", 0.0) * trait_execution
                - weights["redundancy_penalty"] * redundancy_penalty
            )
            total_score = round(max(0.0, min(1.0, total_score)), 4)

            scored.append({
                "text": text,
                "score": total_score,
                "policy_match": round(policy_match, 4),
                "policy_match_base": round(policy_match_base, 4),
                "situational_adequacy": round(situational_adequacy, 4),
                "commitment_continuity": round(commitment_continuity, 4),
                "trait_evidence": round(trait_evidence, 4),
                "relationship_consistency": round(relationship_consistency, 4),
                "trait_execution": round(trait_execution, 4),
                "trait_execution_details": trait_execution_details if use_v5 else {},
                "trait_opportunities": trait_opportunities if use_v5 else {},
                "activation_mask": activation_mask if use_v5 else {},
                "activation_weighted_contract_distance": round(activation_weighted_contract_distance, 4),
                "policy_act_completion": round(policy_act_completion, 4),
                "policy_act_matches": policy_act_matches,
                "policy_act_missing": policy_act_missing,
                "policy_act_required": policy_act_required,
                "redundancy_penalty": round(redundancy_penalty, 4),
                "phase_target_traits": target_traits,
                "phase_style": phase_style,
                "phase_name": phase_name,
                "scoring_version": scoring_version,
                "violations": [v.to_dict() for v in violations],
                "violation_types": [v.violation_type for v in violations],
            })

        return scored

    def _context_window_text(self, turns: list["Turn"], window: int = 4) -> str:
        """Collect a short lowercase context window from recent turns."""
        recent = turns[-window:] if len(turns) > window else turns
        chunks = []
        for t in recent:
            content = getattr(t, "content", "")
            if content:
                chunks.append(content.lower())
        return " ".join(chunks)

    def _count_keyword_hits(self, text_lower: str, keywords: list[str]) -> int:
        """Count keyword matches with boundary-aware checks for single tokens."""
        hits = 0
        for kw in keywords:
            kw_l = kw.lower().strip()
            if not kw_l:
                continue
            if " " in kw_l:
                if kw_l in text_lower:
                    hits += 1
            else:
                if re.search(rf"\b{re.escape(kw_l)}\b", text_lower):
                    hits += 1
        return hits

    def _trait_opportunity_scores(self, turns: list["Turn"], phase_context: dict) -> dict[str, float]:
        """
        Estimate whether O/C expression opportunities exist in the current turn context.

        This drives opportunity-gated scoring: traits are strongly required only when
        the local context actually provides a chance to express them.
        """
        cues = [str(c).lower() for c in (phase_context.get("phase_cues") or [])]
        target_traits = set(phase_context.get("target_traits") or [])
        context_text = self._context_window_text(turns, window=4)

        scores: dict[str, float] = {}
        for trait in ("O", "C"):
            cue_terms = self.config.v5_opportunity_cue_map.get(trait, [])
            cue_hits = 0
            for cue in cues:
                if any(term in cue for term in cue_terms):
                    cue_hits += 1

            keyword_hits = self._count_keyword_hits(
                context_text, self.config.v5_context_keyword_map.get(trait, [])
            )

            score = 0.0
            if cue_hits > 0:
                score += min(0.60, 0.20 * cue_hits)
            if keyword_hits > 0:
                score += min(0.50, 0.15 * keyword_hits)
            if trait in target_traits:
                score += 0.20

            scores[trait] = round(min(1.0, score), 4)

        return scores

    def _trait_signal_coverage(self, trait: str, text_lower: str) -> tuple[float, dict[str, Any]]:
        """Measure how many trait-specific signal categories are present."""
        signal_map = self.config.v5_trait_signal_keywords.get(trait, {})
        if not signal_map:
            return 0.0, {
                "matched_categories": [],
                "missing_categories": [],
                "category_hits": {},
            }

        category_hits: dict[str, int] = {}
        for category, keywords in signal_map.items():
            category_hits[category] = self._count_keyword_hits(text_lower, keywords)

        # Extra structural checks to reduce lexical brittleness for C signals.
        if trait == "C":
            owner_pattern = r"\b(alex|jordan|riley|i|we)\b.{0,40}\b(will|owner|own|responsible|take)\b"
            deadline_pattern = (
                r"\b(deadline|due|by\s+(today|tomorrow|monday|tuesday|wednesday|thursday|friday|"
                r"eod|end of day|\d{1,2}(?:am|pm)?))\b"
            )
            contingency_pattern = r"\b(follow up|check in|contingency|fallback|backup plan|in case|if\b.*\bthen)\b"

            if re.search(owner_pattern, text_lower):
                category_hits["owner_assignment"] = max(1, category_hits.get("owner_assignment", 0))
            if re.search(deadline_pattern, text_lower):
                category_hits["deadline_commitment"] = max(1, category_hits.get("deadline_commitment", 0))
            if re.search(contingency_pattern, text_lower):
                category_hits["follow_up_or_contingency"] = max(
                    1, category_hits.get("follow_up_or_contingency", 0)
                )

        matched = [c for c, h in category_hits.items() if h > 0]
        missing = [c for c, h in category_hits.items() if h <= 0]
        coverage = len(matched) / max(len(category_hits), 1)

        return coverage, {
            "matched_categories": matched,
            "missing_categories": missing,
            "category_hits": category_hits,
        }

    def _trait_execution_score(
        self,
        text: str,
        turns: list["Turn"],
        phase_context: dict,
        opportunities: Optional[dict[str, float]] = None,
    ) -> tuple[float, dict[str, Any], dict[str, float]]:
        """
        Opportunity-gated O/C execution score.

        When opportunity is low, score stays neutral-ish to avoid forcing unnatural
        trait expression. When opportunity is high, missing core O/C signals is
        penalized.
        """
        text_lower = text.lower()
        gate = self.config.v5_opportunity_gate_threshold
        target_traits = set(phase_context.get("target_traits") or [])
        opportunities = opportunities or self._trait_opportunity_scores(turns, phase_context)

        details: dict[str, Any] = {}
        weighted_sum = 0.0
        weight_sum = 0.0

        for trait in ("O", "C"):
            coverage, signal_info = self._trait_signal_coverage(trait, text_lower)
            hit_count = len(signal_info["matched_categories"])
            required = self.config.v5_required_signal_counts.get(trait, 1)
            opportunity = opportunities.get(trait, 0.0)
            active = opportunity >= gate

            if active:
                met_requirement = hit_count >= required
                base = 0.65 if met_requirement else 0.25
                trait_score = min(1.0, base + 0.35 * coverage)
            else:
                # Neutral by default when no opportunity, but still reward clean execution.
                met_requirement = hit_count >= required if hit_count > 0 else False
                trait_score = min(0.85, 0.50 + 0.30 * coverage)

            if trait in target_traits:
                trait_score = min(1.0, trait_score + 0.05)

            trait_weight = 1.0 + opportunity + (0.25 if trait in target_traits else 0.0)
            weighted_sum += trait_score * trait_weight
            weight_sum += trait_weight

            details[trait] = {
                "opportunity_score": round(opportunity, 4),
                "opportunity_active": active,
                "required_signal_categories": required,
                "observed_signal_categories": hit_count,
                "met_requirement": met_requirement,
                "coverage": round(coverage, 4),
                "score": round(trait_score, 4),
                **signal_info,
            }

        final = weighted_sum / max(weight_sum, 1e-6)
        return round(final, 4), details, opportunities

    def _build_activation_mask(
        self,
        opportunities: dict[str, float],
        target_traits: list[str],
        apply_floor: bool = True,
    ) -> dict[str, float]:
        """
        Build trait activation mask a_t(trait) in [0,1].

        O/C are situation-aware; other traits default to fully active.
        """
        floor = self.config.v5_activation_floor if apply_floor else 0.0
        targets = set(target_traits or [])
        mask = {"O": 1.0, "C": 1.0, "E": 1.0, "A": 1.0, "N": 1.0}
        for trait in ("O", "C"):
            raw = float(opportunities.get(trait, 0.0))
            if trait in targets:
                raw = min(1.0, raw + 0.05)
            mask[trait] = round(max(floor, raw), 4)
        return mask

    def _derive_required_policy_acts(
        self,
        policy_plan: dict,
        phase_context: dict,
        opportunities: dict[str, float],
    ) -> set[str]:
        """Derive facet-level policy acts expected in this phase."""
        required: set[str] = set()
        gate = self.config.v5_opportunity_gate_threshold
        targets = set(phase_context.get("target_traits") or [])

        planning_depth = str((policy_plan or {}).get("planning_depth") or "").lower()
        novelty_move = str((policy_plan or {}).get("novelty_move") or "").lower()
        goal_mode = str((policy_plan or {}).get("goal_mode") or "").lower()

        if planning_depth == "milestone":
            required.add("c_sequence")
        elif planning_depth == "owner_deadline":
            required.add("c_owner_deadline")
        elif planning_depth == "contingency":
            required.add("c_contingency")

        if novelty_move in {"new_option", "third_option"}:
            required.add("o_alternative")
        elif novelty_move in {"analogy", "reframe"}:
            required.add("o_reframe")

        if goal_mode == "coordinate":
            required.add("c_owner_deadline")
        elif goal_mode == "discover":
            required.add("o_alternative")

        if "O" in targets and opportunities.get("O", 0.0) >= gate:
            required.add("o_alternative")
        if "C" in targets and opportunities.get("C", 0.0) >= gate:
            required.add("c_owner_deadline")
        if opportunities.get("O", 0.0) >= 0.75:
            required.add("o_tradeoff")

        return required

    def _policy_act_completion_score(
        self,
        text: str,
        policy_plan: dict,
        phase_state: dict[str, set[str]],
        opportunities: dict[str, float],
        trait_execution_details: dict[str, Any],
    ) -> tuple[float, list[str], list[str], list[str]]:
        """
        Score completion of currently missing phase policy acts.

        Returns:
            completion_score, matched_acts, missing_acts, required_acts
        """
        required_now = self._derive_required_policy_acts(policy_plan, {"target_traits": []}, opportunities)
        phase_state["required_acts"].update(required_now)
        required = set(phase_state["required_acts"])
        completed = set(phase_state["completed_acts"])
        missing = required - completed

        o_hits = (
            trait_execution_details.get("O", {}).get("category_hits", {})
            if trait_execution_details
            else {}
        )
        c_hits = (
            trait_execution_details.get("C", {}).get("category_hits", {})
            if trait_execution_details
            else {}
        )
        text_lower = text.lower()
        act_hits = {
            "o_alternative": (o_hits.get("alternative_generation", 0) > 0),
            "o_reframe": (o_hits.get("reframing_or_analogy", 0) > 0),
            "o_tradeoff": (o_hits.get("tradeoff_exploration", 0) > 0),
            "c_owner_deadline": (
                c_hits.get("owner_assignment", 0) > 0
                or c_hits.get("deadline_commitment", 0) > 0
            ),
            "c_sequence": (c_hits.get("sequence_structure", 0) > 0),
            "c_contingency": (c_hits.get("follow_up_or_contingency", 0) > 0),
        }

        if "owner" in text_lower and re.search(r"\b(by|due|deadline|eod)\b", text_lower):
            act_hits["c_owner_deadline"] = True

        matched = sorted([a for a in missing if act_hits.get(a, False)])
        missing_sorted = sorted(missing)
        required_sorted = sorted(required)

        if not missing_sorted:
            return 1.0, matched, missing_sorted, required_sorted
        score = len(matched) / len(missing_sorted)
        return round(score, 4), matched, missing_sorted, required_sorted

    def _policy_match_score_v5(
        self,
        policy_plan: dict,
        text: str,
        phase_context: dict,
        turns: list["Turn"],
    ) -> float:
        """
        v5 policy-match bridge:
        - keeps existing latent-plan keyword match
        - adds O/C execution alignment for planning/novelty policy dimensions
        """
        base = self._policy_match_score(policy_plan, text)
        if not policy_plan:
            return base

        text_lower = text.lower()
        bridge_parts: list[float] = []

        planning_depth = (policy_plan.get("planning_depth") or "").lower()
        if planning_depth in {"milestone", "owner_deadline", "contingency"}:
            c_cov, _ = self._trait_signal_coverage("C", text_lower)
            bridge_parts.append(c_cov)

        novelty_move = (policy_plan.get("novelty_move") or "").lower()
        if novelty_move in {"analogy", "reframe", "new_option", "third_option"}:
            o_cov, _ = self._trait_signal_coverage("O", text_lower)
            bridge_parts.append(o_cov)

        goal_mode = (policy_plan.get("goal_mode") or "").lower()
        if goal_mode == "coordinate":
            c_cov, _ = self._trait_signal_coverage("C", text_lower)
            bridge_parts.append(c_cov)
        elif goal_mode == "discover":
            o_cov, _ = self._trait_signal_coverage("O", text_lower)
            bridge_parts.append(o_cov)

        bridge = sum(bridge_parts) / len(bridge_parts) if bridge_parts else 0.5
        opportunities = self._trait_opportunity_scores(turns, phase_context)
        active_ratio = sum(
            1 for t in ("O", "C")
            if opportunities.get(t, 0.0) >= self.config.v5_opportunity_gate_threshold
        ) / 2.0

        # Lean more on execution bridge when O/C opportunity is high.
        base_weight = 0.70 if active_ratio > 0 else 0.82
        score = (base_weight * base) + ((1.0 - base_weight) * bridge)
        return round(max(0.0, min(1.0, score)), 4)

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

    def _trait_evidence_score(self, features: dict, target_traits: list[str]) -> float:
        """Compute trait evidence score based on target traits in phase."""
        if not target_traits:
            return 0.5
        trait_weights = {t: 1.0 for t in target_traits if t in ["O", "C", "E", "A", "N"]}
        if not trait_weights:
            return 0.5
        distance = self._compute_weighted_distance(features, trait_weights=trait_weights)
        clipped = min(1.0, distance / max(self.config.distance_clip, 1e-6))
        return max(0.0, 1.0 - clipped)

    def _situational_adequacy_score(
        self,
        text: str,
        turns: list["Turn"],
        violations: list[ConstraintViolation],
        candidate_name: str,
    ) -> float:
        relevance_penalty = self._relevance_penalty(text, turns)
        adequacy_penalty, _ = self._adequacy_penalty(text, turns, violations, candidate_name)
        penalty = min(1.0, relevance_penalty + adequacy_penalty)
        return max(0.0, 1.0 - penalty)

    def _policy_match_score(self, policy_plan: dict, text: str) -> float:
        """Heuristic policy match against the latent policy plan."""
        if not policy_plan:
            return 0.5
        lower = text.lower()

        def _match(expected: str, keywords: list[str]) -> float:
            if expected in (None, "", "none"):
                return 0.5
            if any(k in lower for k in keywords):
                return 1.0
            return 0.3

        stance = policy_plan.get("stance", "")
        stance_score = _match(stance, {
            "support": ["agree", "support", "yes", "good point", "aligned"],
            "oppose": ["disagree", "but", "however", "push back", "not"],
            "synthesize": ["both", "combine", "balance", "middle ground", "merge"],
            "probe": ["?", "clarify", "help me understand", "can you explain"],
        }.get(stance, []))

        goal = policy_plan.get("goal_mode", "")
        goal_score = _match(goal, {
            "influence": ["convince", "persuade", "align", "sell"],
            "coordinate": ["assign", "owner", "next steps", "timeline", "schedule"],
            "protect": ["risk", "avoid", "mitigate", "protect"],
            "discover": ["explore", "learn", "test", "experiment"],
        }.get(goal, []))

        planning = policy_plan.get("planning_depth", "")
        planning_score = _match(planning, {
            "milestone": ["milestone", "phase", "step"],
            "owner_deadline": ["owner", "deadline", "by friday", "by end"],
            "contingency": ["if", "backup", "fallback", "contingency"],
        }.get(planning, []))

        novelty = policy_plan.get("novelty_move", "")
        novelty_score = _match(novelty, {
            "analogy": ["like", "similar to", "as if"],
            "reframe": ["reframe", "another way", "different lens"],
            "new_option": ["alternative", "another option", "new approach"],
            "third_option": ["third option", "middle option"],
        }.get(novelty, []))

        social = policy_plan.get("social_tactic", "")
        social_score = _match(social, {
            "empathize": ["i understand", "i hear you", "makes sense"],
            "challenge": ["i disagree", "push back", "challenge"],
            "persuade": ["convince", "persuade", "should"],
            "mediate": ["both sides", "compromise", "bridge"],
            "align": ["align", "agree", "same page"],
        }.get(social, []))

        risk = policy_plan.get("risk_posture", "")
        risk_score = _match(risk, {
            "bold": ["let's do it", "move fast", "go for it"],
            "balanced": ["tradeoff", "balance", "careful"],
            "cautious": ["risk", "concern", "mitigate", "safe"],
        }.get(risk, []))

        memory_focus = policy_plan.get("memory_focus", "")
        memory_score = _match(memory_focus, {
            "commitment": ["as we agreed", "we said", "commit", "promise"],
            "relation": ["alex", "jordan", "riley"],
            "identity": ["i tend to", "i prefer", "my approach"],
        }.get(memory_focus, []))

        scores = [stance_score, goal_score, planning_score, novelty_score, social_score, risk_score, memory_score]
        return round(sum(scores) / len(scores), 4)

    def _compute_weighted_distance(
        self,
        features,
        trait_weights: Optional[dict] = None,
        activation_mask: Optional[dict[str, float]] = None,
    ) -> float:
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
            if activation_mask and trait in activation_mask:
                trait_w *= activation_mask[trait]
            total += rel * trait_w * dist
            weight_sum += rel * trait_w

        return total / max(weight_sum, 1e-6)

    def _compute_activation_weighted_distance(self, features, activation_mask: dict[str, float]) -> float:
        """Compute contract distance scaled by activation mask a_t(trait)."""
        return self._compute_weighted_distance(
            features,
            activation_mask=activation_mask,
        )

    def select_candidate_policy_v5(
        self,
        scored: list[dict],
        phase_context: dict,
        turn_number: int,
    ) -> dict[str, Any]:
        """
        Select candidate with lexicographic two-stage BoN:
        A) adequacy gate, B) min activation-weighted contract distance,
        C) tie-break by relevance/redundancy (+ policy-act completion).
        """
        if not scored:
            audit = {
                "turn_number": turn_number,
                "phase_name": phase_context.get("phase_name"),
                "selection_mode": "two_stage_v5",
                "error": "empty_scored_pool",
            }
            self.log.selection_audit.append(audit)
            return {"selected_index": -1, "selected": None, "audit": audit}

        n = len(scored)
        all_indices = list(range(n))
        tau = self.config.v5_adequacy_threshold
        tie_delta = self.config.v5_tie_delta
        policy_tie_weight = self.config.v5_policy_tie_weight
        phase_name = str(phase_context.get("phase_name") or "UNKNOWN")
        phase_state = self._phase_policy_state.setdefault(
            phase_name,
            {"required_acts": set(), "completed_acts": set()},
        )

        # Stage A: adequacy gate
        adequate = [
            i for i, c in enumerate(scored)
            if (c.get("situational_adequacy", 0.0) >= tau) and not c.get("hard_fail_reason")
        ]
        stage_a_pool = adequate
        fail_open = False
        if not stage_a_pool:
            stage_a_pool = [i for i, c in enumerate(scored) if not c.get("hard_fail_reason")]
            fail_open = True
        if not stage_a_pool:
            stage_a_pool = all_indices
            fail_open = True

        # Stage B: minimize activation-weighted contract distance
        def _dist(idx: int) -> float:
            c = scored[idx]
            return float(c.get("activation_weighted_contract_distance", c.get("contract_distance", 1.0)))

        best_dist = min(_dist(i) for i in stage_a_pool)
        near = [i for i in stage_a_pool if abs(_dist(i) - best_dist) <= tie_delta]

        # Stage C: tie-break
        tie_rows: list[dict[str, Any]] = []
        selected_idx = near[0]
        if len(near) > 1:
            best_tie = None
            for i in near:
                c = scored[i]
                tie_score = (
                    (1.0 - float(c.get("relevance_penalty", 1.0)))
                    - float(c.get("redundancy_penalty", 1.0))
                    + (policy_tie_weight * float(c.get("policy_act_completion", 0.0)))
                )
                row = {"index": i, "tie_score": round(tie_score, 4)}
                tie_rows.append(row)
                if best_tie is None or tie_score > best_tie[1]:
                    best_tie = (i, tie_score)
            selected_idx = best_tie[0] if best_tie else near[0]

        selected = scored[selected_idx]
        selected_matches = set(selected.get("policy_act_matches") or [])
        if selected_matches:
            phase_state["completed_acts"].update(selected_matches)

        audit = {
            "turn_number": turn_number,
            "phase_name": phase_name,
            "selection_mode": "two_stage_v5",
            "adequacy_threshold": tau,
            "tie_delta": tie_delta,
            "stage_a_pool_size": len(stage_a_pool),
            "stage_a_rejected_indices": [i for i in all_indices if i not in stage_a_pool],
            "stage_a_fail_open": fail_open,
            "stage_b_best_distance": round(best_dist, 4),
            "stage_b_near_indices": near,
            "stage_c_tie_scores": tie_rows,
            "selected_index": selected_idx,
            "activation_mask": selected.get("activation_mask", {}),
            "phase_required_policy_acts": sorted(phase_state["required_acts"]),
            "phase_completed_policy_acts": sorted(phase_state["completed_acts"]),
            "phase_missing_policy_acts": sorted(
                set(phase_state["required_acts"]) - set(phase_state["completed_acts"])
            ),
        }
        self.log.selection_audit.append(audit)
        return {"selected_index": selected_idx, "selected": selected, "audit": audit}

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
        phase_context: Optional[dict] = None,
        scoring_version: str = "v4",
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

        is_v5 = scoring_version.lower() == "v5"
        hard_activation = {}
        if is_v5:
            opportunities = self._trait_opportunity_scores(turns, phase_context or {})
            hard_activation = self._build_activation_mask(
                opportunities=opportunities,
                target_traits=(phase_context or {}).get("target_traits") or [],
                apply_floor=False,
            )

        for constraint in self.contract.hard_constraints:
            violation = self._check_single_constraint(
                constraint, response_text, text_lower, turns, turn_number
            )
            if violation:
                # Only strong/reliable features remain hard-gated
                if self._is_hard_violation(violation):
                    if is_v5:
                        trait = self._VIOLATION_TRAIT_MAP.get(violation.violation_type)
                        if trait in {"O", "C"}:
                            act = float(hard_activation.get(trait, 0.0))
                            if act < self.config.v5_hard_activation_threshold:
                                continue
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
