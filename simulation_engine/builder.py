"""Deterministic builder enrichment for brief-to-simulation generation."""

from __future__ import annotations

import copy
import re
from dataclasses import asdict, dataclass
from typing import Any

from .action_layer import ACTION_TYPES, ACTION_FAMILIES
from .script import DEFAULT_GLOBAL_WORLD_STATE_KEYS, SimulationScript, normalize_personality_vector

REQUIRED_SCRIPT_FIELDS = (
    "scenario_family",
    "world_state_schema",
    "initial_world_state",
    "allowed_action_types",
    "transition_rules",
    "state_visibility_rules",
    "metadata.phase_action_policies",
    "metadata.actor_action_preferences",
)

DEFAULT_PHASES = [
    {"name": "OPENING", "goal": "Surface the direct objective and each stakeholder's first-order view.", "style": "neutral", "max_turns": 3, "cues": ["direct_impact", "goal_clarity"]},
    {"name": "TENSION", "goal": "Expose risks, tradeoffs, or conflicting incentives.", "style": "disagreement", "max_turns": 3, "cues": ["risk", "tradeoff", "constraint"]},
    {"name": "NEGOTIATION", "goal": "Search for bounded compromises or concrete mitigations.", "style": "consensus", "max_turns": 3, "cues": ["mitigation", "ownership", "coordination"]},
    {"name": "CLOSING", "goal": "Summarize commitments, unresolved issues, and owners.", "style": "neutral", "max_turns": 2, "cues": ["summary", "commitment", "follow_up"]},
]

