"""Final Benchmark: Engine vs Naive Baseline (480 runs).

20 real-world historical scenarios x 3 actor counts (3/5/10) x 2 conditions x 4 reps = 480 runs.

Usage:
    # Full run (480 runs with checkpoint resume)
    python3 -m simulation_engine.run_final_benchmark

    # Smoke test (2 briefs x 1 actor count x 2 conditions x 1 rep = 4 runs)
    python3 -m simulation_engine.run_final_benchmark --smoke

    # Script generation only (no benchmark execution)
    python3 -m simulation_engine.run_final_benchmark --generate-only

    # Skip generation, run benchmark on existing scripts
    python3 -m simulation_engine.run_final_benchmark --skip-generation
"""
import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

from simulation_engine.benchmark import SimulationBenchmarkRunner
from simulation_engine.builder import enrich_generated_script_payload, inspect_script, validate_enriched_script
from simulation_engine.final_benchmark_briefs import (
    ACTOR_COUNTS,
    CONDITIONS,
    FINAL_BENCHMARK_BRIEFS,
    REPETITIONS,
    BenchmarkBrief,
)
from simulation_engine.reporting import atomic_write_json, save_benchmark_outputs
from simulation_engine.run_exp3_userinput import generate_script_from_brief
from simulation_engine.script import SimulationScript

OUTPUT_DIR = "simulation_engine/results_final_benchmark"


# ── Phase A: Script Generation ──────────────────────────────────────────────


def scale_max_turns(script_dict: dict, actor_count: int) -> dict:
    """Scale phase max_turns based on actor count.

    More actors need more turns for everyone to speak. CLOSING gets a
    gentler increase to avoid convergence-magnet bloat.
    """
    for phase in script_dict["phases"]:
        base = phase["max_turns"]
        if phase["name"] == "CLOSING":
            phase["max_turns"] = base + max(0, int(0.3 * (actor_count - 3)))
        else:
            phase["max_turns"] = base + max(0, int(0.5 * (actor_count - 3)))
    return script_dict


async def generate_all_scripts(
    gen_client,
    briefs: list[BenchmarkBrief],
    actor_counts: list[int],
    output_dir: Path,
) -> tuple[list[SimulationScript], list[dict]]:
    """Phase A: Generate scripts for all brief x actor_count combinations."""
    scripts_dir = output_dir / "generated_scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)

    scripts: list[SimulationScript] = []
    generation_log: list[dict] = []
    total = len(briefs) * len(actor_counts)
    completed = 0

    for brief in briefs:
        for actor_count in actor_counts:
            completed += 1
            variant_id = f"{brief.brief_id}_{actor_count}actor"
            script_path = scripts_dir / f"{variant_id}.json"

            # Skip if already generated
            if script_path.exists():
                try:
                    data = json.loads(script_path.read_text())
                    script = SimulationScript.from_dict(data)
                    scripts.append(script)
                    generation_log.append({
                        "brief_id": brief.brief_id,
                        "variant_id": variant_id,
                        "actor_count": actor_count,
                        "status": "cached",
                        "actors": len(script.stakeholders),
                        "phases": len(script.phases),
                        "simulation_mode": script.simulation_mode,
                    })
                    print(
                        f"[{completed}/{total}] {variant_id}: cached "
                        f"({len(script.stakeholders)} actors)",
                        flush=True,
                    )
                    continue
                except Exception:
                    pass  # Regenerate on corrupt cache

            print(
                f"[{completed}/{total}] Generating {variant_id}...",
                flush=True,
            )
            try:
                script = await generate_script_from_brief(
                    gen_client,
                    brief=brief.brief_text,
                    brief_id=variant_id,
                    actor_count=actor_count,
                    simulation_mode=brief.simulation_mode,
                    max_retries=3,
                )

                # Apply max_turns scaling
                script_dict = script.to_dict()
                script_dict = scale_max_turns(script_dict, actor_count)
                script = SimulationScript.from_dict(script_dict)

                # Save generated script
                with open(script_path, "w") as f:
                    json.dump(script.to_dict(), f, indent=2)

                # Log structural inspection
                inspection = inspect_script(script.to_dict())

                scripts.append(script)
                generation_log.append({
                    "brief_id": brief.brief_id,
                    "variant_id": variant_id,
                    "actor_count": actor_count,
                    "status": "success",
                    "actors": len(script.stakeholders),
                    "phases": len(script.phases),
                    "simulation_mode": script.simulation_mode,
                    "scenario_family": script.scenario_family,
                    "structural_profile": inspection.get("structural_profile", {}),
                    "pair_conflicts": len(inspection.get("pair_conflicts", [])),
                })
                print(
                    f"  Generated: {len(script.stakeholders)} actors, "
                    f"{len(script.phases)} phases, mode={script.simulation_mode}",
                    flush=True,
                )

            except Exception as e:
                error_text = str(e)
                if "Expecting value" in error_text:
                    failure_type = "invalid_json"
                elif "must contain" in error_text or "requires" in error_text:
                    failure_type = "schema_invalid"
                elif "Expected" in error_text and "stakeholders" in error_text:
                    failure_type = "actor_count_mismatch"
                else:
                    failure_type = "runtime_error"
                generation_log.append({
                    "brief_id": brief.brief_id,
                    "variant_id": variant_id,
                    "actor_count": actor_count,
                    "status": "error",
                    "failure_type": failure_type,
                    "error": error_text,
                })
                print(f"  FAILED ({failure_type}): {e}", flush=True)

    # Save generation log
    with open(output_dir / "generation_log.json", "w") as f:
        json.dump(generation_log, f, indent=2)

    return scripts, generation_log


