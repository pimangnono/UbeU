#!/usr/bin/env python3
"""
Generate a single simulation session.
Usage: python scripts/generate_single.py --profile balanced_leader --scenario resource_conflict
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from clients.llm_client import create_client
from config.personality_profiles import get_all_profile_ids, get_profile
from config.scenarios import get_all_scenario_ids, get_scenario
from scripts.simulation_engine import SimulationEngine


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a single Pressure Cooker simulation"
    )
    parser.add_argument(
        "--profile",
        type=str,
        required=True,
        choices=get_all_profile_ids(),
        help="Personality profile ID",
    )
    parser.add_argument(
        "--scenario",
        type=str,
        required=True,
        choices=get_all_scenario_ids(),
        help="Scenario ID",
    )
    parser.add_argument(
        "--turn-limit",
        type=int,
        default=None,
        help="Override turn limit (default: use scenario default)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file path (default: outputs/sessions/<session_id>.json)",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use mock client (no API calls)",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print progress during simulation",
    )
    return parser.parse_args()


async def main():
    args = parse_args()

    # Load profile and scenario
    profile = get_profile(args.profile)
    scenario = get_scenario(args.scenario)

    print(f"Profile: {profile.name}")
    print(f"Scenario: {scenario.name}")
    print(f"Turn limit: {args.turn_limit or scenario.turn_limit}")

    # Create client
    client = create_client(use_mock=args.mock)

    if args.mock:
        print("Using mock client (no API calls)")
    else:
        print(f"Using Gemini API")
        print(f"Daily requests remaining: {client.rate_limiter.get_remaining_daily()}")

    # Create and run engine
    engine = SimulationEngine(
        client=client,
        profile=profile,
        scenario=scenario,
        turn_limit=args.turn_limit,
    )

    output = await engine.run(verbose=args.verbose)

    # Save output
    if args.output:
        output_path = Path(args.output)
    else:
        output_dir = Path("outputs/sessions")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{output.metadata.session_id}.json"

    with open(output_path, "w") as f:
        f.write(output.to_json())

    print(f"\nSession saved to: {output_path}")

    # Print summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Session ID: {output.metadata.session_id}")
    print(f"Total turns: {output.metadata.total_turns}")
    print(f"Duration: {output.metadata.duration_seconds:.1f}s")
    print(f"API calls: {output.metadata.api_calls}")

    if output.intent_statistics:
        print(f"\nDominant intent: {output.intent_statistics.dominant_intent}")
        if output.intent_statistics.secondary_intent:
            print(f"Secondary intent: {output.intent_statistics.secondary_intent}")

    if output.assessment_mapping:
        print("\nAssessment scores:")
        print(f"  Collaboration: {output.assessment_mapping.collaboration_score:.2f}")
        print(f"  Leadership: {output.assessment_mapping.leadership_score:.2f}")
        print(f"  Stress Management: {output.assessment_mapping.stress_management_score:.2f}")
        print(f"  Communication: {output.assessment_mapping.communication_score:.2f}")
        print(f"  Problem Solving: {output.assessment_mapping.problem_solving_score:.2f}")


if __name__ == "__main__":
    asyncio.run(main())
