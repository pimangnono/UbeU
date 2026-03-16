"""Output persistence and reporting helpers for simulation benchmarks."""

from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

from .traceability import build_trace_bundle


def atomic_write_json(path: Path, data: Any, **json_kwargs) -> None:
    """Write JSON atomically: write to temp file, then os.replace().

    Prevents corruption if the process is killed mid-write (e.g. laptop restart).
    os.replace() is atomic on POSIX — the file is either the old version or the
    new version, never a partial write.
    """
    parent = path.parent
    parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=parent, suffix=".tmp", prefix=path.stem)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, **json_kwargs)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def atomic_write_text(path: Path, content: str) -> None:
    """Write text atomically: write to temp file, then os.replace()."""
    parent = path.parent
    parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=parent, suffix=".tmp", prefix=path.stem)
    try:
        with os.fdopen(fd, "w") as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


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
    atomic_write_json(runs_path, runs_payload, default=str, separators=(",", ":"))

    aggregate_payload = {
        "saved_at": datetime.now().isoformat(),
        "config": results.get("config", {}),
        "aggregate": results.get("aggregate", {}),
        "aggregate_by_script": results.get("aggregate_by_script", {}),
        "aggregate_by_mode": results.get("aggregate_by_mode", {}),
        "aggregate_by_family": results.get("aggregate_by_family", {}),
        "trace_bundle": trace_paths,
    }
    atomic_write_json(aggregate_path, aggregate_payload, indent=2, default=str)

    atomic_write_text(report_path, build_benchmark_report(results))

    # Save dialogue cache for offline re-scoring
    _save_dialogue_cache(results, output_path)

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
        "script_id": run.get("script_id", run.get("simulation_id")),
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

    # New explanation-level traceability sections
    lines.extend(_format_feature_attribution_table(runs))
    lines.extend(_format_three_way_decomposition(aggregate))
    lines.extend(_format_decision_driver_analysis(runs))
    lines.extend(_format_archetype_trait_table(runs))
    lines.extend(_format_phase_feature_summary(runs))
    lines.extend(_format_scenario_difficulty_table(runs))
    lines.extend(_format_influence_attribution_section(runs))

    # Statistical significance tables
    condition_pairs = []
    condition_list = list(aggregate.keys())
    if "engine_structural" in condition_list and "naive" in condition_list:
        condition_pairs.append(("engine_structural", "naive"))
    if "engine_dialogue_only" in condition_list and "naive" in condition_list:
        condition_pairs.append(("engine_dialogue_only", "naive"))
    if "engine_dialogue_only" in condition_list and "naive_informed" in condition_list:
        condition_pairs.append(("engine_dialogue_only", "naive_informed"))
    if "naive_informed" in condition_list and "naive" in condition_list:
        condition_pairs.append(("naive_informed", "naive"))
    if not condition_pairs and len(condition_list) >= 2:
        condition_pairs.append((condition_list[0], condition_list[1]))

    for pair in condition_pairs:
        lines.extend(_format_significance_table(runs, pair))
        lines.extend(_format_per_trait_table(runs, pair))

    # Actor count scaling table
    lines.extend(_format_scaling_table(runs))

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
        f"- Dialogue coherence: {summary.get('dialogue_coherence_score_mean', 0.0):.4f}",
        f"- Repetition rate: {summary.get('repetition_rate_mean', 0.0):.4f}",
        f"- Topic drift rate: {summary.get('topic_drift_rate_mean', 0.0):.4f}",
        f"- Fallback taxonomy: {fallback_type_line}",
        f"- Semantic identity consistency: {summary.get('semantic_identity_consistency_mean', 0.0):.4f}",
        f"- Commitment fulfillment rate: {summary.get('commitment_fulfillment_rate_mean', 0.0):.4f}",
        f"- State trajectory variance: {summary.get('state_trajectory_variance_mean', 0.0):.4f}",
        f"- Mean turns: {summary.get('turn_count_mean', 0.0):.2f}",
        f"- Persona drift 95% CI: {summary.get('ci_95', {}).get('persona_drift_mae', [0.0, 0.0])}",
        "",
    ]
    phase_quality = summary.get("phase_quality_mean", {})
    if phase_quality:
        rows.append("- Phase-level quality:")
        for phase_name in ("OPENING", "TENSION", "NEGOTIATION", "CLOSING"):
            pq = phase_quality.get(phase_name)
            if pq:
                rows.append(
                    f"  - {phase_name}: drift={pq.get('drift', 0.0):.4f}, "
                    f"convergence={pq.get('convergence', 0.0):.4f}, "
                    f"diversity={pq.get('diversity', 0.0):.4f}"
                )
        rows.append("")
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

    coherence_delta = round(
        controlled.get("dialogue_coherence_score_mean", 0.0) - naive.get("dialogue_coherence_score_mean", 0.0),
        4,
    )
    repetition_delta = round(
        controlled.get("repetition_rate_mean", 0.0) - naive.get("repetition_rate_mean", 0.0),
        4,
    )
    topic_drift_delta = round(
        controlled.get("topic_drift_rate_mean", 0.0) - naive.get("topic_drift_rate_mean", 0.0),
        4,
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
        f"- Dialogue coherence delta: {coherence_delta:+.4f}",
        f"- Repetition rate delta: {repetition_delta:+.4f}",
        f"- Topic drift rate delta: {topic_drift_delta:+.4f}",
        f"- Fallback utterance delta: {fallback_delta:+.4f}",
        f"- State trajectory variance delta: {trajectory_delta:+.4f}",
    ]