def load_existing_scripts(output_dir: Path, inject_structural_profile: bool = True) -> list[SimulationScript]:
    """Load previously generated scripts from disk.

    If inject_structural_profile=True, infer and inject structural_profile
    into script metadata for scripts that don't have it (needed for engine_structural).
    """
    scripts_dir = output_dir / "generated_scripts"
    if not scripts_dir.exists():
        return []

    scripts: list[SimulationScript] = []
    injected_count = 0
    for path in sorted(scripts_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text())

            # Inject structural_profile if missing
            if inject_structural_profile:
                metadata = data.get("metadata", {})
                if "structural_profile" not in metadata:
                    from dataclasses import asdict
                    from simulation_engine.builder import infer_structural_profile
                    stakeholders = data.get("stakeholders", [])
                    phases = data.get("phases", [])
                    profile = infer_structural_profile(stakeholders, phases)
                    metadata["structural_profile"] = asdict(profile)
                    data["metadata"] = metadata
                    injected_count += 1

            scripts.append(SimulationScript.from_dict(data))
        except Exception as e:
            print(f"  Warning: skipping {path.name}: {e}", flush=True)

    if injected_count > 0:
        print(f"  Injected structural_profile into {injected_count} scripts", flush=True)

    return scripts


# ── Phase B: Benchmark Execution ────────────────────────────────────────────


async def run_benchmark(
    gen_client,
    scripts: list[SimulationScript],
    conditions: list[str],
    repetitions: int,
    output_dir: Path,
) -> dict:
    """Phase B: Run all benchmark conditions with checkpoint resume."""
    print(
        f"\n[benchmark] Starting: {len(scripts)} scripts x "
        f"{len(conditions)} conditions x {repetitions} reps = "
        f"{len(scripts) * len(conditions) * repetitions} total runs",
        flush=True,
    )

    runner = SimulationBenchmarkRunner(gen_client=gen_client)
    results = await runner.run_suite(
        conditions=conditions,
        repetitions=repetitions,
        scripts=scripts,
        checkpoint_dir=str(output_dir),
    )

    return results


# ── Phase C: Output & Analysis ──────────────────────────────────────────────


