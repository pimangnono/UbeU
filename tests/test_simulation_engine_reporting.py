import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiment import run_experiment
from simulation_engine.reporting import build_benchmark_report, save_benchmark_outputs


def _sample_results():
    return {
        "config": {
            "conditions": ["naive", "engine_controller"],
            "repetitions": 2,
            "script_ids": ["policy_alpha"],
            "style_slots": ["planner", "skeptic"],
        },
        "runs": [
            {
                "condition": "naive",
                "simulation_id": "policy_alpha",
                "runtime_summary": {"turn_count": 11},
                "metrics": {"persona_drift_mae": 0.21},
                "selection_audits": [],
            }
        ],
        "aggregate": {
            "naive": {
                "num_runs": 2,
                "persona_drift_mae_mean": 0.21,
                "persona_drift_mae_std": 0.03,
                "relationship_inconsistency_mean": 0.10,
                "commitment_contradiction_mean": 0.05,
                "envelope_violations_mean": 1.0,
                "per_trait_error_mean": {"O": 0.08, "C": 0.34, "E": 0.22, "A": 0.07, "N": 0.18},
                "turn_count_mean": 11.0,
            },
            "engine_controller": {
                "num_runs": 2,
                "persona_drift_mae_mean": 0.12,
                "persona_drift_mae_std": 0.01,
                "relationship_inconsistency_mean": 0.04,
                "commitment_contradiction_mean": 0.01,
                "envelope_violations_mean": 0.0,
                "per_trait_error_mean": {"O": 0.07, "C": 0.20, "E": 0.16, "A": 0.06, "N": 0.11},
                "turn_count_mean": 11.0,
            },
        },
        "aggregate_by_script": {
            "policy_alpha:naive": {
                "num_runs": 2,
                "persona_drift_mae_mean": 0.21,
                "persona_drift_mae_std": 0.03,
                "relationship_inconsistency_mean": 0.10,
                "commitment_contradiction_mean": 0.05,
                "envelope_violations_mean": 1.0,
                "per_trait_error_mean": {"O": 0.08, "C": 0.34, "E": 0.22, "A": 0.07, "N": 0.18},
                "turn_count_mean": 11.0,
            }
        },
    }


def test_reporting_writes_json_and_markdown(tmp_path):
    results = _sample_results()

    output_paths = save_benchmark_outputs(results, tmp_path)

    runs_path = Path(output_paths["runs"])
    aggregate_path = Path(output_paths["aggregate"])
    report_path = Path(output_paths["report"])

    assert runs_path.exists()
    assert aggregate_path.exists()
    assert report_path.exists()
    report_text = report_path.read_text()
    assert "Simulation Benchmark Report" in report_text
    assert "Controlled Engine vs Baseline" in report_text
    assert "Per-trait absolute error" in report_text


def test_build_benchmark_report_includes_script_summary():
    report = build_benchmark_report(_sample_results())

    assert "policy_alpha:naive" in report
    assert "Persona drift delta" in report
    assert "Per-trait error delta" in report


def test_main_routes_simulation_benchmark_flag(monkeypatch, capsys):
    async def _fake_run_simulation_benchmark(output_dir, conditions, repetitions, script_ids):
        return {
            "output_dir": output_dir,
            "output_paths": {
                "runs": f"{output_dir}/benchmark_runs.json",
                "aggregate": f"{output_dir}/benchmark_aggregate.json",
                "report": f"{output_dir}/benchmark_report.md",
            },
            "aggregate": {"engine_controller": {"persona_drift_mae_mean": 0.12}},
            "aggregate_by_script": {},
            "config": {
                "conditions": conditions or ["naive", "engine_controller"],
                "repetitions": repetitions,
                "script_ids": script_ids or ["policy_alpha"],
            },
            "total_runs": 4,
        }

    monkeypatch.setattr(run_experiment, "run_simulation_benchmark", _fake_run_simulation_benchmark)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_experiment.py",
            "--simulation-benchmark-mvp",
            "--benchmark-repetitions",
            "2",
            "--benchmark-scripts",
            "policy_alpha",
        ],
    )

    run_experiment.main()
    captured = capsys.readouterr()

    assert "Running stakeholder simulation MVP benchmark..." in captured.out
    assert "benchmark_report.md" in captured.out