FAMILY_SPECS: dict[str, dict[str, Any]] = {
    "policy_spillover": {
        "world_state_schema": [
            "alignment",
            "trust",
            "uncertainty",
            "execution_confidence",
            "risk",
            "admin_feasibility",
            "spillover_risk",
        ],
        "initial_world_state": {
            "alignment": 0.48,
            "trust": 0.50,
            "uncertainty": 0.56,
            "execution_confidence": 0.44,
            "risk": 0.52,
            "admin_feasibility": 0.46,
            "spillover_risk": 0.54,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "pilot",
            "defer_decision",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "uncertainty", "risk"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "outcome_spec": {
            "fixed_ending": True,
            "target_end_state": {
                "alignment": "increase",
                "uncertainty": "decrease",
                "execution_confidence": "increase",
            },
            "evaluation_focus": ["persona_stability", "action_coherence", "spillover_control"],
        },
    },
    "launch_pressure": {
        "world_state_schema": [
            "alignment",
            "trust",
            "uncertainty",
            "execution_confidence",
            "risk",
            "launch_readiness",
            "message_alignment",
            "incident_risk",
        ],
        "initial_world_state": {
            "alignment": 0.46,
            "trust": 0.51,
            "uncertainty": 0.55,
            "execution_confidence": 0.45,
            "risk": 0.56,
            "launch_readiness": 0.47,
            "message_alignment": 0.50,
            "incident_risk": 0.58,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "pilot",
            "commit_resource",
            "defer_decision",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "uncertainty", "risk", "launch_readiness"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "outcome_spec": {
            "fixed_ending": True,
            "target_end_state": {
                "execution_confidence": "increase",
                "launch_readiness": "increase",
                "incident_risk": "decrease",
            },
            "evaluation_focus": ["action_coherence", "persona_stability", "owner_clarity"],
        },
    },
    "integration_trust": {
        "world_state_schema": [
            "alignment",
            "trust",
            "uncertainty",
            "execution_confidence",
            "risk",
            "retention_risk",
            "autonomy_confidence",
            "integration_clarity",
        ],
        "initial_world_state": {
            "alignment": 0.43,
            "trust": 0.47,
            "uncertainty": 0.58,
            "execution_confidence": 0.42,
            "risk": 0.55,
            "retention_risk": 0.59,
            "autonomy_confidence": 0.44,
            "integration_clarity": 0.40,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "pilot",
            "defer_decision",
            "preserve_autonomy",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "trust", "uncertainty", "retention_risk"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "outcome_spec": {
            "fixed_ending": True,
            "target_end_state": {
                "integration_clarity": "increase",
                "retention_risk": "decrease",
                "trust": "increase",
            },
            "evaluation_focus": ["trust_preservation", "persona_stability", "coordination_clarity"],
        },
    },
    "brand_crisis": {
        "world_state_schema": [
            "alignment",
            "trust",
            "uncertainty",
            "execution_confidence",
            "risk",
            "reputation_stability",
            "legal_exposure",
        ],
        "initial_world_state": {
            "alignment": 0.42,
            "trust": 0.46,
            "uncertainty": 0.61,
            "execution_confidence": 0.40,
            "risk": 0.62,
            "reputation_stability": 0.34,
            "legal_exposure": 0.57,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "defer_decision",
            "commit_resource",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "trust", "uncertainty", "risk", "reputation_stability"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "outcome_spec": {
            "fixed_ending": False,
            "target_end_state": {},
            "evaluation_focus": ["trajectory_diversity", "persona_stability", "conflict_map"],
        },
    },
    "resource_scarcity": {
        "world_state_schema": [
            "alignment",
            "trust",
            "uncertainty",
            "execution_confidence",
            "risk",
            "budget_health",
            "delivery_capacity",
            "customer_risk",
        ],
        "initial_world_state": {
            "alignment": 0.45,
            "trust": 0.49,
            "uncertainty": 0.57,
            "execution_confidence": 0.43,
            "risk": 0.58,
            "budget_health": 0.38,
            "delivery_capacity": 0.47,
            "customer_risk": 0.55,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "commit_resource",
            "defer_decision",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "uncertainty", "risk", "budget_health", "customer_risk"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "outcome_spec": {
            "fixed_ending": False,
            "target_end_state": {},
            "evaluation_focus": ["trajectory_diversity", "persona_stability", "resource_tradeoffs"],
        },
    },
}

GENERIC_SPEC = {
    "world_state_schema": list(DEFAULT_GLOBAL_WORLD_STATE_KEYS),
    "initial_world_state": {key: 0.5 for key in DEFAULT_GLOBAL_WORLD_STATE_KEYS},
    "allowed_action_types": list(ACTION_TYPES),
    "state_visibility_rules": {
        "global_keys": ["alignment", "uncertainty", "risk"],
        "local_keys": ["trust", "execution_confidence", "alignment"],
        "max_recent_actions": 2,
    },
    "outcome_spec": {
        "fixed_ending": True,
        "target_end_state": {"alignment": "increase", "uncertainty": "decrease"},
        "evaluation_focus": ["persona_stability", "action_coherence"],
    },
}


def infer_scenario_family(brief: str, stakeholders: list[dict[str, Any]], title: str = "") -> str:
    lowered = " ".join(
        [
            title or "",
            brief or "",
            " ".join(str(actor.get("role", "")) for actor in stakeholders),
            " ".join(" ".join(actor.get("concerns", []) or []) for actor in stakeholders),
        ]
    ).lower()
    if any(token in lowered for token in ("policy", "hospital", "adopt", "subsidy", "regulation", "public", "consent", "diagnostics")):
        return "policy_spillover"
    if any(token in lowered for token in ("launch", "release", "go to market", "ship", "marketing", "readiness")):
        return "launch_pressure"
    if any(token in lowered for token in ("merger", "integration", "autonomy", "retention", "operating model")):
        return "integration_trust"
    if any(token in lowered for token in ("crisis", "backlash", "incident", "pr", "liability", "brand", "legal exposure")):
        return "brand_crisis"
    if any(token in lowered for token in ("budget", "resource", "capacity", "headcount", "staffing", "downtime")):
        return "resource_scarcity"
    if any(token in lowered for token in ("migration",)):
        return "resource_scarcity"
    return "generic"


@dataclass
class StructuralProfile:
    polarity: str          # "adversarial" | "fragmented" | "collaborative"
    pressure: str          # "high" | "medium" | "low"
    initial_tension: float # 0.05 - 0.25
    sycophancy_threshold: float  # 0.40 - 0.55 (lower = stricter)
    trust_decay_boost: float     # 1.0 - 1.5 (multiplier on negative trust deltas)
    tension_floor_base: float    # 0.0 - 0.15


def infer_structural_profile(stakeholders: list[dict], phases: list[dict]) -> StructuralProfile:
    """Classify scenario structure from stakeholder incentive/concern conflict."""
    # 1. Polarity: count pairwise incentive-concern keyword conflicts
    all_incentive_words = []
    all_concern_words = []
    for s in stakeholders:
        all_incentive_words.append(set(w.lower() for phrase in s.get("incentives", []) for w in phrase.split()))
        all_concern_words.append(set(w.lower() for phrase in s.get("concerns", []) for w in phrase.split()))

    conflict_pairs = 0
    total_pairs = 0
    for i in range(len(stakeholders)):
        for j in range(i + 1, len(stakeholders)):
            total_pairs += 1
            # A's incentives in B's concerns and vice versa
            ab = len(all_incentive_words[i] & all_concern_words[j])
            ba = len(all_incentive_words[j] & all_concern_words[i])
            denom = max(len(all_incentive_words[i]) + len(all_incentive_words[j]), 1)
            if (ab + ba) / denom > 0.15:
                conflict_pairs += 1

    conflict_ratio = conflict_pairs / max(total_pairs, 1)

    if conflict_ratio > 0.4:
        polarity = "adversarial"
    elif conflict_ratio > 0.15:
        polarity = "fragmented"
    else:
        polarity = "collaborative"

    # 2. Pressure: actor count + phase count
    n_actors = len(stakeholders)
    n_phases = len(phases)
    pressure = "high" if (n_actors >= 5 and n_phases >= 4) else ("medium" if n_actors >= 3 else "low")

    # 3. Derive parameters from classification
    PROFILES = {
        "adversarial": {"initial_tension": 0.22, "sycophancy_threshold": 0.40,
                        "trust_decay_boost": 1.5, "tension_floor_base": 0.12},
        "fragmented":  {"initial_tension": 0.12, "sycophancy_threshold": 0.48,
                        "trust_decay_boost": 1.2, "tension_floor_base": 0.06},
        "collaborative": {"initial_tension": 0.04, "sycophancy_threshold": 0.55,
                          "trust_decay_boost": 1.0, "tension_floor_base": 0.0},
    }
    params = dict(PROFILES[polarity])
    # Adjust for pressure
    if pressure == "high":
        params["initial_tension"] = min(0.30, params["initial_tension"] + 0.04)

    return StructuralProfile(polarity=polarity, pressure=pressure, **params)


@dataclass
class ScriptOverrides:
    """User-provided overrides to structural classification."""
    polarity: str | None = None
    initial_tension: float | None = None
    tension_floor_base: float | None = None
    trust_decay_boost: float | None = None
    sycophancy_threshold: float | None = None


def apply_overrides(script_data: dict, overrides: ScriptOverrides) -> dict:
    """Apply user overrides to a script's structural profile."""
    data = copy.deepcopy(script_data)
    profile = data.get("metadata", {}).get("structural_profile", {})

    if overrides.polarity is not None:
        profile["polarity"] = overrides.polarity
    if overrides.initial_tension is not None:
        profile["initial_tension"] = overrides.initial_tension
    if overrides.tension_floor_base is not None:
        profile["tension_floor_base"] = overrides.tension_floor_base
    if overrides.trust_decay_boost is not None:
        profile["trust_decay_boost"] = overrides.trust_decay_boost
    if overrides.sycophancy_threshold is not None:
        profile["sycophancy_threshold"] = overrides.sycophancy_threshold

    data["metadata"]["structural_profile"] = profile
    return data


def inspect_script(script_data: dict) -> dict[str, Any]:
    """Inspect a generated script's structural classification and parameters."""
    profile = script_data.get("metadata", {}).get("structural_profile", {})
    stakeholders = script_data.get("stakeholders", [])
    phases = script_data.get("phases", [])
    initial_ws = script_data.get("initial_world_state", {})

    # Per-pair conflict analysis
    pair_conflicts = []
    for i, a in enumerate(stakeholders):
        a_inc = set(w.lower() for p in a.get("incentives", []) for w in p.split())
        a_con = set(w.lower() for p in a.get("concerns", []) for w in p.split())
        for j, b in enumerate(stakeholders):
            if j <= i:
                continue
            b_inc = set(w.lower() for p in b.get("incentives", []) for w in p.split())
            b_con = set(w.lower() for p in b.get("concerns", []) for w in p.split())
            ab = a_inc & b_con
            ba = b_inc & a_con
            if ab or ba:
                pair_conflicts.append({
                    "actors": (a.get("display_name"), b.get("display_name")),
                    "conflict_words": list(ab | ba),
                    "severity": len(ab) + len(ba),
                })

    return {
        "simulation_id": script_data.get("simulation_id"),
        "structural_profile": profile,
        "actor_count": len(stakeholders),
        "phase_count": len(phases),
        "phase_styles": [p.get("style") for p in phases],
        "initial_world_state": initial_ws,
        "pair_conflicts": sorted(pair_conflicts, key=lambda x: -x["severity"]),
        "tension_floor_estimates": {
            f"{c['actors'][0]} vs {c['actors'][1]}": round(
                profile.get("tension_floor_base", 0) + 0.18 * c["severity"] / max(len(stakeholders), 1),
                3,
            )
            for c in pair_conflicts
        },
    }


def print_inspection(inspection: dict) -> None:
    """Pretty-print a script inspection report."""
    print(f"\n{'='*60}")
    print(f"SCRIPT INSPECTION: {inspection['simulation_id']}")
    print(f"{'='*60}")

    profile = inspection["structural_profile"]
    print(f"\n  Structural Classification:")
    print(f"    Polarity:    {profile.get('polarity', 'unknown')}")
    print(f"    Pressure:    {profile.get('pressure', 'unknown')}")
    print(f"    Init Tension: {profile.get('initial_tension', 0):.2f}")
    print(f"    Sycophancy Threshold: {profile.get('sycophancy_threshold', 0.55):.2f}")
    print(f"    Trust Decay Boost: {profile.get('trust_decay_boost', 1.0):.1f}x")

    print(f"\n  Actors: {inspection['actor_count']}")
    print(f"  Phases: {inspection['phase_count']} ({', '.join(str(s) for s in inspection['phase_styles'])})")

    if inspection["pair_conflicts"]:
        print(f"\n  Stakeholder Conflicts:")
        for c in inspection["pair_conflicts"][:5]:
            print(f"    {c['actors'][0]} vs {c['actors'][1]}: {', '.join(c['conflict_words'][:5])}")

    if inspection["tension_floor_estimates"]:
        print(f"\n  Tension Floor Estimates:")
        for pair, floor in inspection["tension_floor_estimates"].items():
            print(f"    {pair}: {floor:.3f}")

    print(f"\n{'='*60}\n")


def infer_simulation_mode(scenario_family: str) -> str:
    if scenario_family in {"brand_crisis", "resource_scarcity"}:
        return "exploratory"
    return "guided"


def enrich_generated_script_payload(
    payload: dict[str, Any],
    *,
    brief: str,
    brief_id: str,
    generation_attempts: int = 1,
) -> dict[str, Any]:
    data = copy.deepcopy(payload)
    data["simulation_id"] = brief_id
    data["brief"] = brief
    data["title"] = str(data.get("title") or brief_id.replace("_", " ").title())
    data["objective"] = str(data.get("objective") or brief[:180]).strip()

    stakeholders = _normalize_stakeholders(list(data.get("stakeholders") or []))
    if len(stakeholders) < 2:
        raise ValueError("Generated script must contain at least two stakeholders")
    data["stakeholders"] = stakeholders

    scenario_family = str(data.get("scenario_family") or infer_scenario_family(brief, stakeholders, data["title"]))
    spec = copy.deepcopy(FAMILY_SPECS.get(scenario_family, GENERIC_SPEC))
    simulation_mode = str(data.get("simulation_mode") or infer_simulation_mode(scenario_family))
    data["scenario_family"] = scenario_family
    data["simulation_mode"] = simulation_mode

    data["phases"] = _normalize_phases(list(data.get("phases") or []), scenario_family=scenario_family)
    data["world_events"] = _normalize_world_events(list(data.get("world_events") or []))

    world_state_schema = list(dict.fromkeys(list(data.get("world_state_schema") or spec["world_state_schema"])))
    if not set(DEFAULT_GLOBAL_WORLD_STATE_KEYS).issubset(set(world_state_schema)):
        world_state_schema = list(dict.fromkeys(list(spec["world_state_schema"]) + list(world_state_schema)))
    data["world_state_schema"] = world_state_schema
    data["initial_world_state"] = _normalize_world_state(
        data.get("initial_world_state"),
        world_state_schema=world_state_schema,
        fallback=spec["initial_world_state"],
    )
    data["allowed_action_types"] = _normalize_allowed_action_types(
        data.get("allowed_action_types"),
        fallback=spec["allowed_action_types"],
    )
    data["transition_rules"] = _normalize_transition_rules(
        data.get("transition_rules"),
        phases=data["phases"],
        scenario_family=scenario_family,
        world_state_schema=world_state_schema,
        allowed_action_types=data["allowed_action_types"],
    )
    data["state_visibility_rules"] = dict(data.get("state_visibility_rules") or spec["state_visibility_rules"])
    data["outcome_spec"] = dict(data.get("outcome_spec") or spec["outcome_spec"])
    data["evaluation_targets"] = list(
        data.get("evaluation_targets") or data["outcome_spec"].get("evaluation_focus", [])
    )

    metadata = dict(data.get("metadata") or {})
    metadata["phase_action_policies"] = _merge_phase_action_policies(
        metadata.get("phase_action_policies"),
        simulation_mode=simulation_mode,
        phases=data["phases"],
    )
    metadata["actor_action_preferences"] = _merge_actor_action_preferences(
        metadata.get("actor_action_preferences"),
        stakeholders=stakeholders,
        world_state_schema=world_state_schema,
    )
    structural_profile = infer_structural_profile(stakeholders, data["phases"])
    metadata["structural_profile"] = asdict(structural_profile)

    missing_fields = missing_contract_fields(data={**data, "metadata": metadata})
    completeness = compute_metadata_completeness(missing_fields)
    builder_trace = build_builder_trace(
        data=data,
        brief=brief,
        brief_id=brief_id,
        generation_attempts=generation_attempts,
        missing_fields=missing_fields,
        completeness=completeness,
    )
    metadata["metadata_completeness_score"] = completeness
    metadata["missing_contract_fields"] = missing_fields
    metadata["builder_trace"] = builder_trace
    data["metadata"] = metadata

    return data


def validate_enriched_script(payload: dict[str, Any]) -> SimulationScript:
    return SimulationScript.from_dict(payload)


def missing_contract_fields(data: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    if not data.get("scenario_family"):
        missing.append("scenario_family")
    if not data.get("world_state_schema"):
        missing.append("world_state_schema")
    if not data.get("initial_world_state"):
        missing.append("initial_world_state")
    if not data.get("allowed_action_types"):
        missing.append("allowed_action_types")
    if not data.get("transition_rules"):
        missing.append("transition_rules")
    if not data.get("state_visibility_rules"):
        missing.append("state_visibility_rules")
    metadata = dict(data.get("metadata") or {})
    if not metadata.get("phase_action_policies"):
        missing.append("metadata.phase_action_policies")
    if not metadata.get("actor_action_preferences"):
        missing.append("metadata.actor_action_preferences")
    return missing


def compute_metadata_completeness(missing_fields: list[str]) -> float:
    return round(max(0.0, 1.0 - (len(missing_fields) / len(REQUIRED_SCRIPT_FIELDS))), 4)


def build_builder_trace(
    *,
    data: dict[str, Any],
    brief: str,
    brief_id: str,
    generation_attempts: int,
    missing_fields: list[str],
    completeness: float,
) -> dict[str, Any]:
    stakeholders = list(data.get("stakeholders") or [])
    phase_names = [str(phase.get("name") or "") for phase in list(data.get("phases") or [])]
    return {
        "builder_trace_id": f"builder:{brief_id}",
        "brief_id": brief_id,
        "builder_version": "brief_builder_v2",
        "generation_attempts": generation_attempts,
        "scenario_family": data.get("scenario_family", "generic"),
        "input_understanding": {
            "brief_excerpt": brief[:200],
            "detected_keywords": sorted(set(_keyword_hits(brief))),
            "simulation_mode": data.get("simulation_mode", "guided"),
        },
        "stakeholder_extraction": [
            {
                "actor_id": actor.get("actor_id"),
                "display_name": actor.get("display_name"),
                "role": actor.get("role"),
            }
            for actor in stakeholders
        ],
        "stakeholder_expansion": [
            actor.get("role")
            for actor in stakeholders
            if any(token in str(actor.get("role", "")).lower() for token in ("legal", "ops", "finance", "patient", "community"))
        ],
        "phase_template_selection": {
            "phase_names": phase_names,
            "phase_count": len(phase_names),
        },
        "world_state_schema_selection": {
            "world_state_schema": list(data.get("world_state_schema") or []),
        },
        "allowed_action_types_selection": {
            "allowed_action_types": list(data.get("allowed_action_types") or []),
        },
        "transition_rules_selection": {
            "phase_rule_counts": {
                phase_name: len(dict(rules).keys())
                for phase_name, rules in dict(data.get("transition_rules") or {}).items()
            },
        },
        "phase_action_policies_generation": dict(dict(data.get("metadata") or {}).get("phase_action_policies") or {}),
        "actor_action_preferences_generation": dict(dict(data.get("metadata") or {}).get("actor_action_preferences") or {}),
        "metadata_completeness_score": completeness,
        "missing_contract_fields": missing_fields,
    }


def _normalize_stakeholders(stakeholders: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for index, actor in enumerate(stakeholders, start=1):
        row = dict(actor)
        row["actor_id"] = f"actor_{index}"
        row["display_name"] = str(row.get("display_name") or row.get("name") or f"Actor {index}")
        row["role"] = str(row.get("role") or f"Stakeholder {index}")
        row["identity_core"] = dict(row.get("identity_core") or {})
        row["personality_prior"] = normalize_personality_vector(dict(row.get("personality_prior") or {}))
        row["incentives"] = list(dict.fromkeys(list(row.get("incentives") or [])))[:4]
        row["concerns"] = list(dict.fromkeys(list(row.get("concerns") or [])))[:4]
        row["communication_style"] = dict(row.get("communication_style") or {"tone": "measured", "brevity": "moderate"})
        normalized.append(row)
    return normalized


def _normalize_phases(phases: list[dict[str, Any]], *, scenario_family: str) -> list[dict[str, Any]]:
    if not phases:
        return copy.deepcopy(DEFAULT_PHASES)
    normalized: list[dict[str, Any]] = []
    for template, phase in zip(DEFAULT_PHASES, phases[: len(DEFAULT_PHASES)]):
        row = dict(template)
        row.update({key: value for key, value in dict(phase).items() if value not in (None, "", [])})
        row["name"] = template["name"]
        row["max_turns"] = int(row.get("max_turns", template["max_turns"]))
        row["cues"] = list(dict.fromkeys(list(row.get("cues") or template["cues"])))
        normalized.append(row)
    while len(normalized) < len(DEFAULT_PHASES):
        normalized.append(copy.deepcopy(DEFAULT_PHASES[len(normalized)]))
    if scenario_family in {"brand_crisis", "resource_scarcity"}:
        normalized[1]["cues"] = list(dict.fromkeys(normalized[1]["cues"] + ["pressure", "uncertainty"]))
        normalized[2]["cues"] = list(dict.fromkeys(normalized[2]["cues"] + ["divergence", "bounded_experiment"]))
    return normalized


def _normalize_world_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for index, event in enumerate(events[:4], start=1):
        row = dict(event)
        row["event_id"] = str(row.get("event_id") or f"evt_{index}")
        row["title"] = str(row.get("title") or f"Scenario event {index}")
        row["description"] = str(row.get("description") or row["title"])
        phase_name = str(row.get("trigger_phase") or "").upper()
        row["trigger_phase"] = phase_name if phase_name in {"OPENING", "TENSION", "NEGOTIATION", "CLOSING"} else "TENSION"
        row["visibility"] = str(row.get("visibility") or "public")
        row["affected_actor_ids"] = list(row.get("affected_actor_ids") or [])
        normalized.append(row)
    return normalized


def _normalize_world_state(
    raw_state: Any,
    *,
    world_state_schema: list[str],
    fallback: dict[str, float],
) -> dict[str, float]:
    source = dict(raw_state or {})
    base = {**fallback, **source}
    return {
        key: round(max(0.0, min(1.0, float(base.get(key, 0.5)))), 4)
        for key in world_state_schema
    }


def _normalize_allowed_action_types(raw: Any, *, fallback: list[str]) -> list[str]:
    actions = [str(item) for item in list(raw or fallback)]
    valid = [action for action in actions if action in ACTION_TYPES]
    return list(dict.fromkeys(valid or list(fallback)))


def _normalize_transition_rules(
    raw_rules: Any,
    *,
    phases: list[dict[str, Any]],
    scenario_family: str,
    world_state_schema: list[str],
    allowed_action_types: list[str],
) -> dict[str, dict[str, Any]]:
    normalized = {
        phase["name"]: {
            action_type: _generic_transition_rule(
                action_type=action_type,
                scenario_family=scenario_family,
                world_state_schema=world_state_schema,
            )
            for action_type in _phase_allowed_actions(phase_name=phase["name"], allowed_action_types=allowed_action_types)
        }
        for phase in phases
    }
    for phase_name, rules in dict(raw_rules or {}).items():
        if phase_name not in normalized:
            continue
        for action_type, rule in dict(rules or {}).items():
            if action_type not in allowed_action_types:
                continue
            normalized[phase_name][action_type] = _merge_transition_rule(
                normalized[phase_name].get(action_type, {}),
                dict(rule or {}),
                world_state_schema=world_state_schema,
            )
    return normalized


def _phase_allowed_actions(*, phase_name: str, allowed_action_types: list[str]) -> list[str]:
    defaults = {
        "OPENING": ["request_evidence", "publish_update"],
        "TENSION": ["request_evidence", "narrow_scope", "pilot", "defer_decision", "preserve_autonomy"],
        "NEGOTIATION": ["assign_owner", "pilot", "publish_update", "commit_resource", "preserve_autonomy", "narrow_scope"],
        "CLOSING": ["assign_owner", "publish_update", "defer_decision"],
    }
    ordered = [action for action in defaults.get(phase_name, []) if action in allowed_action_types]
    return ordered or list(allowed_action_types)


def _generic_transition_rule(
    *,
    action_type: str,
    scenario_family: str,
    world_state_schema: list[str],
) -> dict[str, Any]:
    positive_targets = {
        "assign_owner": ["execution_confidence", "alignment"],
        "request_evidence": ["uncertainty", "risk"],
        "publish_update": ["trust", "alignment"],
        "narrow_scope": ["risk", "uncertainty"],
        "pilot": ["uncertainty", "risk", "execution_confidence"],
        "commit_resource": ["execution_confidence"],
        "defer_decision": ["uncertainty"],
        "preserve_autonomy": ["trust"],
    }
    global_deltas: dict[str, float] = {}
    for key in positive_targets.get(action_type, [])[:2]:
        if key in world_state_schema:
            direction = -0.08 if key in {"risk", "uncertainty"} else 0.08
            global_deltas[key] = direction
    family_bonus_key = {
        "launch_pressure": "launch_readiness",
        "integration_trust": "integration_clarity",
        "brand_crisis": "reputation_stability",
        "resource_scarcity": "delivery_capacity",
        "policy_spillover": "admin_feasibility",
    }.get(scenario_family)
    if family_bonus_key and family_bonus_key in world_state_schema and action_type in {"assign_owner", "publish_update", "commit_resource", "pilot"}:
        global_deltas.setdefault(family_bonus_key, 0.04)
    return {
        "global_deltas": global_deltas,
        "owner_local_deltas": {"execution_confidence": 0.04} if action_type in {"assign_owner", "pilot", "commit_resource", "request_evidence"} else {"trust": 0.04},
        "target_local_deltas": {"trust": 0.04} if action_type in {"publish_update", "preserve_autonomy"} else {},
        "feedback_template": f"{ACTION_FAMILIES.get(action_type, action_type)} action shifts the visible state.",
    }


def _merge_transition_rule(base: dict[str, Any], override: dict[str, Any], *, world_state_schema: list[str]) -> dict[str, Any]:
    merged = copy.deepcopy(base)
    merged.update({key: value for key, value in override.items() if key != "global_deltas"})
    if "global_deltas" in override:
        merged["global_deltas"] = {
            key: float(value)
            for key, value in dict(override.get("global_deltas") or {}).items()
            if key in world_state_schema
        }
    return merged


def _merge_phase_action_policies(raw: Any, *, simulation_mode: str, phases: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    defaults: dict[str, dict[str, Any]] = {}
    for phase in phases:
        phase_name = str(phase.get("name"))
        policy = {
            "action_mode": "execute" if phase_name in {"NEGOTIATION", "CLOSING"} else "shadow",
            "diversity_required": phase_name in {"TENSION", "NEGOTIATION"},
            "duplicate_penalty": 0.32 if phase_name == "NEGOTIATION" else 0.16,
            "uniqueness_bonus": 0.18 if phase_name == "NEGOTIATION" else 0.08,
            "convergence_backoff_threshold": 0.90 if phase_name == "NEGOTIATION" else 0.95,
            "allow_no_action": True,
            "family_cap": 1 if phase_name == "NEGOTIATION" else 2,
            "max_same_family_per_phase": 1 if phase_name == "NEGOTIATION" else 2,
            "max_actions_per_phase": 3 if phase_name == "NEGOTIATION" else 2,
            "sparsity_threshold": 0.82 if phase_name == "NEGOTIATION" else 0.68,
            "style_slot_limit": 3 if phase_name != "NEGOTIATION" else 4,
            "pool_max_concurrency": 2 if phase_name != "CLOSING" else 1,
            "planner_cache": phase_name in {"OPENING", "CLOSING"},
        }
        if simulation_mode == "exploratory":
            policy["action_mode"] = "execute" if phase_name == "NEGOTIATION" else "shadow"
            policy["diversity_required"] = True
            policy["sparsity_threshold"] = 0.55 if phase_name == "NEGOTIATION" else 0.52
            policy["style_slot_limit"] = 4
        defaults[phase_name] = policy
    for phase_name, policy in dict(raw or {}).items():
        if phase_name in defaults:
            defaults[phase_name].update(dict(policy or {}))
    return defaults


def _merge_actor_action_preferences(
    raw: Any,
    *,
    stakeholders: list[dict[str, Any]],
    world_state_schema: list[str],
) -> dict[str, dict[str, dict[str, Any]]]:
    existing = dict(raw or {})
    preferences: dict[str, dict[str, dict[str, Any]]] = {}
    for actor in stakeholders:
        actor_id = actor["actor_id"]
        inferred = _infer_actor_action_preference(actor, world_state_schema)
        actor_pref = copy.deepcopy(inferred)
        actor_pref.update(dict(existing.get(actor_id) or {}))
        preferences[actor_id] = actor_pref
    return preferences


def _infer_actor_action_preference(actor: dict[str, Any], world_state_schema: list[str]) -> dict[str, dict[str, Any]]:
    role_text = " ".join(
        [
            str(actor.get("role") or ""),
            " ".join(actor.get("incentives") or []),
            " ".join(actor.get("concerns") or []),
        ]
    ).lower()
    if any(token in role_text for token in ("ops", "operations", "devops", "admin", "administrator", "coordinator")):
        primary = ["ownership", "resourcing"]
        secondary = ["evidence", "communication"]
    elif any(token in role_text for token in ("legal", "compliance", "risk", "cfo", "finance")):
        primary = ["evidence", "timing"]
        secondary = ["governance", "scope"]
    elif any(token in role_text for token in ("marketing", "communications", "patient advocacy", "community", "sales")):
        primary = ["communication", "scope"]
        secondary = ["governance", "timing"]
    elif any(token in role_text for token in ("cto", "engineering", "product", "technical", "radiology", "medicine")):
        primary = ["ownership", "evidence"]
        secondary = ["scope", "resourcing"]
    else:
        primary = ["evidence", "communication"]
        secondary = ["scope", "ownership"]
    priorities = [
        key for key in (
            "execution_confidence",
            "alignment",
            "trust",
            "risk",
            "uncertainty",
            "launch_readiness",
            "integration_clarity",
            "reputation_stability",
            "delivery_capacity",
            "admin_feasibility",
        )
        if key in world_state_schema
    ][:3]
    return {
        "default": {
            "primary_families": primary,
            "secondary_families": secondary,
            "avoid_families": [],
            "state_priority_keys": priorities,
            "preferred_action_types": [],
            "preferred_target_keys": priorities[:2],
        }
    }


def _keyword_hits(text: str) -> list[str]:
    lowered = (text or "").lower()
    keywords = [
        "migration",
        "launch",
        "budget",
        "risk",
        "merger",
        "integration",
        "open source",
        "liability",
        "consent",
        "downtime",
        "accuracy",
    ]
    return [keyword for keyword in keywords if keyword in lowered]