# ── Statistical helpers (stdlib-only, no scipy) ────────────────────────────

def _welch_t_and_df(
    values_a: list[float], values_b: list[float]
) -> tuple[float, float]:
    """Welch's t-statistic and approximate degrees of freedom."""
    import math

    na, nb = len(values_a), len(values_b)
    if na < 2 or nb < 2:
        return 0.0, 0.0
    ma = sum(values_a) / na
    mb = sum(values_b) / nb
    va = sum((x - ma) ** 2 for x in values_a) / (na - 1)
    vb = sum((x - mb) ** 2 for x in values_b) / (nb - 1)
    pooled_se_sq = va / na + vb / nb
    if pooled_se_sq < 1e-15:
        # Both groups have (near-)zero variance — degenerate case
        return 0.0, 0.0
    se = math.sqrt(pooled_se_sq)
    t_stat = (ma - mb) / se
    # Welch-Satterthwaite degrees of freedom
    num = pooled_se_sq ** 2
    denom = (va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1)
    df = num / denom if denom > 1e-15 else 1.0
    return t_stat, df


def _t_to_p_approx(t_stat: float, df: float) -> float:
    """Approximate two-tailed p-value from t-statistic.

    Uses normal approximation with Welch-Satterthwaite df correction for small df.
    For df < 30, applies the Cornish-Fisher expansion to adjust the critical value.
    """
    import math

    if df <= 0 or t_stat == 0.0:
        return 1.0

    x = abs(t_stat)

    # For small df, adjust t → z using the Cornish-Fisher approximation:
    # z ≈ t * (1 - 1/(4*df)) — shrinks t toward zero for heavy-tailed distribution
    if df < 120:
        x = x * (1.0 - 1.0 / (4.0 * df))

    # Abramowitz and Stegun 26.2.17: normal CDF approximation (max error ~1e-5)
    a1, a2, a3 = 0.4361836, -0.1201676, 0.9372980
    t_val = 1.0 / (1.0 + 0.33267 * x)
    phi = 1.0 - (1.0 / math.sqrt(2 * math.pi)) * math.exp(-x * x / 2) * (
        a1 * t_val + a2 * t_val ** 2 + a3 * t_val ** 3
    )
    p_one_tail = 1.0 - phi
    return min(1.0, 2.0 * p_one_tail)


def _cohens_d(values_a: list[float], values_b: list[float]) -> float:
    """Cohen's d effect size."""
    na, nb = len(values_a), len(values_b)
    if na < 2 or nb < 2:
        return 0.0
    ma = sum(values_a) / na
    mb = sum(values_b) / nb
    va = sum((x - ma) ** 2 for x in values_a) / (na - 1)
    vb = sum((x - mb) ** 2 for x in values_b) / (nb - 1)
    pooled_sd = ((va * (na - 1) + vb * (nb - 1)) / (na + nb - 2)) ** 0.5
    if pooled_sd < 1e-12:
        return 0.0
    return (ma - mb) / pooled_sd


def _mean_95ci(values: list[float]) -> tuple[float, float, float]:
    """Return (mean, ci_low, ci_high) for a list of values."""
    if not values:
        return 0.0, 0.0, 0.0
    n = len(values)
    m = sum(values) / n
    if n < 2:
        return m, m, m
    var = sum((x - m) ** 2 for x in values) / (n - 1)
    se = (var / n) ** 0.5
    margin = 1.96 * se
    return m, m - margin, m + margin


def _effect_size_label(d: float) -> str:
    """Interpret Cohen's d magnitude."""
    ad = abs(d)
    if ad < 0.2:
        return "negligible"
    if ad < 0.5:
        return "small"
    if ad < 0.8:
        return "medium"
    return "large"


def _paired_t_test(
    vals_a: list[float], vals_b: list[float]
) -> tuple[float, float, float]:
    """Paired t-test: returns (t_stat, df, p_value).

    vals_a and vals_b must be same-length paired observations.
    """
    import math

    n = len(vals_a)
    if n < 2 or len(vals_b) != n:
        return 0.0, 0.0, 1.0
    diffs = [a - b for a, b in zip(vals_a, vals_b)]
    mean_d = sum(diffs) / n
    var_d = sum((d - mean_d) ** 2 for d in diffs) / (n - 1)
    if var_d < 1e-15:
        return 0.0, float(n - 1), 1.0
    se_d = math.sqrt(var_d / n)
    t_stat = mean_d / se_d
    df = float(n - 1)
    p_value = _t_to_p_approx(t_stat, df)
    return t_stat, df, p_value


