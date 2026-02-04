#!/usr/bin/env python3
"""
Resume an incomplete batch by generating only missing sessions.
Writes new sessions into the same batch directory.

Usage: python scripts/resume_batch.py --batch-dir outputs/batches/4501beb2
"""

import argparse
import asyncio
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from clients.llm_client import create_client
from config.personality_profiles import get_all_profile_ids, get_profile
from config.scenarios import get_all_scenario_ids, get_scenario
from scripts.simulation_engine import SimulationEngine


def find_missing(batch_dir: Path, target_reps: int = 3):
    """Find profile/scenario combos that need more sessions."""
    sessions_dir = batch_dir / "sessions"
    coverage = defaultdict(int)

    for f in sessions_dir.glob("*.json"):
        with open(f) as fp:
            data = json.load(fp)
        m = data["metadata"]
        key = (m["profile_id"], m["scenario_id"])
        coverage[key] += 1

    missing = []
    for pid in get_all_profile_ids():
        for sid in get_all_scenario_ids():
            have = coverage.get((pid, sid), 0)
            need = target_reps - have
            if need > 0:
                missing.append((pid, sid, need))

    return missing


async def main():
    parser = argparse.ArgumentParser(description="Resume incomplete batch")
    parser.add_argument("--batch-dir", type=str, required=True)
    parser.add_argument("--target-reps", type=int, default=3)
    parser.add_argument("--turn-limit", type=int, default=30)
    parser.add_argument("--mock", action="store_true")
    args = parser.parse_args()

    batch_dir = Path(args.batch_dir)
    if not batch_dir.is_absolute():
        batch_dir = Path(__file__).parent.parent / batch_dir

    sessions_dir = batch_dir / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)

    missing = find_missing(batch_dir, args.target_reps)
    total = sum(need for _, _, need in missing)

    print(f"Batch dir: {batch_dir}")
    print(f"Missing sessions: {total}")
    print(f"Combos to generate: {len(missing)}")

    if total == 0:
        print("Nothing to do — batch is complete.")
        return

    client = create_client(use_mock=args.mock)
    successful = 0
    failed = 0
    session_num = 0

    for pid, sid, need in missing:
        profile = get_profile(pid)
        scenario = get_scenario(sid)

        for i in range(need):
            session_num += 1
            print(f"\n[{session_num}/{total}] {pid} x {sid} (#{i+1} of {need} needed)")

            try:
                engine = SimulationEngine(
                    client=client,
                    profile=profile,
                    scenario=scenario,
                    turn_limit=args.turn_limit,
                )

                output = await engine.run(verbose=False)

                session_path = sessions_dir / f"{output.metadata.session_id}.json"
                with open(session_path, "w") as f:
                    f.write(output.to_json())

                successful += 1
                print(f"  -> {output.metadata.session_id} ({output.metadata.total_turns} turns)")

            except Exception as e:
                failed += 1
                print(f"  -> ERROR: {e}")

    print(f"\nDone. Successful: {successful}, Failed: {failed}")
    print(f"Total sessions in batch: {len(list(sessions_dir.glob('*.json')))}")


if __name__ == "__main__":
    asyncio.run(main())
