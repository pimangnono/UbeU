"""Typed action layer for action-conditioned stakeholder simulations."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Protocol


ACTION_TYPES = (
    "assign_owner",
    "request_evidence",
    "publish_update",
    "narrow_scope",
    "pilot",
    "commit_resource",
    "defer_decision",
    "preserve_autonomy",
)

ACTION_FAMILIES = {
    "assign_owner": "ownership",
    "request_evidence": "evidence",
    "publish_update": "communication",
    "narrow_scope": "scope",
    "pilot": "scope",
    "commit_resource": "resourcing",
    "defer_decision": "timing",
    "preserve_autonomy": "governance",
}

DELTA_PALETTE = {
    "low": 0.04,
    "medium": 0.08,
    "high": 0.12,
}

DEFAULT_LOCAL_STATE_KEYS = ("trust", "execution_confidence", "alignment", "risk", "uncertainty")

ACTION_CUE_PATTERNS: dict[str, tuple[str, ...]] = {
    "assign_owner": ("owner", "own", "assign", "take point", "take the lead"),
    "request_evidence": ("evidence", "data", "verify", "confirm", "proof"),
    "publish_update": ("publish", "update", "communicate", "send note", "announce"),
    "narrow_scope": ("narrow", "scope", "cut scope", "reduce scope", "focus on"),
    "pilot": ("pilot", "test first", "small test", "trial", "experiment"),
    "commit_resource": ("commit resources", "allocate", "staff", "budget", "support team"),
    "defer_decision": ("defer", "wait", "hold off", "not decide yet", "delay decision"),
    "preserve_autonomy": ("autonomy", "independent", "preserve control", "keep roadmap", "keep authority"),
}

ACTION_STATE_HINTS: dict[str, tuple[str, ...]] = {
    "alignment": ("align", "alignment", "consensus", "same page"),
    "trust": ("trust", "confidence", "credibility", "retain people"),
    "uncertainty": ("uncertain", "clarity", "unknown", "ambiguity"),
    "execution_confidence": ("execute", "delivery", "owner", "timeline", "readiness"),
    "risk": ("risk", "incident", "backlash", "fraud", "exposure"),
    "admin_feasibility": ("admin", "processing", "paperwork", "verification"),
    "spillover_risk": ("spillover", "side effect", "neighbor", "second-order"),
    "launch_readiness": ("launch", "ready", "release", "ship"),
    "message_alignment": ("message", "positioning", "narrative", "brand"),
    "incident_risk": ("incident", "outage", "support load", "regression"),
    "retention_risk": ("retention", "exit", "attrition", "leave"),
    "autonomy_confidence": ("autonomy", "control", "roadmap", "independent"),
    "integration_clarity": ("integration", "operating model", "sequencing", "clarity"),
}


class SupportsGenerate(Protocol):
    async def generate(
        self,
        prompt: str,
        system_instruction: str | None = None,
        temperature: float = 0.7,
        max_tokens: int = 500,
        tier: Any | None = None,
    ) -> str: ...


def clip_unit(value: float) -> float:
    return max(0.0, min(1.0, round(float(value), 4)))


@dataclass
class ActionProposal:
    proposal_id: str
    actor_id: str
    phase_name: str
    turn_index: int
    action_type: str | None
    target_key: str | None
    target_actor_id: str | None = None
    owner_actor_id: str | None = None
    deadline_phase: str | None = None
    strength: str = "medium"
    confidence: float = 0.0
    evidence_text: str = ""
    commitment_id: str | None = None
    status: str = "proposed"
    rejection_reason: str | None = None
    action_bearing: bool = False
    compiler_source: str = "none"
    raw_payload: dict[str, Any] = field(default_factory=dict)
    validation_trace: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class PlannedActionArtifact:
    action_type: str | None
    target_key: str | None
    target_actor_id: str | None = None
    owner_actor_id: str | None = None
    deadline_phase: str | None = None
    strength: str = "medium"
    confidence: float = 0.0
    expected_state_effect: str | None = None
    rationale: str = ""
    source: str = "policy_plan"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ExecutedAction:
    proposal_id: str
    action_type: str
    phase_name: str
    owner_actor_id: str | None
    target_key: str
    applied_delta: dict[str, float]
    pre_state: dict[str, Any]
    post_state: dict[str, Any]
    target_actor_id: str | None = None
    coherence_score: float = 1.0
    contradiction_flag: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class WorldStateSnapshot:
    phase_name: str
    turn_index: int
    global_state: dict[str, float]
    local_state_by_actor: dict[str, dict[str, float]]
    executed_action_ids: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class TransitionRule:
    global_deltas: dict[str, float] = field(default_factory=dict)
    owner_local_deltas: dict[str, float] = field(default_factory=dict)
    target_local_deltas: dict[str, float] = field(default_factory=dict)
    preconditions: list[dict[str, Any]] = field(default_factory=list)
    feedback_template: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def default_local_state(actor_ids: list[str]) -> dict[str, dict[str, float]]:
    return {
        actor_id: {key: 0.5 for key in DEFAULT_LOCAL_STATE_KEYS}
        for actor_id in actor_ids
    }


def action_family(action_type: str | None) -> str:
    if not action_type:
        return "none"
    return ACTION_FAMILIES.get(action_type, action_type)


def commitment_strength_to_band(value: str | None) -> str:
    lowered = (value or "").lower()
    if lowered in {"high", "strong"}:
        return "high"
    if lowered in {"low", "light"}:
        return "low"
    return "medium"


def commitment_strength_to_confidence(value: str | None) -> float:
    band = commitment_strength_to_band(value)
    if band == "high":
        return 0.78
    if band == "low":
        return 0.52
    return 0.64


def _first_matching_action_type(text: str) -> str | None:
    lowered = text.lower()
    for action_type, patterns in ACTION_CUE_PATTERNS.items():
        if any(pattern in lowered for pattern in patterns):
            return action_type
    return None


def _first_matching_target_key(text: str, valid_target_keys: list[str]) -> str | None:
    lowered = text.lower()
    for target_key in valid_target_keys:
        normalized_key = target_key.lower()
        natural_key = normalized_key.replace("_", " ")
        if normalized_key in lowered or natural_key in lowered:
            return target_key
    for target_key, patterns in ACTION_STATE_HINTS.items():
        if target_key not in valid_target_keys:
            continue
        if any(pattern in lowered for pattern in patterns):
            return target_key
    return valid_target_keys[0] if valid_target_keys else None


def _first_matching_actor(text: str, actor_name_map: dict[str, str]) -> str | None:
    lowered = text.lower()
    for actor_id, display_name in actor_name_map.items():
        if display_name.lower() in lowered:
            return actor_id
    return None


def _detect_strength(text: str) -> str:
    lowered = text.lower()
    if any(token in lowered for token in ("immediately", "must", "critical", "urgent", "strongly")):
        return "high"
    if any(token in lowered for token in ("small", "pilot", "tentative", "lightweight")):
        return "low"
    return "medium"


def _detect_confidence(text: str) -> float:
    lowered = text.lower()
    base = 0.45
    if any(token in lowered for token in ("will", "must", "need to", "we should")):
        base += 0.18
    if any(token in lowered for token in ("might", "could", "maybe", "tentative")):
        base -= 0.12
    return clip_unit(base)


def detect_action_bearing_turn(text: str) -> bool:
    lowered = text.lower()
    return any(
        any(pattern in lowered for pattern in patterns)
        for patterns in ACTION_CUE_PATTERNS.values()
    )


def heuristic_action_executability_score(
    text: str,
    valid_target_keys: list[str],
    allowed_action_types: list[str],
) -> float:
    if not detect_action_bearing_turn(text):
        return 0.0
    action_type = _first_matching_action_type(text)
    if not action_type or action_type not in allowed_action_types:
        return 0.0
    score = 0.35
    target_key = _first_matching_target_key(text, valid_target_keys)
    if target_key:
        score += 0.25
    if any(token in text.lower() for token in ("owner", "assign", "will ", "i will", "we will", "by ")):
        score += 0.2
    if any(token in text.lower() for token in ("timeline", "deadline", "next step", "this week", "today", "tomorrow")):
        score += 0.1
    if any(token in text.lower() for token in ("update", "evidence", "pilot", "scope", "autonomy", "resource")):
        score += 0.1
    return clip_unit(score)


def heuristic_state_consistency_score(
    text: str,
    action_type: str | None,
    target_key: str | None,
    global_state: dict[str, float],
    phase_name: str,
) -> float:
    if not action_type or not target_key:
        return 0.45
    current = float(global_state.get(target_key, 0.5))
    positive_alignment = {
        "assign_owner": ("execution_confidence", "alignment", "integration_clarity", "admin_feasibility"),
        "request_evidence": ("uncertainty", "risk", "spillover_risk"),
        "publish_update": ("trust", "message_alignment", "alignment"),
        "narrow_scope": ("risk", "incident_risk", "spillover_risk"),
        "pilot": ("uncertainty", "risk", "launch_readiness"),
        "commit_resource": ("execution_confidence", "launch_readiness", "integration_clarity"),
        "defer_decision": ("uncertainty", "risk"),
        "preserve_autonomy": ("autonomy_confidence", "trust", "retention_risk"),
    }
    preferred_targets = positive_alignment.get(action_type, ())
    score = 0.5
    if target_key in preferred_targets:
        score += 0.2
    if action_type in {"request_evidence", "narrow_scope", "defer_decision"} and current >= 0.55:
        score += 0.2
    if action_type in {"assign_owner", "publish_update", "commit_resource"} and current <= 0.55:
        score += 0.2
    if phase_name == "CLOSING" and action_type in {"assign_owner", "publish_update"}:
        score += 0.05
    return clip_unit(score)


async def compile_action_proposal(
    client: SupportsGenerate | Any,
    *,
    script,
    actor_id: str,
    actor_name_map: dict[str, str],
    phase_name: str,
    turn_index: int,
    selected_text: str,
    policy_plan: dict[str, Any] | None,
    actor_snapshot: dict[str, Any] | None,
    planned_action_artifact: dict[str, Any] | None = None,
    seed_action_hint: dict[str, Any] | None = None,
) -> ActionProposal | None:
    allowed_action_types = list(script.allowed_action_types_for_phase(phase_name))
    valid_target_keys = list(script.target_keys_for_phase(phase_name))
    normalized_plan = normalize_planned_action_artifact(
        script=script,
        actor_id=actor_id,
        phase_name=phase_name,
        policy_plan=policy_plan or {},
        planned_action_artifact=planned_action_artifact,
        valid_target_keys=valid_target_keys,
        allowed_action_types=allowed_action_types,
    )
    proposal_id = f"{script.simulation_id}:{actor_id}:{phase_name}:{turn_index}"
    if normalized_plan:
        plan_payload = normalized_plan.to_dict()
        owner_actor_id = normalized_plan.owner_actor_id
        if not owner_actor_id and seed_action_hint and seed_action_hint.get("owner_actor_id") in script.actor_ids:
            owner_actor_id = seed_action_hint.get("owner_actor_id")
        target_actor_id = normalized_plan.target_actor_id
        if not target_actor_id and seed_action_hint and seed_action_hint.get("target_actor_id") in script.actor_ids:
            target_actor_id = seed_action_hint.get("target_actor_id")
        planned = ActionProposal(
            proposal_id=proposal_id,
            actor_id=actor_id,
            phase_name=phase_name,
            turn_index=turn_index,
            action_type=normalized_plan.action_type,
            target_key=normalized_plan.target_key,
            target_actor_id=target_actor_id,
            owner_actor_id=owner_actor_id,
            deadline_phase=normalized_plan.deadline_phase,
            strength=normalized_plan.strength,
            confidence=normalized_plan.confidence,
            evidence_text=selected_text[:160],
            status="proposed",
            action_bearing=True,
            compiler_source="planned_action",
            raw_payload={
                "planned_action_artifact": plan_payload,
                "selected_action_hint": dict(seed_action_hint or {}),
                "policy_action_intent": (policy_plan or {}).get("action_intent"),
                "policy_target_state_key": (policy_plan or {}).get("target_state_key"),
            },
        )
        planned = validate_action_proposal(
            script,
            planned,
            phase_name=phase_name,
            valid_target_keys=valid_target_keys,
            allowed_action_types=allowed_action_types,
        )
        if planned and planned.status == "proposed":
            return planned
    if seed_action_hint:
        seeded = ActionProposal(
            proposal_id=proposal_id,
            actor_id=actor_id,
            phase_name=phase_name,
            turn_index=turn_index,
            action_type=seed_action_hint.get("action_type"),
            target_key=seed_action_hint.get("target_key"),
            target_actor_id=seed_action_hint.get("target_actor_id"),
            owner_actor_id=seed_action_hint.get("owner_actor_id"),
            deadline_phase=seed_action_hint.get("deadline_phase"),
            strength=(seed_action_hint.get("strength") or "medium"),
            confidence=float(seed_action_hint.get("confidence") or 0.0),
            evidence_text=seed_action_hint.get("evidence_text") or selected_text[:160],
            status="proposed",
            action_bearing=bool(seed_action_hint.get("action_bearing", True)),
            compiler_source="selection_hint",
            raw_payload={
                **dict(seed_action_hint),
                "planned_action_artifact": normalized_plan.to_dict() if normalized_plan else {},
                "policy_action_intent": (policy_plan or {}).get("action_intent"),
                "policy_target_state_key": (policy_plan or {}).get("target_state_key"),
            },
        )
        seeded = validate_action_proposal(
            script,
            seeded,
            phase_name=phase_name,
            valid_target_keys=valid_target_keys,
            allowed_action_types=allowed_action_types,
        )
        if seeded and seeded.status == "proposed":
            return seeded
    heuristic = heuristic_action_proposal(
        script=script,
        actor_id=actor_id,
        actor_name_map=actor_name_map,
        phase_name=phase_name,
        turn_index=turn_index,
        selected_text=selected_text,
        policy_plan=policy_plan or {},
        planned_action_artifact=normalized_plan.to_dict() if normalized_plan else None,
        valid_target_keys=valid_target_keys,
        allowed_action_types=allowed_action_types,
    )
    if heuristic and heuristic.status == "proposed":
        return heuristic
    if not detect_action_bearing_turn(selected_text):
        return None
    if not hasattr(client, "generate"):
        return heuristic

    phase_names = ", ".join(phase.name for phase in script.phases)
    actor_snapshot = actor_snapshot or {}
    prompt = (
        "Extract one structured action proposal from the utterance.\n"
        f"Allowed action types: {', '.join(allowed_action_types)}\n"
        f"Allowed target keys: {', '.join(valid_target_keys)}\n"
        f"Allowed actor ids: {', '.join(script.actor_ids)}\n"
        f"Allowed deadline phases: {phase_names}\n"
        f"Policy plan: {json.dumps(policy_plan or {}, ensure_ascii=True)}\n"
        f"Actor snapshot goals: {json.dumps(actor_snapshot.get('actor_state', {}).get('goals', []), ensure_ascii=True)}\n"
        f"Utterance: {selected_text}\n\n"
        "Return JSON only with fields: action_type, target_key, target_actor_id, owner_actor_id, deadline_phase, "
        "strength, confidence, evidence_text. Use null when unknown."
    )
    try:
        raw = await client.generate(
            prompt=prompt,
            system_instruction="Return JSON only. No explanation.",
            temperature=0.0,
            max_tokens=220,
        )
        payload = parse_json_payload(raw)
        proposal = ActionProposal(
            proposal_id=proposal_id,
            actor_id=actor_id,
            phase_name=phase_name,
            turn_index=turn_index,
            action_type=payload.get("action_type"),
            target_key=payload.get("target_key"),
            target_actor_id=payload.get("target_actor_id"),
            owner_actor_id=payload.get("owner_actor_id"),
            deadline_phase=payload.get("deadline_phase"),
            strength=(payload.get("strength") or "medium"),
            confidence=float(payload.get("confidence") or 0.0),
            evidence_text=payload.get("evidence_text") or selected_text[:160],
            status="proposed",
            action_bearing=True,
            compiler_source="llm",
            raw_payload={
                **payload,
                "planned_action_artifact": normalized_plan.to_dict() if normalized_plan else {},
                "selected_action_hint": dict(seed_action_hint or {}),
                "policy_action_intent": (policy_plan or {}).get("action_intent"),
                "policy_target_state_key": (policy_plan or {}).get("target_state_key"),
            },
        )
        return validate_action_proposal(
            script,
            proposal,
            phase_name=phase_name,
            valid_target_keys=valid_target_keys,
            allowed_action_types=allowed_action_types,
        )
    except Exception:
        return heuristic


def parse_json_payload(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if "{" in stripped and "}" in stripped:
        stripped = stripped[stripped.find("{"):stripped.rfind("}") + 1]
    payload = json.loads(stripped)
    if not isinstance(payload, dict):
        raise ValueError("payload is not a JSON object")
    return payload


def heuristic_action_proposal(
    *,
    script,
    actor_id: str,
    actor_name_map: dict[str, str],
    phase_name: str,
    turn_index: int,
    selected_text: str,
    policy_plan: dict[str, Any],
    planned_action_artifact: dict[str, Any] | None = None,
    valid_target_keys: list[str] | None = None,
    allowed_action_types: list[str] | None = None,
) -> ActionProposal | None:
    action_bearing = detect_action_bearing_turn(selected_text)
    if not action_bearing:
        return None
    valid_target_keys = list(valid_target_keys or script.world_state_schema)
    allowed_action_types = list(allowed_action_types or script.allowed_action_types)
    action_type = _first_matching_action_type(selected_text)
    if not action_type:
        action_type = _fallback_action_from_policy_plan(
            planned_action_artifact or policy_plan,
            allowed_action_types,
        )
    elif action_type not in allowed_action_types:
        action_type = _fallback_action_from_policy_plan(
            planned_action_artifact or policy_plan,
            allowed_action_types,
        )
    target_key = (
        policy_plan.get("target_state_key")
        if policy_plan.get("target_state_key") in valid_target_keys
        else _first_matching_target_key(selected_text, valid_target_keys)
    )
    target_actor_id = _first_matching_actor(selected_text, actor_name_map)
    proposal = ActionProposal(
        proposal_id=f"{script.simulation_id}:{actor_id}:{phase_name}:{turn_index}",
        actor_id=actor_id,
        phase_name=phase_name,
        turn_index=turn_index,
        action_type=action_type,
        target_key=target_key,
        target_actor_id=target_actor_id if target_actor_id != actor_id else None,
        owner_actor_id=actor_id if action_type in {"assign_owner", "commit_resource", "publish_update"} else None,
        deadline_phase=policy_plan.get("deadline_phase"),
        strength=_detect_strength(selected_text),
        confidence=_detect_confidence(selected_text),
        evidence_text=selected_text[:160],
        status="proposed",
        action_bearing=True,
        compiler_source="heuristic",
        raw_payload={
            "policy_action_intent": policy_plan.get("action_intent"),
            "policy_target_state_key": policy_plan.get("target_state_key"),
            "planned_action_artifact": dict(planned_action_artifact or {}),
        },
    )
    return validate_action_proposal(
        script,
        proposal,
        phase_name=phase_name,
        valid_target_keys=valid_target_keys,
        allowed_action_types=allowed_action_types,
    )


def _fallback_action_from_policy_plan(policy_plan: dict[str, Any], allowed_action_types: list[str]) -> str | None:
    action_intent = (
        policy_plan.get("action_type")
        or policy_plan.get("action_intent")
        or policy_plan.get("planned_action", {}).get("action_type")
        or policy_plan.get("planned_action_artifact", {}).get("action_type")
        or ""
    ).lower()
    mapping = {
        "assign_owner": "assign_owner",
        "evidence": "request_evidence",
        "update": "publish_update",
        "scope": "narrow_scope",
        "pilot": "pilot",
        "resource": "commit_resource",
        "defer": "defer_decision",
        "autonomy": "preserve_autonomy",
    }
    for token, action_type in mapping.items():
        if token in action_intent and action_type in allowed_action_types:
            return action_type
    return None


def normalize_planned_action_artifact(
    *,
    script,
    actor_id: str,
    phase_name: str,
    policy_plan: dict[str, Any],
    planned_action_artifact: dict[str, Any] | None,
    valid_target_keys: list[str],
    allowed_action_types: list[str],
) -> PlannedActionArtifact | None:
    source = dict(planned_action_artifact or policy_plan.get("action_plan") or {})
    action_type = source.get("action_type") or policy_plan.get("action_intent")
    target_key = source.get("target_key") or policy_plan.get("target_state_key")
    if action_type not in allowed_action_types or target_key not in valid_target_keys:
        return None
    owner_actor_id = source.get("owner_actor_id")
    if not owner_actor_id and action_type in {"assign_owner", "publish_update", "commit_resource"}:
        owner_actor_id = actor_id
    strength = commitment_strength_to_band(
        source.get("strength") or policy_plan.get("commitment_strength")
    )
    confidence = float(
        source.get("confidence")
        if source.get("confidence") is not None
        else commitment_strength_to_confidence(policy_plan.get("commitment_strength"))
    )
    return PlannedActionArtifact(
        action_type=action_type,
        target_key=target_key,
        target_actor_id=source.get("target_actor_id"),
        owner_actor_id=owner_actor_id,
        deadline_phase=source.get("deadline_phase") or policy_plan.get("deadline_phase") or phase_name,
        strength=strength,
        confidence=clip_unit(confidence),
        expected_state_effect=source.get("expected_state_effect") or policy_plan.get("expected_state_effect"),
        rationale=source.get("rationale")
        or f"{policy_plan.get('stance', 'unknown')}:{policy_plan.get('goal_mode', 'unknown')}",
        source=source.get("source", "policy_plan"),
    )


def action_plan_alignment_score(
    planned_action: dict[str, Any] | None,
    candidate_action: dict[str, Any] | None,
) -> tuple[float, dict[str, Any]]:
    if not planned_action:
        return 0.5, {"available": False, "reason": "no_planned_action"}
    if not candidate_action:
        return 0.25, {"available": True, "reason": "no_candidate_action"}

    score = 0.2
    details = {
        "planned_action_type": planned_action.get("action_type"),
        "candidate_action_type": candidate_action.get("action_type"),
        "planned_target_key": planned_action.get("target_key"),
        "candidate_target_key": candidate_action.get("target_key"),
    }
    if planned_action.get("action_type") == candidate_action.get("action_type"):
        score += 0.45
    if planned_action.get("target_key") == candidate_action.get("target_key"):
        score += 0.25
    planned_owner = planned_action.get("owner_actor_id")
    candidate_owner = candidate_action.get("owner_actor_id")
    if planned_owner and candidate_owner and planned_owner == candidate_owner:
        score += 0.1
    planned_deadline = planned_action.get("deadline_phase")
    candidate_deadline = candidate_action.get("deadline_phase")
    if planned_deadline and candidate_deadline and planned_deadline == candidate_deadline:
        score += 0.05
    return clip_unit(score), details


def validate_action_proposal(
    script,
    proposal: ActionProposal | None,
    *,
    phase_name: str | None = None,
    valid_target_keys: list[str] | None = None,
    allowed_action_types: list[str] | None = None,
) -> ActionProposal | None:
    if proposal is None:
        return None
    if not proposal.action_bearing:
        return None
    phase_name = phase_name or proposal.phase_name
    valid_target_keys = list(valid_target_keys or script.target_keys_for_phase(phase_name))
    allowed_action_types = list(allowed_action_types or script.allowed_action_types_for_phase(phase_name))
    proposal.validation_trace = list(proposal.validation_trace)

    if proposal.action_type not in allowed_action_types:
        repaired = _fallback_action_from_policy_plan(proposal.raw_payload, allowed_action_types)
        if repaired:
            proposal.action_type = repaired
            proposal.validation_trace.append("repaired_action_type_from_fallback")
    if proposal.action_type not in allowed_action_types:
        proposal.status = "rejected"
        proposal.rejection_reason = "invalid_action_type"
        return proposal
    if proposal.target_key not in valid_target_keys:
        policy_target = proposal.raw_payload.get("policy_target_state_key") if proposal.raw_payload else None
        if policy_target in valid_target_keys:
            proposal.target_key = policy_target
            proposal.validation_trace.append("repaired_target_from_policy")
        elif len(valid_target_keys) == 1:
            proposal.target_key = valid_target_keys[0]
            proposal.validation_trace.append("repaired_target_single_phase_key")
    if proposal.target_key not in valid_target_keys:
        proposal.status = "rejected"
        proposal.rejection_reason = "invalid_target_key"
        return proposal
    if proposal.owner_actor_id and proposal.owner_actor_id not in script.actor_ids:
        proposal.status = "rejected"
        proposal.rejection_reason = "invalid_owner_actor"
        return proposal
    if not proposal.owner_actor_id and proposal.action_type in {"assign_owner", "publish_update", "commit_resource"}:
        proposal.owner_actor_id = proposal.actor_id
        proposal.validation_trace.append("repaired_owner_from_actor")
    if proposal.target_actor_id and proposal.target_actor_id not in script.actor_ids:
        proposal.status = "rejected"
        proposal.rejection_reason = "invalid_target_actor"
        return proposal
    if proposal.deadline_phase and proposal.deadline_phase not in {phase.name for phase in script.phases}:
        proposal.status = "rejected"
        proposal.rejection_reason = "invalid_deadline_phase"
        return proposal
    if proposal.strength not in DELTA_PALETTE:
        proposal.strength = "medium"
    proposal.confidence = clip_unit(proposal.confidence)
    proposal.status = "proposed"
    proposal.rejection_reason = None
    return proposal


def arbitrate_phase_actions(script, phase_name: str, proposals: list[ActionProposal]) -> tuple[list[ActionProposal], list[ActionProposal]]:
    if not proposals:
        return [], []
    candidates = [proposal for proposal in proposals if proposal.status == "proposed"]
    rejected: list[ActionProposal] = []
    deduped: dict[tuple[str, str], ActionProposal] = {}

    for proposal in sorted(candidates, key=lambda row: row.turn_index):
        key = (proposal.actor_id, action_family(proposal.action_type))
        existing = deduped.get(key)
        if existing is None or proposal.turn_index >= existing.turn_index:
            if existing is not None:
                existing.status = "rejected"
                existing.rejection_reason = "superseded_by_later_same_family"
                rejected.append(existing)
            deduped[key] = proposal
        else:
            proposal.status = "rejected"
            proposal.rejection_reason = "superseded_by_later_same_family"
            rejected.append(proposal)

    approved: list[ActionProposal] = []
    phase_rows = sorted(deduped.values(), key=lambda row: row.turn_index)
    consumed: set[str] = set()
    for proposal in phase_rows:
        if proposal.proposal_id in consumed:
            continue
        conflicting = [
            other
            for other in phase_rows
            if other.proposal_id != proposal.proposal_id and other.proposal_id not in consumed and _actions_conflict(proposal, other)
        ]
        if not conflicting:
            proposal.status = "approved"
            approved.append(proposal)
            consumed.add(proposal.proposal_id)
            continue

        ordered = sorted([proposal, *conflicting], key=_proposal_priority_key, reverse=True)
        winner = ordered[0]
        winner.status = "approved"
        approved.append(winner)
        consumed.add(winner.proposal_id)
        for loser in ordered[1:]:
            loser.status = "rejected"
            loser.rejection_reason = "conflict"
            rejected.append(loser)
            consumed.add(loser.proposal_id)

    for proposal in approved:
        proposal.rejection_reason = None
    return approved, rejected


def _actions_conflict(left: ActionProposal, right: ActionProposal) -> bool:
    if left.phase_name != right.phase_name:
        return False
    same_target = left.target_key == right.target_key and left.target_actor_id == right.target_actor_id
    if not same_target:
        return False
    if left.actor_id == right.actor_id:
        return action_family(left.action_type) != action_family(right.action_type)
    contradictory_pairs = {
        frozenset({"assign_owner", "preserve_autonomy"}),
        frozenset({"narrow_scope", "commit_resource"}),
        frozenset({"defer_decision", "assign_owner"}),
    }
    return frozenset({left.action_type, right.action_type}) in contradictory_pairs


def _proposal_priority_key(proposal: ActionProposal) -> tuple[int, float, int]:
    explicit_count = int(bool(proposal.owner_actor_id)) + int(bool(proposal.deadline_phase))
    return (explicit_count, proposal.confidence, proposal.turn_index)


def preconditions_satisfied(
    current_state: dict[str, float],
    preconditions: list[dict[str, Any]],
) -> bool:
    for condition in preconditions[:2]:
        key = condition.get("state_key")
        op = condition.get("op")
        value = float(condition.get("value", 0.0))
        observed = float(current_state.get(key, 0.0))
        if op == ">=" and observed < value:
            return False
        if op == "<=" and observed > value:
            return False
    return True


def apply_transition_rule(
    script,
    proposal: ActionProposal,
    current_snapshot: WorldStateSnapshot,
) -> tuple[ExecutedAction | None, WorldStateSnapshot | None, str | None]:
    rule = script.transition_rule_for(proposal.phase_name, proposal.action_type or "")
    if not rule:
        return None, None, "missing_transition_rule"
    if not preconditions_satisfied(current_snapshot.global_state, list(rule.get("preconditions", []))):
        return None, None, "precondition_failed"

    next_global_state = dict(current_snapshot.global_state)
    next_local_state = {
        actor_id: dict(local_state)
        for actor_id, local_state in current_snapshot.local_state_by_actor.items()
    }
    applied_delta: dict[str, float] = {}

    for state_key, delta in dict(rule.get("global_deltas", {})).items():
        next_global_state[state_key] = clip_unit(next_global_state.get(state_key, 0.5) + float(delta))
        applied_delta[state_key] = round(float(delta), 4)

    for state_key, delta in dict(rule.get("owner_local_deltas", {})).items():
        owner_actor_id = proposal.owner_actor_id or proposal.actor_id
        next_local_state.setdefault(owner_actor_id, {})
        next_local_state[owner_actor_id][state_key] = clip_unit(
            next_local_state[owner_actor_id].get(state_key, 0.5) + float(delta)
        )

    if proposal.target_actor_id:
        for state_key, delta in dict(rule.get("target_local_deltas", {})).items():
            next_local_state.setdefault(proposal.target_actor_id, {})
            next_local_state[proposal.target_actor_id][state_key] = clip_unit(
                next_local_state[proposal.target_actor_id].get(state_key, 0.5) + float(delta)
            )

    next_snapshot = WorldStateSnapshot(
        phase_name=proposal.phase_name,
        turn_index=proposal.turn_index,
        global_state=next_global_state,
        local_state_by_actor=next_local_state,
        executed_action_ids=list(current_snapshot.executed_action_ids) + [proposal.proposal_id],
    )
    executed = ExecutedAction(
        proposal_id=proposal.proposal_id,
        action_type=proposal.action_type or "unknown",
        phase_name=proposal.phase_name,
        owner_actor_id=proposal.owner_actor_id or proposal.actor_id,
        target_key=proposal.target_key or "",
        target_actor_id=proposal.target_actor_id,
        applied_delta=applied_delta,
        pre_state={
            "global_state": dict(current_snapshot.global_state),
            "local_state_by_actor": {
                actor_id: dict(local_state)
                for actor_id, local_state in current_snapshot.local_state_by_actor.items()
            },
        },
        post_state={
            "global_state": dict(next_snapshot.global_state),
            "local_state_by_actor": {
                actor_id: dict(local_state)
                for actor_id, local_state in next_snapshot.local_state_by_actor.items()
            },
        },
        coherence_score=1.0,
        contradiction_flag=False,
    )
    return executed, next_snapshot, None


def build_phase_feedback(
    world_state: WorldStateSnapshot,
    executed_actions: list[ExecutedAction],
    actor_id: str,
    max_actions: int = 2,
) -> dict[str, Any]:
    local_state = world_state.local_state_by_actor.get(actor_id, {})
    recent_actions = [
        action
        for action in executed_actions
        if action.owner_actor_id == actor_id or action.target_actor_id == actor_id
    ][:max_actions]
    global_keys = ("alignment", "uncertainty", "risk")
    global_line = ", ".join(
        f"{key} {world_state.global_state.get(key, 0.5):.2f}"
        for key in global_keys
        if key in world_state.global_state
    )
    local_line = ", ".join(
        f"{key} {local_state.get(key, 0.5):.2f}"
        for key in ("trust", "execution_confidence", "alignment")
        if key in local_state
    )
    action_line = ", ".join(
        f"{action.action_type}({action.target_key})"
        for action in recent_actions
    ) or "none"
    return {
        "world_state_line": f"world_state={global_line}",
        "local_state_line": f"your_local_state={local_line}",
        "last_actions_line": f"last_actions={action_line}",
        "recent_action_ids": [action.proposal_id for action in recent_actions],
    }
