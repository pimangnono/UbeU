"""Role-conditioned action priors for action-conditioned simulation."""

from __future__ import annotations

from dataclasses import asdict, dataclass


def _dedupe_keep_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


@dataclass
class RoleActionPrior:
    preferred_action_types: list[str]
    preferred_target_keys: list[str]
    rationale: list[str]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def infer_role_action_prior(
    *,
    role: str,
    incentives: list[str],
    concerns: list[str],
    phase_name: str,
    phase_cues: list[str] | None,
    allowed_action_types: list[str],
    valid_target_keys: list[str],
) -> RoleActionPrior:
    lowered = " ".join([role, *incentives, *concerns]).lower()
    cues = " ".join(phase_cues or []).lower()

    actions: list[str] = []
    targets: list[str] = []
    rationale: list[str] = []

    phase_defaults = {
        "OPENING": (["publish_update", "request_evidence"], ["alignment", "trust", "uncertainty"]),
        "TENSION": (["request_evidence", "pilot", "narrow_scope", "preserve_autonomy"], ["risk", "uncertainty"]),
        "NEGOTIATION": (["assign_owner", "narrow_scope", "pilot", "commit_resource"], ["execution_confidence", "alignment"]),
        "CLOSING": (["assign_owner", "publish_update", "defer_decision", "preserve_autonomy"], ["execution_confidence", "trust", "alignment"]),
    }
    default_actions, default_targets = phase_defaults.get(phase_name, ([], []))
    actions.extend(default_actions)
    targets.extend(default_targets)
    rationale.append(f"phase:{phase_name.lower()}")

    if any(token in lowered for token in ("marketing", "brand", "communications", "comms", "pr", "narrative")):
        actions = ["publish_update", "pilot", *actions]
        targets = ["message_alignment", "alignment", "trust", *targets]
        rationale.append("role:communication")

    if any(token in lowered for token in ("operations", "reliability", "risk", "legal", "compliance", "finance", "administrator", "admin")):
        actions = ["request_evidence", "pilot", "narrow_scope", *actions]
        targets = ["risk", "incident_risk", "uncertainty", "admin_feasibility", "spillover_risk", *targets]
        rationale.append("role:risk_ops")

    if any(token in lowered for token in ("product", "strategy", "coordinator", "integration", "policy coordinator", "people")):
        actions = ["assign_owner", "commit_resource", "publish_update", *actions]
        targets = ["execution_confidence", "integration_clarity", "launch_readiness", "alignment", *targets]
        rationale.append("role:coordination")

    if any(token in lowered for token in ("founder", "owner", "merchant", "worker", "commuter", "affected", "resident", "tenant")):
        actions = ["preserve_autonomy", "request_evidence", "publish_update", *actions]
        targets = ["autonomy_confidence", "trust", "spillover_risk", "uncertainty", *targets]
        rationale.append("role:protective")

    if "owner" in cues or "sequencing" in cues or "coordination" in cues:
        actions = ["assign_owner", *actions]
        targets = ["execution_confidence", *targets]
        rationale.append("cue:owner_coordination")
    if "scope" in cues or "mitigation" in cues or "fallback" in cues:
        actions = ["narrow_scope", "pilot", *actions]
        targets = ["risk", "launch_readiness", "spillover_risk", *targets]
        rationale.append("cue:mitigation")
    if "autonomy" in cues:
        actions = ["preserve_autonomy", *actions]
        targets = ["autonomy_confidence", "trust", *targets]
        rationale.append("cue:autonomy")
    if "evidence" in cues or "uncertainty" in cues:
        actions = ["request_evidence", *actions]
        targets = ["uncertainty", "risk", *targets]
        rationale.append("cue:evidence")

    preferred_actions = [
        action for action in _dedupe_keep_order(actions)
        if action in allowed_action_types
    ]
    preferred_targets = [
        target for target in _dedupe_keep_order(targets)
        if target in valid_target_keys
    ]

    return RoleActionPrior(
        preferred_action_types=preferred_actions,
        preferred_target_keys=preferred_targets,
        rationale=rationale,
    )


def action_role_fit_score(
    *,
    action_type: str | None,
    target_key: str | None,
    prior: RoleActionPrior,
) -> tuple[float, dict[str, object]]:
    if not prior.preferred_action_types and not prior.preferred_target_keys:
        return 0.5, {"available": False, "reason": "no_role_prior"}
    if not action_type and not target_key:
        return 0.5, {
            "available": True,
            "reason": "no_action",
            "preferred_action_types": prior.preferred_action_types,
            "preferred_target_keys": prior.preferred_target_keys,
        }

    score = 0.2
    if action_type in prior.preferred_action_types[:1]:
        score += 0.45
    elif action_type in prior.preferred_action_types[:3]:
        score += 0.3
    elif action_type in prior.preferred_action_types:
        score += 0.15

    if target_key in prior.preferred_target_keys[:2]:
        score += 0.25
    elif target_key in prior.preferred_target_keys:
        score += 0.12

    return min(1.0, round(score, 4)), {
        "available": True,
        "preferred_action_types": prior.preferred_action_types,
        "preferred_target_keys": prior.preferred_target_keys,
        "rationale": prior.rationale,
    }
