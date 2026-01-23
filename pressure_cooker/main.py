#!/usr/bin/env python3
"""
Pressure Cooker - Multi-Agent Personality Simulation Framework

Main entry point providing CLI interface for:
- Running single simulations
- Running batch generation
- Running validation
- Listing available profiles and scenarios

Usage:
    python main.py simulate --profile balanced_leader --scenario resource_conflict
    python main.py batch --profiles all --scenarios all
    python main.py validate --session outputs/sessions/abc123.json
    python main.py list
    python main.py test
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from clients.llm_client import create_client
from config.personality_profiles import get_all_profile_ids, get_profile, PERSONALITY_PROFILES
from config.scenarios import get_all_scenario_ids, get_scenario, SCENARIOS
from scripts.simulation_engine import SimulationEngine


def cmd_simulate(args):
    """Run a single simulation."""
    # Validate inputs
    if args.profile not in get_all_profile_ids():
        print(f"Error: Unknown profile '{args.profile}'")
        print(f"Available profiles: {', '.join(get_all_profile_ids())}")
        return 1

    if args.scenario not in get_all_scenario_ids():
        print(f"Error: Unknown scenario '{args.scenario}'")
        print(f"Available scenarios: {', '.join(get_all_scenario_ids())}")
        return 1

    async def run():
        profile = get_profile(args.profile)
        scenario = get_scenario(args.scenario)

        print(f"Profile: {profile.name}")
        print(f"Scenario: {scenario.name}")
        print(f"Turn limit: {args.turn_limit or scenario.turn_limit}")

        client = create_client(use_mock=args.mock)

        if args.mock:
            print("Using mock client (no API calls)")
        else:
            print("Using Gemini API")
            print(f"Daily requests remaining: {client.rate_limiter.get_remaining_daily()}")

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
        print(f"\nSUMMARY")
        print(f"Session ID: {output.metadata.session_id}")
        print(f"Total turns: {output.metadata.total_turns}")
        print(f"Duration: {output.metadata.duration_seconds:.1f}s")
        print(f"API calls: {output.metadata.api_calls}")

        if output.intent_statistics:
            print(f"Dominant intent: {output.intent_statistics.dominant_intent}")

    asyncio.run(run())
    return 0


def cmd_batch(args):
    """Run batch generation."""
    from scripts.generate_batch import run_batch
    from utils.models import BatchConfig

    profile_list = args.profiles if args.profiles != ["all"] else ["all"]
    scenario_list = args.scenarios if args.scenarios != ["all"] else ["all"]

    config = BatchConfig(
        profiles=profile_list,
        scenarios=scenario_list,
        sessions_per_combination=args.sessions_per,
        turn_limit=args.turn_limit,
        output_dir=args.output_dir,
    )

    asyncio.run(run_batch(config, mock=args.mock, dry_run=args.dry_run))
    return 0


def cmd_validate(args):
    """Run validation."""
    if not args.session and not args.batch:
        print("Error: Must specify --session or --batch")
        return 1

    # Build args for run_validation
    sys.argv = ["run_validation.py", "--mode", args.mode]
    if args.session:
        sys.argv.extend(["--session", args.session])
    if args.batch:
        sys.argv.extend(["--batch", args.batch])
    if args.evaluator:
        sys.argv.extend(["--evaluator", args.evaluator])
    if args.mock:
        sys.argv.append("--mock")
    if args.verbose:
        sys.argv.append("--verbose")

    from scripts.run_validation import main as run_validation
    asyncio.run(run_validation())
    return 0


def cmd_list(args):
    """List available profiles and scenarios."""
    print("\n=== PERSONALITY PROFILES (12 total) ===\n")

    for profile_id, profile in PERSONALITY_PROFILES.items():
        v = profile.vector
        traits = []
        if v.openness >= 0.7:
            traits.append("High O")
        elif v.openness <= 0.3:
            traits.append("Low O")
        if v.conscientiousness >= 0.7:
            traits.append("High C")
        elif v.conscientiousness <= 0.3:
            traits.append("Low C")
        if v.extraversion >= 0.7:
            traits.append("High E")
        elif v.extraversion <= 0.3:
            traits.append("Low E")
        if v.agreeableness >= 0.7:
            traits.append("High A")
        elif v.agreeableness <= 0.3:
            traits.append("Low A")
        if v.neuroticism >= 0.7:
            traits.append("High N")
        elif v.neuroticism <= 0.3:
            traits.append("Low N")

        trait_str = ", ".join(traits) if traits else "Balanced"
        print(f"  {profile_id:25s} {profile.name:25s} [{trait_str}]")

    print("\n=== SCENARIOS (4 total) ===\n")

    for scenario_id, scenario in SCENARIOS.items():
        print(f"  {scenario_id:20s} {scenario.name}")

    print("\n=== QUICK START ===\n")
    print("  # Run a single simulation (mock mode, no API key needed)")
    print("  python main.py simulate --profile balanced_leader --scenario resource_conflict --mock --verbose")
    print("")
    print("  # Run with real API")
    print("  python main.py simulate --profile creative_maverick --scenario deadline_pressure --verbose")
    print("")
    return 0


def cmd_test(args):
    """Run a quick test simulation."""
    print("\nRunning quick test simulation...\n")

    async def run_test():
        profile = get_profile("balanced_leader")
        scenario = get_scenario("resource_conflict")

        client = create_client(use_mock=args.mock)

        engine = SimulationEngine(
            client=client,
            profile=profile,
            scenario=scenario,
            turn_limit=5,
        )

        output = await engine.run(verbose=True)

        print(f"\nTest completed successfully!")
        print(f"Session ID: {output.metadata.session_id}")
        print(f"Turns generated: {output.metadata.total_turns}")

        if not args.mock:
            print(f"API calls used: {output.metadata.api_calls}")

    asyncio.run(run_test())
    return 0


def cmd_info(args):
    """Show framework information."""
    print("\n=== PRESSURE COOKER FRAMEWORK ===")
    print("Multi-agent personality simulation for synthetic conversation data\n")

    print("Components:")
    print("  - 12 distinct personality profiles (Big Five based)")
    print("  - 4 workplace conflict scenarios")
    print("  - Multi-agent simulation engine")
    print("  - Intent classification pipeline")
    print("  - Validation tools (LLM + human)")

    print("\nConfiguration:")
    import os
    from dotenv import load_dotenv
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        print("  GOOGLE_API_KEY: Configured")
    else:
        print("  GOOGLE_API_KEY: Not set (use --mock for testing)")

    print("\nRate Limits (Free Tier):")
    print("  - 2 requests per minute")
    print("  - 50 requests per day")
    print("  - ~2-3 simulations per day with default settings")

    print("\nModels:")
    print("  - gemini-1.5-pro: Candidate & Colleague agents")
    print("  - gemini-1.5-flash: System Manager agent")
    print("")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Pressure Cooker - Multi-agent personality simulation framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Simulate command
    sim_parser = subparsers.add_parser("simulate", help="Run a single simulation")
    sim_parser.add_argument("--profile", "-p", required=True, help="Personality profile ID")
    sim_parser.add_argument("--scenario", "-s", required=True, help="Scenario ID")
    sim_parser.add_argument("--turn-limit", "-t", type=int, help="Override turn limit")
    sim_parser.add_argument("--output", "-o", help="Output file path")
    sim_parser.add_argument("--mock", action="store_true", help="Use mock client")
    sim_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    # Batch command
    batch_parser = subparsers.add_parser("batch", help="Generate batch of simulations")
    batch_parser.add_argument("--profiles", "-p", nargs="+", default=["all"], help="Profile IDs")
    batch_parser.add_argument("--scenarios", "-s", nargs="+", default=["all"], help="Scenario IDs")
    batch_parser.add_argument("--sessions-per", type=int, default=1, help="Sessions per combination")
    batch_parser.add_argument("--turn-limit", "-t", type=int, default=30, help="Turn limit")
    batch_parser.add_argument("--output-dir", "-o", default="outputs/batches", help="Output directory")
    batch_parser.add_argument("--mock", action="store_true", help="Use mock client")
    batch_parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")

    # Validate command
    val_parser = subparsers.add_parser("validate", help="Validate generated sessions")
    val_parser.add_argument("--session", help="Path to session JSON file")
    val_parser.add_argument("--batch", help="Path to batch directory")
    val_parser.add_argument("--mode", "-m", choices=["llm", "human"], default="llm", help="Validation mode")
    val_parser.add_argument("--evaluator", "-e", default="anonymous", help="Evaluator ID")
    val_parser.add_argument("--mock", action="store_true", help="Use mock client")
    val_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    # List command
    subparsers.add_parser("list", help="List available profiles and scenarios")

    # Test command
    test_parser = subparsers.add_parser("test", help="Run quick test simulation")
    test_parser.add_argument("--mock", action="store_true", default=True, help="Use mock client (default)")
    test_parser.add_argument("--live", action="store_false", dest="mock", help="Use live API")

    # Info command
    subparsers.add_parser("info", help="Show framework information")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "simulate": cmd_simulate,
        "batch": cmd_batch,
        "validate": cmd_validate,
        "list": cmd_list,
        "test": cmd_test,
        "info": cmd_info,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
