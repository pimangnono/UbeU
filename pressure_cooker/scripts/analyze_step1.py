#!/usr/bin/env python3
"""
Step 1 Analysis: Agent Trait Consistency.

Loads all session data and validation results from multiple LLM judges,
then produces per-profile, per-scenario, per-trait breakdowns with
proper statistical metrics (Pearson correlation, MAE, inter-judge agreement).

Usage:
    python scripts/analyze_step1.py --batch-dir outputs/batches/8aec86a0
    python scripts/analyze_step1.py --batch-dir outputs/batches/8aec86a0 --output-report outputs/step1_report.md
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


TRAITS = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
TRAIT_SHORT = {"openness": "O", "conscientiousness": "C", "extraversion": "E",
               "agreeableness": "A", "neuroticism": "N"}


def load_sessions(batch_dir: Path) -> dict[str, dict]:
    """Load all session JSONs from a batch directory."""
    sessions = {}
    sessions_dir = batch_dir / "sessions"
    if not sessions_dir.exists():
        print(f"Error: sessions directory not found: {sessions_dir}")
        return sessions

    for f in sorted(sessions_dir.glob("*.json")):
        with open(f) as fp:
            data = json.load(fp)
        sid = data["metadata"]["session_id"]
        sessions[sid] = data

    return sessions


def discover_judges(validation_dir: Path, session_ids: list[str]) -> dict[str, str]:
    """
    Discover which LLM judges have validation results.

    Returns dict of {judge_label: file_prefix}.
    The default judge has files like llm_validation_{sid}.json.
    Additional judges have files like llm_validation_{model}_{sid}.json.
    """
    judges = {}

    # Check for default judge
    sample_id = session_ids[0]
    default_path = validation_dir / f"llm_validation_{sample_id}.json"
    if default_path.exists():
        judges["default"] = "llm_validation_"

    # Scan for other judges by looking for validation files with model prefixes.
    # Pattern: llm_validation_{model_name}_{session_id}.json
    # We find all unique model prefixes by checking files against known session IDs.
    seen_prefixes = set()
    for f in validation_dir.glob("llm_validation_*.json"):
        fname = f.stem  # e.g. "llm_validation_x-ai_grok-4.1-fast_7c4ebab6"
        # Check if this file ends with any known session ID
        for sid in session_ids:
            suffix = f"_{sid}"
            if fname.endswith(suffix):
                prefix_part = fname[: -len(suffix)]  # "llm_validation_x-ai_grok-4.1-fast"
                if prefix_part != "llm_validation":  # Skip default judge
                    model_name = prefix_part.replace("llm_validation_", "")
                    if model_name not in seen_prefixes:
                        seen_prefixes.add(model_name)
                        judges[model_name] = f"llm_validation_{model_name}_"
                break  # Only need one match per file

    return judges


def load_validation_results(
    validation_dir: Path,
    session_ids: list[str],
    judges: dict[str, str],
) -> dict[str, dict[str, dict]]:
    """
    Load validation results for all sessions and judges.

    Returns: {judge_label: {session_id: validation_data}}
    """
    results = {}
    for judge_label, prefix in judges.items():
        results[judge_label] = {}
        for sid in session_ids:
            fpath = validation_dir / f"{prefix}{sid}.json"
            if fpath.exists():
                with open(fpath) as fp:
                    results[judge_label][sid] = json.load(fp)
    return results


def compute_trait_metrics(
    sessions: dict[str, dict],
    validations: dict[str, dict],
    judge: str,
) -> dict:
    """Compute per-trait Pearson correlation, MAE, and RMSE across all sessions for one judge."""
    ground_truths = {t: [] for t in TRAITS}
    inferred = {t: [] for t in TRAITS}

    for sid, val in validations.get(judge, {}).items():
        if sid not in sessions:
            continue
        gt = val.get("ground_truth_profile", {})
        inf = val.get("inferred_profile", {})
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

        # Pearson correlation
        if np.std(gt_arr) > 0 and np.std(inf_arr) > 0:
            r, p = stats.pearsonr(gt_arr, inf_arr)
        else:
            r, p = 0.0, 1.0

        # Signed bias (positive = judge overestimates)
        bias = float(np.mean(inf_arr - gt_arr))

        metrics[t] = {
            "n": n,
            "pearson_r": round(r, 3),
            "p_value": round(p, 4),
            "mae": round(mae, 3),
            "rmse": round(rmse, 3),
            "bias": round(bias, 3),
        }

    return metrics


def compute_profile_breakdown(
    sessions: dict[str, dict],
    validations: dict[str, dict],
    judge: str,
) -> dict[str, dict]:
    """Compute per-profile mean accuracy and per-trait errors for one judge."""
    profile_data = defaultdict(lambda: {"accuracies": [], "errors": {t: [] for t in TRAITS}})

    for sid, val in validations.get(judge, {}).items():
        if sid not in sessions:
            continue
        profile_id = sessions[sid]["metadata"]["profile_id"]
        overall_acc = val.get("overall_accuracy", val.get("accuracy_scores", {}).get("overall", 0))
        profile_data[profile_id]["accuracies"].append(overall_acc)

        gt = val.get("ground_truth_profile", {})
        inf = val.get("inferred_profile", {})
        for t in TRAITS:
            error = inf.get(t, 0.5) - gt.get(t, 0.5)
            profile_data[profile_id]["errors"][t].append(error)

    breakdown = {}
    for pid, data in sorted(profile_data.items()):
        accs = data["accuracies"]
        breakdown[pid] = {
            "n_sessions": len(accs),
            "mean_accuracy": round(np.mean(accs), 3),
            "std_accuracy": round(np.std(accs), 3),
            "min_accuracy": round(min(accs), 3),
            "trait_mae": {},
            "trait_bias": {},
        }
        for t in TRAITS:
            errs = np.array(data["errors"][t])
            breakdown[pid]["trait_mae"][t] = round(float(np.mean(np.abs(errs))), 3)
            breakdown[pid]["trait_bias"][t] = round(float(np.mean(errs)), 3)

    return breakdown


def compute_scenario_breakdown(
    sessions: dict[str, dict],
    validations: dict[str, dict],
    judge: str,
) -> dict[str, dict]:
    """Compute per-scenario mean accuracy for one judge."""
    scenario_data = defaultdict(list)

    for sid, val in validations.get(judge, {}).items():
        if sid not in sessions:
            continue
        scenario_id = sessions[sid]["metadata"]["scenario_id"]
        overall_acc = val.get("overall_accuracy", val.get("accuracy_scores", {}).get("overall", 0))
        scenario_data[scenario_id].append(overall_acc)

    breakdown = {}
    for scid, accs in sorted(scenario_data.items()):
        breakdown[scid] = {
            "n_sessions": len(accs),
            "mean_accuracy": round(np.mean(accs), 3),
            "std_accuracy": round(np.std(accs), 3),
        }

    return breakdown


def compute_inter_judge_agreement(
    sessions: dict[str, dict],
    validations: dict[str, dict[str, dict]],
) -> dict:
    """
    Compute inter-judge agreement across all judges.

    Uses pairwise Pearson correlation between judge inferences
    and mean absolute difference.
    """
    judge_labels = list(validations.keys())
    if len(judge_labels) < 2:
        return {"note": "need at least 2 judges"}

    # Get common session IDs across all judges
    common_sids = set(validations[judge_labels[0]].keys())
    for jl in judge_labels[1:]:
        common_sids &= set(validations[jl].keys())
    common_sids = sorted(common_sids)

    if not common_sids:
        return {"note": "no common sessions across judges"}

    # Per-trait agreement
    trait_agreement = {}
    for t in TRAITS:
        judge_vectors = {}
        for jl in judge_labels:
            judge_vectors[jl] = []
            for sid in common_sids:
                inf = validations[jl][sid].get("inferred_profile", {})
                judge_vectors[jl].append(inf.get(t, 0.5))

        # Pairwise correlations
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

    # Overall (flatten all traits)
    all_r = []
    all_mad = []
    for t in TRAITS:
        if trait_agreement[t]["mean_pairwise_r"] is not None:
            all_r.append(trait_agreement[t]["mean_pairwise_r"])
        all_mad.append(trait_agreement[t]["mean_pairwise_mad"])

    return {
        "n_judges": len(judge_labels),
        "judges": judge_labels,
        "n_common_sessions": len(common_sids),
        "per_trait": trait_agreement,
        "overall_mean_pairwise_r": round(np.mean(all_r), 3) if all_r else None,
        "overall_mean_pairwise_mad": round(np.mean(all_mad), 3),
    }


def identify_weak_spots(
    profile_breakdown: dict[str, dict],
    trait_metrics: dict[str, dict],
) -> dict:
    """Identify profiles and traits that underperform."""
    # Worst profiles by accuracy
    sorted_profiles = sorted(profile_breakdown.items(), key=lambda x: x[1]["mean_accuracy"])
    worst_profiles = [(pid, d["mean_accuracy"]) for pid, d in sorted_profiles[:3]]

    # Worst traits by correlation
    sorted_traits = sorted(
        [(t, m.get("pearson_r", 0)) for t, m in trait_metrics.items()],
        key=lambda x: x[1],
    )
    weakest_traits = sorted_traits[:2]

    # Profiles with highest trait-specific errors
    worst_trait_per_profile = {}
    for pid, data in profile_breakdown.items():
        worst_t = max(data["trait_mae"].items(), key=lambda x: x[1])
        if worst_t[1] > 0.15:  # Only flag if MAE > 0.15
            worst_trait_per_profile[pid] = {"trait": worst_t[0], "mae": worst_t[1]}

    return {
        "worst_profiles": worst_profiles,
        "weakest_traits": weakest_traits,
        "high_error_profile_traits": worst_trait_per_profile,
    }


def generate_markdown_report(
    sessions: dict[str, dict],
    validations: dict[str, dict[str, dict]],
    judges: dict[str, str],
    batch_id: str,
) -> str:
    """Generate a comprehensive markdown report."""
    lines = []
    lines.append("# Step 1 Analysis: Agent Trait Consistency Report")
    lines.append("")
    lines.append(f"**Batch**: `{batch_id}`")
    lines.append(f"**Sessions**: {len(sessions)}")
    lines.append(f"**Judges**: {', '.join(judges.keys())}")
    lines.append(f"**Profiles**: {len(set(s['metadata']['profile_id'] for s in sessions.values()))}")
    lines.append(f"**Scenarios**: {len(set(s['metadata']['scenario_id'] for s in sessions.values()))}")
    lines.append("")

    # --- Per-Judge Results ---
    for judge in judges:
        lines.append(f"---")
        lines.append(f"## Judge: `{judge}`")
        lines.append("")

        # Trait-level metrics
        trait_metrics = compute_trait_metrics(sessions, validations, judge)
        lines.append("### Per-Trait Metrics")
        lines.append("")
        lines.append("| Trait | r | p-value | MAE | RMSE | Bias |")
        lines.append("|-------|---|---------|-----|------|------|")
        for t in TRAITS:
            m = trait_metrics[t]
            if "note" in m:
                lines.append(f"| {TRAIT_SHORT[t]} ({t}) | - | - | - | - | {m['note']} |")
            else:
                r_str = f"{m['pearson_r']:.3f}"
                p_str = f"{m['p_value']:.4f}"
                sig = ""
                if m["p_value"] < 0.001:
                    sig = " ***"
                elif m["p_value"] < 0.01:
                    sig = " **"
                elif m["p_value"] < 0.05:
                    sig = " *"
                lines.append(
                    f"| {TRAIT_SHORT[t]} ({t}) | {r_str}{sig} | {p_str} | "
                    f"{m['mae']:.3f} | {m['rmse']:.3f} | {m['bias']:+.3f} |"
                )
        lines.append("")

        # Profile breakdown
        profile_breakdown = compute_profile_breakdown(sessions, validations, judge)
        lines.append("### Per-Profile Accuracy")
        lines.append("")
        lines.append("| Profile | N | Mean Acc | Std | Worst Trait (MAE) | Bias Direction |")
        lines.append("|---------|---|----------|-----|-------------------|----------------|")
        for pid, data in sorted(profile_breakdown.items(), key=lambda x: x[1]["mean_accuracy"]):
            worst_trait = max(data["trait_mae"].items(), key=lambda x: x[1])
            # Find which direction the worst trait is biased
            bias_dir = data["trait_bias"][worst_trait[0]]
            bias_str = f"{TRAIT_SHORT[worst_trait[0]]} {'over' if bias_dir > 0 else 'under'} ({bias_dir:+.2f})"
            lines.append(
                f"| {pid} | {data['n_sessions']} | {data['mean_accuracy']:.3f} | "
                f"{data['std_accuracy']:.3f} | {TRAIT_SHORT[worst_trait[0]]}: {worst_trait[1]:.3f} | {bias_str} |"
            )
        lines.append("")

        # Scenario breakdown
        scenario_breakdown = compute_scenario_breakdown(sessions, validations, judge)
        lines.append("### Per-Scenario Accuracy")
        lines.append("")
        lines.append("| Scenario | N | Mean Acc | Std |")
        lines.append("|----------|---|----------|-----|")
        for scid, data in sorted(scenario_breakdown.items(), key=lambda x: x[1]["mean_accuracy"]):
            lines.append(
                f"| {scid} | {data['n_sessions']} | {data['mean_accuracy']:.3f} | "
                f"{data['std_accuracy']:.3f} |"
            )
        lines.append("")

        # Weak spots
        weak = identify_weak_spots(profile_breakdown, trait_metrics)
        lines.append("### Weak Spots")
        lines.append("")
        lines.append("**Bottom 3 profiles by accuracy:**")
        for pid, acc in weak["worst_profiles"]:
            lines.append(f"- `{pid}`: {acc:.3f}")
        lines.append("")
        lines.append("**Weakest traits by correlation:**")
        for t, r in weak["weakest_traits"]:
            lines.append(f"- `{t}`: r = {r:.3f}")
        lines.append("")
        if weak["high_error_profile_traits"]:
            lines.append("**Profile-trait combinations with MAE > 0.15:**")
            for pid, info in weak["high_error_profile_traits"].items():
                lines.append(f"- `{pid}` / `{info['trait']}`: MAE = {info['mae']:.3f}")
        lines.append("")

    # --- Inter-Judge Agreement ---
    lines.append("---")
    lines.append("## Inter-Judge Agreement")
    lines.append("")
    agreement = compute_inter_judge_agreement(sessions, validations)
    if "note" in agreement:
        lines.append(f"_{agreement['note']}_")
    else:
        lines.append(f"**Judges**: {', '.join(agreement['judges'])}")
        lines.append(f"**Common sessions**: {agreement['n_common_sessions']}")
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

    # --- Coverage Matrix ---
    lines.append("---")
    lines.append("## Coverage Matrix (Profile x Scenario)")
    lines.append("")
    all_profiles = sorted(set(s["metadata"]["profile_id"] for s in sessions.values()))
    all_scenarios = sorted(set(s["metadata"]["scenario_id"] for s in sessions.values()))

    header = "| Profile | " + " | ".join(all_scenarios) + " | Total |"
    lines.append(header)
    lines.append("|" + "---|" * (len(all_scenarios) + 2))

    for pid in all_profiles:
        counts = []
        total = 0
        for scid in all_scenarios:
            c = sum(
                1 for s in sessions.values()
                if s["metadata"]["profile_id"] == pid and s["metadata"]["scenario_id"] == scid
            )
            counts.append(str(c))
            total += c
        lines.append(f"| {pid} | " + " | ".join(counts) + f" | {total} |")

    lines.append("")

    # --- Recommendations ---
    lines.append("---")
    lines.append("## Recommendations")
    lines.append("")

    # Compute aggregate stats for recommendations
    default_judge = list(judges.keys())[0]
    tm = compute_trait_metrics(sessions, validations, default_judge)
    pb = compute_profile_breakdown(sessions, validations, default_judge)

    # Check if any traits have low correlation
    low_corr_traits = [t for t in TRAITS if tm[t].get("pearson_r", 0) < 0.4]
    if low_corr_traits:
        lines.append(f"1. **Low trait correlation**: {', '.join(low_corr_traits)} have r < 0.40. "
                      "Consider refining the personality prompts for these traits, or adding "
                      "more explicit behavioral instructions.")
    else:
        lines.append("1. **Trait correlations** are acceptable across all traits.")

    # Check if any profiles are consistently poor
    poor_profiles = [pid for pid, d in pb.items() if d["mean_accuracy"] < 0.80]
    if poor_profiles:
        lines.append(f"2. **Underperforming profiles**: {', '.join(poor_profiles)} have mean accuracy < 0.80. "
                      "Review their system prompts and behavioral tendencies.")
    else:
        lines.append("2. **All profiles** have mean accuracy >= 0.80.")

    # Check inter-judge agreement
    if "overall_mean_pairwise_r" in agreement and agreement["overall_mean_pairwise_r"] is not None:
        if agreement["overall_mean_pairwise_r"] < 0.5:
            lines.append(f"3. **Inter-judge agreement is low** (r = {agreement['overall_mean_pairwise_r']:.3f}). "
                          "Judges disagree on trait inference, which suggests the behavioral signals are ambiguous.")
        else:
            lines.append(f"3. **Inter-judge agreement** is reasonable (r = {agreement['overall_mean_pairwise_r']:.3f}).")

    # Repetitions
    reps = len(sessions) / (len(all_profiles) * len(all_scenarios))
    if reps < 3:
        lines.append(f"4. **Only {reps:.1f} rep(s) per combination**. Recommend expanding to 3 reps "
                      "to compute within-profile consistency (SD, ICC).")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Step 1 Analysis: Agent Trait Consistency")
    parser.add_argument(
        "--batch-dir",
        type=str,
        required=True,
        help="Path to batch directory (e.g., outputs/batches/8aec86a0)",
    )
    parser.add_argument(
        "--validation-dir",
        type=str,
        default=None,
        help="Path to validation directory (default: outputs/validation/)",
    )
    parser.add_argument(
        "--output-report",
        type=str,
        default=None,
        help="Output markdown report path (default: prints to stdout)",
    )
    parser.add_argument(
        "--output-json",
        type=str,
        default=None,
        help="Output JSON results path",
    )
    args = parser.parse_args()

    batch_dir = Path(args.batch_dir)
    if not batch_dir.is_absolute():
        batch_dir = Path(__file__).parent.parent / batch_dir

    validation_dir = Path(args.validation_dir) if args.validation_dir else batch_dir.parent.parent / "validation"
    if not validation_dir.is_absolute():
        validation_dir = Path(__file__).parent.parent / validation_dir

    # Load data
    print(f"Loading sessions from {batch_dir}...")
    sessions = load_sessions(batch_dir)
    print(f"  Found {len(sessions)} sessions")

    session_ids = list(sessions.keys())
    if not session_ids:
        print("No sessions found. Exiting.")
        return

    # Discover judges
    print(f"Scanning validation directory: {validation_dir}")
    judges = discover_judges(validation_dir, session_ids)
    print(f"  Found {len(judges)} judge(s): {list(judges.keys())}")

    # Load validations
    validations = load_validation_results(validation_dir, session_ids, judges)
    for jl, vd in validations.items():
        print(f"  {jl}: {len(vd)} validation results")

    # Read batch ID
    batch_summary_path = batch_dir / "batch_summary.json"
    if batch_summary_path.exists():
        with open(batch_summary_path) as f:
            batch_id = json.load(f).get("batch_id", batch_dir.name)
    else:
        batch_id = batch_dir.name

    # Generate report
    report = generate_markdown_report(sessions, validations, judges, batch_id)

    if args.output_report:
        output_path = Path(args.output_report)
        if not output_path.is_absolute():
            output_path = Path(__file__).parent.parent / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(report)
        print(f"\nReport written to: {output_path}")
    else:
        print("\n" + report)

    # Optionally output JSON
    if args.output_json:
        json_path = Path(args.output_json)
        if not json_path.is_absolute():
            json_path = Path(__file__).parent.parent / json_path
        json_path.parent.mkdir(parents=True, exist_ok=True)

        json_output = {}
        for judge in judges:
            json_output[judge] = {
                "trait_metrics": compute_trait_metrics(sessions, validations, judge),
                "profile_breakdown": compute_profile_breakdown(sessions, validations, judge),
                "scenario_breakdown": compute_scenario_breakdown(sessions, validations, judge),
                "weak_spots": identify_weak_spots(
                    compute_profile_breakdown(sessions, validations, judge),
                    compute_trait_metrics(sessions, validations, judge),
                ),
            }
        json_output["inter_judge_agreement"] = compute_inter_judge_agreement(sessions, validations)

        with open(json_path, "w") as f:
            json.dump(json_output, f, indent=2, default=str)
        print(f"JSON results written to: {json_path}")


if __name__ == "__main__":
    main()