def build_scenario_outcome_summary(results: dict) -> dict:
    """Build per-scenario outcome summary with actor-count breakdowns."""
    runs = results.get("runs", [])
    by_scenario: dict[str, list[dict]] = {}
    for run in runs:
        sim_id = run.get("simulation_id", "")
        by_scenario.setdefault(sim_id, []).append(run)

    summary: dict[str, dict] = {}
    for sim_id, sim_runs in sorted(by_scenario.items()):
        # Parse actor count from simulation_id (e.g. "california_ab5_3actor")
        parts = sim_id.rsplit("_", 1)
        actor_label = parts[-1] if len(parts) > 1 else "unknown"
        base_scenario = parts[0] if len(parts) > 1 else sim_id

        condition_metrics: dict[str, dict] = {}
        for run in sim_runs:
            condition = run.get("condition", "unknown")
            metrics = run.get("metrics", {})
            cond_data = condition_metrics.setdefault(condition, {
                "runs": 0,
                "drift_values": [],
                "contradiction_values": [],
                "convergence_values": [],
                "diversity_values": [],
                "envelope_values": [],
            })
            cond_data["runs"] += 1
            cond_data["drift_values"].append(metrics.get("persona_drift_mae", 0.0))
            cond_data["contradiction_values"].append(metrics.get("commitment_contradiction_rate", 0.0))
            cond_data["convergence_values"].append(metrics.get("action_family_convergence_rate", 0.0))
            cond_data["diversity_values"].append(metrics.get("role_action_diversity_score", 0.0))
            cond_data["envelope_values"].append(metrics.get("envelope_violations", 0.0))

        for condition, data in condition_metrics.items():
            from statistics import mean
            for key in ("drift_values", "contradiction_values", "convergence_values",
                        "diversity_values", "envelope_values"):
                values = data.pop(key)
                metric_name = key.replace("_values", "_mean")
                data[metric_name] = round(mean(values), 4) if values else 0.0

        summary[sim_id] = {
            "base_scenario": base_scenario,
            "actor_count_label": actor_label,
            "total_runs": len(sim_runs),
            "conditions": condition_metrics,
        }

    return summary


def save_final_outputs(results: dict, output_dir: Path) -> None:
    """Phase C: Save all benchmark outputs plus scenario summaries + outcome analysis."""
    save_benchmark_outputs(results, str(output_dir))

    # Additional: per-scenario outcome summary
    scenario_summary = build_scenario_outcome_summary(results)
    atomic_write_json(output_dir / "scenario_outcome_summary.json", scenario_summary, indent=2, default=str)

    # Actor-count comparison table
    actor_count_comparison = build_actor_count_comparison(results)
    atomic_write_json(output_dir / "actor_count_comparison.json", actor_count_comparison, indent=2, default=str)

    # Auto-run outcome analysis if ground truth data exists
    try:
        from simulation_engine.outcome_analysis import (
            run_outcome_analysis,
            save_outcome_report,
            save_results_json,
        )
        print("\n[Phase C] Running outcome analysis...", flush=True)
        outcome_results = run_outcome_analysis(output_dir)
        save_outcome_report(outcome_results, output_dir / "outcome_analysis_report.md")
        save_results_json(outcome_results, output_dir / "outcome_analysis.json")
        print("  - outcome_analysis_report.md", flush=True)
        print("  - outcome_analysis.json", flush=True)
    except Exception as e:
        print(f"  Warning: outcome analysis failed: {e}", flush=True)

    # Game theory post-hoc analysis
    try:
        from simulation_engine.game_theory_analysis import (
            run_game_theory_analysis,
            save_game_theory_report,
            save_game_theory_json,
        )
        print("\n[Phase C] Running game theory analysis...", flush=True)
        gt_results, gt_classifications = run_game_theory_analysis(output_dir)
        save_game_theory_report(gt_results, output_dir / "game_theory_report.md", gt_classifications)
        save_game_theory_json(gt_results, output_dir / "game_theory_analysis.json")
        print("  - game_theory_report.md", flush=True)
        print("  - game_theory_analysis.json", flush=True)
    except Exception as e:
        print(f"  Warning: game theory analysis failed: {e}", flush=True)

    print(f"\n[output] All results saved to {output_dir}/", flush=True)
    print(f"  - benchmark_report.md", flush=True)
    print(f"  - benchmark_aggregate.json", flush=True)
    print(f"  - scenario_outcome_summary.json", flush=True)
    print(f"  - actor_count_comparison.json", flush=True)


