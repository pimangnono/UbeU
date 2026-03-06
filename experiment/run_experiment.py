"""
Experiment CLI Entry Point.

Usage:
    python -m experiment.run_experiment                        # Full (176 sessions)
    python -m experiment.run_experiment --pilot                # Pilot (4 sessions)
    python -m experiment.run_experiment --pilot-v5             # V5.1 pilot (8-12 sessions)
    python -m experiment.run_experiment --bcfc-pilot           # BCFC pilot (16 paired sessions)
    python -m experiment.run_experiment --bcfc-freeze-pilot    # BCFC v1.1 freeze pilot (6 sessions)
    python -m experiment.run_experiment --bcfc-midcheck        # BCFC v1.1 mid-check (20 sessions)
    python -m experiment.run_experiment --bcfc                 # BCFC v1.1 full (176 sessions)
    python -m experiment.run_experiment --analyze              # Analysis only
    python -m experiment.run_experiment --temporal             # Temporal analysis only
    python -m experiment.run_experiment --audit-overlap        # Overlap audit only
    python -m experiment.run_experiment --bcfc-v5-mini         # BCFC v5 mini (12 sessions)
    python -m experiment.run_experiment --bcfc-v5-langgraph-mini  # BCFC v5 LangGraph mini (12 sessions)
"""

import argparse
import asyncio
import logging
import sys
import random

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
    """Run the full 176-session experiment."""
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


async def run_pilot_v5(output_dir: str = "experiment/results_v5_pilot"):
    """
    Run a V5.1 pilot with fixed session matrix (8 main + optional 4 baselines).

    Profiles: assertive_leader, passive_avoider, anxious_perfectionist, withdrawn_critic
    Scenarios: resource_conflict, crisis_management
    Reps: 1
    Total main: 8 sessions
    """
    gen_client, eval_client = create_clients()

    from experiment.batch_runner import BatchRunner, SessionSpec

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
    )

    pilot_profiles = [
        "assertive_leader", "passive_avoider",
        "anxious_perfectionist", "withdrawn_critic",
    ]
    pilot_scenarios = ["resource_conflict", "crisis_management"]

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

    # Optional baseline_a sessions (2)
    for scenario_id in pilot_scenarios:
        key = f"baseline_a_none_{scenario_id}_r1"
        pilot_sessions.append(SessionSpec(
            session_key=key,
            condition="baseline_a",
            profile_id="none",
            scenario_id=scenario_id,
            rep=1,
        ))

    # Optional baseline_b sessions (2)
    for scenario_id in pilot_scenarios:
        key = f"baseline_b_assertive_leader_{scenario_id}_r1"
        pilot_sessions.append(SessionSpec(
            session_key=key,
            condition="baseline_b",
            profile_id="assertive_leader",
            scenario_id=scenario_id,
            rep=1,
        ))

    runner._build_session_list = lambda: pilot_sessions

    summary = await runner.run_all()
    return summary


async def run_bcfc_pilot(output_dir: str = "experiment/results_bcfc_pilot"):
    """
    Run a BCFC pilot: 4 profiles x 2 scenarios x 2 conditions (baseline + BCFC) = 16 sessions.

    Tests the full BCFC pipeline before committing to the full 128-session experiment.
    """
    gen_client, eval_client = create_clients()

    from experiment.batch_runner import BatchRunner, SessionSpec
    from experiment.profiles import EXPERIMENT_PROFILES

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
    )

    pilot_profiles = [
        "assertive_leader",       # High E, Low A — tests A constraint enforcement
        "anxious_perfectionist",  # High C, High N — tests C/N nudges
        "creative_rebel",         # High O, Low C — tests O/C constraints
        "withdrawn_critic",       # Low E, Low A, High N — tests E/N constraints
    ]
    pilot_scenarios = ["resource_conflict", "crisis_management"]

    sessions = []
    for profile_id in pilot_profiles:
        for scenario_id in pilot_scenarios:
            # Baseline session (no intervention)
            sessions.append(SessionSpec(
                session_key=f"baseline_{profile_id}_{scenario_id}_r1",
                condition="main",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="none",
            ))
            # BCFC session (with intervention)
            sessions.append(SessionSpec(
                session_key=f"bcfc_{profile_id}_{scenario_id}_r1",
                condition="main",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="bcfc",
            ))

    runner._build_session_list = lambda: sessions

    summary = await runner.run_all()
    return summary


