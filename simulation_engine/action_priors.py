"""Role-conditioned action priors for action-conditioned simulation."""

from __future__ import annotations

from dataclasses import asdict, dataclass

from .action_layer import action_family

REDUCE_KEYS = {"risk", "incident_risk", "uncertainty", "spillover_risk", "retention_risk"}
INCREASE_KEYS = {
    "execution_confidence",
    "alignment",
    "launch_readiness",
    "message_alignment",
    "integration_clarity",
    "autonomy_confidence",
    "admin_feasibility",
    "trust",
}


def _dedupe_keep_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def _clip_unit(value: float) -> float:
    return max(0.0, min(1.0, round(float(value), 4)))


@dataclass
class RoleActionPrior:
    preferred_action_types: list[str]
    preferred_target_keys: list[str]
    primary_families: list[str]
    secondary_families: list[str]
    avoid_families: list[str]
    state_priority_keys: list[str]
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

    families = _dedupe_keep_order(
        action_family(item)
        for item in preferred_actions
    )
    primary = families[:2]
    secondary = families[2:4]
    included = set(primary + secondary)
    all_possible_families = _dedupe_keep_order(
        action_family(action) for action in allowed_action_types
    )
    computed_avoid = [f for f in all_possible_families if f not in included]
    return RoleActionPrior(
        preferred_action_types=preferred_actions,
        preferred_target_keys=preferred_targets,
        primary_families=primary,
        secondary_families=secondary,
        avoid_families=computed_avoid,
        state_priority_keys=preferred_targets[:3],
        rationale=rationale,
    )


def apply_actor_action_preferences(
    *,
    prior: RoleActionPrior,
    preferences: dict[str, object] | None,
    allowed_action_types: list[str],
    valid_target_keys: list[str],
) -> RoleActionPrior:
    if not preferences:
        return prior

    preferred_action_types = _dedupe_keep_order(
        [
            *[
                action
                for action in list(preferences.get("preferred_action_types", []))
                if action in allowed_action_types
            ],
            *prior.preferred_action_types,
        ]
    )
    preferred_target_keys = _dedupe_keep_order(
        [
            *[
                key
                for key in list(preferences.get("preferred_target_keys", []))
                if key in valid_target_keys
            ],
            *prior.preferred_target_keys,
        ]
    )
    primary_families = _dedupe_keep_order(
        list(preferences.get("primary_families", [])) + prior.primary_families
    )
    secondary_families = _dedupe_keep_order(
        list(preferences.get("secondary_families", [])) + prior.secondary_families
    )
    avoid_families = _dedupe_keep_order(
        list(preferences.get("avoid_families", [])) + prior.avoid_families
    )
    state_priority_keys = _dedupe_keep_order(
        [
            *[
                key
                for key in list(preferences.get("state_priority_keys", []))
                if key in valid_target_keys
            ],
            *prior.state_priority_keys,
        ]
    )

    rationale = list(prior.rationale)
    if preferences:
        rationale.append("metadata:actor_action_preferences")

    return RoleActionPrior(
        preferred_action_types=preferred_action_types,
        preferred_target_keys=preferred_target_keys,
        primary_families=primary_families,
        secondary_families=secondary_families,
        avoid_families=avoid_families,
        state_priority_keys=state_priority_keys,
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
            "primary_families": prior.primary_families,
            "secondary_families": prior.secondary_families,
            "avoid_families": prior.avoid_families,
            "state_priority_keys": prior.state_priority_keys,
        }

    score = 0.2
    family = action_family(action_type)
    if action_type in prior.preferred_action_types[:1]:
        score += 0.45
    elif action_type in prior.preferred_action_types[:3]:
        score += 0.3
    elif action_type in prior.preferred_action_types:
        score += 0.15

    if family in prior.primary_families:
        score += 0.18
    elif family in prior.secondary_families:
        score += 0.1
    elif family in prior.avoid_families:
        score -= 0.18

    if target_key in prior.preferred_target_keys[:2]:
        score += 0.25
    elif target_key in prior.preferred_target_keys:
        score += 0.12

    if target_key in prior.state_priority_keys[:2]:
        score += 0.14
    elif target_key in prior.state_priority_keys:
        score += 0.08

    return min(1.0, round(score, 4)), {
        "available": True,
        "preferred_action_types": prior.preferred_action_types,
        "preferred_target_keys": prior.preferred_target_keys,
        "primary_families": prior.primary_families,
        "secondary_families": prior.secondary_families,
        "avoid_families": prior.avoid_families,
        "state_priority_keys": prior.state_priority_keys,
        "rationale": prior.rationale,
    }


def action_activation_score(
    *,
    action_type: str | None,
    target_key: str | None,
    prior: RoleActionPrior,
    phase_action_policy: dict[str, object] | None,
    phase_action_family_counts: dict[str, int] | None,
    local_state: dict[str, float] | None,
    global_state: dict[str, float] | None,
) -> tuple[float, dict[str, object]]:
    if not action_type or not target_key:
        return 0.0, {"available": False, "reason": "missing_action_or_target"}

    role_fit, role_fit_details = action_role_fit_score(
        action_type=action_type,
        target_key=target_key,
        prior=prior,
    )
    policy = dict(phase_action_policy or {})
    family_counts = dict(phase_action_family_counts or {})
    family = action_family(action_type)
    duplicates = int(family_counts.get(family, 0))
    family_cap = int(policy.get("family_cap", 2))
    max_actions_per_phase = int(policy.get("max_actions_per_phase", 3))
    total_actions = int(sum(family_counts.values()))
    state_value = float((local_state or {}).get(target_key, (global_state or {}).get(target_key, 0.5)))

    score = 0.18 + 0.42 * role_fit
    if family in prior.primary_families:
        score += 0.12
    elif family in prior.secondary_families:
        score += 0.06
    if family in prior.avoid_families:
        score -= 0.20

    if target_key in prior.state_priority_keys[:2]:
        score += 0.12
    elif target_key in prior.state_priority_keys:
        score += 0.06

    if target_key in REDUCE_KEYS and state_value >= 0.55:
        score += 0.14
    elif target_key in INCREASE_KEYS and state_value <= 0.55:
        score += 0.14

    if duplicates >= family_cap:
        score -= 0.30 if family not in prior.primary_families else 0.12
    if total_actions >= max_actions_per_phase:
        score -= 0.24 if family not in prior.primary_families else 0.10

    return _clip_unit(score), {
        "available": True,
        "family": family,
        "duplicates": duplicates,
        "family_cap": family_cap,
        "total_actions": total_actions,
        "max_actions_per_phase": max_actions_per_phase,
        "state_value": round(state_value, 4),
        "role_fit": role_fit,
        "role_fit_details": role_fit_details,
    }