def build_actor_count_comparison(results: dict) -> dict:
    """Build engine vs naive comparison grouped by actor count."""
    from statistics import mean, pstdev

    runs = results.get("runs", [])

    # Group by (actor_count, condition)
    grouped: dict[tuple[str, str], list[dict]] = {}
    for run in runs:
        sim_id = run.get("simulation_id", "")
        condition = run.get("condition", "unknown")
        parts = sim_id.rsplit("_", 1)
        actor_label = parts[-1] if len(parts) > 1 else "unknown"
        key = (actor_label, condition)
        grouped.setdefault(key, []).append(run)

    comparison: dict[str, dict] = {}
    for (actor_label, condition), group_runs in sorted(grouped.items()):
        key = f"{actor_label}:{condition}"
        metrics_lists: dict[str, list[float]] = {
            "persona_drift_mae": [],
            "commitment_contradiction_rate": [],
            "action_family_convergence_rate": [],
            "role_action_diversity_score": [],
            "envelope_violations": [],
            "fallback_utterance_rate": [],
        }
        for run in group_runs:
            metrics = run.get("metrics", {})
            for metric_key in metrics_lists:
                metrics_lists[metric_key].append(float(metrics.get(metric_key, 0.0)))

        summary: dict[str, float] = {}
        for metric_key, values in metrics_lists.items():
            if values:
                summary[f"{metric_key}_mean"] = round(mean(values), 4)
                summary[f"{metric_key}_std"] = round(pstdev(values), 4) if len(values) > 1 else 0.0
            else:
                summary[f"{metric_key}_mean"] = 0.0
                summary[f"{metric_key}_std"] = 0.0

        comparison[key] = {
            "actor_count": actor_label,
            "condition": condition,
            "num_runs": len(group_runs),
            **summary,
        }

    return comparison


# ── Main ─────────────────────────────────────────────────────────────────────