def _format_significance_table(
    runs: list[dict[str, Any]],
    conditions: tuple[str, str],
) -> list[str]:
    """Build a markdown table comparing two conditions with significance tests.

    Includes Bonferroni correction, effect size labels, paired t-test, and win rates.
    """
    cond_a, cond_b = conditions
    runs_a = [r for r in runs if r.get("condition") == cond_a]
    runs_b = [r for r in runs if r.get("condition") == cond_b]
    if not runs_a or not runs_b:
        return []

    metrics_to_compare = [
        ("persona_drift_mae", "Persona Drift MAE"),
        ("relationship_inconsistency", "Relationship Inconsistency"),
        ("commitment_contradiction_rate", "Commitment Contradiction"),
        ("envelope_violations", "Envelope Violations"),
        ("action_family_convergence_rate", "Action Convergence"),
        ("role_action_diversity_score", "Role Diversity"),
        ("dialogue_coherence_score", "Dialogue Coherence"),
        ("repetition_rate", "Repetition Rate"),
        ("topic_drift_rate", "Topic Drift Rate"),
        ("fallback_utterance_rate", "Fallback Rate"),
        ("semantic_identity_consistency", "Semantic Identity Consistency"),
        ("commitment_fulfillment_rate", "Commitment Fulfillment Rate"),
    ]

    num_metrics = len(metrics_to_compare)
    bonferroni_threshold = 0.05 / num_metrics

    lines = [
        "",
        f"## Statistical Significance: {cond_a} vs {cond_b}",
        "",
        f"Bonferroni-corrected threshold: p < {bonferroni_threshold:.4f} ({num_metrics} comparisons)",
        "",
        f"| Metric | {cond_a} (n={len(runs_a)}) | {cond_b} (n={len(runs_b)}) | Delta | p (Welch) | p (paired) | Cohen's d | Effect | Sig? |",
        "|--------|" + "----|" * 8,
    ]

    # Build paired index: match runs by script_id × repetition_index
    paired_index_a: dict[str, dict] = {}
    for r in runs_a:
        script_id = r.get("script_id", r.get("simulation_id", ""))
        rep_idx = r.get("repetition_index", 0)
        paired_index_a[(script_id, rep_idx)] = r
    paired_index_b: dict[str, dict] = {}
    for r in runs_b:
        script_id = r.get("script_id", r.get("simulation_id", ""))
        rep_idx = r.get("repetition_index", 0)
        paired_index_b[(script_id, rep_idx)] = r

    # Lower-is-better metrics (engine "wins" when it has lower value)
    lower_is_better = {
        "persona_drift_mae", "relationship_inconsistency", "commitment_contradiction_rate",
        "envelope_violations", "action_family_convergence_rate", "repetition_rate",
        "topic_drift_rate", "fallback_utterance_rate",
    }
    win_counts: dict[str, int] = {}

    for metric_key, metric_label in metrics_to_compare:
        vals_a = [r.get("metrics", {}).get(metric_key, 0.0) for r in runs_a]
        vals_b = [r.get("metrics", {}).get(metric_key, 0.0) for r in runs_b]
        mean_a, _, _ = _mean_95ci(vals_a)
        mean_b, _, _ = _mean_95ci(vals_b)
        delta = mean_a - mean_b

        # Unpaired Welch's t-test
        t_stat, df = _welch_t_and_df(vals_a, vals_b)
        p_welch = _t_to_p_approx(t_stat, df)

        # Paired t-test (matched by script_id × rep_index)
        common_keys = sorted(set(paired_index_a.keys()) & set(paired_index_b.keys()))
        if len(common_keys) >= 3:
            paired_a = [paired_index_a[k].get("metrics", {}).get(metric_key, 0.0) for k in common_keys]
            paired_b = [paired_index_b[k].get("metrics", {}).get(metric_key, 0.0) for k in common_keys]
            _, _, p_paired = _paired_t_test(paired_a, paired_b)
        else:
            p_paired = 1.0

        d = _cohens_d(vals_a, vals_b)
        d_label = _effect_size_label(d)
        sig = "Yes" if p_welch < bonferroni_threshold or p_paired < bonferroni_threshold else "No"

        lines.append(
            f"| {metric_label} | {mean_a:.4f} | {mean_b:.4f} | {delta:+.4f} | "
            f"{p_welch:.4f} | {p_paired:.4f} | {d:+.3f} | {d_label} | {sig} |"
        )

        # Win rate: per-script comparison
        script_wins = 0
        script_total = 0
        # Group runs by script_id
        scripts_a: dict[str, list[float]] = {}
        scripts_b: dict[str, list[float]] = {}
        for r in runs_a:
            sid = r.get("script_id", r.get("simulation_id", ""))
            scripts_a.setdefault(sid, []).append(r.get("metrics", {}).get(metric_key, 0.0))
        for r in runs_b:
            sid = r.get("script_id", r.get("simulation_id", ""))
            scripts_b.setdefault(sid, []).append(r.get("metrics", {}).get(metric_key, 0.0))
        for sid in set(scripts_a.keys()) & set(scripts_b.keys()):
            ma = sum(scripts_a[sid]) / len(scripts_a[sid])
            mb = sum(scripts_b[sid]) / len(scripts_b[sid])
            script_total += 1
            if metric_key in lower_is_better:
                if ma < mb:
                    script_wins += 1
            else:
                if ma > mb:
                    script_wins += 1
        win_counts[metric_key] = script_wins

    # Win rate summary
    lines.extend(["", "### Win Rate Summary (per-script comparison)", ""])
    lines.append(f"| Metric | {cond_a} wins | Total scripts |")
    lines.append("|--------|" + "----|" * 2)
    for metric_key, metric_label in metrics_to_compare:
        wins = win_counts.get(metric_key, 0)
        # Count total scripts
        sids_a = {r.get("script_id", r.get("simulation_id", "")) for r in runs_a}
        sids_b = {r.get("script_id", r.get("simulation_id", "")) for r in runs_b}
        total_scripts = len(sids_a & sids_b)
        lines.append(f"| {metric_label} | {wins}/{total_scripts} | {total_scripts} |")

    # Per-scenario paired comparison
    lines.extend(_format_per_scenario_comparison(runs_a, runs_b, cond_a, cond_b))

    return lines