def _build_bcfc_v11_sessions() -> list:
    """Build the full BCFC v1.1 session list (176 sessions)."""
    from experiment.batch_runner import SessionSpec
    from experiment.profiles import EXPERIMENT_PROFILES
    from config.group_scenarios import MAIN_SCENARIO_IDS
    from experiment.bcfc_config import DEFAULT_CONFIG

    # Main/high-pressure scenarios exclude the low-pressure manipulation.
    scenario_ids = MAIN_SCENARIO_IDS
    sessions = []

    # High-pressure main sessions
    for profile_id in EXPERIMENT_PROFILES:
        for scenario_id in scenario_ids:
            sessions.append(SessionSpec(
                session_key=f"baseline_{profile_id}_{scenario_id}_r1",
                condition="main",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="none",
            ))
            sessions.append(SessionSpec(
                session_key=f"bcfc_{profile_id}_{scenario_id}_r1",
                condition="main",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="bcfc",
            ))

    # Low-pressure main sessions (focused test)
    low_id = DEFAULT_CONFIG.low_pressure_scenario
    for profile_id in EXPERIMENT_PROFILES:
        sessions.append(SessionSpec(
            session_key=f"baseline_{profile_id}_{low_id}_r1",
            condition="main",
            profile_id=profile_id,
            scenario_id=low_id,
            rep=1,
            intervention="none",
        ))
        sessions.append(SessionSpec(
            session_key=f"bcfc_{profile_id}_{low_id}_r1",
            condition="main",
            profile_id=profile_id,
            scenario_id=low_id,
            rep=1,
            intervention="bcfc",
        ))

    # Baseline_a: no personality (shared)
    for scenario_id in scenario_ids:
        sessions.append(SessionSpec(
            session_key=f"baseline_a_none_{scenario_id}_r1",
            condition="baseline_a",
            profile_id="none",
            scenario_id=scenario_id,
            rep=1,
            intervention="none",
        ))

    # Baseline_b: shuffled vectors (paired)
    baseline_b_profiles = ["assertive_leader", "neutral_observer"]
    for profile_id in baseline_b_profiles:
        for scenario_id in scenario_ids:
            sessions.append(SessionSpec(
                session_key=f"baseline_b_baseline_{profile_id}_{scenario_id}_r1",
                condition="baseline_b",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="none",
            ))
            sessions.append(SessionSpec(
                session_key=f"baseline_b_bcfc_{profile_id}_{scenario_id}_r1",
                condition="baseline_b",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="bcfc",
            ))

    # Compute-control subset: BoN-random
    bon_scenario = DEFAULT_CONFIG.bon_random_scenario
    for profile_id in EXPERIMENT_PROFILES:
        for rep in range(1, DEFAULT_CONFIG.bon_random_reps + 1):
            sessions.append(SessionSpec(
                session_key=f"bon_random_{profile_id}_{bon_scenario}_r{rep}",
                condition="main",
                profile_id=profile_id,
                scenario_id=bon_scenario,
                rep=rep,
                intervention="bon_random",
            ))

    return sessions


async def run_bcfc_freeze_pilot(output_dir: str = "experiment/results_bcfc_freeze_pilot"):
    """
    Stage 1: Freeze pilot (6 sessions) to lock parameters.
    3 profiles x 1 scenario x 1 rep x 2 conditions.
    """
    gen_client, eval_client = create_clients()
    from experiment.batch_runner import BatchRunner, SessionSpec
    from experiment.bcfc_config import DEFAULT_CONFIG

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
        main_reps=1,
        baseline_a_reps=0,
        baseline_b_reps=0,
        shuffle=False,
    )

    sessions = []
    for profile_id in DEFAULT_CONFIG.freeze_pilot_profiles:
        scenario_id = DEFAULT_CONFIG.freeze_pilot_scenario
        sessions.append(SessionSpec(
            session_key=f"baseline_{profile_id}_{scenario_id}_r1",
            condition="main",
            profile_id=profile_id,
            scenario_id=scenario_id,
            rep=1,
            intervention="none",
        ))
        sessions.append(SessionSpec(
            session_key=f"bcfc_{profile_id}_{scenario_id}_r1",
            condition="main",
            profile_id=profile_id,
            scenario_id=scenario_id,
            rep=1,
            intervention="bcfc",
        ))

    runner._build_session_list = lambda: sessions
    return await runner.run_all()


