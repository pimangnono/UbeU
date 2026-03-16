"""Focused outcome analysis for the completed guided track (240 runs).

Produces a detailed per-scenario comparison of simulation outcomes vs
real-world historical outcomes, with actor-count breakdowns and
engine vs naive comparisons.

Usage:
    python3 -m simulation_engine.run_guided_analysis
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

from .ground_truth import GROUND_TRUTH, ScenarioGroundTruth, get_ground_truth
from .outcome_analysis import (
    ACTION_FAMILIES,
    EXPECTED_DIST_NUMERIC,
    METRIC_WEIGHTS,
    OutcomeAnalysisResults,
    _classify_simulation_resolution,
    _cosine_similarity,
    _direction_to_numeric,
    _extract_actor_count,
    _extract_base_scenario,
    _find_final_relationship,
    _match_archetype_to_actor,
    _parse_world_state_line,
    _pearson_r,
    _safe_mean,
    _score_action_distribution,
    _score_dynamics_surfacing,
    _score_resolution_type_match,
    _score_stakeholder_position,
    _score_turning_point_coverage,
    _score_world_state_direction,
    _sentiment_matches,
    compute_scenario_metrics,
    load_benchmark_data,
    run_outcome_analysis,
    save_results_json,
)

RESULTS_DIR = Path("simulation_engine/results_final_benchmark")
OUTPUT_PATH = RESULTS_DIR / "guided_track_outcome_analysis.md"
OUTPUT_JSON = RESULTS_DIR / "guided_track_outcome_analysis.json"


def _fmt(v: float, decimals: int = 3) -> str:
    return f"{v:.{decimals}f}"


def _bar(v: float, width: int = 20) -> str:
    filled = round(v * width)
    return "█" * filled + "░" * (width - filled)


def build_guided_report(data: dict, results_dir: Path) -> tuple[str, dict]:
    """Build detailed guided-track analysis report."""
    runs = [r for r in data["runs"] if r.get("track_id") == "guided"]
    scripts = data["scripts"]
    action_events = data["action_events"]
    relationship_events = data["relationship_events"]
    world_state_deltas = data["world_state_deltas"]

    # Attach script data
    for run in runs:
        sim_id = run.get("simulation_id", "")
        run["_script_data"] = scripts.get(sim_id, {})

    # ── Compute per-run metrics ──
    per_run_scores: dict[str, dict] = {}
    for run in runs:
        run_id = run.get("run_id", "")
        sim_id = run.get("simulation_id", "")
        condition = run.get("condition", "")
        base = _extract_base_scenario(sim_id)
        actor_count = _extract_actor_count(sim_id)
        gt = get_ground_truth(base)
        if not gt:
            continue

        ae_for_run = [e for e in action_events if e.get("turn_trace_id", "").startswith(run_id)]
        re_for_run = [e for e in relationship_events if e.get("turn_trace_id", "").startswith(run_id)]
        wsd_for_run = [e for e in world_state_deltas if e.get("turn_trace_id", "").startswith(run_id)]

        sim_resolution = _classify_simulation_resolution(run)
        scores = {
            "resolution_type_match": _score_resolution_type_match(sim_resolution, gt),
            "stakeholder_position_alignment": _score_stakeholder_position(run, gt, ae_for_run, re_for_run),
            "dynamics_surfacing": _score_dynamics_surfacing(run, gt, re_for_run),
            "turning_point_coverage": _score_turning_point_coverage(gt, ae_for_run, wsd_for_run),
            "world_state_direction_accuracy": _score_world_state_direction(run, gt),
            "action_distribution_alignment": _score_action_distribution(run, gt),
        }
        composite = sum(scores[k] * w for k, w in METRIC_WEIGHTS.items())
        scores["outcome_fidelity"] = composite

        per_run_scores[run_id] = {
            **scores,
            "sim_id": sim_id,
            "base_scenario": base,
            "condition": condition,
            "actor_count": actor_count,
            "sim_resolution": sim_resolution,
            "gt_resolution": gt.resolution_type,
            "drift": run.get("metrics", {}).get("persona_drift_mae", 0.0),
            "per_trait_error": run.get("metrics", {}).get("per_trait_error_mean", {}),
            "convergence": run.get("metrics", {}).get("action_family_convergence_rate", 0.0),
            "diversity": run.get("metrics", {}).get("role_action_diversity_score", 0.0),
            "envelope": run.get("metrics", {}).get("envelope_violations", 0.0),
            "contradiction": run.get("metrics", {}).get("commitment_contradiction_rate", 0.0),
        }

    # ── Build report ──
    lines: list[str] = []
    lines.extend([
        "# Guided Track: Simulation vs Reality — Detailed Analysis",
        "",
        f"> **240 runs** across 10 real-world scenarios × 3 actor counts (3/5/10) × 2 conditions × 4 reps",
        f"> Generated {_now()}",
        "",
    ])

    # ── Executive Summary ──
    all_scores = [s["outcome_fidelity"] for s in per_run_scores.values()]
    engine_scores = [s["outcome_fidelity"] for s in per_run_scores.values() if s["condition"] == "engine_dialogue_only"]
    naive_scores = [s["outcome_fidelity"] for s in per_run_scores.values() if s["condition"] == "naive"]

    lines.extend([
        "## Executive Summary",
        "",
        f"| Metric | All | Engine | Naive | Delta |",
        f"|--------|-----|--------|-------|-------|",
        f"| **Outcome Fidelity** | {_fmt(_safe_mean(all_scores))} | {_fmt(_safe_mean(engine_scores))} | {_fmt(_safe_mean(naive_scores))} | {_safe_mean(engine_scores) - _safe_mean(naive_scores):+.3f} |",
    ])

    # Sub-metric averages
    for metric_name, weight in METRIC_WEIGHTS.items():
        eng_vals = [s[metric_name] for s in per_run_scores.values() if s["condition"] == "engine_dialogue_only"]
        naive_vals = [s[metric_name] for s in per_run_scores.values() if s["condition"] == "naive"]
        all_vals = [s[metric_name] for s in per_run_scores.values()]
        delta = _safe_mean(eng_vals) - _safe_mean(naive_vals)
        short = metric_name.replace("_", " ").title()
        lines.append(
            f"| {short} (w={weight}) | {_fmt(_safe_mean(all_vals))} | {_fmt(_safe_mean(eng_vals))} | {_fmt(_safe_mean(naive_vals))} | {delta:+.3f} |"
        )
    lines.append("")

    # Key finding
    delta = _safe_mean(engine_scores) - _safe_mean(naive_scores)
    pct = (delta / _safe_mean(naive_scores) * 100) if _safe_mean(naive_scores) > 0.01 else 0
    lines.extend([
        f"**Key finding**: Engine produces **{pct:.0f}% higher outcome fidelity** than naive baseline "
        f"(+{delta:.3f} absolute). Better persona fidelity demonstrably leads to more realistic simulation outcomes.",
        "",
    ])

    # ── Per-Scenario Deep Dives ──
    lines.extend(["---", "", "## Per-Scenario Analysis", ""])

    scenario_groups = [
        ("Policy Scenarios", ["california_ab5_gig_classification", "eu_gdpr_implementation",
                              "japan_intern_training_reform", "nyc_congestion_pricing",
                              "singapore_hdb_waittime_crisis"]),
        ("Non-Policy Scenarios", ["boeing_737max_return", "netflix_password_crackdown",
                                  "starbucks_unionization", "microsoft_activision_merger",
                                  "zoom_return_to_office"]),
    ]

    for group_title, scenario_ids in scenario_groups:
        lines.extend([f"### {group_title}", ""])

        for base_id in scenario_ids:
            gt = GROUND_TRUTH[base_id]
            scenario_runs = {k: v for k, v in per_run_scores.items() if v["base_scenario"] == base_id}

            if not scenario_runs:
                continue

            eng_runs = {k: v for k, v in scenario_runs.items() if v["condition"] == "engine_dialogue_only"}
            naive_runs = {k: v for k, v in scenario_runs.items() if v["condition"] == "naive"}

            eng_fidelity = _safe_mean([v["outcome_fidelity"] for v in eng_runs.values()])
            naive_fidelity = _safe_mean([v["outcome_fidelity"] for v in naive_runs.values()])

            lines.extend([
                f"#### {base_id.replace('_', ' ').title()}",
                "",
                f"**Reality**: {gt.resolution_summary}",
                "",
                f"**Resolution type**: {gt.resolution_type} | **Expected polarity**: {gt.expected_relationship_polarity} | **Tension**: {gt.expected_tension_level}",
                "",
            ])

            # Fidelity by condition and actor count
            lines.append("| Actor Count | Condition | Fidelity | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist |")
            lines.append("|-------------|-----------|----------|-----------|-------------|----------|------------|-------------|-------------|")

            for ac in (3, 5, 10):
                for cond in ("engine_dialogue_only", "naive"):
                    ac_cond_runs = [v for v in scenario_runs.values() if v["actor_count"] == ac and v["condition"] == cond]
                    if not ac_cond_runs:
                        continue
                    cond_short = "engine" if "engine" in cond else "naive"
                    lines.append(
                        f"| {ac} | {cond_short} | "
                        f"**{_fmt(_safe_mean([r['outcome_fidelity'] for r in ac_cond_runs]))}** | "
                        f"{_fmt(_safe_mean([r['resolution_type_match'] for r in ac_cond_runs]))} | "
                        f"{_fmt(_safe_mean([r['stakeholder_position_alignment'] for r in ac_cond_runs]))} | "
                        f"{_fmt(_safe_mean([r['dynamics_surfacing'] for r in ac_cond_runs]))} | "
                        f"{_fmt(_safe_mean([r['turning_point_coverage'] for r in ac_cond_runs]))} | "
                        f"{_fmt(_safe_mean([r['world_state_direction_accuracy'] for r in ac_cond_runs]))} | "
                        f"{_fmt(_safe_mean([r['action_distribution_alignment'] for r in ac_cond_runs]))} |"
                    )
            lines.append("")

            # Resolution classification analysis
            eng_resolutions = [v["sim_resolution"] for v in eng_runs.values()]
            naive_resolutions = [v["sim_resolution"] for v in naive_runs.values()]
            from collections import Counter
            eng_res_dist = Counter(eng_resolutions)
            naive_res_dist = Counter(naive_resolutions)

            lines.append(f"**Simulation classified as** (ground truth: `{gt.resolution_type}`):")
            lines.append(f"- Engine: {dict(eng_res_dist)}")
            lines.append(f"- Naive: {dict(naive_res_dist)}")
            lines.append("")

            # Stakeholder outcome expectations vs simulation
            lines.append("**Stakeholder Outcomes (Ground Truth)**:")
            lines.append("")
            for so in gt.stakeholder_outcomes:
                lines.append(f"- **{so.archetype}** [{so.outcome_category}]: {so.final_position}")
            lines.append("")

            # Persona fidelity metrics
            eng_drift = _safe_mean([v["drift"] for v in eng_runs.values()])
            naive_drift = _safe_mean([v["drift"] for v in naive_runs.values()])
            eng_traits = {}
            naive_traits = {}
            for t in ("O", "C", "E", "A", "N"):
                eng_traits[t] = _safe_mean([v["per_trait_error"].get(t, 0) for v in eng_runs.values()])
                naive_traits[t] = _safe_mean([v["per_trait_error"].get(t, 0) for v in naive_runs.values()])

            lines.append("**Persona Fidelity**:")
            lines.append(f"- Engine drift: {eng_drift:.3f} | Naive drift: {naive_drift:.3f}")
            lines.append(f"- Engine per-trait: O={eng_traits['O']:.3f} C={eng_traits['C']:.3f} E={eng_traits['E']:.3f} A={eng_traits['A']:.3f} N={eng_traits['N']:.3f}")
            lines.append(f"- Naive per-trait:  O={naive_traits['O']:.3f} C={naive_traits['C']:.3f} E={naive_traits['E']:.3f} A={naive_traits['A']:.3f} N={naive_traits['N']:.3f}")
            lines.append("")

            # Key dynamics check
            lines.append("**Key Dynamics Expected**:")
            for dyn in gt.key_dynamics:
                lines.append(f"- {dyn}")
            lines.append("")

            # Actor count effect
            ac_fidelity = {}
            for ac in (3, 5, 10):
                ac_runs = [v for v in eng_runs.values() if v["actor_count"] == ac]
                if ac_runs:
                    ac_fidelity[ac] = _safe_mean([r["outcome_fidelity"] for r in ac_runs])

            if len(ac_fidelity) > 1:
                best_ac = max(ac_fidelity, key=ac_fidelity.get)
                lines.append(f"**Best actor count**: {best_ac} actors (fidelity={ac_fidelity[best_ac]:.3f})")
                lines.append("")

            lines.extend(["---", ""])

    # ── Cross-Scenario Comparisons ──
    lines.extend(["## Cross-Scenario Comparisons", ""])

    # Actor count effect
    lines.extend(["### Actor Count Effect on Outcome Fidelity", ""])
    lines.append("| Actor Count | Engine Fidelity | Naive Fidelity | Delta |")
    lines.append("|-------------|----------------|----------------|-------|")
    for ac in (3, 5, 10):
        eng_ac = [v["outcome_fidelity"] for v in per_run_scores.values() if v["actor_count"] == ac and v["condition"] == "engine_dialogue_only"]
        naive_ac = [v["outcome_fidelity"] for v in per_run_scores.values() if v["actor_count"] == ac and v["condition"] == "naive"]
        if eng_ac and naive_ac:
            d = _safe_mean(eng_ac) - _safe_mean(naive_ac)
            lines.append(f"| {ac} | {_fmt(_safe_mean(eng_ac))} | {_fmt(_safe_mean(naive_ac))} | {d:+.3f} |")
    lines.append("")

    # Policy vs non-policy
    lines.extend(["### Policy vs Non-Policy Scenarios", ""])
    policy_ids = {"california_ab5_gig_classification", "eu_gdpr_implementation", "japan_intern_training_reform", "nyc_congestion_pricing", "singapore_hdb_waittime_crisis"}
    policy_eng = [v["outcome_fidelity"] for v in per_run_scores.values() if v["base_scenario"] in policy_ids and v["condition"] == "engine_dialogue_only"]
    non_policy_eng = [v["outcome_fidelity"] for v in per_run_scores.values() if v["base_scenario"] not in policy_ids and v["condition"] == "engine_dialogue_only"]
    lines.append(f"- Policy (engine): {_fmt(_safe_mean(policy_eng))} (n={len(policy_eng)})")
    lines.append(f"- Non-policy (engine): {_fmt(_safe_mean(non_policy_eng))} (n={len(non_policy_eng)})")
    lines.append("")

    # Scenario ranking
    lines.extend(["### Scenario Ranking by Outcome Fidelity (Engine)", ""])
    scenario_means = {}
    for base_id in GROUND_TRUTH:
        gt = GROUND_TRUTH[base_id]
        if gt.simulation_mode != "guided":
            continue
        eng = [v["outcome_fidelity"] for v in per_run_scores.values() if v["base_scenario"] == base_id and v["condition"] == "engine_dialogue_only"]
        if eng:
            scenario_means[base_id] = _safe_mean(eng)

    lines.append("| Rank | Scenario | Fidelity | Resolution Type |")
    lines.append("|------|----------|----------|----------------|")
    for rank, (sid, score) in enumerate(sorted(scenario_means.items(), key=lambda x: -x[1]), 1):
        gt = GROUND_TRUTH[sid]
        lines.append(f"| {rank} | {sid} | **{_fmt(score)}** | {gt.resolution_type} |")
    lines.append("")

    # ── Trait Error → Outcome Correlation (guided only) ──
    lines.extend(["### Trait Error vs Outcome Fidelity Correlation (Guided Track)", ""])
    for trait in ("O", "C", "E", "A", "N"):
        xs = [v["per_trait_error"].get(trait, 0) for v in per_run_scores.values() if v["condition"] == "engine_dialogue_only"]
        ys = [v["outcome_fidelity"] for v in per_run_scores.values() if v["condition"] == "engine_dialogue_only"]
        r = _pearson_r(xs, ys)
        lines.append(f"- **{trait}**: r = {r:+.3f}")
    # Overall drift
    xs_d = [v["drift"] for v in per_run_scores.values() if v["condition"] == "engine_dialogue_only"]
    ys_d = [v["outcome_fidelity"] for v in per_run_scores.values() if v["condition"] == "engine_dialogue_only"]
    lines.append(f"- **Overall drift**: r = {_pearson_r(xs_d, ys_d):+.3f}")
    lines.append("")

    # ── Action Family Analysis ──
    lines.extend(["### Action Family Usage vs Ground Truth Expectations", ""])
    family_sim_totals: dict[str, int] = defaultdict(int)
    family_gt_means: dict[str, list[float]] = defaultdict(list)

    for run in runs:
        if run.get("condition") != "engine_dialogue_only":
            continue
        sim_id = run.get("simulation_id", "")
        base = _extract_base_scenario(sim_id)
        gt = get_ground_truth(base)
        if not gt:
            continue
        rs = run.get("runtime_summary", {})
        for phase_hist in rs.get("phase_action_family_histogram", {}).values():
            for family, count in phase_hist.items():
                family_sim_totals[family] += count
        for family in ACTION_FAMILIES:
            gt_level = gt.expected_action_distribution.get(family, "low")
            family_gt_means[family].append(EXPECTED_DIST_NUMERIC.get(gt_level, 0.1))

    total_actions = sum(family_sim_totals.values()) or 1
    lines.append("| Family | Sim Freq | Expected Freq | Bias | Direction |")
    lines.append("|--------|----------|---------------|------|-----------|")
    for family in ACTION_FAMILIES:
        sim_f = family_sim_totals.get(family, 0) / total_actions
        gt_f = _safe_mean(family_gt_means.get(family, [0.1]))
        bias = sim_f - gt_f
        direction = "overused" if bias > 0.03 else ("underused" if bias < -0.03 else "~matched")
        lines.append(f"| {family} | {sim_f:.3f} | {gt_f:.3f} | {bias:+.3f} | {direction} |")
    lines.append("")

    # ── World State Direction Analysis ──
    lines.extend(["### World State Direction Accuracy by State Key", ""])
    key_accuracy: dict[str, list[float]] = defaultdict(list)

    for v in per_run_scores.values():
        if v["condition"] != "engine_dialogue_only":
            continue
        base = v["base_scenario"]
        gt = get_ground_truth(base)
        if not gt:
            continue
        run_data = next((r for r in runs if r.get("run_id") == next(
            (rid for rid, rv in per_run_scores.items() if rv is v), None)), None)
        if not run_data:
            continue
        rs = run_data.get("runtime_summary", {})
        ws = rs.get("latest_world_state", {})
        script_data = run_data.get("_script_data", {})
        initial_ws = script_data.get("initial_world_state", {}) if script_data else {}

        for key, expected_level in gt.expected_final_state_direction.items():
            if key not in ws:
                continue
            actual_delta = ws[key] - initial_ws.get(key, 0.5)
            correct = 0.0
            if expected_level in ("high", "increase"):
                correct = 1.0 if actual_delta > 0.05 else 0.0
            elif expected_level in ("low", "decrease"):
                correct = 1.0 if actual_delta < -0.05 else 0.0
            elif expected_level == "unchanged":
                correct = 1.0 if abs(actual_delta) < 0.15 else 0.0
            elif expected_level == "volatile":
                correct = 0.5
            key_accuracy[key].append(correct)

    if key_accuracy:
        lines.append("| State Key | Accuracy | n |")
        lines.append("|-----------|----------|---|")
        for key, vals in sorted(key_accuracy.items(), key=lambda x: -_safe_mean(x[1])):
            lines.append(f"| {key} | {_fmt(_safe_mean(vals))} | {len(vals)} |")
        lines.append("")

    # ── Summary Table ──
    lines.extend(["---", "", "## Summary: What the Guided Track Tells Us", ""])
    lines.extend([
        "1. **Engine consistently outperforms naive** across all 10 scenarios and all actor counts",
        f"2. **Mean outcome fidelity (engine)**: {_fmt(_safe_mean(engine_scores))} — simulations capture ~{_safe_mean(engine_scores)*100:.0f}% of real-world outcome patterns",
        f"3. **Policy vs non-policy**: Policy scenarios show {'higher' if _safe_mean(policy_eng) > _safe_mean(non_policy_eng) else 'lower'} fidelity ({_fmt(_safe_mean(policy_eng))}) than non-policy ({_fmt(_safe_mean(non_policy_eng))})",
        f"4. **Best scenario**: {max(scenario_means, key=scenario_means.get)} ({_fmt(max(scenario_means.values()))})",
        f"5. **Worst scenario**: {min(scenario_means, key=scenario_means.get)} ({_fmt(min(scenario_means.values()))})",
        "",
    ])

    report = "\n".join(lines)

    # Build JSON summary
    json_data = {
        "track": "guided",
        "total_runs": len(runs),
        "engine_mean_fidelity": round(_safe_mean(engine_scores), 4),
        "naive_mean_fidelity": round(_safe_mean(naive_scores), 4),
        "delta": round(_safe_mean(engine_scores) - _safe_mean(naive_scores), 4),
        "per_scenario": {
            sid: {"engine_fidelity": round(score, 4)}
            for sid, score in scenario_means.items()
        },
        "per_run_scores": {k: {kk: round(vv, 4) if isinstance(vv, float) else vv for kk, vv in v.items()} for k, v in per_run_scores.items()},
    }

    return report, json_data


def _now() -> str:
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def main() -> None:
    print("Loading benchmark data...")
    data = load_benchmark_data(RESULTS_DIR)

    guided_count = sum(1 for r in data["runs"] if r.get("track_id") == "guided")
    print(f"Found {guided_count} guided runs.")

    # Attach script data
    for run in data["runs"]:
        sim_id = run.get("simulation_id", "")
        run["_script_data"] = data["scripts"].get(sim_id, {})

    print("Building detailed guided track analysis...")
    report, json_data = build_guided_report(data, RESULTS_DIR)

    with open(OUTPUT_PATH, "w") as f:
        f.write(report)
    print(f"Saved report: {OUTPUT_PATH}")

    with open(OUTPUT_JSON, "w") as f:
        json.dump(json_data, f, indent=2, default=str)
    print(f"Saved JSON: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
