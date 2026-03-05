"""
Human-Anchor Session Sampler.

Selects sessions for human annotation to triangulate LLM evaluations.
Sampling strategy:
- 16 from uncertain_queue.csv (highest uncertainty first)
- 16 stratified random from confident sessions
- Balanced by scenario and trait extremes.

Minimum viable anchor set: 20 sessions.
Target: 32 sessions.
"""

import csv
import json
import random
from pathlib import Path


def sample_sessions(
    results_dir: str,
    n_uncertain: int = 16,
    n_confident: int = 16,
    seed: int = 42,
) -> list[dict]:
    """
    Sample sessions for human annotation.

    Args:
        results_dir: Directory containing session JSONs and uncertain_queue.csv.
        n_uncertain: Number of uncertain sessions to include.
        n_confident: Number of confident sessions to include.
        seed: Random seed for reproducibility.

    Returns:
        List of session dicts with metadata for annotation.
    """
    results_path = Path(results_dir)
    random.seed(seed)

    # Load uncertain queue
    queue_path = results_path / "uncertain_queue.csv"
    uncertain_keys = set()
    if queue_path.exists():
        with open(queue_path) as f:
            reader = csv.DictReader(f)
            # Rank by number of uncertain traits per session
            session_uncertainty = {}
            for row in reader:
                key = row["session_key"]
                session_uncertainty[key] = session_uncertainty.get(key, 0) + 1
            # Sort by uncertainty count (descending)
            sorted_keys = sorted(session_uncertainty.keys(), key=lambda k: -session_uncertainty[k])
            uncertain_keys = set(sorted_keys[:n_uncertain])

    # Load all main sessions
    all_sessions = []
    for filepath in sorted(results_path.glob("session_*.json")):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue
        if data.get("condition") != "main":
            continue
        all_sessions.append(data)

    # Split into uncertain and confident
    uncertain_sessions = [s for s in all_sessions if s["session_key"] in uncertain_keys]
    confident_sessions = [s for s in all_sessions if s["session_key"] not in uncertain_keys]

    # Stratified sample from confident: balance by scenario
    scenario_groups = {}
    for s in confident_sessions:
        sid = s.get("scenario_id", "unknown")
        scenario_groups.setdefault(sid, []).append(s)

    n_per_scenario = max(1, n_confident // max(len(scenario_groups), 1))
    confident_sample = []
    for sid, sessions in scenario_groups.items():
        random.shuffle(sessions)
        confident_sample.extend(sessions[:n_per_scenario])

    # If we have fewer than n_confident, pad from remaining
    remaining = [s for s in confident_sessions if s not in confident_sample]
    random.shuffle(remaining)
    while len(confident_sample) < n_confident and remaining:
        confident_sample.append(remaining.pop())

    # Build final sample
    sampled = []
    for s in uncertain_sessions + confident_sample[:n_confident]:
        sampled.append({
            "session_key": s["session_key"],
            "profile_id": s.get("profile_id"),
            "scenario_id": s.get("scenario_id"),
            "assigned_vector": s.get("assigned_vector"),
            "inferred_vector": s.get("inferred_vector"),
            "source": "uncertain" if s["session_key"] in uncertain_keys else "confident",
        })

    return sampled


def save_sample(sampled: list[dict], output_path: str):
    """Save the sampled session list for annotation."""
    with open(output_path, "w") as f:
        json.dump(sampled, f, indent=2)
    print(f"Saved {len(sampled)} sessions for annotation to {output_path}")


def export_annotation_sheets(sampled: list[dict], results_dir: str, output_dir: str):
    """
    Export individual session transcripts as annotation-ready text files.

    Each file contains the transcript and an empty scoring template.
    """
    results_path = Path(results_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for item in sampled:
        key = item["session_key"]
        # Find the session file
        matching = list(results_path.glob(f"session_*_{key}.json"))
        if not matching:
            continue

        with open(matching[0]) as f:
            data = json.load(f)

        transcript = data.get("transcript", [])

        # Write annotation sheet
        sheet_path = output_path / f"annotate_{key}.txt"
        with open(sheet_path, "w") as f:
            f.write(f"SESSION: {key}\n")
            f.write(f"Profile: {data.get('profile_id', 'N/A')}\n")
            f.write(f"Scenario: {data.get('scenario_id', 'N/A')}\n")
            f.write("=" * 60 + "\n\n")
            f.write("TRANSCRIPT:\n\n")
            for turn in transcript:
                f.write(f"[Turn {turn['turn']}] {turn['speaker']}: {turn['content']}\n\n")
            f.write("=" * 60 + "\n")
            f.write("RATING (0.0 - 1.0):\n\n")
            f.write("O (Openness):          ___\n")
            f.write("C (Conscientiousness): ___\n")
            f.write("E (Extraversion):      ___\n")
            f.write("A (Agreeableness):     ___\n")
            f.write("N (Neuroticism):       ___\n\n")
            f.write("Rater ID: ___\n")
            f.write("Notes: \n")

    print(f"Exported {len(sampled)} annotation sheets to {output_dir}")
