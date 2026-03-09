"""Experiment 2: Novel Scripts — Generalization Test.

Creates 2 new scripts the engine has never seen and runs them.
"""
import asyncio
import json
from pathlib import Path

from simulation_engine.benchmark import SimulationBenchmarkRunner, aggregate_benchmark_runs, aggregate_benchmark_runs_by_script
from simulation_engine.reporting import save_benchmark_outputs
from simulation_engine.script import SimulationScript

NOVEL_SCRIPTS = [
    {
        "simulation_id": "university_dept_merger",
        "title": "University Department Merger",
        "objective": "Decide whether to merge the CS and Biology departments into a single unit.",
        "brief": (
            "The university administration is considering merging the Computer Science and Biology "
            "departments to save costs and encourage interdisciplinary research. Stakeholders have "
            "different views on autonomy, resources, and academic identity."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Dean Chen",
                "role": "College Dean",
                "identity_core": {"position": "dean", "domain": "administration"},
                "personality_prior": {"O": 0.55, "C": 0.70, "E": 0.58, "A": 0.52, "N": 0.35},
                "incentives": ["administrative efficiency", "interdisciplinary output"],
                "concerns": ["faculty politics", "enrollment impact"],
                "communication_style": {"tone": "diplomatic", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_2",
                "display_name": "Prof. Rivera",
                "role": "CS Department Head",
                "identity_core": {"position": "department chair", "domain": "computer science"},
                "personality_prior": {"O": 0.72, "C": 0.55, "E": 0.44, "A": 0.38, "N": 0.48},
                "incentives": ["research autonomy", "graduate program prestige"],
                "concerns": ["research dilution", "losing hiring authority"],
                "communication_style": {"tone": "direct", "brevity": "concise"},
            },
            {
                "actor_id": "actor_3",
                "display_name": "Prof. Okafor",
                "role": "Biology Department Head",
                "identity_core": {"position": "department chair", "domain": "biology"},
                "personality_prior": {"O": 0.40, "C": 0.78, "E": 0.50, "A": 0.60, "N": 0.42},
                "incentives": ["lab resources", "faculty stability"],
                "concerns": ["identity loss", "budget reallocation"],
                "communication_style": {"tone": "measured", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_4",
                "display_name": "Maya",
                "role": "Student Council Representative",
                "identity_core": {"position": "student rep", "domain": "undergrad"},
                "personality_prior": {"O": 0.65, "C": 0.42, "E": 0.71, "A": 0.58, "N": 0.55},
                "incentives": ["course availability", "transparent governance"],
                "concerns": ["reduced electives", "advising disruption"],
                "communication_style": {"tone": "earnest", "brevity": "moderate"},
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Present the merger proposal and initial reactions", "style": "neutral", "max_turns": 4, "cues": ["merger_rationale", "initial_concerns"]},
            {"name": "TENSION", "goal": "Surface conflicts about autonomy, resources, and identity", "style": "disagreement", "max_turns": 3, "cues": ["autonomy", "resource_allocation"]},
            {"name": "NEGOTIATION", "goal": "Explore compromise structures and governance models", "style": "consensus", "max_turns": 4, "cues": ["governance_model", "tradeoff"]},
            {"name": "CLOSING", "goal": "Identify agreements and remaining blockers", "style": "neutral", "max_turns": 2, "cues": ["summary", "next_steps"]},
        ],
        "world_events": [
            {
                "event_id": "evt_budget_cut",
                "title": "University budget reduction",
                "description": "The provost announces a 12% budget reduction for next fiscal year, increasing pressure to find efficiencies.",
                "trigger_phase": "TENSION",
            },
            {
                "event_id": "evt_industry_grant",
                "title": "Industry partnership opportunity",
                "description": "A biotech company offers a $2M grant for an interdisciplinary computational biology program, but only if the departments are unified.",
                "trigger_phase": "NEGOTIATION",
            },
        ],
    },
    {
        "simulation_id": "startup_equity_split",
        "title": "Startup Equity Split Negotiation",
        "objective": "Negotiate fair equity distribution among co-founders and first employee.",
        "brief": (
            "A pre-seed startup must finalize equity splits before their first investor meeting. "
            "The technical co-founder built the prototype, the business co-founder has customer traction, "
            "and the first employee joined early and wants recognition for the risk taken."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Alex",
                "role": "Technical Co-founder",
                "identity_core": {"position": "CTO", "domain": "engineering"},
                "personality_prior": {"O": 0.68, "C": 0.50, "E": 0.35, "A": 0.33, "N": 0.52},
                "incentives": ["IP recognition", "technical decision authority"],
                "concerns": ["dilution", "losing control of architecture"],
                "communication_style": {"tone": "analytical", "brevity": "concise"},
            },
            {
                "actor_id": "actor_2",
                "display_name": "Jordan",
                "role": "Business Co-founder",
                "identity_core": {"position": "CEO", "domain": "business development"},
                "personality_prior": {"O": 0.55, "C": 0.72, "E": 0.67, "A": 0.48, "N": 0.38},
                "incentives": ["operational control", "investor confidence"],
                "concerns": ["vesting schedule fairness", "co-founder alignment"],
                "communication_style": {"tone": "persuasive", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_3",
                "display_name": "Sam",
                "role": "First Employee",
                "identity_core": {"position": "lead engineer", "domain": "full-stack"},
                "personality_prior": {"O": 0.48, "C": 0.60, "E": 0.45, "A": 0.62, "N": 0.58},
                "incentives": ["fair equity share", "career growth path"],
                "concerns": ["power dynamics", "being sidelined in decisions"],
                "communication_style": {"tone": "cautious", "brevity": "moderate"},
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "State each person's contribution and expectations", "style": "neutral", "max_turns": 3, "cues": ["contribution", "expectations"]},
            {"name": "TENSION", "goal": "Surface disagreements about valuation of different contributions", "style": "disagreement", "max_turns": 3, "cues": ["valuation", "fairness"]},
            {"name": "NEGOTIATION", "goal": "Propose concrete equity splits and vesting terms", "style": "consensus", "max_turns": 3, "cues": ["equity_split", "vesting"]},
            {"name": "CLOSING", "goal": "Lock in terms or identify remaining blockers", "style": "neutral", "max_turns": 2, "cues": ["agreement", "commitment"]},
        ],
        "world_events": [
            {
                "event_id": "evt_investor_deadline",
                "title": "Investor meeting deadline",
                "description": "The lead investor requests a finalized cap table by end of week or they will pass.",
                "trigger_phase": "NEGOTIATION",
            },
        ],
    },
]


async def main():
    from experiment.run_experiment import create_clients
    gen_client, _ = create_clients()

    scripts = [SimulationScript.from_dict(s) for s in NOVEL_SCRIPTS]
    runner = SimulationBenchmarkRunner(gen_client=gen_client)

    output_dir = "simulation_engine/results_exp2_novel"
    results = await runner.run_suite(
        conditions=["engine_dialogue_only"],
        repetitions=2,
        scripts=scripts,
        checkpoint_dir=output_dir,
    )
    save_benchmark_outputs(results, output_dir)
    print(f"\nExperiment 2 complete. Results in {output_dir}/")
    print(f"Aggregate: {json.dumps(results['aggregate'], indent=2)}")


if __name__ == "__main__":
    asyncio.run(main())