def _format_per_scenario_comparison(
    runs_a: list[dict], runs_b: list[dict],
    cond_a: str, cond_b: str,
) -> list[str]:
    """Per-scenario engine vs naive drift comparison table."""
    # Group by script_id
    from collections import defaultdict

    scripts_a: dict[str, list[float]] = defaultdict(list)
    scripts_b: dict[str, list[float]] = defaultdict(list)
    for r in runs_a:
        sid = r.get("script_id", r.get("simulation_id", ""))
        scripts_a[sid].append(r.get("metrics", {}).get("persona_drift_mae", 0.0))
    for r in runs_b:
        sid = r.get("script_id", r.get("simulation_id", ""))
        scripts_b[sid].append(r.get("metrics", {}).get("persona_drift_mae", 0.0))

    common = sorted(set(scripts_a.keys()) & set(scripts_b.keys()))
    if not common:
        return []

    lines = [
        "",
        f"### Per-Scenario Drift Comparison: {cond_a} vs {cond_b}",
        "",
        f"| Scenario | {cond_a} drift | {cond_b} drift | Delta | Winner |",
        "|----------|" + "----|" * 4,
    ]

    for sid in common:
        ma = sum(scripts_a[sid]) / len(scripts_a[sid])
        mb = sum(scripts_b[sid]) / len(scripts_b[sid])
        delta = ma - mb
        winner = cond_a if delta < 0 else (cond_b if delta > 0 else "tie")
        short = sid.split("_")[-1] if "_" in sid else sid
        lines.append(f"| {short} | {ma:.4f} | {mb:.4f} | {delta:+.4f} | {winner} |")

    return lines


def _format_per_trait_table(
    runs: list[dict[str, Any]],
    conditions: tuple[str, str],
) -> list[str]:
    """Build per-trait error breakdown table with significance and effect size."""
    cond_a, cond_b = conditions
    runs_a = [r for r in runs if r.get("condition") == cond_a]
    runs_b = [r for r in runs if r.get("condition") == cond_b]
    if not runs_a or not runs_b:
        return []

    bonferroni_threshold = 0.05 / 5  # 5 traits

    trait_calibration = {"O": "Static", "C": "Dynamic", "E": "Dynamic", "A": "Dynamic", "N": "Dynamic"}
    lines = [
        "",
        f"## Per-Trait Error: {cond_a} vs {cond_b}",
        "",
        f"Bonferroni-corrected threshold: p < {bonferroni_threshold:.3f} (5 comparisons)",
        "",
        "| Trait | Engine | Naive | Delta | p-value | Cohen's d | Effect | Calibration | Sig? |",
        "|-------|--------|-------|-------|---------|-----------|--------|-------------|------|",
    ]

    for trait in ("O", "C", "E", "A", "N"):
        vals_a = [r.get("metrics", {}).get("per_trait_error_mean", {}).get(trait, 0.0) for r in runs_a]
        vals_b = [r.get("metrics", {}).get("per_trait_error_mean", {}).get(trait, 0.0) for r in runs_b]
        mean_a = sum(vals_a) / len(vals_a) if vals_a else 0.0
        mean_b = sum(vals_b) / len(vals_b) if vals_b else 0.0
        delta = mean_a - mean_b
        t_stat, df = _welch_t_and_df(vals_a, vals_b)
        p_value = _t_to_p_approx(t_stat, df)
        d = _cohens_d(vals_a, vals_b)
        d_label = _effect_size_label(d)
        sig = "Yes" if p_value < bonferroni_threshold else "No"
        lines.append(
            f"| {trait} | {mean_a:.4f} | {mean_b:.4f} | {delta:+.4f} | {p_value:.4f} | {d:+.3f} | {d_label} | {trait_calibration[trait]} | {sig} |"
        )

    return lines


def _format_scaling_table(runs: list[dict[str, Any]]) -> list[str]:
    """Build actor count x condition interaction analysis table."""
    # Extract actor count from simulation_id
    import re

    def _actor_count(run: dict) -> int:
        sim_id = run.get("simulation_id", "")
        m = re.search(r"_(\d+)actor$", sim_id)
        return int(m.group(1)) if m else 0

    grouped: dict[tuple[int, str], list[dict]] = {}
    for run in runs:
        ac = _actor_count(run)
        if ac == 0:
            continue
        condition = run.get("condition", "")
        grouped.setdefault((ac, condition), []).append(run)

    if not grouped:
        return []

    actor_counts = sorted({k[0] for k in grouped})
    conditions = sorted({k[1] for k in grouped})

    lines = [
        "",
        "## Actor Count x Condition Scaling",
        "",
        "| Actors | Condition | n | Drift | Envelope | Convergence | Diversity | Coherence | Repetition | Topic Drift |",
        "|--------|-----------|---|-------|----------|-------------|-----------|-----------|------------|-------------|",
    ]

    for ac in actor_counts:
        for cond in conditions:
            rows = grouped.get((ac, cond), [])
            if not rows:
                continue
            n = len(rows)
            drift = sum(r.get("metrics", {}).get("persona_drift_mae", 0.0) for r in rows) / n
            envelope = sum(r.get("metrics", {}).get("envelope_violations", 0.0) for r in rows) / n
            convergence = sum(r.get("metrics", {}).get("action_family_convergence_rate", 0.0) for r in rows) / n
            diversity = sum(r.get("metrics", {}).get("role_action_diversity_score", 0.0) for r in rows) / n
            coherence = sum(r.get("metrics", {}).get("dialogue_coherence_score", 0.0) for r in rows) / n
            repetition = sum(r.get("metrics", {}).get("repetition_rate", 0.0) for r in rows) / n
            topic_drift = sum(r.get("metrics", {}).get("topic_drift_rate", 0.0) for r in rows) / n
            lines.append(
                f"| {ac} | {cond} | {n} | {drift:.4f} | {envelope:.4f} | {convergence:.4f} | {diversity:.4f} | {coherence:.4f} | {repetition:.4f} | {topic_drift:.4f} |"
            )

    # Drift slope analysis
    lines.extend(["", "### Drift Slope (10-actor minus 3-actor):", ""])
    for cond in conditions:
        rows_3 = grouped.get((3, cond), [])
        rows_10 = grouped.get((10, cond), [])
        if rows_3 and rows_10:
            drift_3 = sum(r.get("metrics", {}).get("persona_drift_mae", 0.0) for r in rows_3) / len(rows_3)
            drift_10 = sum(r.get("metrics", {}).get("persona_drift_mae", 0.0) for r in rows_10) / len(rows_10)
            slope = drift_10 - drift_3
            lines.append(f"- {cond}: {slope:+.4f}")

    return lines


