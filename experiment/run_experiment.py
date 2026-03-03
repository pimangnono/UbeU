"""
Experiment CLI Entry Point.

Usage:
    python -m experiment.run_experiment              # Full (164 sessions)
    python -m experiment.run_experiment --pilot       # Pilot (4 sessions)
    python -m experiment.run_experiment --analyze     # Analysis only
    python -m experiment.run_experiment --temporal    # Temporal analysis only
"""

import argparse
import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("experiment/experiment.log"),
    ],
)
logger = logging.getLogger(__name__)


def create_clients():
    """Create separate LLM clients for generation and evaluation."""
    from clients.llm_client import LLMClient

    # Generation client: uses default pro model (DeepSeek V3 via env or default)
    gen_client = LLMClient()

    # Evaluation client: same client, but ensemble uses Claude Haiku + Gemini + Grok
    # (Ensemble model 1 was already swapped to Claude 3.5 Haiku in Step 0)
    eval_client = LLMClient()

    return gen_client, eval_client


async def run_full_experiment(output_dir: str = "experiment/results"):
    """Run the full 164-session experiment."""
    gen_client, eval_client = create_clients()

    from experiment.batch_runner import BatchRunner
    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
    )

    summary = await runner.run_all()
    return summary


async def run_pilot_experiment(output_dir: str = "experiment/results"):
    """
    Run a pilot with 4 sessions:
    - Assertive Leader x Resource Conflict x 1 rep
    - Assertive Leader x Creative Brainstorm x 1 rep
    - Passive Avoider x Resource Conflict x 1 rep
    - Passive Avoider x Creative Brainstorm x 1 rep
    """
    gen_client, eval_client = create_clients()

    from experiment.batch_runner import BatchRunner, SessionSpec

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
    )

    # Override session list with pilot sessions
    pilot_profiles = ["assertive_leader", "passive_avoider"]
    pilot_scenarios = ["resource_conflict", "creative_brainstorm"]

    pilot_sessions = []
    for profile_id in pilot_profiles:
        for scenario_id in pilot_scenarios:
            key = f"main_{profile_id}_{scenario_id}_r1"
            pilot_sessions.append(SessionSpec(
                session_key=key,
                condition="main",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
            ))

    # Monkey-patch the session list builder
    runner._build_session_list = lambda: pilot_sessions

    summary = await runner.run_all()
    return summary


def run_analysis(results_dir: str = "experiment/results"):
    """Run statistical analysis on completed experiment results."""
    from experiment.analysis import run_full_analysis
    run_full_analysis(results_dir)


def run_temporal(results_dir: str = "experiment/results"):
    """Run temporal decay analysis on completed experiment results."""
    from experiment.temporal_analysis import run_temporal_analysis_batch

    async def _run():
        _, eval_client = create_clients()
        output_path = f"{results_dir}/temporal_analysis.json"
        await run_temporal_analysis_batch(eval_client, results_dir, output_path)

    asyncio.run(_run())


def main():
    parser = argparse.ArgumentParser(description="Behavioral Fidelity Experiment (V4)")
    parser.add_argument("--pilot", action="store_true", help="Run pilot (4 sessions)")
    parser.add_argument("--analyze", action="store_true", help="Run analysis only")
    parser.add_argument("--temporal", action="store_true", help="Run temporal analysis only")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory")

    args = parser.parse_args()

    if args.analyze:
        results_dir = args.output_dir or "experiment/results"
        print("Running statistical analysis...")
        run_analysis(results_dir)
        return

    if args.temporal:
        results_dir = args.output_dir or "experiment/results"
        print("Running temporal decay analysis...")
        run_temporal(results_dir)
        return

    if args.pilot:
        output_dir = args.output_dir or "experiment/results"
        print("Running PILOT experiment (4 sessions)...")
        summary = asyncio.run(run_pilot_experiment(output_dir))
    else:
        output_dir = args.output_dir or "experiment/results"
        print("Running FULL experiment (164 sessions)...")
        summary = asyncio.run(run_full_experiment(output_dir))

    print(f"\nFinal summary: {summary}")


if __name__ == "__main__":
    main()
