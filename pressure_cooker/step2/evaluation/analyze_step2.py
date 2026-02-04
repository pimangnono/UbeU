#!/usr/bin/env python3
"""
Step 2 Analysis: Live Interview Validation.

Mirrors analyze_step1.py structure for Step 2 data:
- Per-trait Pearson r (LLM-inferred vs BFI-44 ground truth)
- Per-trait MAE
- Inter-judge agreement (pairwise Pearson)
- Post-survey averages
- Engagement filtering (exclude sessions with survey engagement < 3)
- Generates markdown report

Usage:
    python step2/evaluation/analyze_step2.py
    python step2/evaluation/analyze_step2.py --output-report outputs/step2/step2_report.md
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


TRAITS = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
TRAIT_SHORT = {
    "openness": "O", "conscientiousness": "C", "extraversion": "E",
    "agreeableness": "A", "neuroticism": "N",
}


def load_evaluation_results(eval_dir: Path) -> dict[str, list[dict]]:
    """Load evaluation results from the combined JSON file."""
    results_path = eval_dir / "step2_evaluation_results.json"
    if not results_path.exists():
        print(f"Error: {results_path} not found")
        return {}
    with open(results_path) as f:
        return json.load(f)


def load_participant_records(participants_dir: Path) -> dict[str, dict]:
    """Load all participant records."""
    records = {}
    for pid_dir in sorted(participants_dir.iterdir()):
        if not pid_dir.is_dir() or not pid_dir.name.startswith("P"):
            continue
        record_path = pid_dir / "record.json"
        if record_path.exists():
            with open(record_path) as f:
                records[pid_dir.name] = json.load(f)
    return records


def compute_trait_metrics(results: list[dict]) -> dict[str, dict]:
    """Compute per-trait Pearson r, MAE, RMSE, and bias for one judge."""
    ground_truths = {t: [] for t in TRAITS}
    inferred = {t: [] for t in TRAITS}

    for r in results:
        gt = r.get("ground_truth_profile", {})
        inf = r.get("inferred_profile", {})
        if not gt or not inf:
            continue
        for t in TRAITS:
            ground_truths[t].append(gt.get(t, 0.5))
            inferred[t].append(inf.get(t, 0.5))

    metrics = {}
    for t in TRAITS:
        gt_arr = np.array(ground_truths[t])
        inf_arr = np.array(inferred[t])
        n = len(gt_arr)

        if n < 3:
            metrics[t] = {"n": n, "note": "insufficient data"}
            continue

        mae = float(np.mean(np.abs(gt_arr - inf_arr)))
        rmse = float(np.sqrt(np.mean((gt_arr - inf_arr) ** 2)))
        bias = float(np.mean(inf_arr - gt_arr))

        if np.std(gt_arr) > 0 and np.std(inf_arr) > 0:
            r, p = stats.pearsonr(gt_arr, inf_arr)
        else:
            r, p = 0.0, 1.0

        metrics[t] = {
            "n": n,
            "pearson_r": round(r, 3),
            "p_value": round(p, 4),
            "mae": round(mae, 3),
            "rmse": round(rmse, 3),
            "bias": round(bias, 3),
        }

    return metrics


def compute_survey_summary(records: dict[str, dict]) -> dict:
    """Compute post-session survey averages."""
    items = ["naturalness", "authenticity", "realism", "engagement", "recommendation"]
    item_scores = {k: [] for k in items}
    open_feedbacks = []

    for pid, rec in records.items():
        survey = rec.get("survey")
        if not survey:
            continue
        for item in items:
            val = survey.get(item)
            if val is not None:
                item_scores[item].append(val)
        fb = survey.get("open_feedback", "")
        if fb:
            open_feedbacks.append(f"{pid}: {fb}")

    summary = {}
    for item in items:
        scores = item_scores[item]
        if scores:
            summary[item] = {
                "mean": round(np.mean(scores), 2),
                "std": round(np.std(scores), 2),
                "n": len(scores),
            }
        else:
            summary[item] = {"mean": 0, "std": 0, "n": 0}

    summary["open_feedbacks"] = open_feedbacks
    return summary


def compute_inter_judge_agreement(all_results: dict[str, list[dict]]) -> dict:
    """Compute inter-judge agreement across all judges."""
    judge_labels = list(all_results.keys())
    if len(judge_labels) < 2:
        return {"note": "need at least 2 judges"}

    # Build per-judge per-participant maps
    judge_data = {}
    for jl, results in all_results.items():
        judge_data[jl] = {r["participant_id"]: r for r in results}

    # Find common participants
    common_pids = set(judge_data[judge_labels[0]].keys())
    for jl in judge_labels[1:]:
        common_pids &= set(judge_data[jl].keys())
    common_pids = sorted(common_pids)

    if not common_pids:
        return {"note": "no common participants across judges"}

    trait_agreement = {}
    for t in TRAITS:
        judge_vectors = {}
        for jl in judge_labels:
            judge_vectors[jl] = [
                judge_data[jl][pid]["inferred_profile"].get(t, 0.5)
                for pid in common_pids
            ]

        pairwise_r = []
        pairwise_mad = []
        for i in range(len(judge_labels)):
            for j in range(i + 1, len(judge_labels)):
                v1 = np.array(judge_vectors[judge_labels[i]])
                v2 = np.array(judge_vectors[judge_labels[j]])
                if np.std(v1) > 0 and np.std(v2) > 0:
                    r, _ = stats.pearsonr(v1, v2)
                    pairwise_r.append(r)
                pairwise_mad.append(float(np.mean(np.abs(v1 - v2))))

        trait_agreement[t] = {
            "mean_pairwise_r": round(np.mean(pairwise_r), 3) if pairwise_r else None,
            "mean_pairwise_mad": round(np.mean(pairwise_mad), 3),
        }

    all_r = [ta["mean_pairwise_r"] for ta in trait_agreement.values() if ta["mean_pairwise_r"] is not None]
    all_mad = [ta["mean_pairwise_mad"] for ta in trait_agreement.values()]

    return {
        "n_judges": len(judge_labels),
        "judges": judge_labels,
        "n_common_participants": len(common_pids),
        "per_trait": trait_agreement,
        "overall_mean_pairwise_r": round(np.mean(all_r), 3) if all_r else None,
        "overall_mean_pairwise_mad": round(np.mean(all_mad), 3),
    }


def filter_by_engagement(
    all_results: dict[str, list[dict]],
    records: dict[str, dict],
    min_engagement: int = 3,
) -> dict[str, list[dict]]:
    """Exclude participants with survey engagement < min_engagement."""
    low_engagement_pids = set()
    for pid, rec in records.items():
        survey = rec.get("survey")
        if survey and survey.get("engagement", 5) < min_engagement:
            low_engagement_pids.add(pid)

    if low_engagement_pids:
        print(f"  Filtering out {len(low_engagement_pids)} low-engagement participants: {low_engagement_pids}")

    filtered = {}
    for judge, results in all_results.items():
        filtered[judge] = [r for r in results if r["participant_id"] not in low_engagement_pids]
    return filtered


def generate_markdown_report(
    all_results: dict[str, list[dict]],
    records: dict[str, dict],
    filtered_results: dict[str, list[dict]],
) -> str:
    """Generate comprehensive markdown report."""
    lines = []
    lines.append("# Step 2 Analysis: Live Interview Validation Report")
    lines.append("")

    n_participants = len(set(
        r["participant_id"]
        for results in all_results.values()
        for r in results
    ))
    lines.append(f"**Participants**: {n_participants}")
    lines.append(f"**Judges**: {', '.join(all_results.keys())}")
    lines.append("")

    # --- Per-Judge Metrics ---
    for judge, results in filtered_results.items():
        lines.append("---")
        lines.append(f"## Judge: `{judge}`")
        lines.append(f"_({len(results)} evaluations after engagement filtering)_")
        lines.append("")

        metrics = compute_trait_metrics(results)
        lines.append("### Per-Trait Metrics (LLM-inferred vs BFI-44 Ground Truth)")
        lines.append("")
        lines.append("| Trait | r | p-value | MAE | RMSE | Bias |")
        lines.append("|-------|---|---------|-----|------|------|")
        for t in TRAITS:
            m = metrics[t]
            if "note" in m:
                lines.append(f"| {TRAIT_SHORT[t]} ({t}) | - | - | - | - | {m['note']} |")
            else:
                sig = ""
                if m["p_value"] < 0.001:
                    sig = " ***"
                elif m["p_value"] < 0.01:
                    sig = " **"
                elif m["p_value"] < 0.05:
                    sig = " *"
                lines.append(
                    f"| {TRAIT_SHORT[t]} ({t}) | {m['pearson_r']:.3f}{sig} | "
                    f"{m['p_value']:.4f} | {m['mae']:.3f} | {m['rmse']:.3f} | "
                    f"{m['bias']:+.3f} |"
                )
        lines.append("")

    # --- Inter-Judge Agreement ---
    lines.append("---")
    lines.append("## Inter-Judge Agreement")
    lines.append("")
    agreement = compute_inter_judge_agreement(filtered_results)
    if "note" in agreement:
        lines.append(f"_{agreement['note']}_")
    else:
        lines.append(f"**Judges**: {', '.join(agreement['judges'])}")
        lines.append(f"**Common participants**: {agreement['n_common_participants']}")
        lines.append(f"**Overall mean pairwise r**: {agreement['overall_mean_pairwise_r']}")
        lines.append(f"**Overall mean pairwise MAD**: {agreement['overall_mean_pairwise_mad']}")
        lines.append("")
        lines.append("| Trait | Pairwise r | Pairwise MAD |")
        lines.append("|-------|-----------|-------------|")
        for t in TRAITS:
            ta = agreement["per_trait"][t]
            r_str = f"{ta['mean_pairwise_r']:.3f}" if ta["mean_pairwise_r"] is not None else "-"
            lines.append(f"| {TRAIT_SHORT[t]} ({t}) | {r_str} | {ta['mean_pairwise_mad']:.3f} |")
    lines.append("")

    # --- Survey Results ---
    lines.append("---")
    lines.append("## Post-Session Survey Results")
    lines.append("")
    survey = compute_survey_summary(records)
    survey_items = ["naturalness", "authenticity", "realism", "engagement", "recommendation"]
    lines.append("| Item | Mean | Std | N |")
    lines.append("|------|------|-----|---|")
    for item in survey_items:
        s = survey[item]
        lines.append(f"| {item.capitalize()} | {s['mean']:.2f} | {s['std']:.2f} | {s['n']} |")
    lines.append("")

    if survey.get("open_feedbacks"):
        lines.append("### Open Feedback")
        lines.append("")
        for fb in survey["open_feedbacks"]:
            lines.append(f"- {fb}")
        lines.append("")

    # --- Recommendations ---
    lines.append("---")
    lines.append("## Recommendations")
    lines.append("")

    # Check trait correlations from first judge
    if filtered_results:
        first_judge = list(filtered_results.keys())[0]
        tm = compute_trait_metrics(filtered_results[first_judge])
        low_corr = [t for t in TRAITS if tm[t].get("pearson_r", 0) < 0.4]
        if low_corr:
            lines.append(
                f"1. **Low trait correlation**: {', '.join(low_corr)} have r < 0.40 "
                "between LLM inference and BFI-44 ground truth. This may indicate "
                "these traits are harder to infer from conversation alone, or that "
                "the live setting produces less trait-diagnostic behavior."
            )
        else:
            lines.append("1. **All trait correlations** are above 0.40.")

    # Survey quality
    engagement = survey.get("engagement", {})
    if engagement.get("mean", 5) < 3.5:
        lines.append(
            "2. **Low engagement scores** suggest participants may not have been "
            "fully invested. Consider improving scenario engagement or screening."
        )
    else:
        lines.append("2. **Engagement scores** are satisfactory.")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Step 2 Analysis")
    parser.add_argument(
        "--eval-dir",
        type=str,
        default="outputs/step2/evaluation",
        help="Evaluation results directory",
    )
    parser.add_argument(
        "--participants-dir",
        type=str,
        default="outputs/step2/participants",
        help="Participants data directory",
    )
    parser.add_argument("--output-report", type=str, default=None)
    parser.add_argument("--output-json", type=str, default=None)
    parser.add_argument("--min-engagement", type=int, default=3)
    args = parser.parse_args()

    eval_dir = Path(args.eval_dir)
    participants_dir = Path(args.participants_dir)

    if not eval_dir.is_absolute():
        eval_dir = Path(__file__).parent.parent.parent / eval_dir
    if not participants_dir.is_absolute():
        participants_dir = Path(__file__).parent.parent.parent / participants_dir

    # Load data
    print("Loading evaluation results...")
    all_results = load_evaluation_results(eval_dir)
    if not all_results:
        print("No evaluation results found. Run run_step2_evaluation.py first.")
        return

    print("Loading participant records...")
    records = load_participant_records(participants_dir)
    print(f"  Found {len(records)} participant records")

    # Filter by engagement
    filtered = filter_by_engagement(all_results, records, args.min_engagement)

    # Generate report
    report = generate_markdown_report(all_results, records, filtered)

    if args.output_report:
        output_path = Path(args.output_report)
        if not output_path.is_absolute():
            output_path = Path(__file__).parent.parent.parent / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(report)
        print(f"\nReport written to: {output_path}")
    else:
        print("\n" + report)

    # Optional JSON output
    if args.output_json:
        json_path = Path(args.output_json)
        if not json_path.is_absolute():
            json_path = Path(__file__).parent.parent.parent / json_path
        json_path.parent.mkdir(parents=True, exist_ok=True)

        json_output = {}
        for judge, results in filtered.items():
            json_output[judge] = {
                "trait_metrics": compute_trait_metrics(results),
                "n_evaluations": len(results),
            }
        json_output["inter_judge_agreement"] = compute_inter_judge_agreement(filtered)
        json_output["survey_summary"] = compute_survey_summary(records)

        with open(json_path, "w") as f:
            json.dump(json_output, f, indent=2, default=str)
        print(f"JSON results written to: {json_path}")


if __name__ == "__main__":
    main()