def _format_feature_attribution_table(runs: list[dict[str, Any]]) -> list[str]:
    """Feature attribution: what raw behavioral features drive each OCEAN trait score."""
    from collections import defaultdict

    # Collect feature breakdowns across all runs, grouped by condition
    condition_breakdowns: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for run in runs:
        condition = run.get("condition", "unknown")
        metrics = run.get("metrics", {})
        breakdowns = metrics.get("actor_feature_breakdowns", {})
        for actor_id, breakdown in breakdowns.items():
            condition_breakdowns[condition].append(breakdown)

    if not condition_breakdowns:
        return []

    lines = ["", "## Feature Attribution: What Drives Each Trait Score", ""]

    trait_features = {
        "O": ["idea_count", "hypothetical_count", "unique_word_ratio"],
        "C": ["planning_count", "structure_marker_count", "detail_count", "goal_reference_count", "correction_count"],
        "E": ["exclamation_count", "question_count", "word_count", "filler_count"],
        "A": ["acknowledgment_count", "disagreement_count", "negation_count", "politeness_count", "compliment_count"],
        "N": ["hedge_count", "self_doubt_count", "reassurance_seeking_count", "apology_count", "emotional_word_count"],
    }

    for trait in ("O", "C", "E", "A", "N"):
        features = trait_features[trait]
        # Compute mean trait error across all runs for this trait
        trait_errors = [
            r.get("metrics", {}).get("per_trait_error_mean", {}).get(trait, 0.0) for r in runs
        ]
        mean_error = sum(trait_errors) / len(trait_errors) if trait_errors else 0.0
        trait_names = {"O": "Openness", "C": "Conscientiousness", "E": "Extraversion", "A": "Agreeableness", "N": "Neuroticism"}
        lines.append(f"### {trait_names[trait]} ({trait}) — Mean Error: {mean_error:.4f}")
        lines.append("")

        # Build header from conditions
        conditions = sorted(condition_breakdowns.keys())
        header = "| Feature |"
        separator = "|---------|"
        for cond in conditions:
            n = len(condition_breakdowns[cond])
            header += f" {cond} (n={n}) |"
            separator += "------|"
        if len(conditions) == 2:
            header += " Delta |"
            separator += "------|"
        lines.append(header)
        lines.append(separator)

        for feature in features:
            row = f"| {feature} |"
            means = []
            for cond in conditions:
                vals = [
                    b.get("raw_features", {}).get(feature, 0.0)
                    for b in condition_breakdowns[cond]
                ]
                m = sum(vals) / len(vals) if vals else 0.0
                means.append(m)
                row += f" {m:.3f} |"
            if len(conditions) == 2:
                delta = means[0] - means[1]
                row += f" {delta:+.3f} |"
            lines.append(row)

        # Show calibration mode
        sample = next(iter(next(iter(condition_breakdowns.values()), [{}])), {})
        cal_mode = sample.get("calibration_mode", {}).get(trait, "unknown")
        lines.extend(["", f"Calibration: {cal_mode}", ""])

    return lines


def _format_three_way_decomposition(aggregate: dict[str, Any]) -> list[str]:
    """Engine advantage decomposition: naive → naive_informed → engine."""
    naive = aggregate.get("naive") or aggregate.get("naive_action_baseline")
    informed = aggregate.get("naive_informed")
    engine = aggregate.get("engine_dialogue_only") or aggregate.get("engine_action_v0") or aggregate.get("engine_controller")

    if not naive or not engine:
        return []

    naive_drift = naive.get("persona_drift_mae_mean", 0.0)
    engine_drift = engine.get("persona_drift_mae_mean", 0.0)

    lines = ["", "## Engine Advantage Decomposition", ""]
    lines.append("| Stage | Drift MAE | Delta from Previous | % of Total Improvement |")
    lines.append("|-------|-----------|--------------------|-----------------------|")
    lines.append(f"| Naive (baseline) | {naive_drift:.4f} | — | — |")

    total_improvement = naive_drift - engine_drift
    if informed:
        informed_drift = informed.get("persona_drift_mae_mean", 0.0)
        pool_delta = naive_drift - informed_drift
        controller_delta = informed_drift - engine_drift
        pool_pct = (pool_delta / total_improvement * 100) if abs(total_improvement) > 1e-6 else 0.0
        controller_pct = (controller_delta / total_improvement * 100) if abs(total_improvement) > 1e-6 else 0.0
        lines.append(f"| + Multi-candidate pool (naive_informed) | {informed_drift:.4f} | {-pool_delta:+.4f} | {pool_pct:.0f}% |")
        lines.append(f"| + Controller intelligence (engine) | {engine_drift:.4f} | {-controller_delta:+.4f} | {controller_pct:.0f}% |")
    else:
        lines.append(f"| + Engine (full) | {engine_drift:.4f} | {-total_improvement:+.4f} | 100% |")

    lines.append(f"| **Total improvement** | | **{-total_improvement:+.4f}** | **100%** |")

    if informed and abs(total_improvement) > 1e-6:
        pool_delta = naive_drift - informed.get("persona_drift_mae_mean", 0.0)
        pool_pct = pool_delta / total_improvement * 100
        lines.extend([
            "",
            f"Interpretation: {pool_pct:.0f}% of the engine's drift advantage comes from having multiple candidates;",
            f"{100 - pool_pct:.0f}% comes from the controller's scoring intelligence.",
        ])

    return lines


