"""Output persistence and reporting helpers for simulation benchmarks."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


def save_benchmark_outputs(results: dict[str, Any], output_dir: str | Path) -> dict[str, str]:
    """Persist benchmark suite results and a concise markdown report."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    runs_path = output_path / "benchmark_runs.json"
    aggregate_path = output_path / "benchmark_aggregate.json"
    report_path = output_path / "benchmark_report.md"

    with open(runs_path, "w") as f:
        json.dump(results, f, indent=2, default=str)

    aggregate_payload = {
        "saved_at": datetime.now().isoformat(),
        "config": results.get("config", {}),
        "aggregate": results.get("aggregate", {}),
        "aggregate_by_script": results.get("aggregate_by_script", {}),
    }
    with open(aggregate_path, "w") as f:
        json.dump(aggregate_payload, f, indent=2, default=str)

    with open(report_path, "w") as f:
        f.write(build_benchmark_report(results))

    return {
        "runs": str(runs_path),
        "aggregate": str(aggregate_path),
        "report": str(report_path),
    }


def build_benchmark_report(results: dict[str, Any]) -> str:
    """Render a markdown summary optimized for quick MVP benchmark review."""
    config = results.get("config", {})
    aggregate = results.get("aggregate", {})
    aggregate_by_script = results.get("aggregate_by_script", {})
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

    return "\n".join(lines).strip() + "\n"


def _format_summary_block(label: str, summary: dict[str, Any]) -> list[str]:
    trait_errors = summary.get("per_trait_error_mean", {})
    trait_line = "n/a"
    if trait_errors:
        trait_line = ", ".join(
            f"{trait} {trait_errors.get(trait, 0.0):.4f}"
            for trait in ("O", "C", "E", "A", "N")
        )
    return [
        f"### {label}",
        f"- Runs: {summary.get('num_runs', 0)}",
        f"- Persona drift MAE: {summary.get('persona_drift_mae_mean', 0.0):.4f} (+/- {summary.get('persona_drift_mae_std', 0.0):.4f})",
        f"- Per-trait absolute error: {trait_line}",
        f"- Relationship inconsistency: {summary.get('relationship_inconsistency_mean', 0.0):.4f}",
        f"- Commitment contradiction: {summary.get('commitment_contradiction_mean', 0.0):.4f}",
        f"- Envelope violations: {summary.get('envelope_violations_mean', 0.0):.4f}",
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
        f"- State trajectory variance: {summary.get('state_trajectory_variance_mean', 0.0):.4f}",
        f"- Mean turns: {summary.get('turn_count_mean', 0.0):.2f}",
        "",
    ]


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
        f"- State trajectory variance delta: {trajectory_delta:+.4f}",
    ]
