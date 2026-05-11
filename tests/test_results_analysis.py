from simulation_engine.results_analysis import ensure_results_analysis


def _sample_result():
    return {
        "simulation_id": "sim_test",
        "runtime_summary": {
            "phase_order": ["OPENING", "CLOSING"],
            "actor_labels": {"actor_1": "CTO", "actor_2": "CEO"},
            "turns": [
                {
                    "turn_index": 1,
                    "actor_id": "actor_1",
                    "display_name": "Jordan",
                    "content": "We should delay until the security issue is fixed.",
                    "phase_name": "OPENING",
                    "metadata": {},
                },
                {
                    "turn_index": 2,
                    "actor_id": "actor_2",
                    "display_name": "Alex",
                    "content": "Launch pressure is high, but I accept the security concern.",
                    "phase_name": "CLOSING",
                    "metadata": {},
                },
            ],
            "relationship_events": [
                {
                    "source_actor_id": "actor_1",
                    "target_actor_id": "actor_2",
                    "trust_delta": -0.08,
                    "tension_delta": 0.03,
                    "turn_index": 1,
                    "phase_name": "OPENING",
                    "evidence": "delay until the security issue is fixed",
                    "sentiment": "negative",
                    "new_sentiment": "negative",
                }
            ],
            "actor_state_events": [
                {
                    "actor_id": "actor_1",
                    "turn_index": 1,
                    "phase_name": "OPENING",
                    "new_state": {
                        "drift_score": 0.18,
                        "rolling_trait_estimate": {"O": 0.7, "C": 0.8, "E": 0.4, "A": 0.3, "N": 0.2},
                        "stress": 0.2,
                    },
                }
            ],
            "action_proposals": [
                {
                    "proposal_id": "prop_1",
                    "actor_id": "actor_1",
                    "phase_name": "OPENING",
                    "turn_index": 1,
                    "action_type": "request_evidence",
                    "status": "executed",
                }
            ],
            "executed_actions": [
                {
                    "proposal_id": "prop_1",
                    "action_type": "request_evidence",
                    "phase_name": "OPENING",
                    "owner_actor_id": "actor_1",
                    "target_key": "risk",
                    "applied_delta": {"risk": 0.11},
                }
            ],
            "world_state_history": [
                {"phase_name": "OPENING", "turn_index": 0, "global_state": {"risk": 0.5, "alignment": 0.5}},
                {"phase_name": "OPENING", "turn_index": 1, "global_state": {"risk": 0.61, "alignment": 0.48}},
                {"phase_name": "CLOSING", "turn_index": 2, "global_state": {"risk": 0.61, "alignment": 0.48}},
            ],
        },
        "metrics": {
            "actor_trait_estimates": {
                "actor_1": {"O": 0.7, "C": 0.8, "E": 0.4, "A": 0.3, "N": 0.2},
                "actor_2": {"O": 0.4, "C": 0.6, "E": 0.7, "A": 0.5, "N": 0.2},
            },
            "actor_trait_errors": {},
            "actor_display_names": {"actor_1": "Jordan", "actor_2": "Alex"},
            "persona_drift_mae": 0.12,
            "relationship_inconsistency": 0.0,
            "commitment_contradiction_rate": 0.0,
            "envelope_violations": 0,
        },
        "key_moments": [],
        "conclusion": {
            "mode": "guided",
            "outcome_achieved": "partial",
            "outcome_summary": "The team paused to weigh launch pressure against security risk.",
            "actor_arcs": [{"actor_id": "actor_1", "role": "CTO", "arc": "Pressed to delay launch until risk fell."}],
            "contributing_factors": [],
            "unresolved_tensions": [],
        },
        "script": {
            "simulation_id": "sim_test",
            "title": "Security Launch Debate",
            "objective": "Decide whether to delay launch.",
            "brief": "A leadership team debates delaying launch after a security finding.",
            "scenario_family": "generic",
            "simulation_mode": "guided",
            "outcome_spec": {"desired_outcome": "Delay launch until security risk is addressed."},
            "stakeholders": [
                {
                    "actor_id": "actor_1",
                    "display_name": "Jordan",
                    "role": "CTO",
                    "personality_prior": {"O": 0.7, "C": 0.8, "E": 0.4, "A": 0.3, "N": 0.2},
                    "strategic_disposition": "competitive",
                    "incentives": ["avoid breach"],
                    "concerns": ["brand damage"],
                },
                {
                    "actor_id": "actor_2",
                    "display_name": "Alex",
                    "role": "CEO",
                    "personality_prior": {"O": 0.4, "C": 0.6, "E": 0.7, "A": 0.5, "N": 0.2},
                    "strategic_disposition": "neutral",
                    "incentives": ["ship on time"],
                    "concerns": ["customer churn"],
                },
            ],
            "initial_relationships": [
                {"source": "actor_1", "target": "actor_2", "label": "tension"},
            ],
        },
    }