def _format_decision_driver_analysis(runs: list[dict[str, Any]]) -> list[str]:
    """Show which scoring dimensions dominate candidate selection per condition and phase."""
    from collections import Counter, defaultdict

    condition_phase_drivers: dict[str, dict[str, dict[str, Counter]]] = defaultdict(
        lambda: defaultdict(lambda: {"positive": Counter(), "negative": Counter()})
    )

    for run in runs:
        condition = run.get("condition", "unknown")
        selection_audits = run.get("selection_audits") or []
        runtime_summary = run.get("runtime_summary", {})
        for turn in runtime_summary.get("turns", []):
            audit = dict(dict(turn.get("metadata") or {}).get("audit") or {})
            if audit:
                selection_audits.append(audit)

        for audit in selection_audits:
            phase = str(audit.get("phase_name") or "unknown")
            for score_row in list(audit.get("score_rows") or []):
                for name, value in dict(score_row.get("score_components") or {}).items():
                    v = float(value or 0)
                    if v > 0:
                        condition_phase_drivers[condition][phase]["positive"][name] += 1
                for name, value in dict(score_row.get("penalty_components") or {}).items():
                    v = float(value or 0)
                    if v < 0:
                        condition_phase_drivers[condition][phase]["negative"][name] += 1

    if not condition_phase_drivers:
        return []

    lines = ["", "## Decision Driver Analysis", ""]

    for condition in sorted(condition_phase_drivers.keys()):
        phase_data = condition_phase_drivers[condition]
        lines.append(f"### {condition} — What Drives Candidate Selection")
        lines.append("")
        lines.append("| Phase | Top Positive Driver | Count | Top Negative Driver | Count |")
        lines.append("|-------|-------------------|-------|-------------------|-------|")
        for phase in ("OPENING", "TENSION", "NEGOTIATION", "CLOSING"):
            data = phase_data.get(phase)
            if not data:
                continue
            top_pos = data["positive"].most_common(1)
            top_neg = data["negative"].most_common(1)
            pos_name = top_pos[0][0] if top_pos else "—"
            pos_count = top_pos[0][1] if top_pos else 0
            neg_name = top_neg[0][0] if top_neg else "—"
            neg_count = top_neg[0][1] if top_neg else 0
            lines.append(f"| {phase} | {pos_name} | {pos_count} | {neg_name} | {neg_count} |")
        lines.append("")

    return lines


def _format_archetype_trait_table(runs: list[dict[str, Any]]) -> list[str]:
    """Per-archetype × per-trait error breakdown."""
    from collections import defaultdict

    archetype_errors: dict[str, list[dict[str, float]]] = defaultdict(list)

    for run in runs:
        metrics = run.get("metrics", {})
        labels = metrics.get("actor_labels", {})
        errors = metrics.get("actor_trait_errors", {})
        for actor_id, label in labels.items():
            error_map = errors.get(actor_id, {})
            if error_map:
                archetype_errors[label].append(error_map)

    if not archetype_errors:
        return []

    lines = [
        "",
        "## Per-Archetype Trait Error",
        "",
        "| Archetype | n | O | C | E | A | N | MAE | Top Failed Trait |",
        "|-----------|---|---|---|---|---|---|-----|-----------------|",
    ]

    for label in sorted(archetype_errors.keys()):
        error_list = archetype_errors[label]
        n = len(error_list)
        trait_means = {}
        for trait in ("O", "C", "E", "A", "N"):
            vals = [e.get(trait, 0.0) for e in error_list]
            trait_means[trait] = sum(vals) / len(vals) if vals else 0.0
        mae = sum(trait_means.values()) / 5
        top_failed = max(trait_means, key=trait_means.get)
        trait_cells = " | ".join(f"{trait_means[t]:.3f}" for t in ("O", "C", "E", "A", "N"))
        lines.append(f"| {label} | {n} | {trait_cells} | {mae:.3f} | {top_failed} |")

    return lines


def _format_phase_feature_summary(runs: list[dict[str, Any]]) -> list[str]:
    """Per-phase behavioral feature summary from phase_quality mean_features."""
    from collections import defaultdict

    # Collect per-phase features across engine runs
    phase_features: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    engine_conditions = {"engine_dialogue_only", "engine_action_v0", "engine_controller", "engine_structural"}

    for run in runs:
        condition = run.get("condition", "")
        if condition not in engine_conditions:
            continue
        metrics = run.get("metrics", {})
        pq = metrics.get("phase_quality", {})
        for phase_name, phase_data in pq.items():
            mean_feats = phase_data.get("mean_features", {})
            for feat, val in mean_feats.items():
                phase_features[phase_name][feat].append(float(val))

    if not phase_features:
        return []

    phases = [p for p in ("OPENING", "TENSION", "NEGOTIATION", "CLOSING") if p in phase_features]
    if not phases:
        return []

    # Get feature names from first available phase
    all_features = sorted(next(iter(phase_features.values())).keys())

    lines = [
        "",
        "## Phase-Level Behavioral Features (Engine Condition)",
        "",
    ]

    header = "| Feature |"
    sep = "|---------|"
    for p in phases:
        header += f" {p} |"
        sep += "------|"
    if len(phases) >= 2:
        header += f" Delta ({phases[-1]} - {phases[0]}) |"
        sep += "------|"
    lines.append(header)
    lines.append(sep)

    for feat in all_features:
        row = f"| {feat} |"
        phase_means = []
        for p in phases:
            vals = phase_features[p].get(feat, [])
            m = sum(vals) / len(vals) if vals else 0.0
            phase_means.append(m)
            row += f" {m:.3f} |"
        if len(phases) >= 2:
            delta = phase_means[-1] - phase_means[0]
            row += f" {delta:+.3f} |"
        lines.append(row)

    return lines


