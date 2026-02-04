#!/usr/bin/env python3
"""
Run validation on generated sessions.
Usage: python scripts/run_validation.py --session outputs/sessions/abc123.json
       python scripts/run_validation.py --batch outputs/batches/xyz789
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from clients.llm_client import create_client
from utils.models import SessionOutput
from validation.reverse_inference import (
    validate_session,
    batch_validate,
    summarize_validation_results,
)
from validation.human_evaluation import (
    format_session_for_display,
    run_cli_evaluation,
    save_evaluation,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Validate Pressure Cooker sessions"
    )
    parser.add_argument(
        "--session",
        type=str,
        help="Path to single session JSON file",
    )
    parser.add_argument(
        "--batch",
        type=str,
        help="Path to batch directory",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["llm", "human"],
        default="llm",
        help="Validation mode: llm (reverse inference) or human",
    )
    parser.add_argument(
        "--evaluator",
        type=str,
        default="anonymous",
        help="Evaluator ID for human validation",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs/validation",
        help="Output directory for results",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Override model for LLM validation (e.g. x-ai/grok-4.1-fast)",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use mock client for LLM validation",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
    )
    return parser.parse_args()


def load_session(filepath: str) -> SessionOutput:
    """Load a session from JSON file."""
    with open(filepath) as f:
        data = json.load(f)
    return SessionOutput.model_validate(data)


async def validate_single_llm(session_path: str, mock: bool, output_dir: str, verbose: bool, model: str = None):
    """Run LLM validation on a single session."""
    session = load_session(session_path)
    client = create_client(use_mock=mock, pro_model=model, flash_model=model) if model else create_client(use_mock=mock)

    print(f"Validating session: {session.metadata.session_id}")
    print(f"Profile: {session.profile.name}")
    print(f"Validation model: {client.pro_model_name if hasattr(client, 'pro_model_name') else 'mock'}")
    print(f"Ground truth traits: {session.profile.vector.to_dict()}")

    result = await validate_session(session, client)

    print(f"\nInferred traits: {result.inferred_profile.to_dict() if result.inferred_profile else 'N/A'}")
    print(f"\nAccuracy by trait:")
    for trait, acc in result.accuracy_scores.items():
        print(f"  {trait}: {acc:.1%}")

    # Save result
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    model_tag = client.pro_model_name.replace("/", "_") if hasattr(client, "pro_model_name") else "mock"
    result_file = output_path / f"llm_validation_{model_tag}_{session.metadata.session_id}.json"

    with open(result_file, "w") as f:
        f.write(result.model_dump_json(indent=2))

    print(f"\nResult saved to: {result_file}")

    return result


async def validate_batch_llm(batch_path: str, mock: bool, output_dir: str, verbose: bool, model: str = None):
    """Run LLM validation on a batch of sessions."""
    batch_dir = Path(batch_path)
    sessions_dir = batch_dir / "sessions"

    if not sessions_dir.exists():
        print(f"Error: No sessions directory found at {sessions_dir}")
        return

    # Load all sessions
    session_files = list(sessions_dir.glob("*.json"))
    print(f"Found {len(session_files)} sessions to validate")

    sessions = [load_session(str(f)) for f in session_files]
    client = create_client(use_mock=mock, pro_model=model, flash_model=model) if model else create_client(use_mock=mock)
    print(f"Validation model: {client.pro_model_name if hasattr(client, 'pro_model_name') else 'mock'}")

    # Run validation
    results = await batch_validate(sessions, client, verbose=verbose)

    # Summarize
    summary = summarize_validation_results(results)

    print(f"\n{'='*60}")
    print("VALIDATION SUMMARY")
    print(f"{'='*60}")
    print(f"Sessions validated: {summary['total_sessions']}")
    print(f"\nMean accuracy by trait:")
    for trait, acc in summary["mean_accuracy"].items():
        print(f"  {trait}: {acc:.1%}")

    # Save results
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Save individual results
    model_tag = client.pro_model_name.replace("/", "_") if hasattr(client, "pro_model_name") else "mock"
    for result in results:
        result_file = output_path / f"llm_validation_{model_tag}_{result.session_id}.json"
        with open(result_file, "w") as f:
            f.write(result.model_dump_json(indent=2))

    # Save summary
    summary_file = output_path / f"batch_validation_summary_{model_tag}_{batch_dir.name}.json"
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nResults saved to: {output_path}")

    return results, summary


def validate_single_human(session_path: str, evaluator: str, output_dir: str):
    """Run human validation on a single session."""
    session = load_session(session_path)

    print(f"\nStarting human evaluation for session: {session.metadata.session_id}")
    print(f"Evaluator: {evaluator}")
    print(f"\nPRESS ENTER TO BEGIN READING THE CONVERSATION")
    input()

    evaluation = run_cli_evaluation(session, evaluator)

    # Save evaluation
    filepath = save_evaluation(evaluation, output_dir)
    print(f"\nEvaluation saved to: {filepath}")

    # Show comparison if complete
    result = evaluation.to_validation_result()
    if result:
        print(f"\n{'='*60}")
        print("COMPARISON WITH GROUND TRUTH")
        print(f"{'='*60}")
        print(f"Ground truth: {session.profile.vector.to_dict()}")
        print(f"Your inference: {result.inferred_profile.to_dict() if result.inferred_profile else 'N/A'}")
        print(f"\nAccuracy by trait:")
        for trait, acc in result.accuracy_scores.items():
            print(f"  {trait}: {acc:.1%}")

    return evaluation


async def main():
    args = parse_args()

    if not args.session and not args.batch:
        print("Error: Must specify --session or --batch")
        return

    if args.mode == "llm":
        if args.session:
            await validate_single_llm(
                args.session, args.mock, args.output_dir, args.verbose, args.model
            )
        else:
            await validate_batch_llm(
                args.batch, args.mock, args.output_dir, args.verbose, args.model
            )
    else:  # human
        if not args.session:
            print("Error: Human validation requires --session (one at a time)")
            return
        validate_single_human(args.session, args.evaluator, args.output_dir)


if __name__ == "__main__":
    asyncio.run(main())
