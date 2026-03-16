"""Arm B — Actor Scaling Stress Test.

Tests whether persona fidelity degrades as actor count increases.
Variants per script: 2-actor, 3-actor (baseline), 5-actor.
Scripts: housing_support_policy, commuting_support_policy,
         new_product_launch, post_merger_integration.
"""
import asyncio
import copy
import json
from pathlib import Path

from simulation_engine.benchmark import SimulationBenchmarkRunner
from simulation_engine.reporting import save_benchmark_outputs
from simulation_engine.script import SimulationScript
from simulation_engine.manual_scripts import (
    _MVP_POLICY_SCRIPTS,
    _augment_with_action_layer_spec,
)

# ── Load base scripts ────────────────────────────────────────────────────────

_TARGET_IDS = [
    "housing_support_policy",
    "commuting_support_policy",
    "new_product_launch",
    "post_merger_integration",
]

_BASE_SCRIPTS = {
    s["simulation_id"]: copy.deepcopy(s)
    for s in _MVP_POLICY_SCRIPTS
    if s["simulation_id"] in _TARGET_IDS
}


# ── 2-actor variants ─────────────────────────────────────────────────────────

def build_2_actor(base: dict) -> dict:
    """Drop actor_3 (administrator/coordinator/ops role) → 2 direct stakeholders."""
    v = copy.deepcopy(base)
    v["simulation_id"] = f"{base['simulation_id']}_2actor"
    v["title"] = f"{base['title']} — 2 Actor"
    kept_ids = {"actor_1", "actor_2"}
    v["stakeholders"] = [s for s in v["stakeholders"] if s["actor_id"] in kept_ids]
    # Clear target_actor_ids so the engine schedules freely
    for phase in v["phases"]:
        phase.pop("target_actor_ids", None)
    # Remove events referencing specific actors
    v["world_events"] = [
        e for e in v.get("world_events", [])
        if not e.get("affected_actor_ids")
    ]
    # Filter actor_action_preferences to only kept actors
    if "metadata" in v and isinstance(v["metadata"], dict):
        prefs = v["metadata"].get("actor_action_preferences", {})
        if prefs:
            v["metadata"]["actor_action_preferences"] = {
                k: val for k, val in prefs.items() if k in kept_ids
            }
    return v


# ── 5-actor variants ─────────────────────────────────────────────────────────

_EXTRA_ACTORS = {
    "housing_support_policy": [
        {
            "actor_id": "actor_4",
            "display_name": "Researcher Baek",
            "role": "Housing market analyst",
            "identity_core": {"age_band": "30s", "occupation": "think-tank researcher"},
            "personality_prior": {"O": 0.72, "C": 0.65, "E": 0.55, "A": 0.50, "N": 0.42},
            "incentives": ["evidence-based policy", "data transparency"],
            "concerns": ["selection bias in subsidy targeting", "long-run market distortion"],
            "communication_style": {"tone": "analytical", "brevity": "moderate"},
        },
        {
            "actor_id": "actor_5",
            "display_name": "Tenant Rep. Noh",
            "role": "Community tenant organizer",
            "identity_core": {"age_band": "40s", "occupation": "tenant association chair"},
            "personality_prior": {"O": 0.45, "C": 0.55, "E": 0.62, "A": 0.58, "N": 0.52},
            "incentives": ["broad access to subsidy", "tenant protections"],
            "concerns": ["administrative gatekeeping", "displacement from renovations"],
            "communication_style": {"tone": "advocacy", "brevity": "moderate"},
        },
    ],
    "commuting_support_policy": [
        {
            "actor_id": "actor_4",
            "display_name": "Driver Kwon",
            "role": "Logistics fleet operator",
            "identity_core": {"age_band": "40s", "occupation": "delivery fleet manager"},
            "personality_prior": {"O": 0.35, "C": 0.71, "E": 0.40, "A": 0.44, "N": 0.45},
            "incentives": ["predictable road congestion patterns", "fuel cost parity"],
            "concerns": ["transit overload worsening road access", "unfair mode subsidy"],
            "communication_style": {"tone": "pragmatic", "brevity": "concise"},
        },
        {
            "actor_id": "actor_5",
            "display_name": "Council Rep. Shin",
            "role": "District budget councillor",
            "identity_core": {"age_band": "50s", "occupation": "elected councillor"},
            "personality_prior": {"O": 0.40, "C": 0.75, "E": 0.58, "A": 0.42, "N": 0.38},
            "incentives": ["fiscal accountability", "constituent satisfaction"],
            "concerns": ["unfunded mandates", "coverage inequality between districts"],
            "communication_style": {"tone": "structured", "brevity": "moderate"},
        },
    ],
    "new_product_launch": [
        {
            "actor_id": "actor_4",
            "display_name": "Hyunwoo",
            "role": "Engineering tech lead",
            "identity_core": {"function": "engineering", "seniority": "senior engineer", "company_stage": "growth"},
            "personality_prior": {"O": 0.55, "C": 0.76, "E": 0.38, "A": 0.45, "N": 0.50},
            "incentives": ["technical stability", "manageable scope"],
            "concerns": ["rushed code", "test coverage gaps"],
            "communication_style": {"tone": "precise", "brevity": "moderate"},
        },
        {
            "actor_id": "actor_5",
            "display_name": "Sarah",
            "role": "Customer success lead",
            "identity_core": {"function": "customer_success", "seniority": "head", "company_stage": "growth"},
            "personality_prior": {"O": 0.48, "C": 0.68, "E": 0.56, "A": 0.62, "N": 0.44},
            "incentives": ["smooth onboarding experience", "low support ticket volume"],
            "concerns": ["missing documentation", "feature-gap complaints"],
            "communication_style": {"tone": "empathetic", "brevity": "moderate"},
        },
    ],
    "post_merger_integration": [
        {
            "actor_id": "actor_4",
            "display_name": "Ravi",
            "role": "Acquired team engineering lead",
            "identity_core": {"function": "engineering", "seniority": "tech lead", "company_type": "acquired"},
            "personality_prior": {"O": 0.60, "C": 0.58, "E": 0.44, "A": 0.48, "N": 0.56},
            "incentives": ["technical autonomy", "team stability"],
            "concerns": ["forced stack migration", "loss of development velocity"],
            "communication_style": {"tone": "direct", "brevity": "moderate"},
        },
        {
            "actor_id": "actor_5",
            "display_name": "Claire",
            "role": "Acquirer finance controller",
            "identity_core": {"function": "finance", "seniority": "VP", "company_type": "acquirer"},
            "personality_prior": {"O": 0.38, "C": 0.82, "E": 0.45, "A": 0.40, "N": 0.32},
            "incentives": ["cost synergy realization", "clean audit trail"],
            "concerns": ["hidden liabilities", "integration cost overruns"],
            "communication_style": {"tone": "analytical", "brevity": "concise"},
        },
    ],
}


