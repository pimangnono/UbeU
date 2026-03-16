"""Structural Dynamics Benchmark: engine_structural vs existing baseline.

Reuses the 60 generated scripts from the GPT-4o-mini final benchmark,
running only the new engine_structural condition for direct comparison.

60 scripts x 1 condition (engine_structural) x 2 reps = 120 runs.

Usage:
    python3 -m simulation_engine.run_structural_benchmark
"""
import asyncio
import json
import sys
from pathlib import Path

from simulation_engine.benchmark import SimulationBenchmarkRunner
from simulation_engine.builder import inspect_script, print_inspection
from simulation_engine.reporting import atomic_write_json, save_benchmark_outputs
from simulation_engine.script import SimulationScript

SOURCE_SCRIPTS_DIR = Path("simulation_engine/results_final_benchmark_gpt4o_mini/generated_scripts")
OUTPUT_DIR = Path("simulation_engine/results_structural_benchmark_gpt4o_mini")

CONDITIONS = ["engine_structural"]
REPETITIONS = 2


def load_and_enrich_scripts() -> list[SimulationScript]:
    """Load existing scripts and inject structural_profile into metadata."""
    from simulation_engine.builder import infer_structural_profile
    from dataclasses import asdict

    scripts: list[SimulationScript] = []
    for path in sorted(SOURCE_SCRIPTS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text())

            # Inject structural_profile if missing (existing scripts don't have it)
            metadata = data.get("metadata", {})
            if "structural_profile" not in metadata:
                stakeholders = data.get("stakeholders", [])
                phases = data.get("phases", [])
                profile = infer_structural_profile(stakeholders, phases)
                metadata["structural_profile"] = asdict(profile)
                data["metadata"] = metadata

            script = SimulationScript.from_dict(data)
            scripts.append(script)
        except Exception as e:
            print(f"  Warning: skipping {path.name}: {e}", flush=True)

    return scripts


async def main():
    from experiment.run_experiment import create_clients
    gen_client, _ = create_clients()

    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    # Phase A: Load and enrich existing scripts
    print(f"\n{'='*60}", flush=True)
    print(f"[Phase A] Loading scripts from {SOURCE_SCRIPTS_DIR}", flush=True)
    print(f"{'='*60}\n", flush=True)

    scripts = load_and_enrich_scripts()
    if not scripts:
        print("ERROR: No scripts found. Run the final benchmark first.", flush=True)
        sys.exit(1)

    # Log structural inspections
    inspections = []
    polarity_counts = {"adversarial": 0, "fragmented": 0, "collaborative": 0}
    for script in scripts:
        inspection = inspect_script(script.to_dict())
        inspections.append(inspection)
        polarity = inspection.get("structural_profile", {}).get("polarity", "unknown")
        polarity_counts[polarity] = polarity_counts.get(polarity, 0) + 1

    atomic_write_json(output_dir / "structural_inspections.json", inspections, indent=2, default=str)

    print(f"  Loaded {len(scripts)} scripts", flush=True)
    print(f"  Structural classification:", flush=True)
    for polarity, count in sorted(polarity_counts.items()):
        print(f"    {polarity}: {count}", flush=True)

    # Phase B: Benchmark Execution
    total_runs = len(scripts) * len(CONDITIONS) * REPETITIONS
    print(f"\n{'='*60}", flush=True)
    print(f"[Phase B] Benchmark Execution", flush=True)
    print(f"  Scripts: {len(scripts)}", flush=True)
    print(f"  Conditions: {CONDITIONS}", flush=True)
    print(f"  Repetitions: {REPETITIONS}", flush=True)
    print(f"  Total runs: {total_runs}", flush=True)
    print(f"{'='*60}\n", flush=True)

    runner = SimulationBenchmarkRunner(gen_client=gen_client)
    results = await runner.run_suite(
        conditions=CONDITIONS,
        repetitions=REPETITIONS,
        scripts=scripts,
        checkpoint_dir=str(output_dir),
    )

    # Phase C: Output
    print(f"\n{'='*60}", flush=True)
    print(f"[Phase C] Output & Analysis", flush=True)
    print(f"{'='*60}\n", flush=True)

    save_benchmark_outputs(results, str(output_dir))

    # Print summary
    aggregate = results.get("aggregate", {})
    print("\n" + "="*60, flush=True)
    print("STRUCTURAL BENCHMARK SUMMARY", flush=True)
    print("="*60, flush=True)
    for condition, summary in sorted(aggregate.items()):
        print(f"\n  {condition} (n={summary.get('num_runs', 0)}):", flush=True)
        print(f"    drift={summary.get('persona_drift_mae_mean', 0.0):.4f}", flush=True)
        print(f"    contradiction={summary.get('commitment_contradiction_mean', 0.0):.4f}", flush=True)
        print(f"    convergence={summary.get('action_family_convergence_rate_mean', 0.0):.4f}", flush=True)
        print(f"    diversity={summary.get('role_action_diversity_score_mean', 0.0):.4f}", flush=True)
        print(f"    envelope={summary.get('envelope_violations_mean', 0.0):.1f}", flush=True)

    # Compare with existing GPT-4o-mini baseline
    baseline_path = Path("simulation_engine/results_final_benchmark_gpt4o_mini/benchmark_aggregate.json")
    if baseline_path.exists():
        baseline = json.loads(baseline_path.read_text())
        baseline_engine = baseline.get("engine_dialogue_only", {})
        structural = aggregate.get("engine_structural", {})
        if baseline_engine and structural:
            print("\n  ENGINE_STRUCTURAL vs ENGINE_DIALOGUE_ONLY (existing baseline):", flush=True)
            for metric in ("persona_drift_mae_mean", "commitment_contradiction_mean",
                            "action_family_convergence_rate_mean", "role_action_diversity_score_mean",
                            "envelope_violations_mean"):
                new_val = structural.get(metric, 0.0)
                old_val = baseline_engine.get(metric, 0.0)
                delta = round(new_val - old_val, 4)
                label = metric.replace("_mean", "").replace("_", " ")
                better = "better" if (delta < 0 and "penalty" not in label and "violation" not in label and "convergence" not in label) else ("better" if delta > 0 and "diversity" in label else "")
                print(f"    {label}: {old_val:.4f} -> {new_val:.4f} ({delta:+.4f}) {better}", flush=True)

    print(f"\nResults: {output_dir}/", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