def _format_scenario_difficulty_table(runs: list[dict[str, Any]]) -> list[str]:
    """Scenario difficulty vs drift comparison."""
    try:
        from .outcome_analysis import scenario_difficulty_index
        from .ground_truth import get_ground_truth
    except ImportError:
        return []

    # Group runs by script_id and condition
    from collections import defaultdict

    script_condition: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for run in runs:
        script_id = run.get("script_id", run.get("simulation_id", ""))
        condition = run.get("condition", "")
        drift = run.get("metrics", {}).get("persona_drift_mae", 0.0)
        script_condition[script_id][condition].append(drift)

    if not script_condition:
        return []

    lines = [
        "",
        "## Scenario Difficulty vs Drift",
        "",
        "| Scenario | Difficulty | Engine Drift | Naive Drift | Delta |",
        "|----------|-----------|-------------|-------------|-------|",
    ]

    engine_conditions = {"engine_dialogue_only", "engine_action_v0", "engine_controller", "engine_structural"}
    naive_conditions = {"naive", "naive_action_baseline", "naive_informed"}

    for script_id in sorted(script_condition.keys()):
        try:
            gt = get_ground_truth(script_id)
            difficulty = scenario_difficulty_index(gt)
        except Exception:
            difficulty = 0.0

        cond_data = script_condition[script_id]
        engine_vals = []
        naive_vals = []
        for cond, vals in cond_data.items():
            if cond in engine_conditions:
                engine_vals.extend(vals)
            elif cond in naive_conditions:
                naive_vals.extend(vals)

        engine_drift = sum(engine_vals) / len(engine_vals) if engine_vals else 0.0
        naive_drift = sum(naive_vals) / len(naive_vals) if naive_vals else 0.0
        delta = engine_drift - naive_drift

        short_name = script_id.split("_")[-1] if "_" in script_id else script_id
        lines.append(f"| {short_name} | {difficulty:.2f} | {engine_drift:.4f} | {naive_drift:.4f} | {delta:+.4f} |")

    return lines


def _format_influence_attribution_section(runs: list[dict[str, Any]]) -> list[str]:
    """Influence attribution: who drove key decisions."""
    from collections import Counter, defaultdict

    all_decision_points = []
    type_counts: Counter = Counter()
    type_concentrations: dict[str, list[float]] = defaultdict(list)
    influential_actors: Counter = Counter()
    total_dp = 0

    engine_conditions = {"engine_dialogue_only", "engine_action_v0", "engine_controller", "engine_structural"}

    for run in runs:
        condition = run.get("condition", "")
        if condition not in engine_conditions:
            continue
        metrics = run.get("metrics", {})
        ia = metrics.get("influence_attribution")
        if not ia:
            continue
        # Handle both formats: metrics stores build_influence_attribution() output (summary.total_decision_points)
        # and traceability stores compact format (decision_point_count)
        if isinstance(ia, dict):
            total_dp += ia.get("decision_point_count", 0) or ia.get("summary", {}).get("total_decision_points", 0)
        for dp in (ia.get("decision_points") or []) if isinstance(ia, dict) else []:
            all_decision_points.append(dp)
            dtype = dp.get("decision_type", "unknown")
            type_counts[dtype] += 1
            influences = dp.get("influences", [])
            if influences:
                top_score = influences[0].get("influence_score", 0.0) if influences else 0.0
                total_score = sum(inf.get("influence_score", 0.0) for inf in influences)
                concentration = top_score / total_score if total_score > 0 else 0.0
                type_concentrations[dtype].append(concentration)
                if influences:
                    influential_actors[influences[0].get("influencer_actor_id", "unknown")] += 1

    engine_run_count = sum(1 for r in runs if r.get("condition", "") in engine_conditions)
    if total_dp == 0:
        return []

    lines = [
        "",
        "## Influence Attribution: Who Drove Key Decisions?",
        "",
        f"### Decision Points Detected: {total_dp} across {engine_run_count} engine runs (mean {total_dp / max(engine_run_count, 1):.2f}/run)",
        "",
        "| Decision Type | Count | Mean Influence Concentration |",
        "|---------------|-------|------------------------------|",
    ]

    for dtype, count in type_counts.most_common():
        concs = type_concentrations.get(dtype, [])
        mean_conc = sum(concs) / len(concs) if concs else 0.0
        lines.append(f"| {dtype} | {count} | {mean_conc:.3f} |")

    # Top influence patterns
    if all_decision_points:
        lines.extend(["", "### Sample Decision Traces", ""])
        # Pick top 3 most interesting decision points (highest influence concentration)
        sorted_dps = sorted(
            all_decision_points,
            key=lambda dp: max((inf.get("influence_score", 0) for inf in dp.get("influences", [{}])), default=0),
            reverse=True,
        )
        for dp in sorted_dps[:3]:
            actor = dp.get("actor_id", "unknown")
            turn_idx = dp.get("turn_index", "?")
            phase = dp.get("phase_name", "?")
            dtype = dp.get("decision_type", "?")
            desc = dp.get("description", "")
            lines.append(f"> **{actor}** at turn {turn_idx} ({phase}): {dtype}")
            if desc:
                lines.append(f"> {desc}")
            influences = dp.get("influences", [])
            for inf in influences[:2]:
                inf_id = inf.get("influencer_actor_id", "?")
                score = inf.get("influence_score", 0.0)
                key_signal = inf.get("key_signal", "")
                lines.append(f"> - {inf_id}: score={score:.3f} — {key_signal}")
            narrative = dp.get("narrative", "")
            if narrative:
                lines.append(f"> {narrative}")
            lines.append("")

    return lines