async def run_bcfc_midcheck(output_dir: str = "experiment/results_bcfc_midcheck"):
    """
    Stage 2: Mid-check run (first N sessions from full matrix).
    """
    gen_client, eval_client = create_clients()
    from experiment.batch_runner import BatchRunner
    from experiment.bcfc_config import DEFAULT_CONFIG

    sessions = _build_bcfc_v11_sessions()
    rng = random.Random(DEFAULT_CONFIG.mid_check_seed)
    rng.shuffle(sessions)
    sessions = sessions[:DEFAULT_CONFIG.mid_check_size]

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
        main_reps=1,
        baseline_a_reps=0,
        baseline_b_reps=0,
        shuffle=False,
    )
    runner._build_session_list = lambda: sessions
    return await runner.run_all()


async def run_bcfc_experiment(output_dir: str = "experiment/results_bcfc"):
    """
    Stage 3: Full BCFC v1.1 run (176 sessions).
    """
    gen_client, eval_client = create_clients()
    from experiment.batch_runner import BatchRunner

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
        main_reps=1,
        baseline_a_reps=1,
        baseline_b_reps=1,
    )

    sessions = _build_bcfc_v11_sessions()
    runner._build_session_list = lambda: sessions

    print(f"Total sessions: {len(sessions)}")
    print(f"  BCFC main: {sum(1 for s in sessions if s.intervention == 'bcfc' and s.condition == 'main')}")
    print(f"  Baseline main: {sum(1 for s in sessions if s.intervention == 'none' and s.condition == 'main')}")
    print(f"  Baseline_a: {sum(1 for s in sessions if s.condition == 'baseline_a')}")
    print(f"  Baseline_b: {sum(1 for s in sessions if s.condition == 'baseline_b')}")
    print(f"  BoN-random: {sum(1 for s in sessions if s.intervention == 'bon_random')}")

    return await runner.run_all()


async def run_bcfc_v3_mini(output_dir: str = "experiment/results_bcfc_v3_mini"):
    """
    BCFC v3 mini experiment (27 sessions):
    3 profiles x 3 scenarios x 3 conditions (baseline, bcfc_v2, bcfc_v3).
    """
    gen_client, eval_client = create_clients()
    from experiment.batch_runner import BatchRunner, SessionSpec

    profiles = [
        "anxious_perfectionist",
        "creative_rebel",
        "neutral_observer",
    ]
    scenarios = [
        "crisis_management",
        "strategy_pivot",
        "release_recovery",
    ]

    sessions: list[SessionSpec] = []
    for profile_id in profiles:
        for scenario_id in scenarios:
            sessions.append(SessionSpec(
                session_key=f"baseline_v3_{profile_id}_{scenario_id}_r1",
                condition="mini_v3",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="none",
            ))
            sessions.append(SessionSpec(
                session_key=f"bcfc_v2_{profile_id}_{scenario_id}_r1",
                condition="mini_v3",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="bcfc",
            ))
            sessions.append(SessionSpec(
                session_key=f"bcfc_v3_{profile_id}_{scenario_id}_r1",
                condition="mini_v3",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="bcfc_v3",
            ))

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
        main_reps=1,
        baseline_a_reps=0,
        baseline_b_reps=0,
        shuffle=False,
    )
    runner._build_session_list = lambda: sessions
    return await runner.run_all()


async def run_bcfc_v4_mini(output_dir: str = "experiment/results_bcfc_v4_mini"):
    """
    BCFC v4 mini experiment (9 sessions):
    3 profiles x 3 scenarios x 1 condition (bcfc_v4).
    """
    gen_client, eval_client = create_clients()
    from experiment.batch_runner import BatchRunner, SessionSpec

    profiles = [
        "anxious_perfectionist",
        "creative_rebel",
        "neutral_observer",
    ]
    scenarios = [
        "crisis_management",
        "strategy_pivot",
        "release_recovery",
    ]

    sessions: list[SessionSpec] = []
    for profile_id in profiles:
        for scenario_id in scenarios:
            sessions.append(SessionSpec(
                session_key=f"bcfc_v4_{profile_id}_{scenario_id}_r1",
                condition="mini_v4",
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention="bcfc_v4",
            ))

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
        main_reps=1,
        baseline_a_reps=0,
        baseline_b_reps=0,
        shuffle=False,
    )
    runner._build_session_list = lambda: sessions
    return await runner.run_all()


