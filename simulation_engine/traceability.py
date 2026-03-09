"""Post-run trace bundle generation for benchmark explainability."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Any


def build_trace_bundle(results: dict[str, Any], output_dir: str | Path) -> dict[str, str]:
    """Write structured trace files that support run/turn/action drill-down."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    trace_views_dir = output_path / "trace_views"
    trace_views_dir.mkdir(parents=True, exist_ok=True)

    suite_id = str(results.get("suite_id") or dict(results.get("config", {})).get("suite_id") or "suite_unknown")
    runs = [dict(run) for run in results.get("runs", [])]

    builder_rows_by_id: dict[str, dict[str, Any]] = {}
    run_outcomes: list[dict[str, Any]] = []
    turn_decisions: list[dict[str, Any]] = []
    candidate_scores: list[dict[str, Any]] = []
    action_events: list[dict[str, Any]] = []
    world_state_deltas: list[dict[str, Any]] = []
    relationship_events: list[dict[str, Any]] = []
    metric_attributions: list[dict[str, Any]] = []
    trace_events: list[dict[str, Any]] = []

    for index, run in enumerate(runs, start=1):
        runtime_summary = dict(run.get("runtime_summary", {}))
        metrics = dict(run.get("metrics", {}))
        run_id = str(run.get("run_id") or runtime_summary.get("run_id") or f"{suite_id}:run:{index}")
        track_id = str(run.get("track_id") or runtime_summary.get("track_id") or runtime_summary.get("simulation_mode") or "unknown")
        simulation_id = str(run.get("simulation_id") or runtime_summary.get("simulation_id") or f"simulation_{index}")
        builder_trace_id = str(
            run.get("builder_trace_ref")
            or runtime_summary.get("builder_trace_ref")
            or f"manual:{simulation_id}"
        )
        builder_row = _normalize_builder_trace(
            runtime_summary=runtime_summary,
            builder_trace_id=builder_trace_id,
            simulation_id=simulation_id,
        )
        builder_rows_by_id[builder_trace_id] = builder_row

        selection_map = _selection_audit_map(run)
        state_event_map = _state_event_map(runtime_summary)
        relationship_event_map = _relationship_event_map(runtime_summary, run_id)
        action_audits = list(runtime_summary.get("action_audits") or [])
        action_audits_by_turn: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for audit in action_audits:
            turn_trace_id = _normalize_turn_trace_id(
                run_id,
                dict(audit).get("turn_trace_id"),
                actor_id=str(dict(audit).get("actor_id") or ""),
                phase_name=str(dict(audit).get("phase_name") or ""),
                turn_index=int(dict(audit).get("turn_index") or 0),
            )
            audit["turn_trace_id"] = turn_trace_id
            action_audits_by_turn[turn_trace_id].append(audit)

        for event_group in relationship_event_map.values():
            for event in event_group:
                relationship_events.append(event)
                trace_events.append({"event_type": "relationship_event", **event})

        candidate_id_by_turn_slot: dict[tuple[str, str], str] = {}
        turns = list(runtime_summary.get("turns") or [])
        actor_envelopes = dict(runtime_summary.get("actor_personality_envelopes") or {})
        for turn in turns:
            turn_actor_id = str(turn.get("actor_id") or "")
            phase_name = str(turn.get("phase_name") or "")
            turn_index = int(turn.get("turn_index") or 0)
            turn_trace_id = _normalize_turn_trace_id(
                run_id,
                dict(turn.get("metadata") or {}).get("turn_trace_id"),
                actor_id=turn_actor_id,
                phase_name=phase_name,
                turn_index=turn_index,
            )
            phase_trace_id = f"{run_id}:{phase_name}"
            audit = selection_map.get((turn_actor_id, phase_name, turn_index))

            selected_candidate_trace_id = ""
            if audit:
                for rank, score_row in enumerate(list(audit.get("score_rows") or []), start=1):
                    slot = str(score_row.get("slot") or f"slot_{rank}")
                    candidate_trace_id = f"{turn_trace_id}:candidate:{slot}"
                    candidate_id_by_turn_slot[(turn_trace_id, slot)] = candidate_trace_id
                    is_selected = rank - 1 == int(audit.get("selected_index", -1))
                    if is_selected:
                        selected_candidate_trace_id = candidate_trace_id
                    row = {
                        "candidate_trace_id": candidate_trace_id,
                        "turn_trace_id": turn_trace_id,
                        "slot": slot,
                        "rank": rank,
                        "selected": is_selected,
                        "candidate_text_excerpt": score_row.get("text_excerpt", ""),
                        "inferred_traits": dict(score_row.get("inferred_traits") or {}),
                        "trait_error_map": dict(score_row.get("trait_error_map") or {}),
                        "score_total": round(float(score_row.get("score", 0.0)), 4),
                        "score_components": dict(score_row.get("score_components") or {}),
                        "penalty_components": dict(score_row.get("penalty_components") or {}),
                        "tie_detected": bool(audit.get("tie_detected", False)),
                        "tie_break_axis": audit.get("tie_break_axis", "none"),
                        "tie_break_reason": audit.get("tie_break_reason", ""),
                        "planned_action_artifact": dict(score_row.get("planned_action_artifact") or {}),
                        "compiled_action_family": score_row.get("compiled_action_family") or "none",
                    }
                    candidate_scores.append(row)
                    trace_events.append({"event_type": "candidate_score", **row})

            selected_slot = str(
                (audit or {}).get("selected_slot")
                or dict(turn.get("metadata") or {}).get("slot")
                or ""
            )
            if not selected_candidate_trace_id and selected_slot:
                selected_candidate_trace_id = candidate_id_by_turn_slot.get((turn_trace_id, selected_slot), "")

            selection_state = _select_state_event(state_event_map, turn_actor_id, phase_name, turn_index)
            drift_before = _nested_float(selection_state, "prior_state", "drift_score")
            drift_after = _nested_float(selection_state, "new_state", "drift_score")
            turn_rel_events = relationship_event_map.get(turn_trace_id, [])
            turn_action_audits = action_audits_by_turn.get(turn_trace_id, [])
            action_trace_id = str(
                (turn_action_audits[0].get("trace_id") if turn_action_audits else "")
                or dict(turn.get("metadata") or {}).get("action_audit_trace_id")
                or ""
            )
            fallback_meta = dict(dict(turn.get("metadata") or {}).get("generation_meta") or {})
            turn_row = {
                "turn_trace_id": turn_trace_id,
                "run_id": run_id,
                "track_id": track_id,
                "phase_name": phase_name,
                "turn_index": turn_index,
                "actor_id": turn_actor_id,
                "actor_role": dict(runtime_summary.get("actor_labels") or {}).get(turn_actor_id, ""),
                "input_state_ref": f"state:{phase_trace_id}:before:{turn_index}",
                "policy_plan_ref": f"policy_plan:{turn_trace_id}" if dict(turn.get("metadata") or {}).get("policy_plan") else "",
                "selected_candidate_trace_id": selected_candidate_trace_id,
                "selection_reason_summary": _selection_reason_summary(audit),
                "drift_before": drift_before,
                "drift_after": drift_after,
                "drift_delta": _round_or_none((drift_after - drift_before) if drift_before is not None and drift_after is not None else None),
                "envelope_before": _envelope_summary(
                    _nested_dict(selection_state, "prior_state", "last_inferred_traits"),
                    actor_envelopes.get(turn_actor_id, {}),
                ),
                "envelope_after": _envelope_summary(
                    _nested_dict(selection_state, "new_state", "last_inferred_traits"),
                    actor_envelopes.get(turn_actor_id, {}),
                ),
                "relationship_before": [
                    {
                        "target_actor_id": event.get("target_actor_id"),
                        "sentiment": event.get("prior_sentiment"),
                        "trust": event.get("prior_trust"),
                        "tension": event.get("prior_tension"),
                    }
                    for event in turn_rel_events
                ],
                "relationship_after": [
                    {
                        "target_actor_id": event.get("target_actor_id"),
                        "sentiment": event.get("new_sentiment"),
                        "trust": event.get("new_trust"),
                        "tension": event.get("new_tension"),
                    }
                    for event in turn_rel_events
                ],
                "action_trace_id": action_trace_id,
                "fallback_used": bool(fallback_meta.get("used_fallback", False)),
                "fallback_type": str(fallback_meta.get("fallback_type") or ""),
            }
            turn_decisions.append(turn_row)
            trace_events.append({"event_type": "turn_decision", **turn_row})

        for audit in action_audits:
            action_trace_id = str(audit.get("trace_id") or audit.get("proposal_id") or "")
            owner_actor_id = (
                dict(audit.get("compiled_proposal") or {}).get("owner_actor_id")
                or dict(audit.get("executed_action") or {}).get("owner_actor_id")
                or ""
            )
            compile_row = {
                "action_trace_id": action_trace_id,
                "turn_trace_id": audit.get("turn_trace_id", ""),
                "proposal_id": audit.get("proposal_id"),
                "phase_name": audit.get("phase_name"),
                "actor_id": audit.get("actor_id"),
                "event_type": "compile",
                "compiled_proposal": dict(audit.get("compiled_proposal") or {}),
                "validation_trace": list(audit.get("validation_trace") or []),
                "arbitration_status": "",
                "rejection_reason": audit.get("compile_rejection_reason"),
                "execution_status": "",
                "coherence_score": None,
                "owner_actor_id": owner_actor_id,
            }
            action_events.append(compile_row)
            trace_events.append({"event_type": "action_event", **compile_row})

            if audit.get("arbitration_status") or audit.get("arbitration_reason"):
                arbitration_row = {
                    **compile_row,
                    "event_type": "arbitration",
                    "arbitration_status": audit.get("arbitration_status") or "",
                    "rejection_reason": audit.get("arbitration_reason") or "",
                }
                action_events.append(arbitration_row)
                trace_events.append({"event_type": "action_event", **arbitration_row})

            if audit.get("execution_status") or audit.get("executed_action"):
                executed = dict(audit.get("executed_action") or {})
                execution_row = {
                    **compile_row,
                    "event_type": "execution",
                    "execution_status": audit.get("execution_status") or "",
                    "rejection_reason": audit.get("execution_rejection_reason") or "",
                    "coherence_score": _round_or_none(executed.get("coherence_score")),
                    "owner_actor_id": owner_actor_id or executed.get("owner_actor_id") or "",
                }
                action_events.append(execution_row)
                trace_events.append({"event_type": "action_event", **execution_row})

            if audit.get("pre_state") is not None or audit.get("post_state") is not None or audit.get("executed_action"):
                executed = dict(audit.get("executed_action") or {})
                delta = dict(executed.get("applied_delta") or _state_delta(audit.get("pre_state"), audit.get("post_state")))
                world_row = {
                    "action_trace_id": action_trace_id,
                    "turn_trace_id": audit.get("turn_trace_id", ""),
                    "phase_trace_id": f"{run_id}:{audit.get('phase_name', '')}",
                    "pre_state": dict(audit.get("pre_state") or {}),
                    "delta": delta,
                    "post_state": dict(audit.get("post_state") or {}),
                    "causal_keys": list(delta.keys()),
                    "transition_rule_ref": f"{audit.get('phase_name', '')}:{dict(audit.get('compiled_proposal') or {}).get('action_type', '')}",
                }
                world_state_deltas.append(world_row)
                trace_events.append({"event_type": "world_state_delta", **world_row})

        run_metric_rows = _build_metric_attributions(
            run_id=run_id,
            track_id=track_id,
            metrics=metrics,
            runtime_summary=runtime_summary,
            relationship_events=relationship_event_map,
            turn_decisions=turn_decisions,
            builder_row=builder_row,
        )
        metric_attributions.extend(run_metric_rows)
        trace_events.extend({"event_type": "metric_attribution", **row} for row in run_metric_rows)

        run_outcome = {
            "run_id": run_id,
            "suite_id": suite_id,
            "track_id": track_id,
            "simulation_id": simulation_id,
            "scenario_family": runtime_summary.get("scenario_family", "generic"),
            "builder_trace_id": builder_trace_id,
            "clean_status": "clean" if float(metrics.get("fallback_utterance_rate", 0.0)) < 0.30 else "contaminated",
            "fallback_summary": {
                "fallback_utterance_rate": round(float(metrics.get("fallback_utterance_rate", 0.0)), 4),
                "fallback_type_rates": dict(metrics.get("fallback_type_rates") or {}),
            },
            "headline_metrics": {
                "persona_drift_mae": metrics.get("persona_drift_mae", 0.0),
                "per_trait_error_mean": dict(metrics.get("per_trait_error_mean") or {}),
                "envelope_violations": metrics.get("envelope_violations", 0),
                "commitment_contradiction_rate": metrics.get("commitment_contradiction_rate", 0.0),
                "relationship_shift_rate": metrics.get("relationship_shift_rate", 0.0),
                "relationship_overshoot_rate": metrics.get("relationship_overshoot_rate", 0.0),
                "action_family_convergence_rate": metrics.get("action_family_convergence_rate", 0.0),
                "role_action_diversity_score": metrics.get("role_action_diversity_score", 0.0),
            },
            "top_drivers": _top_driver_summary(run_metric_rows, scope_id=run_id),
            "top_failures": _top_failure_summary(run_metric_rows, builder_row),
            "phase_refs": [
                f"{run_id}:{phase_name}"
                for phase_name in dict.fromkeys(
                    str(turn.get("phase_name") or "")
                    for turn in turns
                )
                if phase_name
            ],
        }
        run_outcomes.append(run_outcome)

    track_outcomes = _build_track_outcomes(
        suite_id=suite_id,
        run_outcomes=run_outcomes,
        metric_attributions=metric_attributions,
    )
    metric_attributions.extend(
        _build_track_metric_attributions(track_outcomes=track_outcomes)
    )

    suite_manifest = {
        "saved_at": datetime.now().isoformat(),
        "suite_id": suite_id,
        "config": dict(results.get("config", {})),
        "total_runs": len(runs),
        "trace_version": 1,
        "files": {
            "suite_manifest": str(output_path / "suite_manifest.json"),
            "track_outcomes": str(output_path / "track_outcomes.json"),
            "run_outcomes": str(output_path / "run_outcomes.json"),
            "builder_trace": str(output_path / "builder_trace.json"),
            "trace_events": str(output_path / "trace_events.jsonl"),
            "turn_decisions": str(trace_views_dir / "turn_decisions.jsonl"),
            "candidate_scores": str(trace_views_dir / "candidate_scores.jsonl"),
            "action_events": str(trace_views_dir / "action_events.jsonl"),
            "world_state_deltas": str(trace_views_dir / "world_state_deltas.jsonl"),
            "relationship_events": str(trace_views_dir / "relationship_events.jsonl"),
            "metric_attributions": str(trace_views_dir / "metric_attributions.jsonl"),
        },
    }

    paths = {
        "suite_manifest": str(output_path / "suite_manifest.json"),
        "track_outcomes": str(output_path / "track_outcomes.json"),
        "run_outcomes": str(output_path / "run_outcomes.json"),
        "builder_trace": str(output_path / "builder_trace.json"),
        "trace_events": str(output_path / "trace_events.jsonl"),
        "turn_decisions": str(trace_views_dir / "turn_decisions.jsonl"),
        "candidate_scores": str(trace_views_dir / "candidate_scores.jsonl"),
        "action_events": str(trace_views_dir / "action_events.jsonl"),
        "world_state_deltas": str(trace_views_dir / "world_state_deltas.jsonl"),
        "relationship_events": str(trace_views_dir / "relationship_events.jsonl"),
        "metric_attributions": str(trace_views_dir / "metric_attributions.jsonl"),
    }

    _write_json(paths["suite_manifest"], suite_manifest)
    _write_json(paths["track_outcomes"], track_outcomes)
    _write_json(paths["run_outcomes"], run_outcomes)
    _write_json(paths["builder_trace"], list(builder_rows_by_id.values()))
    _write_jsonl(paths["trace_events"], trace_events)
    _write_jsonl(paths["turn_decisions"], turn_decisions)
    _write_jsonl(paths["candidate_scores"], candidate_scores)
    _write_jsonl(paths["action_events"], action_events)
    _write_jsonl(paths["world_state_deltas"], world_state_deltas)
    _write_jsonl(paths["relationship_events"], relationship_events)
    _write_jsonl(paths["metric_attributions"], metric_attributions)

    for run in results.get("runs", []):
        runtime_summary = dict(run.get("runtime_summary", {}))
        runtime_summary["trace_refs"] = {
            **paths,
            "run_id": run.get("run_id") or runtime_summary.get("run_id"),
            "builder_trace_id": run.get("builder_trace_ref") or runtime_summary.get("builder_trace_ref"),
        }
        run["runtime_summary"] = runtime_summary
        run["trace_bundle_path"] = str(output_path)

    results["trace_bundle"] = dict(paths)
    return paths