async def main():
    parser = argparse.ArgumentParser(description="Final Benchmark: Engine vs Naive (480 runs)")
    parser.add_argument("--smoke", action="store_true", help="Smoke test: 4 runs only")
    parser.add_argument("--generate-only", action="store_true", help="Generate scripts only, no benchmark")
    parser.add_argument("--skip-generation", action="store_true", help="Skip generation, use existing scripts")
    parser.add_argument("--scripts-dir", type=str, default=None, help="Source scripts directory (default: <output-dir>/generated_scripts)")
    parser.add_argument("--output-dir", type=str, default=OUTPUT_DIR, help="Output directory")
    parser.add_argument("--repetitions", type=int, default=None, help="Override repetition count (default: from config)")
    args = parser.parse_args()

    from experiment.run_experiment import create_clients
    gen_client, _ = create_clients()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Determine briefs and params based on mode
    if args.smoke:
        briefs = FINAL_BENCHMARK_BRIEFS[:2]
        actor_counts = [3]
        conditions = list(CONDITIONS)
        repetitions = 1
        print(
            f"[smoke] Running smoke test: {len(briefs)} briefs x "
            f"{len(actor_counts)} actor counts x {len(conditions)} conditions x "
            f"{repetitions} reps = {len(briefs) * len(actor_counts) * len(conditions) * repetitions} runs",
            flush=True,
        )
    else:
        briefs = list(FINAL_BENCHMARK_BRIEFS)
        actor_counts = list(ACTOR_COUNTS)
        conditions = list(CONDITIONS)
        repetitions = args.repetitions if args.repetitions is not None else REPETITIONS

    # Phase A: Script Generation
    if args.skip_generation:
        scripts_source = Path(args.scripts_dir) if args.scripts_dir else output_dir
        print(f"[Phase A] Skipping generation, loading existing scripts from {scripts_source}...", flush=True)
        scripts = load_existing_scripts(scripts_source)
        if not scripts:
            print(f"ERROR: No existing scripts found in {scripts_source}/generated_scripts/. "
                  "Run without --skip-generation first, or use --scripts-dir.", flush=True)
            sys.exit(1)
        print(f"  Loaded {len(scripts)} scripts", flush=True)
    else:
        print(f"\n{'='*60}", flush=True)
        print(f"[Phase A] Script Generation", flush=True)
        print(f"  Briefs: {len(briefs)}, Actor counts: {actor_counts}", flush=True)
        print(f"  Target scripts: {len(briefs) * len(actor_counts)}", flush=True)
        print(f"{'='*60}\n", flush=True)

        scripts, generation_log = await generate_all_scripts(
            gen_client, briefs, actor_counts, output_dir,
        )

        success_count = sum(1 for entry in generation_log if entry["status"] in ("success", "cached"))
        error_count = sum(1 for entry in generation_log if entry["status"] == "error")
        print(
            f"\n[Phase A] Complete: {success_count} scripts generated, "
            f"{error_count} failures",
            flush=True,
        )

        if not scripts:
            print("ERROR: No scripts generated successfully. Aborting.", flush=True)
            sys.exit(1)

    if args.generate_only:
        print(f"\n[generate-only] Scripts saved to {output_dir}/generated_scripts/", flush=True)
        return

    # Phase B: Benchmark Execution
    print(f"\n{'='*60}", flush=True)
    print(f"[Phase B] Benchmark Execution", flush=True)
    print(f"  Scripts: {len(scripts)}", flush=True)
    print(f"  Conditions: {conditions}", flush=True)
    print(f"  Repetitions: {repetitions}", flush=True)
    print(f"  Total runs: {len(scripts) * len(conditions) * repetitions}", flush=True)
    print(f"{'='*60}\n", flush=True)

    results = await run_benchmark(
        gen_client, scripts, conditions, repetitions, output_dir,
    )

    # Phase C: Output
    print(f"\n{'='*60}", flush=True)
    print(f"[Phase C] Output & Analysis", flush=True)
    print(f"{'='*60}\n", flush=True)

    save_final_outputs(results, output_dir)

    # Print summary
    aggregate = results.get("aggregate", {})
    print("\n" + "="*60, flush=True)
    print("FINAL BENCHMARK SUMMARY", flush=True)
    print("="*60, flush=True)
    for condition, summary in sorted(aggregate.items()):
        print(
            f"\n  {condition} (n={summary.get('num_runs', 0)}):",
            flush=True,
        )
        print(f"    drift={summary.get('persona_drift_mae_mean', 0.0):.4f}", flush=True)
        print(f"    contradiction={summary.get('commitment_contradiction_mean', 0.0):.4f}", flush=True)
        print(f"    convergence={summary.get('action_family_convergence_rate_mean', 0.0):.4f}", flush=True)
        print(f"    diversity={summary.get('role_action_diversity_score_mean', 0.0):.4f}", flush=True)
        print(f"    envelope={summary.get('envelope_violations_mean', 0.0):.1f}", flush=True)
        print(f"    fallback={summary.get('fallback_utterance_rate_mean', 0.0):.4f}", flush=True)

    # Engine vs Naive delta
    engine_data = aggregate.get("engine_dialogue_only", {})
    naive_data = aggregate.get("naive", {})
    if engine_data and naive_data:
        print("\n  ENGINE vs NAIVE DELTA:", flush=True)
        for metric in ("persona_drift_mae_mean", "commitment_contradiction_mean",
                        "action_family_convergence_rate_mean", "role_action_diversity_score_mean",
                        "envelope_violations_mean", "fallback_utterance_rate_mean"):
            delta = round(engine_data.get(metric, 0.0) - naive_data.get(metric, 0.0), 4)
            label = metric.replace("_mean", "").replace("_", " ")
            print(f"    {label}: {delta:+.4f}", flush=True)

    print(f"\nResults: {output_dir}/", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