async def run_bcfc_v5_mini(output_dir: str = "experiment/results_bcfc_v5_mini"):
    """
    BCFC v5 mini experiment (12 sessions):
    3 profiles x 4 scenarios x 1 condition (bcfc_v5).

    Scenario mix:
    - Probe set: strategy_pivot, release_recovery
    - Robustness set sample: crisis_management, resource_conflict
    """
    gen_client, eval_client = create_clients()
    from experiment.batch_runner import BatchRunner, SessionSpec
    from experiment.bcfc_config import DEFAULT_CONFIG

    sessions = _build_bcfc_v5_mini_sessions(
        condition="mini_v5",
        intervention="bcfc_v5",
        session_prefix="bcfc_v5",
    )

    runner = BatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
        main_reps=1,
        baseline_a_reps=0,
        baseline_b_reps=0,
        shuffle=False,
    )
    runner._build_session_list = lambda: sessions
    return await runner.run_all()


def _build_bcfc_v5_mini_sessions(
    condition: str,
    intervention: str,
    session_prefix: str,
) -> list:
    """Build the shared v5 mini profile/scenario matrix for one intervention."""
    from experiment.batch_runner import SessionSpec
    from experiment.bcfc_config import DEFAULT_CONFIG

    profiles = [
        "anxious_perfectionist",
        "creative_rebel",
        "neutral_observer",
    ]

    probe = list(DEFAULT_CONFIG.probe_scenario_ids)
    robust = [s for s in DEFAULT_CONFIG.robustness_scenario_ids if s in {"crisis_management", "resource_conflict"}]
    scenarios = probe + robust

    sessions: list[SessionSpec] = []
    for profile_id in profiles:
        for scenario_id in scenarios:
            sessions.append(SessionSpec(
                session_key=f"{session_prefix}_{profile_id}_{scenario_id}_r1",
                condition=condition,
                profile_id=profile_id,
                scenario_id=scenario_id,
                rep=1,
                intervention=intervention,
            ))
    return sessions


async def run_bcfc_v5_langgraph_mini(
    output_dir: str = "experiment/results_bcfc_v5_langgraph_mini",
):
    """
    BCFC v5 LangGraph mini experiment (12 sessions):
    same profile/scenario matrix as v5 mini, but routed through the LangGraph runtime.
    """
    gen_client, eval_client = create_clients()
    from experiment.langgraph_v5 import LangGraphBatchRunner

    sessions = _build_bcfc_v5_mini_sessions(
        condition="mini_v5_langgraph",
        intervention="bcfc_v5_langgraph",
        session_prefix="bcfc_v5_langgraph",
    )

    runner = LangGraphBatchRunner(
        gen_client=gen_client,
        eval_client=eval_client,
        output_dir=output_dir,
        main_reps=1,
        baseline_a_reps=0,
        baseline_b_reps=0,
        shuffle=False,
    )
    runner._build_session_list = lambda: sessions
    return await runner.run_all()


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


def run_overlap_audit():
    """Run the overlap audit and print results."""
    from experiment.validation.overlap_audit import run_full_audit
    result = run_full_audit()
    sys.exit(0 if result["pass"] else 1)