def _save_dialogue_cache(results: dict[str, Any], output_path: Path) -> None:
    """Save lightweight dialogue cache for offline re-scoring."""
    cache_path = output_path / "dialogue_cache.jsonl"
    runs = results.get("runs", [])
    with open(cache_path, "w") as f:
        for run in runs:
            runtime_summary = run.get("runtime_summary", {})
            turns_data = runtime_summary.get("turns", [])
            if not turns_data:
                continue
            run_id = run.get("run_id", "")
            condition = run.get("condition", "")
            simulation_id = run.get("simulation_id", "")
            script_id = run.get("script_id", simulation_id)
            actor_count = len(runtime_summary.get("actor_ids", []))

            metrics = run.get("metrics", {})
            actor_priors = metrics.get("actor_personality_priors", {})
            actor_envelopes = metrics.get("actor_personality_envelopes", {})

            cache_turns = []
            for turn in turns_data:
                cache_turns.append({
                    "turn_index": turn.get("turn_number", turn.get("turn_index", 0)),
                    "actor_id": turn.get("actor_id", ""),
                    "display_name": turn.get("speaker_name", turn.get("display_name", "")),
                    "content": turn.get("content", ""),
                    "phase_name": turn.get("phase_name", ""),
                })

            # Include feature breakdowns and influence attribution for offline re-analysis
            actor_feature_breakdowns = metrics.get("actor_feature_breakdowns", {})
            influence_attribution = metrics.get("influence_attribution", {})

            entry = {
                "run_id": run_id,
                "condition": condition,
                "script_id": script_id,
                "actor_count": actor_count,
                "turns": cache_turns,
                "actor_priors": actor_priors,
                "actor_envelopes": actor_envelopes,
                "actor_feature_breakdowns": actor_feature_breakdowns,
                "influence_attribution": influence_attribution,
            }
            f.write(json.dumps(entry, separators=(",", ":")) + "\n")


def rescore_from_cache(
    cache_path: str | Path,
    metrics_fn=None,
) -> list[dict[str, Any]]:
    """Load dialogue cache and re-compute metrics with current calibration parameters.

    Args:
        cache_path: Path to dialogue_cache.jsonl.
        metrics_fn: Optional custom scoring function(turns, actor_name) -> dict[str, float].
                    Defaults to estimate_actor_traits_from_turns.

    Returns:
        List of dicts with run_id, condition, per-actor rescored traits, and drift.
    """
    from .metrics import estimate_actor_traits_from_turns, persona_drift_mae
    from .runtime import RuntimeTurnView

    if metrics_fn is None:
        metrics_fn = estimate_actor_traits_from_turns

    results = []
    with open(cache_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            turns = [
                RuntimeTurnView(
                    turn_number=t["turn_index"],
                    speaker_name=t["display_name"],
                    content=t["content"],
                )
                for t in entry.get("turns", [])
            ]
            if not turns:
                continue
            # Get unique actor names and their priors
            actor_names = sorted({t.speaker_name for t in turns})
            actor_priors = entry.get("actor_priors", {})
            actor_envelopes = entry.get("actor_envelopes", {})
            actor_traits = {}
            actor_drifts = {}
            actor_envelope_violations = {}
            for name in actor_names:
                traits = metrics_fn(turns, name)
                actor_traits[name] = traits
                # Find prior for this actor by matching display_name to actor_id
                # actor_priors is keyed by actor_id; find the matching one
                matched_prior = None
                matched_envelope = None
                for actor_id, prior in actor_priors.items():
                    # Match by checking if any turn for this name has this actor_id
                    for t_entry in entry.get("turns", []):
                        if t_entry.get("display_name") == name and t_entry.get("actor_id") == actor_id:
                            matched_prior = prior
                            matched_envelope = actor_envelopes.get(actor_id, {})
                            break
                    if matched_prior:
                        break
                if matched_prior:
                    actor_drifts[name] = persona_drift_mae(matched_prior, traits)
                    violations = 0
                    for trait, value in traits.items():
                        bounds = matched_envelope.get(trait, [0.0, 1.0])
                        if len(bounds) == 2 and (value < bounds[0] or value > bounds[1]):
                            violations += 1
                    actor_envelope_violations[name] = violations

            # Compute aggregate drift
            mean_drift = (
                round(sum(actor_drifts.values()) / len(actor_drifts), 4)
                if actor_drifts else 0.0
            )

            results.append({
                "run_id": entry.get("run_id", ""),
                "condition": entry.get("condition", ""),
                "script_id": entry.get("script_id", ""),
                "actor_count": entry.get("actor_count", 0),
                "actor_traits": actor_traits,
                "actor_drifts": actor_drifts,
                "actor_envelope_violations": actor_envelope_violations,
                "mean_drift": mean_drift,
            })
    return results
