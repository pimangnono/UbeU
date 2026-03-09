"""Experiment 3: User-Input Brief → Auto-Generated Script.

Tests the actual product flow: user provides a brief, LLM generates the full script.
"""
import asyncio
import json
from pathlib import Path

from simulation_engine.benchmark import SimulationBenchmarkRunner
from simulation_engine.builder import enrich_generated_script_payload, validate_enriched_script
from simulation_engine.reporting import save_benchmark_outputs
from simulation_engine.script import SimulationScript

SCRIPT_GENERATION_SYSTEM = """\
You are a simulation script generator. Given a user's brief about a decision or discussion,
generate a complete simulation script as JSON.

The JSON must follow this exact schema:
{
  "simulation_id": "<snake_case_id>",
  "title": "<short title>",
  "objective": "<1-2 sentence objective>",
  "brief": "<the user's original brief>",
  "stakeholders": [
    {
      "actor_id": "actor_1",
      "display_name": "<first name or title>",
      "role": "<role description>",
      "identity_core": {"position": "<position>", "domain": "<domain>"},
      "personality_prior": {"O": <0.0-1.0>, "C": <0.0-1.0>, "E": <0.0-1.0>, "A": <0.0-1.0>, "N": <0.0-1.0>},
      "incentives": ["<incentive1>", "<incentive2>"],
      "concerns": ["<concern1>", "<concern2>"],
      "communication_style": {"tone": "<tone>", "brevity": "moderate"}
    }
  ],
  "phases": [
    {"name": "OPENING", "goal": "<goal>", "style": "neutral", "max_turns": 3, "cues": ["<cue1>"]},
    {"name": "TENSION", "goal": "<goal>", "style": "disagreement", "max_turns": 3, "cues": ["<cue1>"]},
    {"name": "NEGOTIATION", "goal": "<goal>", "style": "consensus", "max_turns": 3, "cues": ["<cue1>"]},
    {"name": "CLOSING", "goal": "<goal>", "style": "neutral", "max_turns": 2, "cues": ["<cue1>"]}
  ],
  "scenario_family": "<best guess family>",
  "simulation_mode": "<guided or exploratory>",
  "world_state_schema": ["<state_key1>", "<state_key2>"],
  "initial_world_state": {"<state_key1>": 0.5, "<state_key2>": 0.5},
  "allowed_action_types": ["assign_owner", "request_evidence"],
  "transition_rules": {
    "OPENING": {
      "request_evidence": {
        "global_deltas": {"uncertainty": -0.04},
        "owner_local_deltas": {"execution_confidence": 0.04},
        "feedback_template": "<effect summary>"
      }
    }
  },
  "state_visibility_rules": {
    "global_keys": ["alignment", "uncertainty", "risk"],
    "local_keys": ["trust", "execution_confidence", "alignment"],
    "max_recent_actions": 2
  },
  "metadata": {
    "phase_action_policies": {"OPENING": {"action_mode": "shadow"}},
    "actor_action_preferences": {"actor_1": {"default": {"primary_families": ["evidence"]}}}
  },
  "world_events": [
    {
      "event_id": "evt_1",
      "title": "<event title>",
      "description": "<what happens>",
      "trigger_phase": "TENSION"
    }
  ]
}

Rules:
- Generate 3-4 stakeholders based on the brief
- Personality priors (OCEAN) should vary across stakeholders — don't cluster them
- Each stakeholder needs distinct incentives and concerns that create natural tension
- Phase names MUST be exactly: OPENING, TENSION, NEGOTIATION, CLOSING (in that order)
- Include 1-2 world events that add pressure or new information
- Prefer valid action-layer metadata, but do not invent nonsense if uncertain
- Output ONLY the JSON, no markdown fences or explanation
"""