def run_contract_invariants():
    """Validate contract range invariants."""
    from experiment.validation.contract_invariants import validate_contract_invariants
    result = validate_contract_invariants()
    if result["passed"]:
        print("Contract invariants: PASS")
        return
    print("Contract invariants: FAIL")
    for err in result["errors"][:20]:
        print(err)
    if len(result["errors"]) > 20:
        print(f"... {len(result['errors']) - 20} more")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Behavioral Fidelity Experiment (V5.1 + BCFC)")
    parser.add_argument("--pilot", action="store_true", help="Run pilot (4 sessions)")
    parser.add_argument("--pilot-v5", action="store_true", help="Run V5.1 pilot (12 sessions)")
    parser.add_argument("--bcfc-pilot", action="store_true", help="Run BCFC pilot (16 paired sessions)")
    parser.add_argument("--bcfc-freeze-pilot", action="store_true", help="Run BCFC v1.1 freeze pilot (6 sessions)")
    parser.add_argument("--bcfc-midcheck", action="store_true", help="Run BCFC v1.1 mid-check (20 sessions)")
    parser.add_argument("--bcfc", action="store_true", help="Run full BCFC v1.1 experiment (176 sessions)")
    parser.add_argument("--bcfc-v3-mini", action="store_true", help="Run BCFC v3 mini experiment (27 sessions)")
    parser.add_argument("--bcfc-v4-mini", action="store_true", help="Run BCFC v4 mini experiment (9 sessions)")
    parser.add_argument("--bcfc-v5-mini", action="store_true", help="Run BCFC v5 mini experiment (12 sessions)")
    parser.add_argument("--bcfc-v5-langgraph-mini", action="store_true", help="Run BCFC v5 LangGraph mini experiment (12 sessions)")
    parser.add_argument("--analyze", action="store_true", help="Run analysis only")
    parser.add_argument("--temporal", action="store_true", help="Run temporal analysis only")
    parser.add_argument("--audit-overlap", action="store_true", help="Run overlap audit only")
    parser.add_argument("--validate-contracts", action="store_true", help="Validate contract range invariants")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory")

    args = parser.parse_args()

    if args.audit_overlap:
        print("Running overlap audit...")
        run_overlap_audit()
        return

    if args.validate_contracts:
        print("Validating contract invariants...")
        run_contract_invariants()
        return

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

    if args.bcfc_pilot:
        output_dir = args.output_dir or "experiment/results_bcfc_pilot"
        print("Running BCFC PILOT experiment (16 paired sessions)...")
        summary = asyncio.run(run_bcfc_pilot(output_dir))
    elif args.bcfc_freeze_pilot:
        output_dir = args.output_dir or "experiment/results_bcfc_freeze_pilot"
        print("Running BCFC v1.1 FREEZE PILOT (6 sessions)...")
        summary = asyncio.run(run_bcfc_freeze_pilot(output_dir))
    elif args.bcfc_midcheck:
        output_dir = args.output_dir or "experiment/results_bcfc_midcheck"
        print("Running BCFC v1.1 MID-CHECK (20 sessions)...")
        summary = asyncio.run(run_bcfc_midcheck(output_dir))
    elif args.bcfc:
        output_dir = args.output_dir or "experiment/results_bcfc"
        print("Running FULL BCFC v1.1 experiment (176 sessions)...")
        summary = asyncio.run(run_bcfc_experiment(output_dir))
    elif args.bcfc_v3_mini:
        output_dir = args.output_dir or "experiment/results_bcfc_v3_mini"
        print("Running BCFC v3 MINI experiment (27 sessions)...")
        summary = asyncio.run(run_bcfc_v3_mini(output_dir))
    elif args.bcfc_v4_mini:
        output_dir = args.output_dir or "experiment/results_bcfc_v4_mini"
        print("Running BCFC v4 MINI experiment (9 sessions)...")
        summary = asyncio.run(run_bcfc_v4_mini(output_dir))
    elif args.bcfc_v5_mini:
        output_dir = args.output_dir or "experiment/results_bcfc_v5_mini"
        print("Running BCFC v5 MINI experiment (12 sessions)...")
        summary = asyncio.run(run_bcfc_v5_mini(output_dir))
    elif args.bcfc_v5_langgraph_mini:
        output_dir = args.output_dir or "experiment/results_bcfc_v5_langgraph_mini"
        print("Running BCFC v5 LangGraph MINI experiment (12 sessions)...")
        summary = asyncio.run(run_bcfc_v5_langgraph_mini(output_dir))
    elif args.pilot_v5:
        output_dir = args.output_dir or "experiment/results_v5_pilot"
        print("Running V5.1 PILOT experiment (12 sessions)...")
        summary = asyncio.run(run_pilot_v5(output_dir))
    elif args.pilot:
        output_dir = args.output_dir or "experiment/results"
        print("Running PILOT experiment (4 sessions)...")
        summary = asyncio.run(run_pilot_experiment(output_dir))
    else:
        output_dir = args.output_dir or "experiment/results"
        print("Running FULL experiment (176 sessions)...")
        summary = asyncio.run(run_full_experiment(output_dir))

    print(f"\nFinal summary: {summary}")


if __name__ == "__main__":
    main()
