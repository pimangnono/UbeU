"""Persona-state controller for actor-symmetric stakeholder simulations."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from experiment.memory_backend import Commitment, RelationshipSignal
from experiment.memory_backend import (
    detect_commitment_contradiction,
    score_commitment_continuity,
    score_relationship_consistency,
)

from .action_layer import (
    action_plan_alignment_score,
    heuristic_action_executability_score,
    heuristic_action_proposal,
    heuristic_state_consistency_score,
    normalize_planned_action_artifact,
)
from .ablation import DEFAULT_ABLATION_CONFIG, SimulationAblationConfig
from .action_priors import action_role_fit_score, infer_role_action_prior
from .metrics import estimate_actor_traits_from_turns, persona_drift_mae, trait_absolute_errors
from .runtime import RuntimeTurnView
from .script import SimulationPhase, StakeholderActorSpec


GENERIC_RESPONSE_PATTERNS = (
    "we should think carefully",
    "let us consider all options",
    "let's consider all options",
    "it depends",
    "we need more information",
)

PRACTICAL_PROGRESS_PATTERNS = (
    "evidence",
    "data",
    "verify",
    "confirm",
    "constraint",
    "budget",
    "feasible",
    "start small",
    "scope",
    "proven",
    "validated",
)

SYCOPHANCY_ACK_PATTERNS = (
    "good point",
    "you're right",
    "you are right",
    "that makes sense",
    "exactly",
    "absolutely",
    "totally agree",
    "i agree",
)

POLAR_SIGNAL_LIBRARY = {
    "O": {
        "high": {
            "alternative_generation": (
                "alternative",
                "another option",
                "new option",
                "third option",
                "what if",
            ),
            "reframing_or_analogy": (
                "another way to see",
                "different lens",
                "reframe",
                "frame this as",
                "analogy",
            ),
            "tradeoff_exploration": (
                "tradeoff",
                "upside",
                "downside",
                "on the other hand",
                "tension between",
            ),
            "hypothesis_generation": (
                "could be",
                "might be",
                "if we",
                "hypothesis",
                "possibility",
            ),
        },
        "low": {
            "validated_option_preference": (
                "proven",
                "validated",
                "already works",
                "standard approach",
                "known path",
            ),
            "constraint_focus": (
                "constraint",
                "practical",
                "budget",
                "limit",
                "feasible",
            ),
            "scope_narrowing": (
                "start small",
                "keep it narrow",
                "focus on",
                "limit the scope",
                "one step first",
            ),
            "evidence_preference": (
                "evidence",
                "data first",
                "verify",
                "confirm",
                "before we expand",
            ),
        },
    },
    "C": {
        "high": {
            "owner_assignment": (
                "owner",
                "i will",
                "you take",
                "who owns",
                "assign",
            ),
            "sequence_structure": (
                "first",
                "second",
                "then",
                "step",
                "sequence",
            ),
            "deadline_commitment": (
                "deadline",
                "by friday",
                "by tomorrow",
                "by end of day",
                "timeline",
            ),
            "follow_up_or_contingency": (
                "follow up",
                "check back",
                "contingency",
                "fallback",
                "if that fails",
            ),
        },
        "low": {
            "flexible_progress": (
                "keep it flexible",
                "adjust as we go",
                "adapt",
                "leave room",
                "stay flexible",
            ),
            "partial_commitment": (
                "for now",
                "tentatively",
                "small step",
                "lightweight",
                "temporary",
            ),
            "anti_overplanning": (
                "don't overplan",
                "not too rigid",
                "avoid locking in",
                "not a full plan yet",
                "avoid overcommitting",
            ),
            "adaptive_iteration": (
                "iterate",
                "try it and adjust",
                "test first",
                "pilot",
                "revise after",
            ),
        },
    },
}

TRAIT_OPPORTUNITY_KEYWORDS = {
    "O": (
        "tradeoff",
        "spillover",
        "alternative",
        "uncertainty",
        "reframe",
        "mitigation",
        "option",
        "discover",
        "explore",
    ),
    "C": (
        "coordination",
        "implementation",
        "timeline",
        "owner",
        "deadline",
        "follow up",
        "rollout",
        "process",
        "safeguard",
        "paperwork",
    ),
}

TIE_DELTA = 0.018
NEUTRAL_BAND_CENTER = 0.14
NEAR_TIE_DRIFT_DELTA = 0.02
NEAR_TIE_IDENTITY_DELTA = 0.05
NEAR_TIE_SOCIAL_DELTA = 0.06


@dataclass
class ControllerAudit:
    actor_id: str
    phase_name: str
    turn_index: int
    selected_index: int
    selected_score: float
    drift_nudge: str | None = None
    tie_detected: bool = False
    tie_break_axis: str = "none"
    tie_break_slot: str = ""
    tie_break_reason: str = ""
    score_rows: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "actor_id": self.actor_id,
            "phase_name": self.phase_name,
            "turn_index": self.turn_index,
            "selected_index": self.selected_index,
            "selected_score": self.selected_score,
            "drift_nudge": self.drift_nudge,
            "tie_detected": self.tie_detected,
            "tie_break_axis": self.tie_break_axis,
            "tie_break_slot": self.tie_break_slot,
            "tie_break_reason": self.tie_break_reason,
            "score_rows": self.score_rows,
        }


class PersonaStateController:
    """Deterministic per-actor controller for persona-state stability."""

    def __init__(
        self,
        actor_spec: StakeholderActorSpec,
        actor_name_map: dict[str, str] | None = None,
        ablation_config: SimulationAblationConfig | None = None,
    ):
        self.actor_spec = actor_spec
        self.actor_name_map = actor_name_map or {}
        self.ablation_config = ablation_config or DEFAULT_ABLATION_CONFIG
        self.selection_audits: list[dict[str, Any]] = []

    def build_nudge(self, actor_snapshot: dict[str, Any]) -> str | None:
        if not self.ablation_config.use_extended_ledger_context:
            open_commitments = actor_snapshot.get("open_commitments") or []
            if open_commitments:
                return (
                    "Stay grounded in your stakeholder identity: "
                    "do not ignore your prior commitments unless you explicitly revise them."
                )
            return None

        actor_state = actor_snapshot.get("actor_state", {})
        last_traits = actor_state.get("last_inferred_traits") or {}
        notes: list[str] = []

        for trait, value in last_traits.items():
            low, high = self.actor_spec.personality_envelope[trait]
            if value < low - 0.04:
                notes.append(f"express slightly more of your stable {trait} disposition")
            elif value > high + 0.04:
                notes.append(f"pull back toward your stable {trait} baseline")

        if actor_state.get("drift_score", 0.0) > 0.22:
            notes.append("re-anchor to your stable decision style rather than defaulting to a generic compromise voice")
        if actor_state.get("sycophancy_risk", 0.0) > 0.55:
            notes.append("do not over-accommodate others without stating your own reason or concern")
        trait_drift_map = actor_state.get("trait_drift_map") or {}
        if trait_drift_map.get("E", 0.0) > 0.18:
            notes.append("keep your social energy closer to your baseline instead of sounding overly forceful or dominant")
            if self.actor_spec.personality_prior["E"] <= 0.45:
                notes.append("keep turns compact and avoid extra questions or unnecessary social steering")
        if trait_drift_map.get("O", 0.0) > 0.14:
            if self.actor_spec.personality_prior["O"] <= 0.45:
                notes.append("prefer validated, practical framing over speculative reframing or novelty")
            elif self.actor_spec.personality_prior["O"] >= 0.55:
                notes.append("surface alternatives or tradeoffs instead of narrowing the frame too early")
        if trait_drift_map.get("A", 0.0) > 0.16:
            notes.append("keep your acknowledgment style closer to baseline instead of drifting into excessive warmth or excessive bluntness")
        if trait_drift_map.get("N", 0.0) > 0.16:
            notes.append("keep your risk sensitivity near baseline rather than flattening all uncertainty or overreacting to it")

        unfulfilled = actor_state.get("unfulfilled_persona_acts") or {}
        missing_bits = [
            f"{trait}:{'/'.join(items[:2])}"
            for trait, items in unfulfilled.items()
            if items
        ]
        if missing_bits:
            notes.append(f"recover your stable expression pattern via {', '.join(missing_bits[:2])}")

        open_commitments = actor_snapshot.get("open_commitments") or []
        if open_commitments:
            notes.append("do not ignore your prior commitments unless you explicitly revise them")

        if not notes:
            return None
        return "Stay grounded in your stakeholder identity: " + "; ".join(notes) + "."

    def score_candidate_pool(
        self,
        candidate_pool: list[dict[str, Any]],
        visible_turns: list[RuntimeTurnView],
        actor_snapshot: dict[str, Any],
        phase: SimulationPhase,
        policy_plan: dict | None = None,
        action_context: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        scored: list[dict[str, Any]] = []
        commitments = [
            Commitment(**commitment)
            for commitment in actor_snapshot.get("open_commitments", [])
        ]
        relationships = [
            RelationshipSignal(
                counterpart=self._display_name_for_relationship(edge),
                sentiment=edge.get("sentiment", "neutral"),
                strength=edge.get("trust", 0.5),
                last_turn=edge.get("last_turn", 0),
            )
            for edge in actor_snapshot.get("relationships", [])
        ]
        opportunity_scores = self._trait_opportunity_scores(phase, visible_turns)

        for row in candidate_pool:
            text = row["text"]
            extended_turns = list(visible_turns) + [
                RuntimeTurnView(
                    turn_number=(visible_turns[-1].turn_number + 1) if visible_turns else 1,
                    speaker_name=self.actor_spec.display_name,
                    content=text,
                )
            ]
            inferred_traits = estimate_actor_traits_from_turns(extended_turns, self.actor_spec.display_name)
            drift = persona_drift_mae(self.actor_spec.personality_prior, inferred_traits)
            trait_error_map = trait_absolute_errors(self.actor_spec.personality_prior, inferred_traits)
            envelope_penalty = self._envelope_penalty(inferred_traits)
            identity_consistency = self._identity_consistency_score(text)
            commitment_continuity = score_commitment_continuity(text, commitments)
            relationship_consistency = score_relationship_consistency(text, relationships)
            situational_adequacy = self._situational_adequacy_score(text, visible_turns, phase)
            interaction_progress = self._interaction_progress_score(text)
            redundancy_penalty = self._redundancy_penalty(text, visible_turns)
            genericity_penalty = self._genericity_penalty(text)
            policy_match = self._policy_match_score(policy_plan or {}, text)
            contradiction_penalty = 1.0 if detect_commitment_contradiction(text, commitments) else 0.0
            if self.ablation_config.use_banded_target_matching:
                trait_target_alignment, trait_target_details = self._trait_target_alignment(
                    text=text,
                    phase=phase,
                    visible_turns=visible_turns,
                    opportunity_scores=opportunity_scores,
                )
                unfulfilled_persona_acts = {
                    trait: detail["missing_preferred_categories"]
                    for trait, detail in trait_target_details.items()
                    if detail["missing_preferred_categories"]
                }
            else:
                trait_target_alignment = 0.5
                trait_target_details = {
                    "disabled": True,
                    "reason": "banded_target_matching_ablation",
                }
                unfulfilled_persona_acts = {}
            sycophancy_risk, sycophancy_signals = self._sycophancy_risk(
                text=text,
                visible_turns=visible_turns,
            )
            social_trait_alignment, social_trait_details = self._social_trait_alignment(
                inferred_traits=inferred_traits,
                trait_error_map=trait_error_map,
            )
            expressive_stability_penalty, expressive_stability_details = self._expressive_stability_penalty(
                text=text,
                inferred_traits=inferred_traits,
                trait_error_map=trait_error_map,
                opportunity_scores=opportunity_scores,
            )
            if action_context and action_context.get("use_action_aware_scoring"):
                planned_action_artifact = normalize_planned_action_artifact(
                    script=action_context["script"],
                    actor_id=self.actor_spec.actor_id,
                    phase_name=phase.name,
                    policy_plan=policy_plan or {},
                    planned_action_artifact=(policy_plan or {}).get("action_plan"),
                    valid_target_keys=list(action_context.get("valid_target_keys", [])),
                    allowed_action_types=list(action_context.get("allowed_action_types", [])),
                )
                action_role_prior = infer_role_action_prior(
                    role=self.actor_spec.role,
                    incentives=list(self.actor_spec.incentives),
                    concerns=list(self.actor_spec.concerns),
                    phase_name=phase.name,
                    phase_cues=phase.cues,
                    allowed_action_types=list(action_context.get("allowed_action_types", [])),
                    valid_target_keys=list(action_context.get("valid_target_keys", [])),
                )
                action_proposal = heuristic_action_proposal(
                    script=action_context["script"],
                    actor_id=self.actor_spec.actor_id,
                    actor_name_map=self.actor_name_map,
                    phase_name=phase.name,
                    turn_index=action_context.get("turn_index", 1),
                    selected_text=text,
                    policy_plan=policy_plan or {},
                    planned_action_artifact=planned_action_artifact.to_dict() if planned_action_artifact else None,
                    valid_target_keys=list(action_context.get("valid_target_keys", [])),
                    allowed_action_types=list(action_context.get("allowed_action_types", [])),
                )
                action_executability = heuristic_action_executability_score(
                    text=text,
                    valid_target_keys=list(action_context.get("valid_target_keys", [])),
                    allowed_action_types=list(action_context.get("allowed_action_types", [])),
                )
                state_consistency = heuristic_state_consistency_score(
                    text=text,
                    action_type=action_proposal.action_type if action_proposal else None,
                    target_key=action_proposal.target_key if action_proposal else None,
                    global_state=action_context.get("global_state", {}),
                    phase_name=phase.name,
                )
                action_plan_alignment, action_plan_alignment_details = action_plan_alignment_score(
                    planned_action_artifact.to_dict() if planned_action_artifact else None,
                    action_proposal.to_dict() if action_proposal else None,
                )
                action_role_fit, action_role_fit_details = action_role_fit_score(
                    action_type=(
                        action_proposal.action_type
                        if action_proposal
                        else (planned_action_artifact.action_type if planned_action_artifact else None)
                    ),
                    target_key=(
                        action_proposal.target_key
                        if action_proposal
                        else (planned_action_artifact.target_key if planned_action_artifact else None)
                    ),
                    prior=action_role_prior,
                )
                action_weight_multiplier = 1.0 if planned_action_artifact else 0.2
            else:
                planned_action_artifact = None
                action_proposal = None
                action_executability = 0.5
                state_consistency = 0.5
                action_plan_alignment = 0.5
                action_role_fit = 0.5
                action_role_fit_details = {
                    "available": False,
                    "reason": "action_aware_scoring_disabled",
                }
                action_weight_multiplier = 0.0
                action_plan_alignment_details = {
                    "available": False,
                    "reason": "action_aware_scoring_disabled",
                }

            total = (
                0.18 * identity_consistency
                + 0.18 * (1.0 - drift)
                + (0.14 * trait_target_alignment if self.ablation_config.use_banded_target_matching else 0.0)
                + 0.16 * social_trait_alignment
                + 0.10 * relationship_consistency
                + 0.10 * commitment_continuity
                + 0.09 * situational_adequacy
                + 0.04 * interaction_progress
                + 0.02 * policy_match
                + (0.10 * action_executability * action_weight_multiplier if action_context and action_context.get("use_action_aware_scoring") else 0.0)
                + (0.10 * state_consistency * action_weight_multiplier if action_context and action_context.get("use_action_aware_scoring") else 0.0)
                + (0.10 * action_plan_alignment * action_weight_multiplier if action_context and action_context.get("use_action_aware_scoring") else 0.0)
                + (0.12 * action_role_fit * action_weight_multiplier if action_context and action_context.get("use_action_aware_scoring") else 0.0)
                - 0.18 * contradiction_penalty
                - 0.12 * envelope_penalty
                - 0.08 * sycophancy_risk
                - 0.10 * expressive_stability_penalty
                - 0.07 * redundancy_penalty
                - 0.07 * genericity_penalty
                - (0.04 * (1.0 - action_executability) * action_weight_multiplier if action_context and action_context.get("use_action_aware_scoring") else 0.0)
            )
            total = round(max(0.0, min(1.0, total)), 4)

            scored.append({
                **row,
                "score": total,
                "identity_consistency": round(identity_consistency, 4),
                "persona_drift": drift,
                "persona_consistency": round(1.0 - drift, 4),
                "envelope_penalty": round(envelope_penalty, 4),
                "commitment_continuity": round(commitment_continuity, 4),
                "relationship_consistency": round(relationship_consistency, 4),
                "situational_adequacy": round(situational_adequacy, 4),
                "interaction_progress": round(interaction_progress, 4),
                "policy_match": round(policy_match, 4),
                "trait_target_alignment": round(trait_target_alignment, 4),
                "trait_target_details": trait_target_details,
                "social_trait_alignment": round(social_trait_alignment, 4),
                "social_trait_details": social_trait_details,
                "expressive_stability_penalty": round(expressive_stability_penalty, 4),
                "expressive_stability_details": expressive_stability_details,
                "action_executability": round(action_executability, 4),
                "state_consistency": round(state_consistency, 4),
                "action_plan_alignment": round(action_plan_alignment, 4),
                "action_plan_alignment_details": action_plan_alignment_details,
                "action_role_fit": round(action_role_fit, 4),
                "action_role_fit_details": action_role_fit_details,
                "action_weight_multiplier": round(action_weight_multiplier, 4),
                "action_hint": action_proposal.to_dict() if action_proposal else None,
                "planned_action_artifact": planned_action_artifact.to_dict() if planned_action_artifact else None,
                "trait_error_map": trait_error_map,
                "opportunity_scores": dict(opportunity_scores),
                "redundancy_penalty": round(redundancy_penalty, 4),
                "genericity_penalty": round(genericity_penalty, 4),
                "contradiction_penalty": contradiction_penalty,
                "sycophancy_risk": round(sycophancy_risk, 4),
                "sycophancy_signals": sycophancy_signals,
                "unfulfilled_persona_acts": unfulfilled_persona_acts,
                "inferred_traits": inferred_traits,
            })

        return sorted(scored, key=lambda item: item["score"], reverse=True)

    def select_candidate(
        self,
        scored_candidates: list[dict[str, Any]],
        phase: SimulationPhase,
        turn_index: int,
        drift_nudge: str | None = None,
    ) -> dict[str, Any]:
        if not scored_candidates:
            fallback = {
                "text": "I want to be careful about the tradeoffs before we commit.",
                "score": 0.0,
            }
            audit = ControllerAudit(
                actor_id=self.actor_spec.actor_id,
                phase_name=phase.name,
                turn_index=turn_index,
                selected_index=-1,
                selected_score=0.0,
                drift_nudge=drift_nudge,
                score_rows=[],
            )
            self.selection_audits.append(audit.to_dict())
            return {"selected_index": -1, "selected": fallback, "audit": audit.to_dict()}

        selected_index = 0
        tie_detected = False
        tie_break_axis = "none"
        tie_break_reason = ""
        tie_break_slot = scored_candidates[0].get("slot", "")

        near_tie = [
            (idx, row)
            for idx, row in enumerate(scored_candidates)
            if abs(row["score"] - scored_candidates[0]["score"]) <= TIE_DELTA
        ]
        if (
            self.ablation_config.use_tie_routing
            and len(near_tie) > 1
            and self._should_apply_tie_break(near_tie)
        ):
            tie_detected = True
            selected_index, tie_break_axis, tie_break_reason = self._break_near_tie(
                near_tie=near_tie,
                phase=phase,
                turn_index=turn_index,
            )
            tie_break_slot = scored_candidates[selected_index].get("slot", "")

        selected = scored_candidates[selected_index]
        audit = ControllerAudit(
            actor_id=self.actor_spec.actor_id,
            phase_name=phase.name,
            turn_index=turn_index,
            selected_index=selected_index,
            selected_score=selected["score"],
            drift_nudge=drift_nudge,
            tie_detected=tie_detected,
            tie_break_axis=tie_break_axis,
            tie_break_slot=tie_break_slot,
            tie_break_reason=tie_break_reason,
            score_rows=[
                {
                    "slot": row.get("slot"),
                    "score": row["score"],
                    "persona_drift": row["persona_drift"],
                    "identity_consistency": row["identity_consistency"],
                    "relationship_consistency": row["relationship_consistency"],
                    "trait_target_alignment": row.get("trait_target_alignment"),
                    "social_trait_alignment": row.get("social_trait_alignment"),
                    "action_executability": row.get("action_executability"),
                    "state_consistency": row.get("state_consistency"),
                    "sycophancy_risk": row.get("sycophancy_risk"),
                }
                for row in scored_candidates
            ],
        )
        self.selection_audits.append(audit.to_dict())
        return {"selected_index": selected_index, "selected": selected, "audit": audit.to_dict()}

    def _break_near_tie(
        self,
        near_tie: list[tuple[int, dict[str, Any]]],
        phase: SimulationPhase,
        turn_index: int,
    ) -> tuple[int, str, str]:
        exemplar = near_tie[0][1]
        opportunity_scores = exemplar.get("opportunity_scores") or {}
        primary_axis = self._primary_tie_axis(opportunity_scores)
        slot_order = self._slot_order_for_axis(primary_axis, turn_index)
        slot_rank = {slot: idx for idx, slot in enumerate(slot_order)}

        best = None
        for original_index, row in near_tie:
            rank = slot_rank.get(row.get("slot", ""), len(slot_order) + 1)
            tie_key = (
                -row.get("trait_target_alignment", 0.0),
                rank,
                -row.get("identity_consistency", 0.0),
                row.get("genericity_penalty", 1.0),
                row.get("redundancy_penalty", 1.0),
            )
            if best is None or tie_key < best[1]:
                best = (original_index, tie_key, row.get("slot", ""))

        selected_index = best[0] if best else near_tie[0][0]
        selected_slot = best[2] if best else near_tie[0][1].get("slot", "")
        reason = f"near-tie resolved by {primary_axis} slot priority -> {selected_slot or 'no_slot'}"
        return selected_index, primary_axis, reason

    def _should_apply_tie_break(
        self,
        near_tie: list[tuple[int, dict[str, Any]]],
    ) -> bool:
        top = near_tie[0][1]
        challenger = near_tie[1][1]
        if abs(top.get("persona_drift", 1.0) - challenger.get("persona_drift", 1.0)) > NEAR_TIE_DRIFT_DELTA:
            return False
        if abs(top.get("identity_consistency", 0.0) - challenger.get("identity_consistency", 0.0)) > NEAR_TIE_IDENTITY_DELTA:
            return False
        if abs(top.get("social_trait_alignment", 0.0) - challenger.get("social_trait_alignment", 0.0)) > NEAR_TIE_SOCIAL_DELTA:
            return False
        return True

    def _primary_tie_axis(self, opportunity_scores: dict[str, float]) -> str:
        o_opp = float(opportunity_scores.get("O", 0.0))
        c_opp = float(opportunity_scores.get("C", 0.0))
        if max(o_opp, c_opp) >= 0.35:
            trait = "O" if o_opp >= c_opp else "C"
        else:
            o_strength = abs(self.actor_spec.personality_prior["O"] - 0.5)
            c_strength = abs(self.actor_spec.personality_prior["C"] - 0.5)
            trait = "O" if o_strength >= c_strength else "C"
        pole, _ = self._trait_pole(trait)
        return f"{trait}_{pole}"

    def _slot_order_for_axis(self, axis: str, turn_index: int) -> list[str]:
        orders = {
            "O_high": ["challenger", "integrator", "skeptic", "planner", "ideator"],
            "O_low": ["skeptic", "planner", "integrator", "challenger", "ideator"],
            "O_neutral": ["integrator", "skeptic", "planner", "challenger", "ideator"],
            "C_high": ["planner", "integrator", "skeptic", "challenger", "ideator"],
            "C_low": ["skeptic", "integrator", "challenger", "planner", "ideator"],
            "C_neutral": ["integrator", "planner", "skeptic", "challenger", "ideator"],
        }
        order = list(orders.get(axis, ["integrator", "planner", "skeptic", "challenger", "ideator"]))
        if len(order) >= 2 and turn_index % 2 == 1:
            order[0], order[1] = order[1], order[0]
        return order

    def _trait_target_alignment(
        self,
        text: str,
        phase: SimulationPhase,
        visible_turns: list[RuntimeTurnView],
        opportunity_scores: dict[str, float],
    ) -> tuple[float, dict[str, Any]]:
        lowered = text.lower()
        trait_scores: list[float] = []
        details: dict[str, Any] = {}

        for trait in ("O", "C"):
            pole, strength = self._trait_pole(trait)
            preferred_strength, preferred_hits = self._trait_signal_strength(lowered, trait, pole)
            opposite_pole = "low" if pole == "high" else "high"
            opposite_strength, opposite_hits = self._trait_signal_strength(lowered, trait, opposite_pole)
            opportunity = float(opportunity_scores.get(trait, 0.0))
            band_center, band_width = self._target_band(opportunity, strength, pole)
            lower = max(0.0, band_center - (band_width / 2.0))
            upper = min(1.0, band_center + (band_width / 2.0))
            miss = self._band_miss(preferred_strength, lower, upper)
            if pole == "neutral":
                opposite_penalty = opposite_strength * opportunity * 0.28
            else:
                opposite_penalty = opposite_strength * (
                    0.24 + (0.65 * opportunity) + (0.34 * strength)
                )
                if preferred_strength == 0.0 and opposite_strength > 0.0 and opportunity >= 0.20:
                    opposite_penalty += 0.22
            score = max(0.0, 1.0 - min(1.0, miss + opposite_penalty))
            missing_preferred = [
                category
                for category, hit in preferred_hits.items()
                if not hit
            ]
            if opportunity < 0.35:
                missing_preferred = []

            details[trait] = {
                "pole": pole,
                "strength": round(strength, 4),
                "opportunity_score": round(opportunity, 4),
                "target_band": [round(lower, 4), round(upper, 4)],
                "preferred_signal_strength": round(preferred_strength, 4),
                "opposite_signal_strength": round(opposite_strength, 4),
                "preferred_hits": preferred_hits,
                "opposite_hits": opposite_hits,
                "missing_preferred_categories": missing_preferred[:3],
                "score": round(score, 4),
            }
            trait_scores.append(score)

        return round(sum(trait_scores) / max(len(trait_scores), 1), 4), details

    def _trait_signal_strength(
        self,
        lowered: str,
        trait: str,
        pole: str,
    ) -> tuple[float, dict[str, float]]:
        if pole == "neutral":
            return 0.0, {}
        categories = POLAR_SIGNAL_LIBRARY[trait][pole]
        hits: dict[str, float] = {}
        for category, patterns in categories.items():
            partial_hit = sum(1 for pattern in patterns if pattern in lowered)
            hits[category] = round(min(1.0, partial_hit / 2.0), 4)
        strength = sum(hits.values()) / max(len(categories), 1)
        return round(strength, 4), hits

    def _target_band(
        self,
        opportunity: float,
        strength: float,
        pole: str,
    ) -> tuple[float, float]:
        if pole == "neutral":
            center = NEUTRAL_BAND_CENTER * (0.8 + opportunity)
            width = 0.34
            return center, width
        center = opportunity * (0.14 + (0.66 * strength))
        width = max(0.16, 0.30 - (0.12 * strength)) if pole == "low" else max(0.14, 0.26 - (0.12 * strength))
        return center, width

    def _band_miss(self, observed: float, lower: float, upper: float) -> float:
        if observed < lower:
            return lower - observed
        if observed > upper:
            return observed - upper
        return 0.0

    def _trait_pole(self, trait: str) -> tuple[str, float]:
        value = float(self.actor_spec.personality_prior[trait])
        centered = value - 0.5
        strength = round(abs(centered) * 2.0, 4)
        if abs(centered) < 0.08:
            return "neutral", strength
        return ("high" if centered > 0 else "low"), strength

    def _trait_opportunity_scores(
        self,
        phase: SimulationPhase,
        visible_turns: list[RuntimeTurnView],
    ) -> dict[str, float]:
        recent_text = " ".join(turn.content.lower() for turn in visible_turns[-4:])
        phase_text = " ".join(
            [phase.name.lower(), phase.goal.lower(), phase.style.lower(), *[cue.lower() for cue in phase.cues]]
        )
        context = f"{phase_text} {recent_text}"
        scores: dict[str, float] = {}

        for trait, keywords in TRAIT_OPPORTUNITY_KEYWORDS.items():
            hits = sum(1 for keyword in keywords if keyword in context)
            base = 0.10
            if trait == "O" and phase.style == "disagreement":
                base += 0.05
            if trait == "C" and phase.style in {"consensus", "neutral"}:
                base += 0.05
            score = min(1.0, base + (0.12 * min(hits, 5)))
            scores[trait] = round(score, 4)
        return scores

    def _display_name_for_relationship(self, edge: dict[str, Any]) -> str:
        target_actor_id = edge.get("target_actor_id", "")
        return self.actor_name_map.get(target_actor_id, target_actor_id.replace("_", " ").title())

    def _social_trait_alignment(
        self,
        inferred_traits: dict[str, float],
        trait_error_map: dict[str, float],
    ) -> tuple[float, dict[str, Any]]:
        details: dict[str, Any] = {}
        scores: list[float] = []
        for trait in ("E", "A", "N"):
            prior = float(self.actor_spec.personality_prior[trait])
            observed = float(inferred_traits[trait])
            if trait == "E":
                if prior <= 0.45:
                    tolerance = 0.06
                    miss_scale = 0.18
                elif prior >= 0.55:
                    tolerance = 0.09
                    miss_scale = 0.22
                else:
                    tolerance = 0.07
                    miss_scale = 0.20
            elif trait == "N":
                tolerance = 0.09
                miss_scale = 0.22
            else:
                tolerance = 0.10
                miss_scale = 0.24
            low = max(0.0, prior - tolerance)
            high = min(1.0, prior + tolerance)
            miss = self._band_miss(observed, low, high)
            if trait == "E" and observed > high and prior <= 0.50:
                miss *= 1.2
            score = max(0.0, 1.0 - min(1.0, miss / miss_scale))
            details[trait] = {
                "prior": round(prior, 4),
                "observed": round(observed, 4),
                "target_band": [round(low, 4), round(high, 4)],
                "absolute_error": round(trait_error_map[trait], 4),
                "score": round(score, 4),
            }
            scores.append(score)
        return round(sum(scores) / max(len(scores), 1), 4), details

    def _expressive_stability_penalty(
        self,
        text: str,
        inferred_traits: dict[str, float],
        trait_error_map: dict[str, float],
        opportunity_scores: dict[str, float],
    ) -> tuple[float, dict[str, float]]:
        lowered = text.lower()
        o_prior = float(self.actor_spec.personality_prior["O"])
        e_prior = float(self.actor_spec.personality_prior["E"])

        high_o_strength, _ = self._trait_signal_strength(lowered, "O", "high")
        dominance_signal = self._social_dominance_signal(text)
        o_cap = min(1.0, o_prior + (0.05 if o_prior <= 0.45 else 0.08))
        e_cap = min(1.0, e_prior + (0.05 if e_prior <= 0.45 else 0.08))
        o_overshoot = max(0.0, inferred_traits["O"] - o_cap)
        e_overshoot = max(0.0, inferred_traits["E"] - e_cap)

        penalty = 0.0
        if o_prior <= 0.45:
            penalty += (0.80 * o_overshoot) + (0.28 * high_o_strength)
            if opportunity_scores.get("O", 0.0) < 0.35 and high_o_strength > 0.0:
                penalty += 0.08
        elif o_prior >= 0.55:
            o_floor = max(0.0, o_prior - 0.10)
            penalty += 0.30 * max(0.0, o_floor - inferred_traits["O"])

        if e_prior <= 0.45:
            penalty += (0.95 * e_overshoot) + (0.32 * dominance_signal)
        elif e_prior >= 0.55:
            e_floor = max(0.0, e_prior - 0.10)
            penalty += 0.22 * max(0.0, e_floor - inferred_traits["E"])

        return min(1.0, round(penalty, 4)), {
            "o_overshoot": round(o_overshoot, 4),
            "e_overshoot": round(e_overshoot, 4),
            "high_o_signal_strength": round(high_o_strength, 4),
            "dominance_signal": round(dominance_signal, 4),
            "o_absolute_error": round(trait_error_map["O"], 4),
            "e_absolute_error": round(trait_error_map["E"], 4),
        }

    def _social_dominance_signal(self, text: str) -> float:
        lowered = text.lower()
        words = re.findall(r"[a-zA-Z']+", text)
        word_count = len(words)
        question_count = text.count("?")
        name_mentions = sum(
            1
            for name in self.actor_name_map.values()
            if name and name.lower() in lowered
        )
        we_should_count = lowered.count("we should") + lowered.count("let's")

        signal = 0.0
        if word_count > 34:
            signal += min(0.30, (word_count - 34) / 40.0)
        signal += min(0.25, 0.10 * question_count)
        signal += min(0.20, 0.08 * name_mentions)
        signal += min(0.18, 0.06 * we_should_count)
        return round(min(1.0, signal), 4)

    def _identity_consistency_score(self, text: str) -> float:
        lowered = text.lower()
        keyword_hits = 0
        keyword_pool: list[str] = []
        keyword_pool.extend(self.actor_spec.incentives)
        keyword_pool.extend(self.actor_spec.concerns)
        keyword_pool.append(self.actor_spec.role)
        keyword_pool.extend(str(value) for value in self.actor_spec.identity_core.values())

        for raw in keyword_pool:
            for token in re.findall(r"[a-zA-Z]{4,}", raw.lower()):
                if token in lowered:
                    keyword_hits += 1

        base = 0.55
        if keyword_hits > 0:
            base += min(0.30, 0.08 * keyword_hits)

        if self.actor_spec.display_name.lower() in lowered:
            base -= 0.06

        return max(0.0, min(1.0, base))

    def _envelope_penalty(self, inferred_traits: dict[str, float]) -> float:
        penalty = 0.0
        for trait, value in inferred_traits.items():
            low, high = self.actor_spec.personality_envelope[trait]
            if value < low:
                penalty += low - value
            elif value > high:
                penalty += value - high
        return min(1.0, penalty)

    def _situational_adequacy_score(
        self,
        text: str,
        visible_turns: list[RuntimeTurnView],
        phase: SimulationPhase,
    ) -> float:
        lowered = text.lower()
        score = 0.45
        last_turn = visible_turns[-1].content.lower() if visible_turns else ""
        overlap = self._token_overlap(lowered, last_turn)
        score += min(0.20, overlap)

        for cue in phase.cues:
            for token in re.findall(r"[a-zA-Z]{4,}", cue.lower()):
                if token in lowered:
                    score += 0.08

        for token in re.findall(r"[a-zA-Z]{4,}", phase.goal.lower()):
            if token in lowered:
                score += 0.03

        return max(0.0, min(1.0, score))

    def _interaction_progress_score(self, text: str) -> float:
        lowered = text.lower()
        score = 0.33
        o_prior = float(self.actor_spec.personality_prior["O"])
        e_prior = float(self.actor_spec.personality_prior["E"])
        o_high = max(0.0, (o_prior - 0.5) * 2.0)
        o_low = max(0.0, (0.5 - o_prior) * 2.0)
        e_high = max(0.0, (e_prior - 0.5) * 2.0)
        e_low = max(0.0, (0.5 - e_prior) * 2.0)
        word_count = len(re.findall(r"[a-zA-Z']+", text))

        if "?" in text:
            score += 0.02 + (0.07 * e_high)
        if any(token in lowered for token in ("i will", "we should", "next step", "by ", "deadline")):
            score += 0.16
        if any(token in lowered for token in ("what if", "alternative", "another option", "tradeoff")):
            score += 0.03 + (0.10 * o_high)
        if any(token in lowered for token in PRACTICAL_PROGRESS_PATTERNS):
            score += 0.03 + (0.10 * o_low)
        if any(token in lowered for token in ("agree", "disagree", "good point", "fair point")):
            score += 0.05
        if e_low > 0.10 and word_count <= 24:
            score += 0.07 * e_low
        if e_prior <= 0.45 and word_count > 38:
            score -= min(0.12, (word_count - 38) / 70.0)
        if e_prior <= 0.45 and text.count("?") > 1:
            score -= 0.06
        return max(0.0, min(1.0, score))

    def _policy_match_score(self, policy_plan: dict, text: str) -> float:
        if not policy_plan:
            return 0.5
        lowered = text.lower()
        score = 0.35
        if policy_plan.get("goal_mode") == "coordinate" and any(token in lowered for token in ("next", "owner", "by ", "deadline")):
            score += 0.30
        if policy_plan.get("goal_mode") == "discover" and any(token in lowered for token in ("what if", "why", "another option")):
            score += 0.20
        if policy_plan.get("stance") == "synthesize" and any(token in lowered for token in ("both", "balance", "middle ground")):
            score += 0.20
        if policy_plan.get("stance") == "oppose" and any(token in lowered for token in ("disagree", "push back", "won't work")):
            score += 0.20
        return max(0.0, min(1.0, score))

    def _sycophancy_risk(
        self,
        text: str,
        visible_turns: list[RuntimeTurnView],
    ) -> tuple[float, dict[str, int]]:
        lowered = text.lower()
        last_speaker = visible_turns[-1].speaker_name.lower() if visible_turns else ""
        acknowledges = any(pattern in lowered for pattern in SYCOPHANCY_ACK_PATTERNS)
        names_last_speaker = bool(last_speaker and last_speaker in lowered)
        asserts_self = any(
            pattern in lowered
            for pattern in ("i think", "i worry", "my concern", "from my side", "for me", "however", "but")
        )
        role_anchor = any(
            token in lowered
            for token in (
                *[item.lower() for item in self.actor_spec.incentives],
                *[item.lower() for item in self.actor_spec.concerns],
            )
        )

        risk = 0.08
        if acknowledges:
            risk += 0.22
        if names_last_speaker:
            risk += 0.08
        if not asserts_self:
            risk += 0.20
        if not role_anchor:
            risk += 0.16
        if not any(token in lowered for token in ("risk", "concern", "tradeoff", "owner", "data", "constraint", "timeline")):
            risk += 0.10

        signals = {
            "acknowledgment_without_position": int(acknowledges and not asserts_self),
            "named_deference": int(names_last_speaker and acknowledges),
            "missing_role_anchor": int(not role_anchor),
        }
        return max(0.0, min(1.0, round(risk, 4))), signals

    def _redundancy_penalty(self, text: str, visible_turns: list[RuntimeTurnView]) -> float:
        actor_turns = [turn for turn in visible_turns if turn.speaker_name == self.actor_spec.display_name]
        if not actor_turns:
            return 0.0
        prior = actor_turns[-1].content.lower()
        overlap = self._token_overlap(text.lower(), prior)
        if overlap < 0.45:
            return 0.0
        return min(1.0, overlap)

    def _genericity_penalty(self, text: str) -> float:
        lowered = text.lower().strip()
        if len(lowered.split()) < 7:
            return 0.35
        if any(pattern in lowered for pattern in GENERIC_RESPONSE_PATTERNS):
            return 0.45
        return 0.0

    def _token_overlap(self, left: str, right: str) -> float:
        left_tokens = {
            token
            for token in re.findall(r"[a-zA-Z]{3,}", left)
            if token not in {"that", "with", "this", "have", "from", "should"}
        }
        right_tokens = {
            token
            for token in re.findall(r"[a-zA-Z]{3,}", right)
            if token not in {"that", "with", "this", "have", "from", "should"}
        }
        if not left_tokens or not right_tokens:
            return 0.0
        return len(left_tokens & right_tokens) / max(len(left_tokens), 1)
