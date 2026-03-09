"""Output persistence and reporting helpers for simulation benchmarks."""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from .traceability import build_trace_bundle


def save_benchmark_outputs(results: dict[str, Any], output_dir: str | Path) -> dict[str, str]:
    """Persist benchmark suite results and a concise markdown report."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    runs_path = output_path / "benchmark_runs.json"
    aggregate_path = output_path / "benchmark_aggregate.json"
    report_path = output_path / "benchmark_report.md"
    trace_paths = build_trace_bundle(results, output_path)

    runs_mode = _benchmark_runs_mode()
    runs_payload = _build_runs_payload(results, mode=runs_mode)
    with open(runs_path, "w") as f:
        json.dump(runs_payload, f, default=str, separators=(",", ":"))

    aggregate_payload = {
        "saved_at": datetime.now().isoformat(),
        "config": results.get("config", {}),
        "aggregate": results.get("aggregate", {}),
        "aggregate_by_script": results.get("aggregate_by_script", {}),
        "aggregate_by_mode": results.get("aggregate_by_mode", {}),
        "aggregate_by_family": results.get("aggregate_by_family", {}),
        "trace_bundle": trace_paths,
    }
    with open(aggregate_path, "w") as f:
        json.dump(aggregate_payload, f, indent=2, default=str)

    with open(report_path, "w") as f:
        f.write(build_benchmark_report(results))

    return {
        "runs": str(runs_path),
        "aggregate": str(aggregate_path),
        "report": str(report_path),
        **trace_paths,
    }


def _benchmark_runs_mode() -> str:
    mode = os.getenv("SIM_BENCHMARK_RUNS_MODE", "compact").strip().lower()
    if mode not in {"full", "compact", "none"}:
        return "compact"
    return mode


def _build_runs_payload(results: dict[str, Any], mode: str) -> dict[str, Any]:
    if mode == "full":
        return results
    if mode == "none":
        return {
            "config": results.get("config", {}),
            "run_count": len(results.get("runs", [])),
            "runs_omitted": True,
            "mode": "none",
        }
    return _compact_results_payload(results)


def _compact_results_payload(results: dict[str, Any]) -> dict[str, Any]:
    return {
        "config": results.get("config", {}),
        "runs": [_compact_run(run) for run in results.get("runs", [])],
        "aggregate": results.get("aggregate", {}),
        "aggregate_by_script": results.get("aggregate_by_script", {}),
        "aggregate_by_mode": results.get("aggregate_by_mode", {}),
        "aggregate_by_family": results.get("aggregate_by_family", {}),
        "mode": "compact",
    }


def _compact_run(run: dict[str, Any]) -> dict[str, Any]:
    compact = {
        "condition": run.get("condition"),
        "simulation_id": run.get("simulation_id"),
        "suite_id": run.get("suite_id"),
        "track_id": run.get("track_id"),
        "run_id": run.get("run_id"),
        "builder_trace_ref": run.get("builder_trace_ref"),
        "trace_bundle_path": run.get("trace_bundle_path"),
        "metrics": run.get("metrics", {}),
        "runtime_summary": _compact_runtime_summary(run.get("runtime_summary", {})),
    }
    selection_audits = run.get("selection_audits") or []
    if selection_audits:
        compact["selection_audits"] = selection_audits
    return compact


def _compact_runtime_summary(summary: dict[str, Any]) -> dict[str, Any]:
    keep_direct = {
        "simulation_id",
        "simulation_mode",
        "scenario_family",
        "outcome_spec",
        "turn_count",
        "phase_order",
        "actor_ids",
        "actor_labels",
        "actor_display_names",
        "latest_world_state",
        "action_status_counts",
        "action_rejection_reason_counts",
        "selection_hint_source_counts",
        "fallback_utterance_count",
        "fallback_utterance_rate",
        "fallback_type_counts",
        "fallback_counts",
        "action_family_sequence_by_actor",
        "actor_action_family_sequences",
        "phase_action_family_histograms",
        "phase_action_family_histogram",
        "builder_trace",
        "metadata_completeness_score",
        "trace_refs",
        "phase_count",
        "phase_order",
    }
    compact = {key: value for key, value in summary.items() if key in keep_direct}

    if "action_proposals" in summary:
        compact["action_proposal_count"] = len(summary.get("action_proposals") or [])
    if "executed_actions" in summary:
        compact["executed_action_count"] = len(summary.get("executed_actions") or [])
    if "action_audits" in summary:
        compact["action_audit_count"] = len(summary.get("action_audits") or [])
    if "world_state_history" in summary:
        compact["world_state_history_count"] = len(summary.get("world_state_history") or [])
    if "phase_state_feedback" in summary:
        compact["phase_state_feedback"] = summary.get("phase_state_feedback", {})
    if "turns" in summary:
        compact["turn_count"] = len(summary.get("turns") or []) or compact.get("turn_count", 0)
    if "relationship_events" in summary:
        compact["relationship_event_count"] = len(summary.get("relationship_events") or [])
    if "actor_state_events" in summary:
        compact["actor_state_event_count"] = len(summary.get("actor_state_events") or [])

    return compact


def build_benchmark_report(results: dict[str, Any]) -> str:
    """Render a markdown summary optimized for quick MVP benchmark review."""
    config = results.get("config", {})
    aggregate = results.get("aggregate", {})
    aggregate_by_script = results.get("aggregate_by_script", {})
    aggregate_by_mode = results.get("aggregate_by_mode", {})
    aggregate_by_family = results.get("aggregate_by_family", {})
    runs = results.get("runs", [])

    total_runs = len(runs)
    conditions = ", ".join(config.get("conditions", [])) or "n/a"
    script_ids = ", ".join(config.get("script_ids", [])) or "n/a"
    repetitions = config.get("repetitions", "n/a")

    lines = [
        "# Simulation Benchmark Report",
        "",
        "## Suite Config",
        f"- Total runs: {total_runs}",
        f"- Conditions: {conditions}",
        f"- Script ids: {script_ids}",
        f"- Repetitions per condition: {repetitions}",
        "",
        "## Condition Summary",
    ]

    if not aggregate:
        lines.append("- No benchmark runs were recorded.")
    else:
        for condition, summary in sorted(aggregate.items()):
            lines.extend(_format_summary_block(condition, summary))
    contaminated = [
        (condition, summary.get("fallback_utterance_rate_mean", 0.0))
        for condition, summary in sorted(aggregate.items())
        if summary.get("fallback_utterance_rate_mean", 0.0) >= 0.30
    ]
    if contaminated:
        lines.extend([
            "",
            "## Reliability Warnings",
            "- Fallback utterance contamination detected; treat persona/fidelity deltas as non-decisive until rerun.",
        ])
        for condition, rate in contaminated:
            lines.append(f"- {condition}: fallback utterance rate {rate:.4f}")

    naive = aggregate.get("naive")
    controlled = aggregate.get("engine_controller")
    if not (naive and controlled):
        naive = aggregate.get("naive_action_baseline")
        controlled = aggregate.get("engine_action_v0")
    if naive and controlled:
        lines.extend(_format_delta_block(naive, controlled))
    dialogue_only = aggregate.get("engine_dialogue_only")
    engine_action = aggregate.get("engine_action_v0")
    if dialogue_only and engine_action:
        lines.extend(_format_delta_block(dialogue_only, engine_action, title="## Action Engine vs Dialogue-Only"))

    lines.extend([
        "",
        "## Script-Level Summary",
    ])
    if not aggregate_by_script:
        lines.append("- No script-level aggregates were recorded.")
    else:
        for script_condition, summary in sorted(aggregate_by_script.items()):
            lines.extend(_format_summary_block(script_condition, summary))

    lines.extend([
        "",
        "## Mode Summary",
    ])
    if not aggregate_by_mode:
        lines.append("- No mode-level aggregates were recorded.")
    else:
        for mode_condition, summary in sorted(aggregate_by_mode.items()):
            lines.extend(_format_summary_block(mode_condition, summary))

    lines.extend([
        "",
        "## Family Summary",
    ])
    if not aggregate_by_family:
        lines.append("- No family-level aggregates were recorded.")
    else:
        for family_condition, summary in sorted(aggregate_by_family.items()):
            lines.extend(_format_summary_block(family_condition, summary))

    return "\n".join(lines).strip() + "\n"


def _format_summary_block(label: str, summary: dict[str, Any]) -> list[str]:
    trait_errors = summary.get("per_trait_error_mean", {})
    trait_line = "n/a"
    if trait_errors:
        trait_line = ", ".join(
            f"{trait} {trait_errors.get(trait, 0.0):.4f}"
            for trait in ("O", "C", "E", "A", "N")
        )
    fallback_type_line = ", ".join(
        f"{key} {value:.4f}"
        for key, value in sorted((summary.get("fallback_type_rate_mean") or {}).items())
    ) or "n/a"
    rows = [
        f"### {label}",
        f"- Runs: {summary.get('num_runs', 0)}",
        f"- Clean runs: {summary.get('clean_run_count', 0)}",
        f"- Contaminated runs: {summary.get('contaminated_run_count', 0)}",
        f"- Persona drift MAE: {summary.get('persona_drift_mae_mean', 0.0):.4f} (+/- {summary.get('persona_drift_mae_std', 0.0):.4f})",
        f"- Clean persona drift MAE: {summary.get('clean_persona_drift_mae_mean', summary.get('persona_drift_mae_mean', 0.0)):.4f}",
        f"- Per-trait absolute error: {trait_line}",
        f"- Relationship inconsistency: {summary.get('relationship_inconsistency_mean', 0.0):.4f}",
        f"- Relationship shift rate: {summary.get('relationship_shift_rate_mean', 0.0):.4f}",
        f"- Relationship overshoot rate: {summary.get('relationship_overshoot_rate_mean', 0.0):.4f}",
        f"- Commitment contradiction: {summary.get('commitment_contradiction_mean', 0.0):.4f}",
        f"- Clean commitment contradiction: {summary.get('clean_commitment_contradiction_mean', summary.get('commitment_contradiction_mean', 0.0)):.4f}",
        f"- Envelope violations: {summary.get('envelope_violations_mean', 0.0):.4f}",
        f"- Clean envelope violations: {summary.get('clean_envelope_violations_mean', summary.get('envelope_violations_mean', 0.0)):.4f}",
        f"- Structured action validity: {summary.get('structured_action_validity_rate_mean', 0.0):.4f}",
        f"- Owner resolution rate: {summary.get('owner_resolution_rate_mean', 0.0):.4f}",
        f"- Executed action contradiction: {summary.get('executed_action_contradiction_rate_mean', 0.0):.4f}",
        f"- State transition coherence: {summary.get('state_transition_coherence_mean', 0.0):.4f}",
        f"- Action feedback utilization: {summary.get('action_feedback_utilization_mean', 0.0):.4f}",
        f"- Action-plan alignment: {summary.get('action_plan_alignment_mean', 0.0):.4f}",
        f"- Planned action coverage: {summary.get('planned_action_coverage_rate_mean', 0.0):.4f}",
        f"- Action family convergence: {summary.get('action_family_convergence_rate_mean', 0.0):.4f}",
        f"- Role action diversity: {summary.get('role_action_diversity_score_mean', 0.0):.4f}",
        f"- Negotiation uniqueness: {summary.get('negotiation_uniqueness_rate_mean', 0.0):.4f}",
        f"- Fallback utterance rate: {summary.get('fallback_utterance_rate_mean', 0.0):.4f}",
        f"- Fallback taxonomy: {fallback_type_line}",
        f"- State trajectory variance: {summary.get('state_trajectory_variance_mean', 0.0):.4f}",
        f"- Mean turns: {summary.get('turn_count_mean', 0.0):.2f}",
        f"- Persona drift 95% CI: {summary.get('ci_95', {}).get('persona_drift_mae', [0.0, 0.0])}",
        "",
    ]
    if summary.get("zero_variance_metrics"):
        rows.append(f"- Zero-variance metrics: {', '.join(summary.get('zero_variance_metrics', []))}")
        rows.append("")
    return rows


def _format_delta_block(naive: dict[str, Any], controlled: dict[str, Any], title: str = "## Controlled Engine vs Baseline") -> list[str]:
    drift_delta = round(
        controlled.get("persona_drift_mae_mean", 0.0) - naive.get("persona_drift_mae_mean", 0.0),
        4,
    )
    relation_delta = round(
        controlled.get("relationship_inconsistency_mean", 0.0) - naive.get("relationship_inconsistency_mean", 0.0),
        4,
    )
    commitment_delta = round(
        controlled.get("commitment_contradiction_mean", 0.0) - naive.get("commitment_contradiction_mean", 0.0),
        4,
    )
    action_validity_delta = round(
        controlled.get("structured_action_validity_rate_mean", 0.0) - naive.get("structured_action_validity_rate_mean", 0.0),
        4,
    )
    action_contradiction_delta = round(
        controlled.get("executed_action_contradiction_rate_mean", 0.0) - naive.get("executed_action_contradiction_rate_mean", 0.0),
        4,
    )
    action_plan_alignment_delta = round(
        controlled.get("action_plan_alignment_mean", 0.0) - naive.get("action_plan_alignment_mean", 0.0),
        4,
    )
    action_family_convergence_delta = round(
        controlled.get("action_family_convergence_rate_mean", 0.0) - naive.get("action_family_convergence_rate_mean", 0.0),
        4,
    )
    role_action_diversity_delta = round(
        controlled.get("role_action_diversity_score_mean", 0.0) - naive.get("role_action_diversity_score_mean", 0.0),
        4,
    )
    negotiation_uniqueness_delta = round(
        controlled.get("negotiation_uniqueness_rate_mean", 0.0) - naive.get("negotiation_uniqueness_rate_mean", 0.0),
        4,
    )
    fallback_delta = round(
        controlled.get("fallback_utterance_rate_mean", 0.0) - naive.get("fallback_utterance_rate_mean", 0.0),
        4,
    )
    trajectory_delta = round(
        controlled.get("state_trajectory_variance_mean", 0.0) - naive.get("state_trajectory_variance_mean", 0.0),
        4,
    )
    trait_errors_naive = naive.get("per_trait_error_mean", {})
    trait_errors_controlled = controlled.get("per_trait_error_mean", {})
    trait_delta_line = ", ".join(
        f"{trait} {round(trait_errors_controlled.get(trait, 0.0) - trait_errors_naive.get(trait, 0.0), 4):+0.4f}"
        for trait in ("O", "C", "E", "A", "N")
    )

    return [
        "",
        title,
        f"- Persona drift delta (`controlled - baseline`): {drift_delta:+.4f}",
        f"- Per-trait error delta: {trait_delta_line}",
        f"- Relationship inconsistency delta: {relation_delta:+.4f}",
        f"- Commitment contradiction delta: {commitment_delta:+.4f}",
        f"- Structured action validity delta: {action_validity_delta:+.4f}",
        f"- Executed action contradiction delta: {action_contradiction_delta:+.4f}",
        f"- Action-plan alignment delta: {action_plan_alignment_delta:+.4f}",
        f"- Action family convergence delta: {action_family_convergence_delta:+.4f}",
        f"- Role action diversity delta: {role_action_diversity_delta:+.4f}",
        f"- Negotiation uniqueness delta: {negotiation_uniqueness_delta:+.4f}",
        f"- Fallback utterance delta: {fallback_delta:+.4f}",
        f"- State trajectory variance delta: {trajectory_delta:+.4f}",
    ]
