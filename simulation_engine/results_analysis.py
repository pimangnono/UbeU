"""Normalized analysis payloads for interactive simulation result views."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

ANALYSIS_VERSION = 3


def _round(value: float, digits: int = 4) -> float:
    return round(float(value), digits)


def _clip_unit(value: float) -> float:
    return max(0.0, min(1.0, _round(value)))


def _pair_label(src: str, tgt: str, actor_names: dict[str, str]) -> str:
    return f"{actor_names.get(src, src)} → {actor_names.get(tgt, tgt)}"


def _strongest_trait_shift(
    prior: dict[str, Any],
    final_estimate: dict[str, Any],
) -> tuple[str, float, float, float] | None:
    best_trait = None
    best_delta = -1.0
    best_prior = 0.5
    best_final = 0.5
    for trait in ("O", "C", "E", "A", "N"):
        prior_value = float(prior.get(trait, 0.5))
        final_value = float(final_estimate.get(trait, prior_value))
        delta = abs(final_value - prior_value)
        if delta > best_delta:
            best_trait = trait
            best_delta = delta
            best_prior = prior_value
            best_final = final_value
    if best_trait is None:
        return None
    return best_trait, _round(best_prior), _round(best_final), _round(best_final - best_prior)


def _format_stance_summary(actor: dict[str, Any]) -> str:
    disposition = str(actor.get("strategic_disposition", "neutral"))
    incentives = list(actor.get("incentives", []) or [])
    concerns = list(actor.get("concerns", []) or [])
    incentive_text = incentives[0] if incentives else "their core incentive"
    concern_text = concerns[0] if concerns else "their main concern"
    return f"Started {disposition}, pushing for {incentive_text} while worrying about {concern_text}."


def _format_after_summary(
    actor_name: str,
    end_state_summary: str,
    top_relationship: dict[str, Any] | None,
    drift_score: float,
) -> str:
    relationship_text = "no strong relationship swing was recorded"
    if top_relationship and (
        abs(float(top_relationship.get("trust_delta", 0.0))) > 0.01
        or abs(float(top_relationship.get("tension_delta", 0.0))) > 0.01
    ):
        relationship_text = (
            f"their sharpest relationship movement was toward "
            f"{top_relationship.get('target_label', top_relationship.get('target_actor_id', 'another actor'))}"
        )
    drift_text = "stayed close to the configured persona"
    if drift_score >= 0.2:
        drift_text = "departed noticeably from the configured persona"
    elif drift_score >= 0.08:
        drift_text = "showed some persona drift"
    return f"{end_state_summary} During the run, {actor_name} {relationship_text} and {drift_text}."


def _turn_lookup(runtime_summary: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {
        int(turn.get("turn_index", 0)): turn
        for turn in runtime_summary.get("turns", []) or []
    }


def _proposal_lookup(runtime_summary: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(proposal.get("proposal_id", "")): proposal
        for proposal in runtime_summary.get("action_proposals", []) or []
        if proposal.get("proposal_id")
    }


def _phase_index_map(runtime_summary: dict[str, Any]) -> dict[str, int]:
    return {
        phase_name: index
        for index, phase_name in enumerate(runtime_summary.get("phase_order", []) or [])
    }


def _evidence_item(
    *,
    evidence_id: str,
    evidence_type: str,
    actor_id: str,
    other_actor_id: str | None = None,
    phase_name: str = "",
    turn_index: int = 0,
    summary: str,
    why_it_matters: str,
    quote: str = "",
    related_relationship_id: str | None = None,
    related_action_id: str | None = None,
) -> dict[str, Any]:
    return {
        "evidence_id": evidence_id,
        "type": evidence_type,
        "actor_id": actor_id,
        "other_actor_id": other_actor_id,
        "phase_name": phase_name,
        "turn_index": int(turn_index),
        "summary": summary,
        "why_it_matters": why_it_matters,
        "quote": quote,
        "related_relationship_id": related_relationship_id,
        "related_action_id": related_action_id,
    }


def _build_initial_relationships(
    script: dict[str, Any],
    actor_names: dict[str, str],
) -> list[dict[str, Any]]:
    actor_ids = [actor.get("actor_id", "") for actor in script.get("stakeholders", [])]
    initial_rel_map = {
        (rel.get("source", ""), rel.get("target", "")): rel
        for rel in script.get("initial_relationships", []) or []
        if rel.get("source") and rel.get("target")
    }
    relationships: list[dict[str, Any]] = []
    for src in actor_ids:
        for tgt in actor_ids:
            if not src or not tgt or src == tgt:
                continue
            rel = initial_rel_map.get((src, tgt), {})
            label = str(rel.get("label", "")).strip()
            trust = 0.5
            tension = 0.0
            lowered = label.lower()
            if any(token in lowered for token in ("allies", "ally", "cooperative", "support", "partner")):
                trust = 0.65
            elif any(token in lowered for token in ("tension", "conflict", "competing", "rival", "adversar")):
                trust = 0.35
                tension = 0.2
            relationships.append({
                "relationship_id": f"rel:{src}:{tgt}",
                "source_actor_id": src,
                "target_actor_id": tgt,
                "label": label or "neutral",
                "trust": trust,
                "tension": tension,
                "display_label": _pair_label(src, tgt, actor_names),
            })
    return relationships


def _build_final_relationships(
    runtime_summary: dict[str, Any],
    initial_relationships: list[dict[str, Any]],
    actor_names: dict[str, str],
) -> list[dict[str, Any]]:
    initial_map = {
        (rel["source_actor_id"], rel["target_actor_id"]): rel
        for rel in initial_relationships
    }
    aggregates: dict[tuple[str, str], dict[str, Any]] = {}
    for event in runtime_summary.get("relationship_events", []) or []:
        src = event.get("source_actor_id") or event.get("source") or ""
        tgt = event.get("target_actor_id") or event.get("target") or ""
        if not src or not tgt:
            continue
        key = (src, tgt)
        base = aggregates.setdefault(key, {
            "relationship_id": f"rel:{src}:{tgt}",
            "source_actor_id": src,
            "target_actor_id": tgt,
            "display_label": _pair_label(src, tgt, actor_names),
            "initial_trust": initial_map.get(key, {}).get("trust", 0.5),
            "initial_tension": initial_map.get(key, {}).get("tension", 0.0),
            "total_trust_delta": 0.0,
            "total_tension_delta": 0.0,
            "event_count": 0,
            "last_turn_index": 0,
            "last_evidence": "",
            "sentiment": event.get("sentiment", "neutral"),
            "label": initial_map.get(key, {}).get("label", "neutral"),
        })
        base["total_trust_delta"] += float(event.get("trust_delta", 0.0))
        base["total_tension_delta"] += float(event.get("tension_delta", 0.0))
        base["event_count"] += 1
        base["last_turn_index"] = max(base["last_turn_index"], int(event.get("turn_index", 0)))
        if event.get("evidence"):
            base["last_evidence"] = str(event.get("evidence", ""))
        if event.get("new_sentiment"):
            base["sentiment"] = event.get("new_sentiment")

    seen = set(aggregates)
    for key, rel in initial_map.items():
        if key not in seen:
            aggregates[key] = {
                "relationship_id": f"rel:{key[0]}:{key[1]}",
                "source_actor_id": key[0],
                "target_actor_id": key[1],
                "display_label": _pair_label(key[0], key[1], actor_names),
                "initial_trust": rel.get("trust", 0.5),
                "initial_tension": rel.get("tension", 0.0),
                "total_trust_delta": 0.0,
                "total_tension_delta": 0.0,
                "event_count": 0,
                "last_turn_index": 0,
                "last_evidence": "",
                "sentiment": "neutral",
                "label": rel.get("label", "neutral"),
            }

    results: list[dict[str, Any]] = []
    for rel in aggregates.values():
        rel["initial_trust"] = _round(rel["initial_trust"])
        rel["initial_tension"] = _round(rel["initial_tension"])
        rel["total_trust_delta"] = _round(rel["total_trust_delta"])
        rel["total_tension_delta"] = _round(rel["total_tension_delta"])
        rel["final_trust"] = _clip_unit(rel["initial_trust"] + rel["total_trust_delta"])
        rel["final_tension"] = _clip_unit(rel["initial_tension"] + rel["total_tension_delta"])
        results.append(rel)
    results.sort(
        key=lambda item: abs(item["total_trust_delta"]) + abs(item["total_tension_delta"]),
        reverse=True,
    )
    return results


def _relationship_triggers(
    pair_events: list[dict[str, Any]],
    turn_map: dict[int, dict[str, Any]],
    actor_names: dict[str, str],
) -> list[dict[str, Any]]:
    triggers: list[dict[str, Any]] = []
    ranked = sorted(
        pair_events,
        key=lambda evt: abs(float(evt.get("trust_delta", 0.0))) + 0.6 * abs(float(evt.get("tension_delta", 0.0))),
        reverse=True,
    )
    for index, evt in enumerate(ranked[:3], start=1):
        src = evt.get("source_actor_id") or evt.get("source") or ""
        tgt = evt.get("target_actor_id") or evt.get("target") or ""
        turn_index = int(evt.get("turn_index", 0))
        turn = turn_map.get(turn_index, {})
        trust_delta = float(evt.get("trust_delta", 0.0))
        tension_delta = float(evt.get("tension_delta", 0.0))
        summary = (
            f"{actor_names.get(src, src)} shifted trust toward {actor_names.get(tgt, tgt)} "
            f"by {trust_delta:+.2f} and tension by {tension_delta:+.2f}."
        )
        triggers.append({
            "trigger_id": f"trigger:relationship:{src}:{tgt}:{turn_index}:{index}",
            "kind": "relationship",
            "turn_index": turn_index,
            "phase_name": turn.get("phase_name", evt.get("phase_name", "")),
            "actor_id": src,
            "weight": _round(abs(trust_delta) + abs(tension_delta)),
            "summary": summary,
            "evidence": evt.get("evidence", "") or turn.get("content", ""),
            "related_ids": [f"rel:{src}:{tgt}"],
        })
    return triggers


def _build_actor_final_state_summary(
    runtime_summary: dict[str, Any],
    metrics: dict[str, Any],
    final_relationships: list[dict[str, Any]],
    conclusion: dict[str, Any] | None,
    script: dict[str, Any],
    actor_names: dict[str, str],
) -> list[dict[str, Any]]:
    actor_state_events = runtime_summary.get("actor_state_events", []) or []
    actor_specs = {
        actor.get("actor_id", ""): actor
        for actor in script.get("stakeholders", []) or []
        if actor.get("actor_id")
    }
    arc_map = {
        arc.get("actor_id", ""): arc.get("arc", "")
        for arc in (conclusion or {}).get("actor_arcs", []) or []
    }
    latest_state_by_actor: dict[str, dict[str, Any]] = {}
    for event in actor_state_events:
        actor_id = event.get("actor_id", "")
        if not actor_id:
            continue
        if actor_id not in latest_state_by_actor or int(event.get("turn_index", 0)) >= int(latest_state_by_actor[actor_id].get("turn_index", 0)):
            latest_state_by_actor[actor_id] = event

    relationships_by_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rel in final_relationships:
        relationships_by_actor[rel["source_actor_id"]].append(rel)

    estimates = metrics.get("actor_trait_estimates", {}) or {}
    summaries: list[dict[str, Any]] = []
    for actor in script.get("stakeholders", []) or []:
        actor_id = actor.get("actor_id", "")
        if not actor_id:
            continue
        state_event = latest_state_by_actor.get(actor_id, {})
        new_state = state_event.get("new_state", {}) or {}
        final_trait_estimate = estimates.get(actor_id, new_state.get("rolling_trait_estimate", {})) or actor.get("personality_prior", {})
        strongest_trait = _strongest_trait_shift(actor.get("personality_prior", {}), final_trait_estimate)
        rels = sorted(
            relationships_by_actor.get(actor_id, []),
            key=lambda rel: abs(float(rel.get("total_trust_delta", 0.0))) + abs(float(rel.get("total_tension_delta", 0.0))),
            reverse=True,
        )
        top_relationship = None
        if rels:
            top_relationship = {
                "target_actor_id": rels[0]["target_actor_id"],
                "target_label": actor_names.get(rels[0]["target_actor_id"], rels[0]["target_actor_id"]),
                "trust_delta": rels[0]["total_trust_delta"],
                "tension_delta": rels[0]["total_tension_delta"],
            }
        drift_score = _round(new_state.get("drift_score", 0.0))
        end_state_summary = arc_map.get(actor_id, f"{actor_names.get(actor_id, actor_id)} completed the simulation.")
        summaries.append({
            "actor_id": actor_id,
            "display_name": actor_names.get(actor_id, actor_id),
            "final_trait_estimate": final_trait_estimate,
            "final_drift_score": drift_score,
            "stress": _round(new_state.get("stress", 0.0)),
            "top_relationship_shift": top_relationship,
            "initial_stance_summary": _format_stance_summary(actor),
            "strongest_trait_shift": (
                {
                    "trait": strongest_trait[0],
                    "initial": strongest_trait[1],
                    "final": strongest_trait[2],
                    "delta": strongest_trait[3],
                } if strongest_trait else None
            ),
            "end_state_summary": end_state_summary,
            "after_summary": _format_after_summary(
                actor_names.get(actor_id, actor_id),
                end_state_summary,
                top_relationship,
                drift_score,
            ),
        })
    summaries.sort(key=lambda row: row["display_name"])
    return summaries


def _add_trigger_summary(change: dict[str, Any], triggers: list[dict[str, Any]]) -> None:
    change["trigger_summary"] = triggers[0]["summary"] if triggers else "No strong trigger identified."


def _build_change_events(
    runtime_summary: dict[str, Any],
    script: dict[str, Any],
    metrics: dict[str, Any],
    final_relationships: list[dict[str, Any]],
    actor_final_state_summary: list[dict[str, Any]],
    actor_names: dict[str, str],
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    turn_map = _turn_lookup(runtime_summary)
    proposal_map = _proposal_lookup(runtime_summary)
    relationship_events = runtime_summary.get("relationship_events", []) or []
    executed_actions = runtime_summary.get("executed_actions", []) or []
    world_state_history = runtime_summary.get("world_state_history", []) or []
    actor_state_events = runtime_summary.get("actor_state_events", []) or []
    actor_specs = {
        actor.get("actor_id", ""): actor
        for actor in script.get("stakeholders", []) or []
        if actor.get("actor_id")
    }

    changes: list[dict[str, Any]] = []
    attributions: dict[str, list[dict[str, Any]]] = {}

    events_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for event in relationship_events:
        src = event.get("source_actor_id", "")
        tgt = event.get("target_actor_id", "")
        if src and tgt:
            events_by_pair[(src, tgt)].append(event)
    for rel in final_relationships:
        magnitude = abs(float(rel.get("total_trust_delta", 0.0))) + 0.6 * abs(float(rel.get("total_tension_delta", 0.0)))
        if magnitude < 0.04:
            continue
        change_id = f"change:relationship:{rel['source_actor_id']}:{rel['target_actor_id']}"
        change = {
            "change_id": change_id,
            "category": "relationship",
            "label": f"{rel['display_label']} relationship shift",
            "summary": (
                f"Between the start and end of the simulation, trust moved {float(rel['total_trust_delta']):+.2f} "
                f"and tension moved {float(rel['total_tension_delta']):+.2f}."
            ),
            "magnitude": _round(magnitude),
            "phase_name": "",
            "affected_actor_ids": [rel["source_actor_id"], rel["target_actor_id"]],
            "affected_keys": ["trust", "tension"],
            "meaning": "This tracks whether two actors became more trusting or more adversarial over the run.",
            "initial_value": {"trust": rel["initial_trust"], "tension": rel["initial_tension"]},
            "final_value": {"trust": rel["final_trust"], "tension": rel["final_tension"]},
            "delta": {"trust": rel["total_trust_delta"], "tension": rel["total_tension_delta"]},
        }
        triggers = _relationship_triggers(events_by_pair.get((rel["source_actor_id"], rel["target_actor_id"]), []), turn_map, actor_names)
        if triggers:
            change["phase_name"] = triggers[0].get("phase_name", "")
        _add_trigger_summary(change, triggers)
        changes.append(change)
        attributions[change_id] = triggers

    if world_state_history:
        first_state = world_state_history[0].get("global_state", {}) or {}
        final_state = world_state_history[-1].get("global_state", {}) or {}
        for key, final_value in final_state.items():
            initial_value = float(first_state.get(key, 0.5))
            delta = float(final_value) - initial_value
            if abs(delta) < 0.03:
                continue
            related_actions = []
            for action in executed_actions:
                applied_delta = action.get("applied_delta", {}) or {}
                if key not in applied_delta:
                    continue
                proposal = proposal_map.get(str(action.get("proposal_id", "")), {})
                turn_index = int(proposal.get("turn_index", 0))
                turn = turn_map.get(turn_index, {})
                related_actions.append({
                    "trigger_id": f"trigger:world_state:{key}:{action.get('proposal_id', '')}",
                    "kind": "action",
                    "turn_index": turn_index,
                    "phase_name": action.get("phase_name", turn.get("phase_name", "")),
                    "actor_id": action.get("owner_actor_id", ""),
                    "weight": _round(abs(float(applied_delta.get(key, 0.0)))),
                    "summary": (
                        f"{actor_names.get(action.get('owner_actor_id', ''), action.get('owner_actor_id', ''))} "
                        f"changed {key} by {float(applied_delta.get(key, 0.0)):+.2f}"
                    ),
                    "evidence": turn.get("content", ""),
                    "related_ids": [f"action:{action.get('proposal_id', '')}"],
                })
            related_actions.sort(key=lambda row: row["weight"], reverse=True)
            phase_name = related_actions[0].get("phase_name", "") if related_actions else world_state_history[-1].get("phase_name", "")
            change_id = f"change:world_state:{key}"
            change = {
                "change_id": change_id,
                "category": "world_state",
                "label": key.replace("_", " ").title(),
                "summary": f"{key} moved from {initial_value:.2f} to {float(final_value):.2f}.",
                "magnitude": _round(abs(delta)),
                "phase_name": phase_name,
                "affected_actor_ids": [trigger["actor_id"] for trigger in related_actions if trigger.get("actor_id")][:3],
                "affected_keys": [key],
                "meaning": "This is a simulated system-level outcome variable, not one actor's opinion.",
                "initial_value": initial_value,
                "final_value": _round(final_value),
                "delta": _round(delta),
            }
            _add_trigger_summary(change, related_actions)
            changes.append(change)
            attributions[change_id] = related_actions[:4]

    peak_drift_by_actor: dict[str, dict[str, Any]] = {}
    for event in actor_state_events:
        actor_id = event.get("actor_id", "")
        if not actor_id:
            continue
        new_state = event.get("new_state", {}) or {}
        drift = float(new_state.get("drift_score", 0.0))
        if actor_id not in peak_drift_by_actor or drift > float(peak_drift_by_actor[actor_id].get("new_state", {}).get("drift_score", 0.0)):
            peak_drift_by_actor[actor_id] = event
    for actor_id, event in peak_drift_by_actor.items():
        new_state = event.get("new_state", {}) or {}
        drift = float(new_state.get("drift_score", 0.0))
        if drift < 0.08:
            continue
        turn_index = int(event.get("turn_index", 0))
        turn = turn_map.get(turn_index, {})
        actor_spec = actor_specs.get(actor_id, {})
        prior = actor_spec.get("personality_prior", {})
        final_estimate = metrics.get("actor_trait_estimates", {}).get(actor_id, new_state.get("rolling_trait_estimate", {}))
        strongest_trait = _strongest_trait_shift(prior, final_estimate)
        shift_text = ""
        if strongest_trait:
            shift_text = f" Biggest trait move: {strongest_trait[0]} {strongest_trait[1]:.2f} → {strongest_trait[2]:.2f}."
        change_id = f"change:drift:{actor_id}"
        triggers = [{
            "trigger_id": f"trigger:drift:{actor_id}:{turn_index}",
            "kind": "turn",
            "turn_index": turn_index,
            "phase_name": event.get("phase_name", ""),
            "actor_id": actor_id,
            "weight": _round(drift),
            "summary": f"This turn pushed {actor_names.get(actor_id, actor_id)} furthest away from its configured persona (drift {drift:.2f}).",
            "evidence": turn.get("content", ""),
            "related_ids": [change_id],
        }]
        change = {
            "change_id": change_id,
            "category": "actor_drift",
            "label": f"{actor_names.get(actor_id, actor_id)} persona drift",
            "summary": f"This actor's observed behavior diverged from the configured OCEAN target by {drift:.2f}.{shift_text}",
            "magnitude": _round(drift),
            "phase_name": event.get("phase_name", ""),
            "affected_actor_ids": [actor_id],
            "affected_keys": ["drift_score"],
            "meaning": "Drift measures fidelity: higher drift means the actor behaved less like its intended persona, not that its policy position changed more.",
            "initial_value": 0.0,
            "final_value": _round(drift),
            "delta": _round(drift),
        }
        _add_trigger_summary(change, triggers)
        changes.append(change)
        attributions[change_id] = triggers

    for action in executed_actions:
        applied_delta = action.get("applied_delta", {}) or {}
        magnitude = sum(abs(float(value)) for value in applied_delta.values())
        if magnitude < 0.03:
            continue
        proposal = proposal_map.get(str(action.get("proposal_id", "")), {})
        turn_index = int(proposal.get("turn_index", 0))
        turn = turn_map.get(turn_index, {})
        actor_id = action.get("owner_actor_id", "")
        change_id = f"change:action:{action.get('proposal_id', '')}"
        triggers = [{
            "trigger_id": f"trigger:action:{action.get('proposal_id', '')}",
            "kind": "action",
            "turn_index": turn_index,
            "phase_name": action.get("phase_name", turn.get("phase_name", "")),
            "actor_id": actor_id,
            "weight": _round(magnitude),
            "summary": (
                f"{actor_names.get(actor_id, actor_id)} used {str(action.get('action_type', '')).replace('_', ' ')} "
                f"on {action.get('target_key', '')}"
            ),
            "evidence": turn.get("content", ""),
            "related_ids": [f"action:{action.get('proposal_id', '')}"],
        }]
        change = {
            "change_id": change_id,
            "category": "action",
            "label": str(action.get("action_type", "")).replace("_", " ").title(),
            "summary": f"Applied deltas to {', '.join(applied_delta.keys()) or action.get('target_key', '')}.",
            "magnitude": _round(magnitude),
            "phase_name": action.get("phase_name", turn.get("phase_name", "")),
            "affected_actor_ids": [actor_id],
            "affected_keys": list(applied_delta.keys()) or ([action.get("target_key", "")] if action.get("target_key") else []),
            "meaning": "This captures a concrete simulated move that changed shared state variables.",
            "initial_value": {},
            "final_value": applied_delta,
            "delta": applied_delta,
        }
        _add_trigger_summary(change, triggers)
        changes.append(change)
        attributions[change_id] = triggers

    changes.sort(key=lambda item: item["magnitude"], reverse=True)
    return changes, attributions


def _build_phase_summaries(
    runtime_summary: dict[str, Any],
    change_events: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    world_state_history = runtime_summary.get("world_state_history", []) or []
    phase_summaries: list[dict[str, Any]] = []
    for phase_name in runtime_summary.get("phase_order", []) or []:
        phase_snapshots = [snapshot for snapshot in world_state_history if snapshot.get("phase_name") == phase_name]
        deltas: dict[str, float] = {}
        if len(phase_snapshots) >= 2:
            start = phase_snapshots[0].get("global_state", {}) or {}
            end = phase_snapshots[-1].get("global_state", {}) or {}
            for key in end:
                delta = float(end.get(key, 0.0)) - float(start.get(key, 0.0))
                if abs(delta) >= 0.02:
                    deltas[key] = _round(delta)
        phase_changes = [change for change in change_events if change.get("phase_name") == phase_name]
        phase_summaries.append({
            "phase_name": phase_name,
            "top_change_ids": [change["change_id"] for change in phase_changes[:3]],
            "world_state_deltas": deltas,
        })
    return phase_summaries


def _build_insight_cards(
    conclusion: dict[str, Any] | None,
    change_events: list[dict[str, Any]],
    final_relationships: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    insights: list[dict[str, Any]] = []
    relationship_changes = [
        rel for rel in final_relationships
        if abs(float(rel.get("total_trust_delta", 0.0))) > 0.01 or abs(float(rel.get("total_tension_delta", 0.0))) > 0.01
    ]
    drift_changes = [change for change in change_events if change.get("category") == "actor_drift"]
    state_changes = [change for change in change_events if change.get("category") == "world_state"]
    relationship_change = next((change for change in change_events if change.get("category") == "relationship"), None)

    if relationship_changes:
        rel = relationship_changes[0]
        insights.append({
            "insight_id": "insight:relationship",
            "title": "Interpersonal movement was limited",
            "summary": (
                f"Only {len(relationship_changes)} of {len(final_relationships)} directed ties changed materially. "
                f"The clearest movement was {rel['display_label']}."
            ),
            "meaning": "Most stakeholders talked past each other rather than substantially changing trust dynamics.",
            "related_change_ids": [relationship_change["change_id"]] if relationship_change else [],
        })
    else:
        insights.append({
            "insight_id": "insight:relationship_static",
            "title": "Relationship network stayed almost flat",
            "summary": "No stakeholder pair showed a meaningful trust or tension shift across the run.",
            "meaning": "This run produced discussion, but not enough interpersonal movement to reshape the network.",
            "related_change_ids": [],
        })

    if state_changes:
        state_change = state_changes[0]
        insights.append({
            "insight_id": "insight:state",
            "title": f"{state_change['label']} changed structurally",
            "summary": state_change["summary"],
            "meaning": "This is the clearest system-level outcome variable that actually moved.",
            "related_change_ids": [state_change["change_id"]],
        })
    else:
        insights.append({
            "insight_id": "insight:no_state_shift",
            "title": "The run produced little structural outcome change",
            "summary": "No shared world-state variable moved enough to count as a meaningful system-level shift.",
            "meaning": "The conversation generated positions and reactions, but not a strong simulated outcome change.",
            "related_change_ids": [],
        })

    if drift_changes:
        drift_change = drift_changes[0]
        insights.append({
            "insight_id": "insight:drift",
            "title": "Behavior drift mattered more than negotiation movement",
            "summary": drift_change["summary"],
            "meaning": "The most measurable change in this run was actors deviating from their intended persona, not actors changing one another's relationships or the world state.",
            "related_change_ids": [drift_change["change_id"]],
        })

    if conclusion:
        outcome_summary = conclusion.get("outcome_summary", "")
        insights.append({
            "insight_id": "insight:outcome",
            "title": "Narrative outcome",
            "summary": outcome_summary,
            "meaning": "This is the highest-level reading of where the discussion landed, even if the measurable change signals below stayed weak.",
            "related_change_ids": [],
        })

    return insights[:4]


def _build_relationship_analysis(
    runtime_summary: dict[str, Any],
    final_relationships: list[dict[str, Any]],
    actor_names: dict[str, str],
) -> dict[str, Any]:
    turn_map = _turn_lookup(runtime_summary)
    relationship_events = runtime_summary.get("relationship_events", []) or []
    events_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    phase_order = runtime_summary.get("phase_order", []) or []
    for event in relationship_events:
        src = event.get("source_actor_id") or event.get("source") or ""
        tgt = event.get("target_actor_id") or event.get("target") or ""
        if src and tgt:
            events_by_pair[(src, tgt)].append(event)

    pairs: list[dict[str, Any]] = []
    for rel in final_relationships:
        key = (rel["source_actor_id"], rel["target_actor_id"])
        pair_events = events_by_pair.get(key, [])
        phase_map = {
            phase_name: {
                "phase_name": phase_name,
                "trust_delta": 0.0,
                "tension_delta": 0.0,
                "event_count": 0,
            }
            for phase_name in phase_order
        }
        for evt in pair_events:
            phase_name = evt.get("phase_name", "")
            phase_entry = phase_map.setdefault(phase_name, {
                "phase_name": phase_name,
                "trust_delta": 0.0,
                "tension_delta": 0.0,
                "event_count": 0,
            })
            phase_entry["trust_delta"] += float(evt.get("trust_delta", 0.0))
            phase_entry["tension_delta"] += float(evt.get("tension_delta", 0.0))
            phase_entry["event_count"] += 1
        triggers = _relationship_triggers(pair_events, turn_map, actor_names)
        top_evidence = [
            _evidence_item(
                evidence_id=f"evidence:relationship:{rel['relationship_id']}:{idx}",
                evidence_type="relationship",
                actor_id=rel["source_actor_id"],
                other_actor_id=rel["target_actor_id"],
                phase_name=trigger.get("phase_name", ""),
                turn_index=int(trigger.get("turn_index", 0)),
                summary=trigger.get("summary", ""),
                why_it_matters="This exchange directly shifted trust or tension between the two actors.",
                quote=trigger.get("evidence", ""),
                related_relationship_id=rel["relationship_id"],
            )
            for idx, trigger in enumerate(triggers, start=1)
        ]
        pairs.append({
            "relationship_id": rel["relationship_id"],
            "source_actor_id": rel["source_actor_id"],
            "target_actor_id": rel["target_actor_id"],
            "display_label": rel["display_label"],
            "label": rel.get("label", "neutral"),
            "initial": {"trust": rel["initial_trust"], "tension": rel["initial_tension"]},
            "final": {"trust": rel["final_trust"], "tension": rel["final_tension"]},
            "delta": {"trust": rel["total_trust_delta"], "tension": rel["total_tension_delta"]},
            "event_count": rel["event_count"],
            "phase_deltas": [
                {
                    "phase_name": phase_entry["phase_name"],
                    "trust_delta": _round(phase_entry["trust_delta"]),
                    "tension_delta": _round(phase_entry["tension_delta"]),
                    "event_count": phase_entry["event_count"],
                }
                for phase_entry in phase_map.values()
            ],
            "top_trigger_summaries": top_evidence,
        })
    pairs.sort(
        key=lambda item: abs(float(item["delta"]["trust"])) + abs(float(item["delta"]["tension"])),
        reverse=True,
    )
    return {"pairs": pairs}


def _build_actor_analysis(
    runtime_summary: dict[str, Any],
    script: dict[str, Any],
    metrics: dict[str, Any],
    actor_summaries: list[dict[str, Any]],
    relationship_analysis: dict[str, Any],
    actor_names: dict[str, str],
) -> dict[str, Any]:
    turn_map = _turn_lookup(runtime_summary)
    proposal_map = _proposal_lookup(runtime_summary)
    actor_summary_map = {row["actor_id"]: row for row in actor_summaries}
    actors = script.get("stakeholders", []) or []
    actor_map = {
        actor.get("actor_id", ""): actor
        for actor in actors
        if actor.get("actor_id")
    }
    phase_index = _phase_index_map(runtime_summary)

    relationship_evidence_by_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    relationship_changes_by_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for pair in relationship_analysis.get("pairs", []):
        magnitude = abs(float(pair["delta"]["trust"])) + abs(float(pair["delta"]["tension"]))
        if magnitude < 0.01:
            continue
        src = pair["source_actor_id"]
        tgt = pair["target_actor_id"]
        relationship_changes_by_actor[src].append({
            "relationship_id": pair["relationship_id"],
            "counterpart_actor_id": tgt,
            "counterpart_label": actor_names.get(tgt, tgt),
            "direction": "outgoing",
            "trust_delta": pair["delta"]["trust"],
            "tension_delta": pair["delta"]["tension"],
        })
        relationship_changes_by_actor[tgt].append({
            "relationship_id": pair["relationship_id"],
            "counterpart_actor_id": src,
            "counterpart_label": actor_names.get(src, src),
            "direction": "incoming",
            "trust_delta": pair["delta"]["trust"],
            "tension_delta": pair["delta"]["tension"],
        })
        for evidence in pair.get("top_trigger_summaries", []) or []:
            relationship_evidence_by_actor[src].append(dict(evidence))
            relationship_evidence_by_actor[tgt].append({
                **dict(evidence),
                "evidence_id": f"{evidence['evidence_id']}:inbound",
                "actor_id": tgt,
                "other_actor_id": src,
                "summary": (
                    f"{actor_names.get(src, src)} shifted trust toward {actor_names.get(tgt, tgt)} "
                    f"during {evidence.get('phase_name') or 'the run'}."
                ),
                "why_it_matters": "This exchange changed how another actor related to the selected actor.",
                "related_relationship_id": pair["relationship_id"],
            })

    drift_evidence_by_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in runtime_summary.get("actor_state_events", []) or []:
        actor_id = event.get("actor_id", "")
        if not actor_id:
            continue
        new_state = event.get("new_state", {}) or {}
        drift = float(new_state.get("drift_score", 0.0))
        if drift < 0.05:
            continue
        turn_index = int(event.get("turn_index", 0))
        turn = turn_map.get(turn_index, {})
        summary = actor_summary_map.get(actor_id, {})
        largest_shift = summary.get("strongest_trait_shift")
        drift_evidence_by_actor[actor_id].append(_evidence_item(
            evidence_id=f"evidence:drift:{actor_id}:{turn_index}",
            evidence_type="actor_drift",
            actor_id=actor_id,
            phase_name=event.get("phase_name", ""),
            turn_index=turn_index,
            summary=f"{actor_names.get(actor_id, actor_id)} reached drift {drift:.2f}.",
            why_it_matters=(
                "This is where the actor behaved furthest from the intended persona."
                + (
                    f" The strongest trait movement by the end of the run was {largest_shift['trait']}."
                    if largest_shift else ""
                )
            ),
            quote=turn.get("content", ""),
        ))

    action_evidence_by_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for action in runtime_summary.get("executed_actions", []) or []:
        actor_id = action.get("owner_actor_id", "")
        if not actor_id:
            continue
        proposal = proposal_map.get(str(action.get("proposal_id", "")), {})
        turn_index = int(proposal.get("turn_index", 0))
        turn = turn_map.get(turn_index, {})
        target_key = str(action.get("target_key", "shared state"))
        delta_text = ", ".join(
            f"{key} {float(value):+.2f}"
            for key, value in (action.get("applied_delta", {}) or {}).items()
        ) or target_key
        action_evidence_by_actor[actor_id].append(_evidence_item(
            evidence_id=f"evidence:action:{action.get('proposal_id', '')}",
            evidence_type="action",
            actor_id=actor_id,
            phase_name=action.get("phase_name", proposal.get("phase_name", "")),
            turn_index=turn_index,
            summary=f"{actor_names.get(actor_id, actor_id)} executed {str(action.get('action_type', '')).replace('_', ' ')} on {target_key}.",
            why_it_matters=f"This changed shared state through {delta_text}.",
            quote=turn.get("content", ""),
            related_action_id=f"action:{action.get('proposal_id', '')}",
        ))

    actor_items: list[dict[str, Any]] = []
    for actor in actors:
        actor_id = actor.get("actor_id", "")
        if not actor_id:
            continue
        summary = actor_summary_map.get(actor_id, {})
        relationship_changes = sorted(
            relationship_changes_by_actor.get(actor_id, []),
            key=lambda item: abs(float(item["trust_delta"])) + abs(float(item["tension_delta"])),
            reverse=True,
        )
        evidence_by_type = {
            "relationship": sorted(
                relationship_evidence_by_actor.get(actor_id, []),
                key=lambda item: (
                    phase_index.get(item.get("phase_name", ""), len(phase_index)),
                    item.get("turn_index", 0),
                ),
            ),
            "actor_drift": sorted(
                drift_evidence_by_actor.get(actor_id, []),
                key=lambda item: item.get("turn_index", 0),
            ),
            "action": sorted(
                action_evidence_by_actor.get(actor_id, []),
                key=lambda item: item.get("turn_index", 0),
            ),
        }
        all_evidence = evidence_by_type["relationship"] + evidence_by_type["actor_drift"] + evidence_by_type["action"]
        all_evidence.sort(key=lambda item: item.get("turn_index", 0))
        strongest = summary.get("strongest_trait_shift")
        top_change = relationship_changes[0] if relationship_changes else None
        if all_evidence:
            key_evidence = max(all_evidence, key=lambda item: item.get("turn_index", 0))
            narrative = (
                f"{actor_names.get(actor_id, actor_id)} changed most visibly during {key_evidence.get('phase_name') or 'the run'} "
                f"when {key_evidence.get('summary', '').rstrip('.')}. "
            )
        else:
            narrative = f"{actor_names.get(actor_id, actor_id)} showed little measurable movement across the run. "
        if top_change:
            narrative += (
                f"The main counterpart was {top_change.get('counterpart_label', 'another actor')}, "
                f"with trust {float(top_change.get('trust_delta', 0.0)):+.2f} and tension {float(top_change.get('tension_delta', 0.0)):+.2f}."
            )
        elif strongest:
            narrative += f"The clearest measurable shift was in trait {strongest['trait']}."
        else:
            narrative += "No large relationship or persona shift was recorded."

        actor_items.append({
            "actor_id": actor_id,
            "display_name": actor_names.get(actor_id, actor_id),
            "before_summary": {
                "role": actor.get("role", ""),
                "disposition": actor.get("strategic_disposition", "neutral"),
                "incentives": list(actor.get("incentives", []) or []),
                "concerns": list(actor.get("concerns", []) or []),
                "stance": summary.get("initial_stance_summary") or _format_stance_summary(actor),
            },
            "after_summary": {
                "end_state": summary.get("end_state_summary", ""),
                "comparison_text": summary.get("after_summary", summary.get("end_state_summary", "")),
                "drift_interpretation": (
                    "High drift: behavior moved noticeably away from the configured persona."
                    if float(summary.get("final_drift_score", 0.0)) >= 0.2
                    else "Moderate drift: some behavior deviated from the configured persona."
                    if float(summary.get("final_drift_score", 0.0)) >= 0.08
                    else "Low drift: behavior stayed close to the configured persona."
                ),
                "strongest_relationship_change": top_change,
            },
            "initial_traits": actor.get("personality_prior", {}),
            "final_traits": summary.get("final_trait_estimate", metrics.get("actor_trait_estimates", {}).get(actor_id, {})),
            "largest_trait_shift": strongest,
            "final_drift_score": summary.get("final_drift_score", 0.0),
            "relationship_changes": relationship_changes,
            "evidence_by_type": evidence_by_type,
            "change_narrative": narrative,
        })

    actor_items.sort(key=lambda item: item["display_name"])
    return {"actors": actor_items}


def _build_phase_filtered_attribution(
    runtime_summary: dict[str, Any],
    relationship_analysis: dict[str, Any],
    actor_analysis: dict[str, Any],
) -> dict[str, Any]:
    phases = ["__all__"] + list(runtime_summary.get("phase_order", []) or [])
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = {
        phase_name: {"relationship": [], "actor_drift": [], "action": [], "all": []}
        for phase_name in phases
    }

    def add_item(item: dict[str, Any]) -> None:
        evidence_type = str(item.get("type", ""))
        phase_name = item.get("phase_name", "") or "__all__"
        if evidence_type not in {"relationship", "actor_drift", "action"}:
            return
        grouped["__all__"][evidence_type].append(item)
        grouped["__all__"]["all"].append(item)
        if phase_name in grouped:
            grouped[phase_name][evidence_type].append(item)
            grouped[phase_name]["all"].append(item)

    for pair in relationship_analysis.get("pairs", []) or []:
        for item in pair.get("top_trigger_summaries", []) or []:
            add_item(item)
    seen_ids: set[str] = set()
    for actor in actor_analysis.get("actors", []) or []:
        for evidence_items in (actor.get("evidence_by_type", {}) or {}).values():
            for item in evidence_items or []:
                evidence_id = str(item.get("evidence_id", ""))
                if not evidence_id or evidence_id in seen_ids:
                    continue
                seen_ids.add(evidence_id)
                add_item(item)

    for phase_group in grouped.values():
        for key in ("relationship", "actor_drift", "action", "all"):
            phase_group[key].sort(key=lambda item: item.get("turn_index", 0))
    return grouped


def _build_outcome_analysis(
    script: dict[str, Any],
    conclusion: dict[str, Any] | None,
    change_events: list[dict[str, Any]],
    relationship_analysis: dict[str, Any],
    phase_filtered_attribution: dict[str, Any],
) -> dict[str, Any]:
    mode = script.get("simulation_mode", "guided")
    target_outcome = script.get("outcome_spec") if mode == "guided" else None
    actual_outcome = (conclusion or {}).get("outcome_summary", "")

    preferred_changes = [
        change for change in change_events
        if change.get("category") in {"world_state", "relationship", "action"}
    ]
    if not preferred_changes:
        preferred_changes = list(change_events)
    driver_changes = preferred_changes[:3]

    driver_summaries = []
    relationship_pair_map = {
        pair["relationship_id"]: pair
        for pair in relationship_analysis.get("pairs", []) or []
    }
    all_evidence = phase_filtered_attribution["__all__"]["all"]
    for change in driver_changes:
        related_evidence: list[dict[str, Any]] = []
        category = change.get("category")
        if category == "relationship":
            relationship_id = f"rel:{change['affected_actor_ids'][0]}:{change['affected_actor_ids'][1]}"
            related_evidence = list(relationship_pair_map.get(relationship_id, {}).get("top_trigger_summaries", []))
        elif category == "action":
            proposal_id = str(change["change_id"]).split(":")[-1]
            related_evidence = [
                item for item in all_evidence
                if item.get("related_action_id") == f"action:{proposal_id}"
            ]
        elif category == "actor_drift":
            actor_id = (change.get("affected_actor_ids") or [""])[0]
            related_evidence = [
                item for item in all_evidence
                if item.get("type") == "actor_drift" and item.get("actor_id") == actor_id
            ]
        elif category == "world_state":
            related_evidence = [
                item for item in all_evidence
                if item.get("type") == "action"
                and item.get("phase_name") == change.get("phase_name", "")
                and item.get("actor_id") in change.get("affected_actor_ids", [])
            ]
        driver_summaries.append({
            "driver_id": f"driver:{change['change_id']}",
            "change_id": change["change_id"],
            "title": change["label"],
            "summary": change["summary"],
            "why_it_matters": change.get("meaning", "") or "This contributed to the run's outcome.",
            "phase_name": change.get("phase_name", ""),
            "actor_ids": list(change.get("affected_actor_ids", [])),
            "evidence_ids": [item.get("evidence_id") for item in related_evidence[:3]],
        })

    if mode == "guided":
        outcome_key = str((conclusion or {}).get("outcome_achieved", "partial"))
        status_map = {"achieved": "hit", "partial": "partial", "not_achieved": "miss"}
        outcome_status = status_map.get(outcome_key, "partial")
        difference_summary = {
            "hit": "The simulation broadly landed on the intended target outcome.",
            "partial": "The simulation moved toward the intended target outcome but did not fully reach it.",
            "miss": "The simulation ended away from the intended target outcome.",
        }[outcome_status]
        derivation_summary = " ".join((conclusion or {}).get("contributing_factors", [])[:3]).strip()
        if not derivation_summary:
            derivation_summary = "The result was inferred from the final conclusion and the strongest measured changes in the run."
        return {
            "mode": mode,
            "target_outcome": target_outcome,
            "actual_outcome": actual_outcome,
            "outcome_status": outcome_status,
            "difference_summary": difference_summary,
            "derivation_summary": derivation_summary,
            "driver_change_ids": [change["change_id"] for change in driver_changes],
            "driver_summaries": driver_summaries,
        }

    derivation_summary = " ".join(
        ((conclusion or {}).get("key_discoveries", []) or [])[:2]
        + ((conclusion or {}).get("emergent_patterns", []) or [])[:1]
    ).strip()
    if not derivation_summary:
        top_pair = next(iter(relationship_analysis.get("pairs", [])), None)
        if top_pair and (
            abs(float(top_pair["delta"]["trust"])) > 0.01
            or abs(float(top_pair["delta"]["tension"])) > 0.01
        ):
            derivation_summary = (
                f"The clearest interpersonal movement came from {top_pair['display_label']}, "
                f"which helped shape the emergent outcome."
            )
        else:
            derivation_summary = "The outcome summary is based on the final conclusion plus the clearest measurable shifts in the run."
    return {
        "mode": mode,
        "target_outcome": None,
        "actual_outcome": actual_outcome,
        "outcome_status": "emergent",
        "difference_summary": "Exploratory mode does not compare against a fixed target; it explains what emerged instead.",
        "derivation_summary": derivation_summary,
        "driver_change_ids": [change["change_id"] for change in driver_changes],
        "driver_summaries": driver_summaries,
    }


def ensure_results_analysis(result: dict[str, Any]) -> dict[str, Any]:
    """Attach normalized result analysis fields in-place if they are missing."""
    if not result:
        return result
    if result.get("analysis_version") == ANALYSIS_VERSION:
        return result

    runtime_summary = result.get("runtime_summary", {}) or {}
    script = result.get("script", {}) or {}
    metrics = result.get("metrics", {}) or {}
    conclusion = result.get("conclusion")
    actor_names = runtime_summary.get("actor_labels") or runtime_summary.get("actor_display_names") or {}

    initial_relationships = _build_initial_relationships(script, actor_names)
    final_relationships = _build_final_relationships(runtime_summary, initial_relationships, actor_names)
    actor_final_state_summary = _build_actor_final_state_summary(
        runtime_summary,
        metrics,
        final_relationships,
        conclusion,
        script,
        actor_names,
    )
    change_events, change_attribution = _build_change_events(
        runtime_summary,
        script,
        metrics,
        final_relationships,
        actor_final_state_summary,
        actor_names,
    )
    phase_summaries = _build_phase_summaries(runtime_summary, change_events)
    relationship_analysis = _build_relationship_analysis(runtime_summary, final_relationships, actor_names)
    actor_analysis = _build_actor_analysis(
        runtime_summary,
        script,
        metrics,
        actor_final_state_summary,
        relationship_analysis,
        actor_names,
    )
    phase_filtered_attribution = _build_phase_filtered_attribution(
        runtime_summary,
        relationship_analysis,
        actor_analysis,
    )
    outcome_analysis = _build_outcome_analysis(
        script,
        conclusion,
        change_events,
        relationship_analysis,
        phase_filtered_attribution,
    )
    insight_cards = _build_insight_cards(conclusion, change_events, final_relationships)

    result["initial_relationships"] = initial_relationships
    result["final_relationships"] = final_relationships
    result["actor_final_state_summary"] = actor_final_state_summary
    result["change_events"] = change_events
    result["change_attribution"] = change_attribution
    result["phase_summaries"] = phase_summaries
    result["relationship_analysis"] = relationship_analysis
    result["actor_analysis"] = actor_analysis
    result["phase_filtered_attribution"] = phase_filtered_attribution
    result["outcome_analysis"] = outcome_analysis
    result["insight_cards"] = insight_cards
    result["analysis_version"] = ANALYSIS_VERSION
    return result