def _write_json(path: str | Path, payload: Any) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, default=str))


def _write_jsonl(path: str | Path, rows: list[dict[str, Any]]) -> None:
    handle = Path(path)
    with handle.open("w") as stream:
        for row in rows:
            stream.write(json.dumps(row, default=str))
            stream.write("\n")


def _selection_audit_map(run: dict[str, Any]) -> dict[tuple[str, str, int], dict[str, Any]]:
    audits = list(run.get("selection_audits") or [])
    runtime_summary = dict(run.get("runtime_summary", {}))
    for turn in runtime_summary.get("turns", []):
        audit = dict(dict(turn.get("metadata") or {}).get("audit") or {})
        if audit:
            audits.append(audit)
    return {
        (
            str(audit.get("actor_id") or ""),
            str(audit.get("phase_name") or ""),
            int(audit.get("turn_index") or 0),
        ): audit
        for audit in audits
    }


def _state_event_map(runtime_summary: dict[str, Any]) -> dict[tuple[str, str, int], list[dict[str, Any]]]:
    rows: dict[tuple[str, str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in runtime_summary.get("actor_state_events", []) or []:
        key = (
            str(row.get("actor_id") or ""),
            str(row.get("phase_name") or ""),
            int(row.get("turn_index") or 0),
        )
        rows[key].append(dict(row))
    return rows


def _relationship_event_map(runtime_summary: dict[str, Any], run_id: str) -> dict[str, list[dict[str, Any]]]:
    turns = list(runtime_summary.get("turns") or [])
    turn_lookup = {
        (
            str(turn.get("actor_id") or ""),
            int(turn.get("turn_index") or 0),
        ): _normalize_turn_trace_id(
            run_id,
            dict(turn.get("metadata") or {}).get("turn_trace_id"),
            actor_id=str(turn.get("actor_id") or ""),
            phase_name=str(turn.get("phase_name") or ""),
            turn_index=int(turn.get("turn_index") or 0),
        )
        for turn in turns
    }
    rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in runtime_summary.get("relationship_events", []) or []:
        event = dict(row)
        turn_trace_id = _normalize_turn_trace_id(
            run_id,
            event.get("turn_trace_id"),
            actor_id=str(event.get("source_actor_id") or ""),
            phase_name="",
            turn_index=int(event.get("turn_index") or 0),
        )
        if not event.get("turn_trace_id"):
            turn_trace_id = turn_lookup.get(
                (str(event.get("source_actor_id") or ""), int(event.get("turn_index") or 0)),
                turn_trace_id,
            )
        event["turn_trace_id"] = turn_trace_id
        rows[turn_trace_id].append(event)
    return rows


def _normalize_turn_trace_id(
    run_id: str,
    trace_id: Any,
    *,
    actor_id: str,
    phase_name: str,
    turn_index: int,
) -> str:
    trace_value = str(trace_id or "").strip()
    if trace_value.startswith(f"{run_id}:"):
        return trace_value
    if trace_value:
        return f"{run_id}:{trace_value}"
    phase_part = phase_name or "unknown_phase"
    return f"{run_id}:{phase_part}:{turn_index}:{actor_id or 'unknown_actor'}"


def _select_state_event(
    state_event_map: dict[tuple[str, str, int], list[dict[str, Any]]],
    actor_id: str,
    phase_name: str,
    turn_index: int,
) -> dict[str, Any]:
    rows = state_event_map.get((actor_id, phase_name, turn_index), [])
    if not rows:
        return {}
    rows = sorted(
        rows,
        key=lambda row: 0 if row.get("cause_type") == "candidate_selection" else 1,
    )
    return rows[0]


def _nested_float(row: dict[str, Any], outer: str, inner: str) -> float | None:
    try:
        return _round_or_none(float(dict(row.get(outer) or {}).get(inner)))
    except (TypeError, ValueError):
        return None


def _nested_dict(row: dict[str, Any], outer: str, inner: str) -> dict[str, Any]:
    return dict(dict(row.get(outer) or {}).get(inner) or {})


def _round_or_none(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return round(float(value), 4)
    except (TypeError, ValueError):
        return None


def _envelope_summary(traits: dict[str, Any], envelope: dict[str, Any]) -> dict[str, Any]:
    if not traits or not envelope:
        return {"violations": 0, "trait_violations": {}}
    violations: dict[str, float] = {}
    for trait, value in traits.items():
        bounds = envelope.get(trait)
        if not bounds or len(bounds) != 2:
            continue
        low, high = float(bounds[0]), float(bounds[1])
        observed = float(value)
        if observed < low:
            violations[trait] = round(low - observed, 4)
        elif observed > high:
            violations[trait] = round(observed - high, 4)
    return {
        "violations": len(violations),
        "trait_violations": violations,
    }


def _selection_reason_summary(audit: dict[str, Any] | None) -> dict[str, Any]:
    if not audit:
        return {
            "top_positive_drivers": [],
            "top_negative_drivers": [],
            "tie_break_axis": "none",
            "tie_break_reason": "",
        }
    return {
        "top_positive_drivers": list(audit.get("selected_top_positive_drivers") or []),
        "top_negative_drivers": list(audit.get("selected_top_negative_drivers") or []),
        "tie_break_axis": audit.get("tie_break_axis", "none"),
        "tie_break_reason": audit.get("tie_break_reason", ""),
    }


def _state_delta(pre_state: Any, post_state: Any) -> dict[str, float]:
    before = dict(pre_state or {})
    after = dict(post_state or {})
    delta: dict[str, float] = {}
    for key in sorted(set(before) | set(after)):
        change = round(float(after.get(key, 0.0)) - float(before.get(key, 0.0)), 4)
        if abs(change) > 0.0:
            delta[key] = change
    return delta


def _normalize_builder_trace(
    *,
    runtime_summary: dict[str, Any],
    builder_trace_id: str,
    simulation_id: str,
) -> dict[str, Any]:
    builder_trace = dict(runtime_summary.get("builder_trace", {}) or {})
    missing_fields = list(builder_trace.get("missing_contract_fields") or [])
    completeness = builder_trace.get("metadata_completeness_score")
    if completeness is None:
        completeness = runtime_summary.get("metadata_completeness_score")
    if completeness is None:
        completeness = 1.0 if not missing_fields else max(0.0, 1.0 - (len(missing_fields) / 8.0))
    return {
        "builder_trace_id": builder_trace.get("builder_trace_id") or builder_trace_id,
        "brief_id": builder_trace.get("brief_id") or simulation_id,
        "builder_version": builder_trace.get("builder_version") or ("manual_script_v1" if builder_trace_id.startswith("manual:") else "generated_v1"),
        "generation_attempts": int(builder_trace.get("generation_attempts") or 0),
        "scenario_family": builder_trace.get("scenario_family") or runtime_summary.get("scenario_family", "generic"),
        "input_understanding": builder_trace.get("input_understanding") or {"source_type": "manual_script" if builder_trace_id.startswith("manual:") else "generated_script"},
        "stakeholder_extraction": builder_trace.get("stakeholder_extraction") or [],
        "stakeholder_expansion": builder_trace.get("stakeholder_expansion") or [],
        "phase_template_selection": builder_trace.get("phase_template_selection") or {},
        "world_state_schema_selection": builder_trace.get("world_state_schema_selection") or {},
        "allowed_action_types_selection": builder_trace.get("allowed_action_types_selection") or {},
        "transition_rules_selection": builder_trace.get("transition_rules_selection") or {},
        "phase_action_policies_generation": builder_trace.get("phase_action_policies_generation") or {},
        "actor_action_preferences_generation": builder_trace.get("actor_action_preferences_generation") or {},
        "metadata_completeness_score": round(float(completeness), 4),
        "missing_contract_fields": missing_fields,
    }


def _build_metric_attributions(
    *,
    run_id: str,
    track_id: str,
    metrics: dict[str, Any],
    runtime_summary: dict[str, Any],
    relationship_events: dict[str, list[dict[str, Any]]],
    turn_decisions: list[dict[str, Any]],
    builder_row: dict[str, Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    per_trait_errors = dict(metrics.get("per_trait_error_mean") or {})
    top_trait_rows = sorted(
        (
            {"name": f"{trait}_error", "value": round(float(value), 4)}
            for trait, value in per_trait_errors.items()
        ),
        key=lambda row: row["value"],
        reverse=True,
    )[:3]
    envelope_after_rows = [
        decision
        for decision in turn_decisions
        if decision.get("run_id") == run_id
    ]
    envelope_support = [
        decision["turn_trace_id"]
        for decision in envelope_after_rows
        if int(dict(decision.get("envelope_after") or {}).get("violations", 0)) > 0
    ][:5]
    relationship_rows = []
    for turn_trace_id, events in relationship_events.items():
        for event in events:
            shift = max(
                abs(float(event.get("new_trust", 0.5)) - float(event.get("prior_trust", 0.5))),
                abs(float(event.get("new_tension", 0.0)) - float(event.get("prior_tension", 0.0))),
            )
            relationship_rows.append({"turn_trace_id": turn_trace_id, "value": round(shift, 4)})
    relationship_rows.sort(key=lambda row: row["value"], reverse=True)

    phase_histogram = dict(runtime_summary.get("phase_action_family_histogram") or {})
    convergence_rows = []
    for phase_name, histogram in phase_histogram.items():
        duplicates = max(0, sum(histogram.values()) - len(histogram))
        if duplicates:
            convergence_rows.append({"name": f"{phase_name}_duplicate_families", "value": float(duplicates)})

    builder_missing = [
        {"name": f"builder_missing_{field}", "value": 1.0}
        for field in builder_row.get("missing_contract_fields", [])
    ]
    fallback_rows = [
        {"name": f"fallback_{fallback_type}", "value": round(float(rate), 4)}
        for fallback_type, rate in dict(metrics.get("fallback_type_rates") or {}).items()
    ]

    rows.append(
        {
            "scope_type": "run",
            "scope_id": run_id,
            "track_id": track_id,
            "metric_name": "persona_drift_mae",
            "metric_value": round(float(metrics.get("persona_drift_mae", 0.0)), 4),
            "top_contributors": top_trait_rows,
            "top_counterexamples": [],
            "supporting_trace_ids": envelope_support or [run_id],
        }
    )
    rows.append(
        {
            "scope_type": "run",
            "scope_id": run_id,
            "track_id": track_id,
            "metric_name": "envelope_violations",
            "metric_value": round(float(metrics.get("envelope_violations", 0.0)), 4),
            "top_contributors": [
                {"name": "persistent_envelope_breach", "value": float(len(envelope_support))}
            ] + top_trait_rows[:2],
            "top_counterexamples": [],
            "supporting_trace_ids": envelope_support or [run_id],
        }
    )
    rows.append(
        {
            "scope_type": "run",
            "scope_id": run_id,
            "track_id": track_id,
            "metric_name": "relationship_shift_rate",
            "metric_value": round(float(metrics.get("relationship_shift_rate", 0.0)), 4),
            "top_contributors": relationship_rows[:3],
            "top_counterexamples": [],
            "supporting_trace_ids": [row["turn_trace_id"] for row in relationship_rows[:5]] or [run_id],
        }
    )
    rows.append(
        {
            "scope_type": "run",
            "scope_id": run_id,
            "track_id": track_id,
            "metric_name": "relationship_overshoot_rate",
            "metric_value": round(float(metrics.get("relationship_overshoot_rate", 0.0)), 4),
            "top_contributors": relationship_rows[:3],
            "top_counterexamples": [],
            "supporting_trace_ids": [row["turn_trace_id"] for row in relationship_rows[:5]] or [run_id],
        }
    )
    rows.append(
        {
            "scope_type": "run",
            "scope_id": run_id,
            "track_id": track_id,
            "metric_name": "action_family_convergence_rate",
            "metric_value": round(float(metrics.get("action_family_convergence_rate", 0.0)), 4),
            "top_contributors": convergence_rows[:3],
            "top_counterexamples": [],
            "supporting_trace_ids": [run_id],
        }
    )
    rows.append(
        {
            "scope_type": "run",
            "scope_id": run_id,
            "track_id": track_id,
            "metric_name": "fallback_utterance_rate",
            "metric_value": round(float(metrics.get("fallback_utterance_rate", 0.0)), 4),
            "top_contributors": fallback_rows or [{"name": "low_fallback", "value": 0.0}],
            "top_counterexamples": [],
            "supporting_trace_ids": [run_id],
        }
    )
    rows.append(
        {
            "scope_type": "run",
            "scope_id": run_id,
            "track_id": track_id,
            "metric_name": "builder_completeness",
            "metric_value": round(float(builder_row.get("metadata_completeness_score", 1.0)), 4),
            "top_contributors": builder_missing[:4] or [{"name": "builder_complete", "value": 1.0}],
            "top_counterexamples": [],
            "supporting_trace_ids": [builder_row.get("builder_trace_id", run_id)],
        }
    )
    return rows


def _top_driver_summary(metric_rows: list[dict[str, Any]], *, scope_id: str) -> list[dict[str, Any]]:
    drivers: list[dict[str, Any]] = []
    for row in metric_rows:
        if row.get("scope_id") != scope_id:
            continue
        for contributor in row.get("top_contributors", []):
            drivers.append(
                {
                    "metric": row.get("metric_name"),
                    "source_type": contributor.get("name"),
                    "estimated_contribution": contributor.get("value", 0.0),
                    "supporting_trace_ids": list(row.get("supporting_trace_ids", []))[:3],
                }
            )
    return sorted(drivers, key=lambda item: abs(float(item.get("estimated_contribution", 0.0))), reverse=True)[:5]


def _top_failure_summary(metric_rows: list[dict[str, Any]], builder_row: dict[str, Any]) -> list[dict[str, Any]]:
    failures = [
        row
        for row in _top_driver_summary(metric_rows, scope_id=str(metric_rows[0]["scope_id"]) if metric_rows else "")
        if (
            str(row.get("source_type", "")).startswith("builder_missing_")
            or str(row.get("source_type", "")).startswith("fallback_")
            or "duplicate" in str(row.get("source_type", ""))
        )
    ]
    if not failures and builder_row.get("missing_contract_fields"):
        failures = [
            {
                "metric": "builder_completeness",
                "source_type": f"builder_missing_{builder_row['missing_contract_fields'][0]}",
                "estimated_contribution": 1.0,
                "supporting_trace_ids": [builder_row.get("builder_trace_id", "")],
            }
        ]
    return failures[:5]


def _build_track_outcomes(
    *,
    suite_id: str,
    run_outcomes: list[dict[str, Any]],
    metric_attributions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_track: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in run_outcomes:
        by_track[str(row.get("track_id") or "unknown")].append(row)

    track_outcomes: list[dict[str, Any]] = []
    headline_metric_keys = (
        "persona_drift_mae",
        "envelope_violations",
        "commitment_contradiction_rate",
        "relationship_shift_rate",
        "relationship_overshoot_rate",
        "action_family_convergence_rate",
        "role_action_diversity_score",
    )
    headline_by_track: dict[str, dict[str, float]] = {}
    for track_id, rows in by_track.items():
        headline_metrics = {
            metric: round(
                mean(float(dict(row.get("headline_metrics") or {}).get(metric, 0.0)) for row in rows),
                4,
            )
            for metric in headline_metric_keys
        }
        headline_by_track[track_id] = headline_metrics
        driver_counter = Counter()
        for attribution in metric_attributions:
            if attribution.get("track_id") != track_id or attribution.get("scope_type") != "run":
                continue
            for contributor in attribution.get("top_contributors", []):
                driver_counter[str(contributor.get("name") or "unknown")] += 1
        top_negative_drivers = [
            {"source_type": name, "count": count}
            for name, count in driver_counter.most_common(5)
        ]
        track_outcomes.append(
            {
                "suite_id": suite_id,
                "track_id": track_id,
                "num_runs": len(rows),
                "clean_run_count": sum(1 for row in rows if row.get("clean_status") == "clean"),
                "contaminated_run_count": sum(1 for row in rows if row.get("clean_status") != "clean"),
                "headline_metrics": headline_metrics,
                "delta_vs_other_track": {},
                "top_positive_drivers": [
                    {"source_type": "builder_complete", "count": sum(1 for row in rows if not row.get("top_failures"))},
                    {"source_type": "low_fallback", "count": sum(1 for row in rows if float(dict(row.get("fallback_summary") or {}).get("fallback_utterance_rate", 0.0)) < 0.30)},
                ],
                "top_negative_drivers": top_negative_drivers,
                "metric_confidence": {
                    "persona_drift_mae": "high",
                    "envelope_violations": "medium",
                    "commitment_contradiction_rate": "medium",
                    "relationship_shift_rate": "medium",
                    "relationship_overshoot_rate": "medium",
                    "action_family_convergence_rate": "medium",
                },
                "supporting_run_ids": [row["run_id"] for row in rows],
            }
        )

    if len(track_outcomes) == 2:
        first, second = track_outcomes
        for metric, value in first["headline_metrics"].items():
            first["delta_vs_other_track"][metric] = round(float(value) - float(second["headline_metrics"].get(metric, 0.0)), 4)
        for metric, value in second["headline_metrics"].items():
            second["delta_vs_other_track"][metric] = round(float(value) - float(first["headline_metrics"].get(metric, 0.0)), 4)
    return track_outcomes


def _build_track_metric_attributions(track_outcomes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for track in track_outcomes:
        for metric_name, metric_value in dict(track.get("headline_metrics") or {}).items():
            rows.append(
                {
                    "scope_type": "track",
                    "scope_id": track.get("track_id"),
                    "track_id": track.get("track_id"),
                    "metric_name": metric_name,
                    "metric_value": metric_value,
                    "top_contributors": list(track.get("top_negative_drivers") or [])[:3],
                    "top_counterexamples": list(track.get("top_positive_drivers") or [])[:2],
                    "supporting_trace_ids": list(track.get("supporting_run_ids") or []),
                }
            )
    return rows