def build_5_actor(base: dict) -> dict:
    """Add 2 contextually appropriate actors → 5 total."""
    v = copy.deepcopy(base)
    sim_id = base["simulation_id"]
    v["simulation_id"] = f"{sim_id}_5actor"
    v["title"] = f"{base['title']} — 5 Actor"
    v["stakeholders"].extend(copy.deepcopy(_EXTRA_ACTORS[sim_id]))
    # Increase max_turns for longer phases to accommodate more speakers
    for phase in v["phases"]:
        if phase["name"] in ("OPENING", "TENSION", "NEGOTIATION"):
            phase["max_turns"] = max(phase.get("max_turns", 3), 4)
    return v


# ── Build all variants ────────────────────────────────────────────────────────

def build_all_variants() -> list[dict]:
    """Augment each base script first (original sim_id), then create variants."""
    variants = []
    for sim_id in _TARGET_IDS:
        # Augment with action-layer spec BEFORE renaming simulation_id
        augmented = _augment_with_action_layer_spec(copy.deepcopy(_BASE_SCRIPTS[sim_id]))
        variants.append(build_2_actor(augmented))
        variants.append(copy.deepcopy(augmented))  # 3-actor baseline
        variants.append(build_5_actor(augmented))
    return variants


async def main():
    from experiment.run_experiment import create_clients
    gen_client, _ = create_clients()

    output_dir = "simulation_engine/results_2026-03-10_armB_scaling"

    raw_variants = build_all_variants()
    scripts = [SimulationScript.from_dict(s) for s in raw_variants]
    print(f"[armB] Validated {len(scripts)} variant scripts:")
    for s in scripts:
        print(f"  {s.simulation_id}: {len(s.stakeholders)} actors, {len(s.phases)} phases")

    runner = SimulationBenchmarkRunner(gen_client=gen_client)
    results = await runner.run_suite(
        conditions=["engine_dialogue_only"],
        repetitions=4,
        scripts=scripts,
        checkpoint_dir=output_dir,
    )
    save_benchmark_outputs(results, output_dir)
    print(f"\nArm B complete. Results in {output_dir}/")

    # Per-script breakdown
    print("\nPer-script results:")
    for key, data in sorted(results["aggregate_by_script"].items()):
        print(f"  {key}:")
        print(f"    drift={data['persona_drift_mae_mean']:.4f}, "
              f"contradiction={data['commitment_contradiction_mean']:.4f}, "
              f"convergence={data['action_family_convergence_rate_mean']:.4f}, "
              f"diversity={data['role_action_diversity_score_mean']:.4f}, "
              f"violations={data['envelope_violations_mean']:.1f}")


if __name__ == "__main__":
    asyncio.run(main())
