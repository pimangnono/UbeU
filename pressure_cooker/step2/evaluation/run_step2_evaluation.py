#!/usr/bin/env python3
"""
Step 2 Evaluation: Run LLM judges on live interview transcripts.

Runs all 3 judges (DeepSeek, Gemini, Grok) on Step 2 transcripts using
the existing infer_personality() from validation/reverse_inference.py.

Uses participant's actual name as candidate_name instead of "Alex".

Usage:
    python step2/evaluation/run_step2_evaluation.py
    python step2/evaluation/run_step2_evaluation.py --participant P001
    python step2/evaluation/run_step2_evaluation.py --judge deepseek
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import statistics
from clients.llm_client import LLMClient, ModelTier
from utils.models import SessionOutput, PersonalityVector
from validation.reverse_inference import (
    infer_personality,
    calculate_accuracy,
    format_conversation_for_inference,
    compute_behavioral_stats,
)


# Judge configurations: (label, pro_model)
JUDGES = {
    "deepseek": "deepseek/deepseek-chat-v3-0324",
    "gemini": "google/gemini-2.5-flash-preview",
    "grok": "x-ai/grok-4.1-fast",
}

TRAITS = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]


def aggregate_ensemble_scores(
    all_results: dict[str, list[dict]],
    method: str = "median",
) -> dict[str, dict]:
    """
    Aggregate OCEAN scores from multiple judges into ensemble predictions.

    Args:
        all_results: Dict mapping judge_label -> list of result dicts
        method: Aggregation method - "mean", "median", or "weighted"
                (weighted uses accuracy-based weights)

    Returns:
        Dict mapping participant_id -> ensemble result with:
        - ensemble_scores: Final aggregated OCEAN scores
        - per_judge_scores: Individual judge predictions
        - agreement_metrics: Inter-judge agreement statistics
        - confidence: Overall confidence based on agreement
        - accuracy_vs_ground_truth: Accuracy of ensemble vs BFI-44 ground truth
    """
    # Group results by participant
    participant_results: dict[str, dict[str, dict]] = {}

    for judge_label, results in all_results.items():
        for result in results:
            pid = result["participant_id"]
            if pid not in participant_results:
                participant_results[pid] = {
                    "ground_truth": result["ground_truth_profile"],
                    "judges": {},
                }
            participant_results[pid]["judges"][judge_label] = {
                "inferred": result["inferred_profile"],
                "accuracy": result["overall_accuracy"],
            }

    ensemble_results = {}

    for pid, data in participant_results.items():
        judges_data = data["judges"]
        ground_truth = data["ground_truth"]

        if len(judges_data) < 2:
            # Need at least 2 judges for ensemble
            continue

        # Collect per-trait scores from each judge
        trait_scores: dict[str, list[float]] = {t: [] for t in TRAITS}
        judge_weights: dict[str, float] = {}

        for judge_label, judge_data in judges_data.items():
            inferred = judge_data["inferred"]
            judge_weights[judge_label] = judge_data["accuracy"]

            for trait in TRAITS:
                trait_scores[trait].append(inferred[trait])

        # Aggregate scores based on method
        ensemble_scores: dict[str, float] = {}
        trait_agreement: dict[str, dict] = {}

        for trait in TRAITS:
            scores = trait_scores[trait]

            if method == "median":
                ensemble_scores[trait] = round(statistics.median(scores), 3)
            elif method == "weighted":
                # Weight by each judge's overall accuracy
                total_weight = sum(judge_weights.values())
                weighted_sum = sum(
                    score * judge_weights[judge]
                    for judge, score in zip(judges_data.keys(), scores)
                )
                ensemble_scores[trait] = round(weighted_sum / total_weight, 3)
            else:  # mean
                ensemble_scores[trait] = round(statistics.mean(scores), 3)

            # Calculate agreement metrics for this trait
            trait_std = statistics.stdev(scores) if len(scores) > 1 else 0.0
            trait_range = max(scores) - min(scores)

            trait_agreement[trait] = {
                "std_dev": round(trait_std, 3),
                "range": round(trait_range, 3),
                "min": round(min(scores), 3),
                "max": round(max(scores), 3),
                "high_agreement": trait_std < 0.15,  # Threshold for "good" agreement
            }

        # Calculate overall agreement (inverse of average std dev)
        avg_std = statistics.mean(ta["std_dev"] for ta in trait_agreement.values())
        overall_confidence = round(max(0.0, 1.0 - (avg_std * 2)), 3)  # Scale: 0.15 std -> 0.7 conf

        # Calculate ensemble accuracy vs ground truth
        ensemble_vector = PersonalityVector(**ensemble_scores)
        ground_truth_vector = PersonalityVector(**ground_truth)
        ensemble_accuracy = calculate_accuracy(ensemble_vector, ground_truth_vector)

        # Flag traits with low agreement for review
        low_agreement_traits = [
            trait for trait, metrics in trait_agreement.items()
            if not metrics["high_agreement"]
        ]

        ensemble_results[pid] = {
            "participant_id": pid,
            "ensemble_method": method,
            "num_judges": len(judges_data),
            "ensemble_scores": ensemble_scores,
            "per_judge_scores": {
                judge: data["inferred"] for judge, data in judges_data.items()
            },
            "per_judge_accuracy": {
                judge: data["accuracy"] for judge, data in judges_data.items()
            },
            "ground_truth": ground_truth,
            "trait_agreement": trait_agreement,
            "overall_confidence": overall_confidence,
            "low_agreement_traits": low_agreement_traits,
            "ensemble_accuracy": ensemble_accuracy,
            "improvement_over_best_judge": round(
                ensemble_accuracy["overall"] - max(d["accuracy"] for d in judges_data.values()),
                3
            ),
        }

    return ensemble_results


def print_ensemble_summary(ensemble_results: dict[str, dict]) -> None:
    """Print a summary of ensemble results."""
    if not ensemble_results:
        print("No ensemble results to summarize.")
        return

    print("\n" + "=" * 70)
    print("ENSEMBLE AGGREGATION SUMMARY")
    print("=" * 70)

    # Overall statistics
    accuracies = [r["ensemble_accuracy"]["overall"] for r in ensemble_results.values()]
    confidences = [r["overall_confidence"] for r in ensemble_results.values()]
    improvements = [r["improvement_over_best_judge"] for r in ensemble_results.values()]

    print(f"\nParticipants with ensemble scores: {len(ensemble_results)}")
    print(f"Mean ensemble accuracy: {statistics.mean(accuracies):.3f}")
    print(f"Mean confidence (agreement): {statistics.mean(confidences):.3f}")
    print(f"Mean improvement over best single judge: {statistics.mean(improvements):+.3f}")

    # Per-trait agreement
    print("\nPer-Trait Agreement (avg std dev across participants):")
    for trait in TRAITS:
        std_devs = [r["trait_agreement"][trait]["std_dev"] for r in ensemble_results.values()]
        avg_std = statistics.mean(std_devs)
        agreement_pct = sum(1 for r in ensemble_results.values()
                          if r["trait_agreement"][trait]["high_agreement"]) / len(ensemble_results) * 100
        print(f"  {trait:20s}: std={avg_std:.3f}, high agreement={agreement_pct:.0f}%")

    # Low agreement flags
    all_low_agreement = []
    for r in ensemble_results.values():
        all_low_agreement.extend(r["low_agreement_traits"])

    if all_low_agreement:
        from collections import Counter
        trait_counts = Counter(all_low_agreement)
        print("\nTraits frequently flagged for low agreement:")
        for trait, count in trait_counts.most_common():
            print(f"  {trait}: {count} participants ({count/len(ensemble_results)*100:.0f}%)")

    # Per-participant details
    print("\nPer-Participant Results:")
    print("-" * 70)
    print(f"{'PID':<8} {'Ensemble Acc':>12} {'Confidence':>10} {'Improvement':>11} {'Low Agreement Traits'}")
    print("-" * 70)
    for pid, result in sorted(ensemble_results.items()):
        low_traits = ", ".join(result["low_agreement_traits"][:2]) or "none"
        print(f"{pid:<8} {result['ensemble_accuracy']['overall']:>12.3f} "
              f"{result['overall_confidence']:>10.3f} "
              f"{result['improvement_over_best_judge']:>+11.3f} "
              f"{low_traits}")


def load_participant_data(participants_dir: Path) -> list[dict]:
    """Load all participant data with session outputs and BFI-44 scores."""
    participants = []

    for pid_dir in sorted(participants_dir.iterdir()):
        if not pid_dir.is_dir() or not pid_dir.name.startswith("P"):
            continue

        record_path = pid_dir / "record.json"
        session_path = pid_dir / "session_output.json"

        if not record_path.exists() or not session_path.exists():
            continue

        with open(record_path) as f:
            record = json.load(f)
        with open(session_path) as f:
            session_data = json.load(f)

        # Need BFI-44 scores as ground truth
        bfi44_scores = record.get("bfi44_scores")
        if not bfi44_scores:
            print(f"  Skipping {pid_dir.name}: no BFI-44 scores")
            continue

        participants.append({
            "participant_id": pid_dir.name,
            "name": record.get("name", pid_dir.name),
            "bfi44_ground_truth": PersonalityVector(**bfi44_scores),
            "session": SessionOutput.model_validate(session_data),
        })

    return participants


async def run_judge(
    judge_label: str,
    model_name: str,
    participants: list[dict],
    output_dir: Path,
    verbose: bool = False,
) -> list[dict]:
    """Run a single judge on all participant transcripts."""
    client = LLMClient(pro_model=model_name, flash_model=model_name)
    results = []

    for p in participants:
        pid = p["participant_id"]
        session = p["session"]
        ground_truth = p["bfi44_ground_truth"]
        candidate_name = p["name"]

        if verbose:
            print(f"  [{judge_label}] Inferring personality for {pid} ({candidate_name})...")

        max_retries = 3
        for attempt in range(max_retries):
            try:
                inferred = await infer_personality(
                    session, client, candidate_name=candidate_name
                )

                accuracy = calculate_accuracy(inferred, ground_truth)

                result = {
                    "participant_id": pid,
                    "judge": judge_label,
                    "candidate_name": candidate_name,
                    "session_id": session.metadata.session_id,
                    "inferred_profile": inferred.model_dump(),
                    "ground_truth_profile": ground_truth.model_dump(),
                    "accuracy_scores": accuracy,
                    "overall_accuracy": accuracy["overall"],
                }
                results.append(result)

                # Save individual result
                result_path = output_dir / f"inference_{judge_label}_{pid}.json"
                with open(result_path, "w") as f:
                    json.dump(result, f, indent=2)

                if verbose:
                    print(f"    Accuracy: {accuracy['overall']:.3f}")
                break

            except Exception as e:
                if attempt < max_retries - 1:
                    wait = 10 * (attempt + 1)
                    if verbose:
                        print(f"    Attempt {attempt+1} failed: {e}. Retrying in {wait}s...")
                    await asyncio.sleep(wait)
                else:
                    if verbose:
                        print(f"    SKIPPED after {max_retries} attempts: {e}")

    return results


async def main():
    parser = argparse.ArgumentParser(description="Step 2 Evaluation: Run LLM judges")
    parser.add_argument(
        "--participants-dir",
        type=str,
        default="outputs/step2/participants",
        help="Directory containing participant data",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs/step2/evaluation",
        help="Directory for evaluation results",
    )
    parser.add_argument(
        "--participant",
        type=str,
        default=None,
        help="Run only for a specific participant ID (e.g., P001)",
    )
    parser.add_argument(
        "--judge",
        type=str,
        choices=list(JUDGES.keys()),
        default=None,
        help="Run only a specific judge",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--ensemble-method",
        type=str,
        choices=["median", "mean", "weighted"],
        default="median",
        help="Method for ensemble aggregation (default: median)",
    )
    args = parser.parse_args()

    participants_dir = Path(args.participants_dir)
    if not participants_dir.is_absolute():
        participants_dir = Path(__file__).parent.parent.parent / participants_dir

    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = Path(__file__).parent.parent.parent / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load participant data
    print(f"Loading participants from {participants_dir}...")
    participants = load_participant_data(participants_dir)
    print(f"  Found {len(participants)} participants with complete data")

    if not participants:
        print("No participants found. Exiting.")
        return

    # Filter by participant if specified
    if args.participant:
        participants = [p for p in participants if p["participant_id"] == args.participant]
        if not participants:
            print(f"Participant {args.participant} not found.")
            return

    # Select judges
    judges_to_run = JUDGES
    if args.judge:
        judges_to_run = {args.judge: JUDGES[args.judge]}

    # Run each judge
    all_results = {}
    for judge_label, model_name in judges_to_run.items():
        print(f"\nRunning judge: {judge_label} ({model_name})")
        results = await run_judge(
            judge_label, model_name, participants, output_dir, args.verbose
        )
        all_results[judge_label] = results
        print(f"  Completed {len(results)} evaluations")

    # Save combined results
    summary_path = output_dir / "step2_evaluation_results.json"
    with open(summary_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {summary_path}")

    # Print per-judge summary
    print("\n" + "=" * 60)
    print("PER-JUDGE SUMMARY")
    print("=" * 60)
    for judge_label, results in all_results.items():
        if results:
            accs = [r["overall_accuracy"] for r in results]
            mean_acc = sum(accs) / len(accs)
            print(f"  {judge_label}: mean accuracy = {mean_acc:.3f} ({len(results)} sessions)")

    # Run ensemble aggregation if we have multiple judges
    if len(all_results) >= 2:
        # Run all three aggregation methods
        for method in ["median", "mean", "weighted"]:
            ensemble_results = aggregate_ensemble_scores(all_results, method=method)

            # Save ensemble results
            ensemble_path = output_dir / f"ensemble_{method}_results.json"
            with open(ensemble_path, "w") as f:
                json.dump(ensemble_results, f, indent=2, default=str)

            if method == "median":  # Print detailed summary for default method
                print_ensemble_summary(ensemble_results)

        print(f"\nEnsemble results saved to {output_dir}/ensemble_*.json")
    else:
        print("\nSkipping ensemble aggregation (need at least 2 judges)")


if __name__ == "__main__":
    asyncio.run(main())
