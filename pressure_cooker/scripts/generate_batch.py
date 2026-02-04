#!/usr/bin/env python3
"""
Generate batch of simulations across multiple profiles and scenarios.
Usage: python scripts/generate_batch.py --profiles all --scenarios all
"""

import argparse
import asyncio
import json
import sys
import uuid
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from clients.llm_client import create_client
from config.personality_profiles import get_all_profile_ids, get_profile
from config.scenarios import get_all_scenario_ids, get_scenario
from scripts.simulation_engine import SimulationEngine
from utils.models import BatchConfig, BatchResult


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate batch of Pressure Cooker simulations"
    )
    parser.add_argument(
        "--profiles",
        type=str,
        nargs="+",
        default=["all"],
        help="Profile IDs to use (or 'all')",
    )
    parser.add_argument(
        "--scenarios",
        type=str,
        nargs="+",
        default=["all"],
        help="Scenario IDs to use (or 'all')",
    )
    parser.add_argument(
        "--sessions-per",
        type=int,
        default=1,
        help="Sessions per profile-scenario combination",
    )
    parser.add_argument(
        "--turn-limit",
        type=int,
        default=30,
        help="Turn limit per session",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs/batches",
        help="Output directory for batch",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use mock client (no API calls)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without running",
    )
    return parser.parse_args()


async def run_batch(config: BatchConfig, mock: bool = False, dry_run: bool = False):
    """Run a batch of simulations."""
    batch_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now()

    # Resolve 'all'
    profiles = (
        get_all_profile_ids()
        if config.profiles == ["all"]
        else config.profiles
    )
    scenarios = (
        get_all_scenario_ids()
        if config.scenarios == ["all"]
        else config.scenarios
    )

    # Calculate total sessions
    total = len(profiles) * len(scenarios) * config.sessions_per_combination

    print(f"\n{'='*60}")
    print(f"BATCH GENERATION")
    print(f"{'='*60}")
    print(f"Batch ID: {batch_id}")
    print(f"Profiles: {len(profiles)}")
    print(f"Scenarios: {len(scenarios)}")
    print(f"Sessions per combination: {config.sessions_per_combination}")
    print(f"Total sessions: {total}")
    print(f"Turn limit: {config.turn_limit}")

    if dry_run:
        print(f"\n[DRY RUN - Not generating]\n")
        print("Would generate:")
        for profile_id in profiles:
            for scenario_id in scenarios:
                for i in range(config.sessions_per_combination):
                    print(f"  - {profile_id} x {scenario_id} (#{i+1})")
        return None

    # Check API limits
    client = create_client(use_mock=mock)

    if not mock:
        remaining = client.rate_limiter.get_remaining_daily()
        # Estimate API calls per session (rough: ~turns * 2 for generate + assess)
        estimated_calls = total * config.turn_limit * 2
        print(f"\nDaily API calls remaining: {remaining}")
        print(f"Estimated calls needed: {estimated_calls}")

        if estimated_calls > remaining and remaining < 900:
            print(f"\nWARNING: May exceed daily limit!")
            response = input("Continue anyway? [y/N]: ")
            if response.lower() != "y":
                print("Aborted.")
                return None

    # Create output directory
    output_dir = Path(config.output_dir) / batch_id
    output_dir.mkdir(parents=True, exist_ok=True)
    sessions_dir = output_dir / "sessions"
    sessions_dir.mkdir(exist_ok=True)

    # Track results
    session_ids = []
    errors = []
    successful = 0
    failed = 0

    # Generate sessions
    print(f"\nGenerating sessions...")
    session_num = 0

    for profile_id in profiles:
        profile = get_profile(profile_id)

        for scenario_id in scenarios:
            scenario = get_scenario(scenario_id)

            for i in range(config.sessions_per_combination):
                session_num += 1
                print(f"\n[{session_num}/{total}] {profile_id} x {scenario_id} (#{i+1})")

                try:
                    engine = SimulationEngine(
                        client=client,
                        profile=profile,
                        scenario=scenario,
                        turn_limit=config.turn_limit,
                    )

                    output = await engine.run(verbose=False)

                    # Save session
                    session_path = sessions_dir / f"{output.metadata.session_id}.json"
                    with open(session_path, "w") as f:
                        f.write(output.to_json())

                    session_ids.append(output.metadata.session_id)
                    successful += 1
                    print(f"  -> {output.metadata.session_id} ({output.metadata.total_turns} turns)")

                except Exception as e:
                    error_msg = f"{profile_id}/{scenario_id}/{i}: {str(e)}"
                    errors.append(error_msg)
                    failed += 1
                    print(f"  -> ERROR: {e}")

    # Create batch result
    result = BatchResult(
        batch_id=batch_id,
        timestamp=timestamp,
        config=config,
        total_sessions=total,
        successful_sessions=successful,
        failed_sessions=failed,
        session_ids=session_ids,
        errors=errors,
    )

    # Save batch summary
    summary_path = output_dir / "batch_summary.json"
    with open(summary_path, "w") as f:
        f.write(result.model_dump_json(indent=2))

    # Print summary
    print(f"\n{'='*60}")
    print(f"BATCH COMPLETE")
    print(f"{'='*60}")
    print(f"Successful: {successful}/{total}")
    print(f"Failed: {failed}/{total}")
    print(f"Output: {output_dir}")

    if errors:
        print(f"\nErrors:")
        for error in errors[:5]:  # Show first 5 errors
            print(f"  - {error}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more")

    return result


async def main():
    args = parse_args()

    config = BatchConfig(
        profiles=args.profiles,
        scenarios=args.scenarios,
        sessions_per_combination=args.sessions_per,
        turn_limit=args.turn_limit,
        output_dir=args.output_dir,
    )

    await run_batch(config, mock=args.mock, dry_run=args.dry_run)


if __name__ == "__main__":
    asyncio.run(main())
