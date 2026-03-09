import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine.builder import enrich_generated_script_payload, infer_scenario_family
from simulation_engine.script import SimulationScript


def test_builder_enriches_generated_payload_with_full_contract():
    raw = {
        "title": "AWS to GCP Migration",
        "objective": "Debate whether to migrate cloud providers.",
        "stakeholders": [
            {
                "display_name": "Nina",
                "role": "CTO",
                "personality_prior": {"O": 0.6, "C": 0.5, "E": 0.5, "A": 0.4, "N": 0.4},
                "incentives": ["better ML tooling"],
                "concerns": ["migration risk"],
            },
            {
                "display_name": "Sam",
                "role": "DevOps lead",
                "personality_prior": {"O": 0.4, "C": 0.8, "E": 0.4, "A": 0.4, "N": 0.3},
                "incentives": ["stable platform"],
                "concerns": ["downtime"],
            },
            {
                "display_name": "Iris",
                "role": "CFO",
                "personality_prior": {"O": 0.3, "C": 0.7, "E": 0.3, "A": 0.4, "N": 0.4},
                "incentives": ["cost control"],
                "concerns": ["overrun"],
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Frame the decision"},
            {"name": "TENSION", "goal": "Surface risks"},
            {"name": "NEGOTIATION", "goal": "Look for compromise"},
            {"name": "CLOSING", "goal": "Summarize the decision"},
        ],
    }

    enriched = enrich_generated_script_payload(
        raw,
        brief="The team is debating an AWS to GCP migration and worries about downtime and costs.",
        brief_id="aws_to_gcp_migration",
        generation_attempts=1,
    )
    script = SimulationScript.from_dict(enriched)

    assert script.scenario_family == "resource_scarcity"
    assert script.allowed_action_types
    assert script.transition_rules["NEGOTIATION"]
    assert script.metadata["phase_action_policies"]["NEGOTIATION"]["action_mode"] == "execute"
    assert script.metadata["actor_action_preferences"]["actor_1"]["default"]["primary_families"]
    assert script.metadata["metadata_completeness_score"] == 1.0
    assert script.metadata["builder_trace"]["builder_trace_id"] == "builder:aws_to_gcp_migration"


def test_builder_infers_policy_spillover_family_for_public_adoption_brief():
    family = infer_scenario_family(
        "A hospital is deciding whether to adopt AI-assisted diagnostics while managing consent and liability.",
        [{"role": "Chief of medicine"}, {"role": "Patient advocacy group"}],
        "Hospital AI Diagnostics",
    )

    assert family == "policy_spillover"
