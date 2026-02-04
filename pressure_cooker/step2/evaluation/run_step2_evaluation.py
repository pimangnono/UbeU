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

    # Print summary
    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)
    for judge_label, results in all_results.items():
        if results:
            accs = [r["overall_accuracy"] for r in results]
            mean_acc = sum(accs) / len(accs)
            print(f"  {judge_label}: mean accuracy = {mean_acc:.3f} ({len(results)} sessions)")


if __name__ == "__main__":
    asyncio.run(main())
