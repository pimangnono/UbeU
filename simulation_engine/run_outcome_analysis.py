"""CLI entry point for outcome analysis.

Usage:
    python3 -m simulation_engine.run_outcome_analysis \
        --results-dir simulation_engine/results_final_benchmark
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare simulation outcomes against real-world ground truth."
    )
    parser.add_argument(
        "--results-dir",
        type=str,
        default="simulation_engine/results_final_benchmark",
        help="Path to benchmark results directory",
    )
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    if not results_dir.exists():
        print(f"Error: results directory not found: {results_dir}", file=sys.stderr)
        sys.exit(1)

    # Lazy import to keep CLI startup fast
    from .outcome_analysis import (
        run_outcome_analysis,
        save_outcome_report,
        save_results_json,
    )

    results = run_outcome_analysis(results_dir)

    json_path = results_dir / "outcome_analysis_results.json"
    report_path = results_dir / "outcome_analysis_report.md"

    save_results_json(results, json_path)
    save_outcome_report(results, report_path)

    # Print summary
    total_runs = sum(m.num_runs for m in results.per_scenario)
    scores = [m.outcome_fidelity_score for m in results.per_scenario]
    mean_score = sum(scores) / len(scores) if scores else 0.0

    print(f"\n{'='*60}")
    print(f"Outcome Analysis Complete")
    print(f"{'='*60}")
    print(f"  Scenario-condition pairs: {len(results.per_scenario)}")
    print(f"  Total runs analyzed:      {total_runs}")
    print(f"  Mean outcome fidelity:    {mean_score:.3f}")
    print(f"  Diagnostics generated:    {len(results.diagnostics)}")
    print(f"  Recommendations:          {len(results.recommendations)}")
    print(f"\n  JSON:   {json_path}")
    print(f"  Report: {report_path}")


if __name__ == "__main__":
    main()