async def generate_script_from_brief(gen_client, brief: str, brief_id: str) -> SimulationScript:
    """Generate a complete SimulationScript from a user's brief."""
    prompt = f"Generate a simulation script for this scenario:\n\n{brief}"

    response = await gen_client.generate(
        prompt=prompt,
        system_instruction=SCRIPT_GENERATION_SYSTEM,
        temperature=0.7,
        max_tokens=2000,
    )

    # Clean response — strip markdown fences if present
    text = response.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    if text.startswith("json"):
        text = text[4:].strip()

    data = json.loads(text)
    enriched = enrich_generated_script_payload(
        data,
        brief=brief,
        brief_id=brief_id,
        generation_attempts=1,
    )
    return validate_enriched_script(enriched)


TEST_BRIEFS = [
    (
        "aws_to_gcp_migration",
        "My team is debating whether to migrate from AWS to GCP. The CTO wants it for "
        "better ML tooling, the DevOps lead is worried about migration risk and downtime, "
        "and the CFO wants hard cost data before committing.",
    ),
    (
        "open_source_core_product",
        "Our company needs to decide whether to open-source our core product. Engineering "
        "wants it for community contributions and hiring, sales is concerned about giving "
        "away competitive advantage, and legal worries about IP exposure.",
    ),
    (
        "hospital_ai_diagnostics",
        "A hospital is deciding whether to adopt AI-assisted diagnostics. The chief of "
        "medicine is cautious about liability, the radiology department head wants it for "
        "efficiency, and the patient advocacy group has concerns about consent and accuracy.",
    ),
]


async def main():
    from experiment.run_experiment import create_clients
    gen_client, _ = create_clients()

    output_dir = "simulation_engine/results_exp3_userinput"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Generate scripts from briefs
    scripts = []
    generation_log = []
    for brief_id, brief in TEST_BRIEFS:
        print(f"[exp3] Generating script from brief: {brief_id}...", flush=True)
        try:
            script = await generate_script_from_brief(gen_client, brief, brief_id)
            scripts.append(script)
            generation_log.append({
                "brief_id": brief_id,
                "status": "success",
                "actors": len(script.stakeholders),
                "phases": len(script.phases),
                "events": len(script.world_events),
                "scenario_family": script.scenario_family,
                "simulation_mode": script.simulation_mode,
                "metadata_completeness_score": dict(script.metadata).get("metadata_completeness_score"),
                "missing_contract_fields": list(dict(script.metadata).get("missing_contract_fields", [])),
            })
            print(f"  Generated: {len(script.stakeholders)} actors, {len(script.phases)} phases", flush=True)
        except Exception as e:
            error_text = str(e)
            if "Expecting value" in error_text:
                failure_type = "invalid_json"
            elif "must contain" in error_text or "requires" in error_text or "unknown" in error_text:
                failure_type = "schema_invalid"
            else:
                failure_type = "runtime_unrunnable"
            generation_log.append({
                "brief_id": brief_id,
                "status": "error",
                "failure_type": failure_type,
                "error": error_text,
            })
            print(f"  FAILED: {e}", flush=True)

    # Save generation log
    with open(Path(output_dir) / "generation_log.json", "w") as f:
        json.dump(generation_log, f, indent=2)

    # Save generated scripts for inspection
    for script in scripts:
        with open(Path(output_dir) / f"generated_script_{script.simulation_id}.json", "w") as f:
            json.dump(script.to_dict(), f, indent=2)

    if not scripts:
        print("[exp3] No scripts generated successfully. Aborting.", flush=True)
        return

    # Run benchmark
    print(f"\n[exp3] Running benchmark on {len(scripts)} generated scripts...", flush=True)
    runner = SimulationBenchmarkRunner(gen_client=gen_client)
    results = await runner.run_suite(
        conditions=["engine_dialogue_only"],
        repetitions=2,
        scripts=scripts,
        checkpoint_dir=output_dir,
    )
    save_benchmark_outputs(results, output_dir)
    print(f"\nExperiment 3 complete. Results in {output_dir}/")
    print(f"Aggregate: {json.dumps(results['aggregate'], indent=2)}")


if __name__ == "__main__":
    asyncio.run(main())
