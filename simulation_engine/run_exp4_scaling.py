"""Experiment 4: Variable Actor Count + Phase Structure.

Tests if the engine scales beyond the 3-actor × 4-phase fixture.
Variants:
  - 2-actor (subset of university merger)
  - 5-actor (university merger + 2 new stakeholders)
  - 3-phase (startup equity, drop CLOSING)
  - 5-phase (startup equity, add EXPLORATION between TENSION and NEGOTIATION)
"""
import asyncio
import copy
import json
from pathlib import Path

from simulation_engine.benchmark import SimulationBenchmarkRunner
from simulation_engine.reporting import save_benchmark_outputs
from simulation_engine.script import SimulationScript
from simulation_engine.run_exp2_novel import NOVEL_SCRIPTS

# ── Variant builders ─────────────────────────────────────────────────────────

def build_2_actor() -> dict:
    """2-actor: just the 2 department heads from university merger."""
    base = copy.deepcopy(NOVEL_SCRIPTS[0])  # university_dept_merger
    base["simulation_id"] = "scaling_2_actor"
    base["title"] = "Department Merger — 2 Actor Variant"
    # Keep only CS head (actor_2) and Bio head (actor_3)
    base["stakeholders"] = [s for s in base["stakeholders"] if s["actor_id"] in ("actor_2", "actor_3")]
    # Update phases to only target these actors
    for phase in base["phases"]:
        phase["target_actor_ids"] = []
    # Remove events that reference specific actors
    base["world_events"] = [e for e in base["world_events"] if not e.get("affected_actor_ids")]
    return base


def build_5_actor() -> dict:
    """5-actor: university merger + CFO + faculty union rep."""
    base = copy.deepcopy(NOVEL_SCRIPTS[0])  # university_dept_merger
    base["simulation_id"] = "scaling_5_actor"
    base["title"] = "Department Merger — 5 Actor Variant"
    base["stakeholders"].extend([
        {
            "actor_id": "actor_5",
            "display_name": "VP Torres",
            "role": "Chief Financial Officer",
            "identity_core": {"position": "VP finance", "domain": "university administration"},
            "personality_prior": {"O": 0.38, "C": 0.82, "E": 0.50, "A": 0.42, "N": 0.32},
            "incentives": ["cost reduction", "budget clarity"],
            "concerns": ["transition costs", "hidden liabilities"],
            "communication_style": {"tone": "analytical", "brevity": "concise"},
        },
        {
            "actor_id": "actor_6",
            "display_name": "Dr. Patel",
            "role": "Faculty Union Representative",
            "identity_core": {"position": "union steward", "domain": "faculty governance"},
            "personality_prior": {"O": 0.50, "C": 0.58, "E": 0.62, "A": 0.55, "N": 0.50},
            "incentives": ["job security", "faculty voice in governance"],
            "concerns": ["forced relocations", "workload changes"],
            "communication_style": {"tone": "advocacy", "brevity": "moderate"},
        },
    ])
    # Increase max_turns for phases to accommodate more actors
    for phase in base["phases"]:
        if phase["name"] in ("OPENING", "NEGOTIATION"):
            phase["max_turns"] = 5
    return base


def build_3_phase() -> dict:
    """3-phase: startup equity, drop CLOSING (merge into NEGOTIATION)."""
    base = copy.deepcopy(NOVEL_SCRIPTS[1])  # startup_equity_split
    base["simulation_id"] = "scaling_3_phase"
    base["title"] = "Startup Equity — 3 Phase Variant"
    # Remove CLOSING, extend NEGOTIATION
    base["phases"] = [p for p in base["phases"] if p["name"] != "CLOSING"]
    for phase in base["phases"]:
        if phase["name"] == "NEGOTIATION":
            phase["max_turns"] = 4
            phase["cues"].extend(["summary", "commitment"])
    return base


def build_5_phase() -> dict:
    """5-phase: startup equity, add EXPLORATION between TENSION and NEGOTIATION."""
    base = copy.deepcopy(NOVEL_SCRIPTS[1])  # startup_equity_split
    base["simulation_id"] = "scaling_5_phase"
    base["title"] = "Startup Equity — 5 Phase Variant"
    exploration_phase = {
        "name": "EXPLORATION",
        "goal": "Explore creative equity structures beyond simple percentage splits",
        "style": "neutral",
        "max_turns": 3,
        "cues": ["alternatives", "creative_structures"],
    }
    # Insert EXPLORATION between TENSION (index 1) and NEGOTIATION (index 2)
    base["phases"].insert(2, exploration_phase)
    return base


VARIANT_SCRIPTS = [
    build_2_actor(),
    build_5_actor(),
    build_3_phase(),
    build_5_phase(),
]


async def main():
    from experiment.run_experiment import create_clients
    gen_client, _ = create_clients()

    output_dir = "simulation_engine/results_exp4_scaling"

    scripts = [SimulationScript.from_dict(s) for s in VARIANT_SCRIPTS]
    print(f"[exp4] Validated {len(scripts)} variant scripts:")
    for s in scripts:
        print(f"  {s.simulation_id}: {len(s.stakeholders)} actors, {len(s.phases)} phases")

    runner = SimulationBenchmarkRunner(gen_client=gen_client)
    results = await runner.run_suite(
        conditions=["engine_dialogue_only"],
        repetitions=2,
        scripts=scripts,
        checkpoint_dir=output_dir,
    )
    save_benchmark_outputs(results, output_dir)
    print(f"\nExperiment 4 complete. Results in {output_dir}/")
    print(f"Aggregate: {json.dumps(results['aggregate'], indent=2)}")

    # Per-script breakdown
    print("\nPer-script results:")
    for key, data in results["aggregate_by_script"].items():
        print(f"  {key}:")
        print(f"    drift={data['persona_drift_mae_mean']:.4f}, "
              f"contradiction={data['commitment_contradiction_mean']:.4f}, "
              f"diversity={data['role_action_diversity_score_mean']:.4f}, "
              f"violations={data['envelope_violations_mean']:.1f}")


if __name__ == "__main__":
    asyncio.run(main())
