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
            "suite_id": "suite_test",
        },
        "suite_id": "suite_test",
        "runs": [
            {
                "condition": "naive",
                "simulation_id": "policy_alpha",
                "suite_id": "suite_test",
                "track_id": "guided",
                "run_id": "suite_test:guided:policy_alpha:naive:1",
                "builder_trace_ref": "builder:policy_alpha",
                "runtime_summary": {
                    "simulation_id": "policy_alpha",
                    "simulation_mode": "guided",
                    "scenario_family": "policy_spillover",
                    "turn_count": 11,
                    "builder_trace": {
                        "builder_trace_id": "builder:policy_alpha",
                        "brief_id": "policy_alpha",
                        "builder_version": "brief_builder_v2",
                        "generation_attempts": 1,
                        "scenario_family": "policy_spillover",
                        "metadata_completeness_score": 1.0,
                        "missing_contract_fields": [],
                    },
                    "metadata_completeness_score": 1.0,
                    "turns": [
                        {
                            "turn_index": 1,
                            "actor_id": "actor_1",
                            "phase_name": "OPENING",
                            "content": "We should gather evidence before committing.",
                            "metadata": {
                                "turn_trace_id": "policy_alpha:OPENING:1:actor_1",
                                "slot": "planner",
                                "policy_plan": {"action_plan": {"action_type": "request_evidence"}},
                                "audit": {
                                    "actor_id": "actor_1",
                                    "phase_name": "OPENING",
                                    "turn_index": 1,
                                    "selected_index": 0,
                                    "selected_score": 0.61,
                                    "selected_slot": "planner",
                                    "selected_top_positive_drivers": [{"name": "identity_consistency", "value": 0.18}],
                                    "selected_top_negative_drivers": [{"name": "genericity_penalty", "value": -0.04}],
                                    "score_rows": [
                                        {
                                            "slot": "planner",
                                            "score": 0.61,
                                            "text_excerpt": "We should gather evidence before committing.",
                                            "inferred_traits": {"O": 0.5, "C": 0.6, "E": 0.4, "A": 0.5, "N": 0.4},
                                            "trait_error_map": {"O": 0.1, "C": 0.1, "E": 0.1, "A": 0.1, "N": 0.1},
                                            "score_components": {"identity_consistency": 0.18},
                                            "penalty_components": {"genericity_penalty": -0.04},
                                            "compiled_action_family": "evidence",
                                        }
                                    ],
                                },
                            },
                        }
                    ],
                    "relationship_events": [],
                    "actor_state_events": [],
                    "action_audits": [],
                    "latest_world_state": {"alignment": 0.5},
                    "actor_labels": {"actor_1": "Analyst"},
                    "actor_display_names": {"actor_1": "Alex"},
                    "actor_personality_envelopes": {"actor_1": {"O": [0.2, 0.8], "C": [0.2, 0.8], "E": [0.2, 0.8], "A": [0.2, 0.8], "N": [0.2, 0.8]}},
                },
                "metrics": {"persona_drift_mae": 0.21, "per_trait_error_mean": {"O": 0.08, "C": 0.34, "E": 0.22, "A": 0.07, "N": 0.18}},
                "selection_audits": [],
            }
        ],
        "aggregate": {
            "naive": {
                "num_runs": 2,
                "clean_run_count": 1,
                "contaminated_run_count": 1,
                "persona_drift_mae_mean": 0.21,
                "clean_persona_drift_mae_mean": 0.18,
                "persona_drift_mae_std": 0.03,
                "relationship_inconsistency_mean": 0.10,
                "relationship_shift_rate_mean": 0.06,
                "relationship_overshoot_rate_mean": 0.03,
                "commitment_contradiction_mean": 0.05,
                "clean_commitment_contradiction_mean": 0.02,
                "envelope_violations_mean": 1.0,
                "clean_envelope_violations_mean": 0.0,
                "fallback_utterance_rate_mean": 0.50,
                "fallback_type_rate_mean": {"timeout_fallback": 0.25, "empty_pool_fallback": 0.25},
                "per_trait_error_mean": {"O": 0.08, "C": 0.34, "E": 0.22, "A": 0.07, "N": 0.18},
                "turn_count_mean": 11.0,
                "ci_95": {"persona_drift_mae": [0.18, 0.24]},
                "zero_variance_metrics": [],
            },
            "engine_controller": {
                "num_runs": 2,
                "clean_run_count": 2,
                "contaminated_run_count": 0,
                "persona_drift_mae_mean": 0.12,
                "clean_persona_drift_mae_mean": 0.12,
                "persona_drift_mae_std": 0.01,
                "relationship_inconsistency_mean": 0.04,
                "relationship_shift_rate_mean": 0.05,
                "relationship_overshoot_rate_mean": 0.01,
                "commitment_contradiction_mean": 0.01,
                "clean_commitment_contradiction_mean": 0.01,
                "envelope_violations_mean": 0.0,
                "clean_envelope_violations_mean": 0.0,
                "fallback_utterance_rate_mean": 0.10,
                "fallback_type_rate_mean": {"timeout_fallback": 0.10},
                "per_trait_error_mean": {"O": 0.07, "C": 0.20, "E": 0.16, "A": 0.06, "N": 0.11},
                "turn_count_mean": 11.0,
                "ci_95": {"persona_drift_mae": [0.11, 0.13]},
                "zero_variance_metrics": ["fallback_utterance_rate"],
            },
        },
        "aggregate_by_script": {
            "policy_alpha:naive": {
                "num_runs": 2,
                "clean_run_count": 1,
                "contaminated_run_count": 1,
                "persona_drift_mae_mean": 0.21,
                "clean_persona_drift_mae_mean": 0.18,
                "persona_drift_mae_std": 0.03,
                "relationship_inconsistency_mean": 0.10,
                "relationship_shift_rate_mean": 0.06,
                "relationship_overshoot_rate_mean": 0.03,
                "commitment_contradiction_mean": 0.05,
                "clean_commitment_contradiction_mean": 0.02,
                "envelope_violations_mean": 1.0,
                "clean_envelope_violations_mean": 0.0,
                "fallback_utterance_rate_mean": 0.50,
                "fallback_type_rate_mean": {"timeout_fallback": 0.25, "empty_pool_fallback": 0.25},
                "per_trait_error_mean": {"O": 0.08, "C": 0.34, "E": 0.22, "A": 0.07, "N": 0.18},
                "turn_count_mean": 11.0,
                "ci_95": {"persona_drift_mae": [0.18, 0.24]},
                "zero_variance_metrics": [],
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
    assert Path(output_paths["suite_manifest"]).exists()
    assert Path(output_paths["turn_decisions"]).exists()
    assert Path(output_paths["metric_attributions"]).exists()
    report_text = report_path.read_text()
    assert "Simulation Benchmark Report" in report_text
    assert "Controlled Engine vs Baseline" in report_text
    assert "Per-trait absolute error" in report_text
    assert "Fallback utterance rate" in report_text
    assert "Relationship shift rate" in report_text


def test_reporting_defaults_to_compact_runs_payload(tmp_path, monkeypatch):
    monkeypatch.delenv("SIM_BENCHMARK_RUNS_MODE", raising=False)
    results = _sample_results()
    results["runs"][0]["runtime_summary"] = {
        "turn_count": 11,
        "action_proposals": [{"id": "a1"}],
        "executed_actions": [{"id": "e1"}],
        "action_audits": [{"id": "x"}],
        "world_state_history": [{"phase": "OPENING"}],
        "latest_world_state": {"alignment": 0.5},
    }

    output_paths = save_benchmark_outputs(results, tmp_path)
    payload = __import__("json").loads(Path(output_paths["runs"]).read_text())

    assert payload["mode"] == "compact"
    compact_summary = payload["runs"][0]["runtime_summary"]
    assert "action_proposals" not in compact_summary
    assert compact_summary["action_proposal_count"] == 1
    assert compact_summary["executed_action_count"] == 1
    assert compact_summary["action_audit_count"] == 1
    assert compact_summary["world_state_history_count"] == 1
    assert "trace_refs" in compact_summary


def test_reporting_can_omit_runs_payload(tmp_path, monkeypatch):
    monkeypatch.setenv("SIM_BENCHMARK_RUNS_MODE", "none")
    results = _sample_results()

    output_paths = save_benchmark_outputs(results, tmp_path)
    payload = __import__("json").loads(Path(output_paths["runs"]).read_text())

    assert payload["runs_omitted"] is True
    assert payload["mode"] == "none"
    assert payload["run_count"] == 1


def test_build_benchmark_report_includes_script_summary():
    report = build_benchmark_report(_sample_results())

    assert "policy_alpha:naive" in report
    assert "Persona drift delta" in report
    assert "Per-trait error delta" in report
    assert "Reliability Warnings" in report
    assert "Persona drift 95% CI" in report


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