def test_results_analysis_adds_expected_keys():
    analyzed = ensure_results_analysis(_sample_result())
    assert "initial_relationships" in analyzed
    assert "final_relationships" in analyzed
    assert "change_events" in analyzed
    assert "change_attribution" in analyzed
    assert "phase_summaries" in analyzed
    assert "outcome_analysis" in analyzed
    assert "relationship_analysis" in analyzed
    assert "actor_analysis" in analyzed
    assert "phase_filtered_attribution" in analyzed


def test_results_analysis_aggregates_relationship_changes_and_emits_stable_ids():
    analyzed = ensure_results_analysis(_sample_result())
    final_relationships = analyzed["final_relationships"]
    rel = next(item for item in final_relationships if item["relationship_id"] == "rel:actor_1:actor_2")
    assert rel["initial_trust"] == 0.35
    assert rel["final_trust"] == 0.27

    change = next(item for item in analyzed["change_events"] if item["change_id"] == "change:relationship:actor_1:actor_2")
    assert change["category"] == "relationship"
    assert analyzed["change_attribution"][change["change_id"]][0]["turn_index"] == 1
    pair = next(item for item in analyzed["relationship_analysis"]["pairs"] if item["relationship_id"] == "rel:actor_1:actor_2")
    assert pair["phase_deltas"][0]["phase_name"] == "OPENING"
    assert pair["top_trigger_summaries"][0]["type"] == "relationship"


def test_results_analysis_builds_guided_outcome_and_actor_analysis():
    analyzed = ensure_results_analysis(_sample_result())
    outcome = analyzed["outcome_analysis"]
    assert outcome["mode"] == "guided"
    assert outcome["outcome_status"] == "partial"
    assert outcome["target_outcome"]["desired_outcome"].startswith("Delay launch")

    actor = next(item for item in analyzed["actor_analysis"]["actors"] if item["actor_id"] == "actor_1")
    assert actor["before_summary"]["role"] == "CTO"
    assert actor["after_summary"]["end_state"].startswith("Pressed to delay launch")
    assert actor["evidence_by_type"]["relationship"][0]["related_relationship_id"] == "rel:actor_1:actor_2"
    assert actor["evidence_by_type"]["actor_drift"][0]["type"] == "actor_drift"
    assert actor["evidence_by_type"]["action"][0]["type"] == "action"


def test_results_analysis_builds_exploratory_outcome_for_emergent_runs():
    sample = _sample_result()
    sample["script"]["simulation_mode"] = "exploratory"
    sample["script"]["outcome_spec"] = {}
    sample["conclusion"] = {
        "mode": "exploratory",
        "outcome_summary": "The team surfaced a shared concern about launch risk without reaching full alignment.",
        "key_discoveries": ["Risk language spread faster than commitment language."],
        "emergent_patterns": ["Conflict stayed interpersonal rather than structural."],
        "actor_arcs": [{"actor_id": "actor_1", "role": "CTO", "arc": "Pressed to delay launch until risk fell."}],
        "unresolved_tensions": [],
    }
    analyzed = ensure_results_analysis(sample)
    outcome = analyzed["outcome_analysis"]
    assert outcome["mode"] == "exploratory"
    assert outcome["outcome_status"] == "emergent"
    assert outcome["target_outcome"] is None
    assert "does not compare against a fixed target" in outcome["difference_summary"].lower()


def test_results_analysis_builds_phase_filtered_attribution():
    analyzed = ensure_results_analysis(_sample_result())
    phase_items = analyzed["phase_filtered_attribution"]["OPENING"]
    assert phase_items["relationship"]
    assert phase_items["actor_drift"]
    assert phase_items["action"]
    assert all(item["phase_name"] == "OPENING" for item in phase_items["all"])


def test_results_analysis_handles_sparse_result_without_crashing():
    sparse = {
        "simulation_id": "sparse",
        "runtime_summary": {"phase_order": [], "turns": [], "relationship_events": [], "actor_state_events": [], "action_proposals": [], "executed_actions": [], "world_state_history": [], "actor_labels": {}},
        "metrics": {"actor_trait_estimates": {}, "actor_trait_errors": {}, "actor_display_names": {}, "persona_drift_mae": 0.0, "relationship_inconsistency": 0.0, "commitment_contradiction_rate": 0.0, "envelope_violations": 0},
        "key_moments": [],
        "script": {"stakeholders": [], "initial_relationships": []},
    }
    analyzed = ensure_results_analysis(sparse)
    assert analyzed["change_events"] == []
    assert analyzed["phase_summaries"] == []
    assert analyzed["actor_analysis"]["actors"] == []
