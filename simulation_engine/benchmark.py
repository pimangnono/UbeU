"""Benchmark harness for naive vs engine stakeholder simulation runs."""

from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, pstdev
from typing import Any

from .ablation import (
    ALL_BENCHMARK_CONDITIONS,
    BenchmarkCondition,
    resolve_benchmark_condition,
)
from .action_layer import (
    action_plan_alignment_score,
    apply_transition_rule,
    arbitrate_phase_actions,
    compile_action_proposal,
    normalize_planned_action_artifact,
)
from .controller import PersonaStateController
from .graph_runner import StakeholderSimulationGraphRunner
from .manual_scripts import load_mvp_policy_scripts
from .metrics import (
    BenchmarkRunMetrics,
    aggregate_phase_end_state_variance,
    compute_runtime_metrics,
    estimate_actor_traits_from_turns,
    persona_drift_mae,
)
from .runtime import StakeholderSimulationRuntime
from .reporting import save_benchmark_outputs

DEFAULT_STYLE_SLOTS = ["integrator", "planner", "challenger", "skeptic"]


@dataclass
class BenchmarkRunResult:
    condition: str
    simulation_id: str
    runtime_summary: dict[str, Any]
    metrics: BenchmarkRunMetrics
    selection_audits: list[dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "condition": self.condition,
            "simulation_id": self.simulation_id,
            "runtime_summary": self.runtime_summary,
            "metrics": self.metrics.to_dict(),
            "selection_audits": self.selection_audits,
        }


class SimulationBenchmarkRunner:
    """Run repeated benchmark conditions on pre-injected policy scripts."""

    def __init__(
        self,
        gen_client,
        style_slots: list[str] | None = None,
        use_graph: bool = True,
    ):
        self.gen_client = gen_client
        self.style_slots = style_slots or list(DEFAULT_STYLE_SLOTS)
        self.use_graph = use_graph
        self.graph_runner = (
            StakeholderSimulationGraphRunner(
                gen_client=gen_client,
                style_slots=self.style_slots,
            )
            if use_graph
            else None
        )

    async def run_single(
        self,
        script,
        condition: BenchmarkCondition,
    ) -> BenchmarkRunResult:
        if self.graph_runner is not None:
            graph_result = await self.graph_runner.run(script, condition)
            return BenchmarkRunResult(
                condition=graph_result["condition"],
                simulation_id=graph_result["simulation_id"],
                runtime_summary=graph_result["runtime_summary"],
                metrics=graph_result["metrics"],
                selection_audits=graph_result["selection_audits"],
            )

        return await self._run_single_manual(script, condition)

    async def _run_single_manual(
        self,
        script,
        condition: BenchmarkCondition,
    ) -> BenchmarkRunResult:
        base_condition, ablation_config = resolve_benchmark_condition(condition)
        runtime = StakeholderSimulationRuntime(
            script=script,
            gen_client=self.gen_client,
            ablation_config=ablation_config,
        )
        actor_name_map = {
            actor_id: actor.display_name
            for actor_id, actor in runtime.actors.items()
        }
        controllers = {
            actor_id: PersonaStateController(
                actor.actor_spec,
                actor_name_map=actor_name_map,
                ablation_config=ablation_config,
            )
            for actor_id, actor in runtime.actors.items()
        }
        injected_events: set[str] = set()

        for phase in script.phases:
            while runtime.current_phase.name != phase.name:
                runtime.advance_phase()

            for event in script.world_events:
                if event.event_id in injected_events:
                    continue
                if event.trigger_phase == phase.name:
                    runtime.record_world_event(event.event_id)
                    injected_events.add(event.event_id)

            for _ in range(phase.max_turns):
                actor_id = runtime.select_next_actor_round_robin()
                actor = runtime.actors[actor_id]
                context = runtime.actor_context(actor_id, max_turns=8)
                phase_action_policy = runtime.script.phase_action_policy(phase.name)

                if base_condition == "naive":
                    response_payload = await actor.generate_response_payload(
                        turns=context["turns"],
                        phase_style=phase.style,
                        actor_snapshot=None,
                        phase_name=phase.name,
                        phase_cues=phase.cues,
                    )
                    text = response_payload["text"]
                    selected_meta = {
                        "mode": "naive",
                        "generation_meta": dict(response_payload.get("generation_meta", {})),
                    }
                else:
                    controller = controllers[actor_id]
                    drift_nudge = (
                        controller.build_nudge(context["snapshot"])
                        if base_condition == "engine_controller"
                        else None
                    )
                    actor.update_nudge(drift_nudge)
                    policy_plan = await actor.generate_policy_plan(
                        turns=context["turns"],
                        actor_snapshot=context["snapshot"] if base_condition != "naive" else None,
                        phase_name=phase.name,
                        phase_cues=phase.cues,
                        allowed_action_types=list(runtime.script.allowed_action_types_for_phase(phase.name)),
                        valid_target_keys=list(runtime.script.target_keys_for_phase(phase.name)),
                        actor_action_preferences=runtime.script.actor_action_preferences(actor_id, phase.name),
                        use_cache=runtime.script.planner_cache_enabled_for_phase(phase.name),
                    )
                    planned_action_artifact = normalize_planned_action_artifact(
                        script=runtime.script,
                        actor_id=actor_id,
                        phase_name=phase.name,
                        policy_plan=policy_plan,
                        planned_action_artifact=policy_plan.get("action_plan"),
                        valid_target_keys=list(runtime.script.target_keys_for_phase(phase.name)),
                        allowed_action_types=list(runtime.script.allowed_action_types_for_phase(phase.name)),
                    )
                    pool = await actor.generate_candidate_pool_styles(
                        turns=context["turns"],
                        phase_style=phase.style,
                        style_slots=runtime.script.style_slots_for_phase(phase.name, self.style_slots),
                        actor_snapshot=context["snapshot"] if base_condition != "naive" else None,
                        phase_name=phase.name,
                        phase_cues=phase.cues,
                        policy_plan=policy_plan,
                        enable_trait_execution=(base_condition == "engine_controller"),
                        max_concurrency_override=runtime.script.pool_max_concurrency_for_phase(
                            phase.name,
                            default=2,
                        ),
                    )
                    if base_condition == "engine":
                        selected = pool[0]
                        selected_meta = {
                            "mode": "engine_first_candidate",
                            "policy_plan": policy_plan,
                            "slot": selected["slot"],
                            "planned_action_artifact": planned_action_artifact.to_dict() if planned_action_artifact else None,
                            "generation_meta": dict(selected.get("generation_meta", {})),
                        }
                        text = selected["text"]
                    else:
                        scored = controller.score_candidate_pool(
                            candidate_pool=pool,
                            visible_turns=context["turns"],
                            actor_snapshot=context["snapshot"],
                            phase=phase,
                            policy_plan=policy_plan,
                            action_context={
                                "script": runtime.script,
                                "valid_target_keys": list(runtime.script.target_keys_for_phase(phase.name)),
                                "allowed_action_types": list(runtime.script.allowed_action_types_for_phase(phase.name)),
                                "global_state": dict(runtime.ledger.latest_world_state().global_state),
                                "local_state": dict(context["snapshot"].get("local_state", {})),
                                "phase_action_policy": runtime.script.phase_action_policy(phase.name),
                                "actor_action_preferences": runtime.script.actor_action_preferences(actor_id, phase.name),
                                "phase_action_family_counts": runtime.ledger.phase_action_family_counts(
                                    phase.name,
                                    exclude_actor_id=actor_id,
                                ),
                                "phase_actor_action_families": runtime.ledger.phase_actor_action_families(
                                    phase.name,
                                    exclude_actor_id=actor_id,
                                ),
                                "turn_index": runtime.turn_index + 1,
                                "use_action_aware_scoring": bool(
                                    ablation_config.use_action_aware_scoring
                                    and phase_action_policy.get("action_mode", "execute") == "execute"
                                ),
                            },
                        )
                        selection = controller.select_candidate(
                            scored_candidates=scored,
                            phase=phase,
                            turn_index=runtime.turn_index + 1,
                            drift_nudge=drift_nudge,
                        )
                        selected = selection["selected"]
                        selected_meta = {
                            "mode": "engine_controller",
                            "policy_plan": policy_plan,
                            "audit": selection["audit"],
                            "slot": selected.get("slot"),
                            "action_hint": selected.get("action_hint"),
                            "planned_action_artifact": selected.get("planned_action_artifact") or (planned_action_artifact.to_dict() if planned_action_artifact else None),
                            "action_plan_alignment": selected.get("action_plan_alignment"),
                            "generation_meta": dict(selected.get("generation_meta", {})),
                        }
                        text = selected["text"]
                        runtime.ledger.apply_state_delta(
                            actor_id=actor_id,
                            last_inferred_traits=selected.get("inferred_traits"),
                            rolling_trait_estimate=selected.get("inferred_traits"),
                            drift_score=selected.get("persona_drift"),
                            sycophancy_risk=selected.get("sycophancy_risk"),
                            sycophancy_signals=selected.get("sycophancy_signals"),
                            unfulfilled_persona_acts=selected.get("unfulfilled_persona_acts"),
                            reflection=f"selected_score={selected.get('score', 0.0):.3f}",
                        )

                runtime.append_actor_turn(
                    actor_id=actor_id,
                    content=text,
                    metadata=selected_meta,
                )
                if ablation_config.use_action_layer:
                    phase_action_policy = runtime.script.phase_action_policy(phase.name)
                    proposal = await compile_action_proposal(
                        self.gen_client,
                        script=runtime.script,
                        actor_id=actor_id,
                        actor_name_map=actor_name_map,
                        phase_name=phase.name,
                        turn_index=runtime.turn_index,
                        selected_text=text,
                        policy_plan=selected_meta.get("policy_plan", {}),
                        actor_snapshot=context["snapshot"],
                        planned_action_artifact=selected_meta.get("planned_action_artifact"),
                        seed_action_hint=selected_meta.get("action_hint"),
                        actor_action_preferences=runtime.script.actor_action_preferences(actor_id, phase.name),
                        phase_action_policy=runtime.script.phase_action_policy(phase.name),
                        phase_action_family_counts=runtime.ledger.phase_action_family_counts(
                            phase.name,
                            exclude_actor_id=actor_id,
                        ),
                    )
                    trace_id = f"{runtime.script.simulation_id}:{actor_id}:{phase.name}:{runtime.turn_index}"
                    alignment_score, alignment_details = action_plan_alignment_score(
                        selected_meta.get("planned_action_artifact"),
                        proposal.to_dict() if proposal else selected_meta.get("action_hint"),
                    )
                    runtime.ledger.upsert_action_audit(
                        trace_id,
                        {
                            "trace_id": trace_id,
                            "proposal_id": proposal.proposal_id if proposal else trace_id,
                            "actor_id": actor_id,
                            "phase_name": phase.name,
                            "turn_index": runtime.turn_index,
                            "planned_action_artifact": selected_meta.get("planned_action_artifact"),
                            "selected_action_hint": selected_meta.get("action_hint"),
                            "compiled_proposal": proposal.to_dict() if proposal else None,
                            "compiler_source": proposal.compiler_source if proposal else "none",
                            "compile_status": proposal.status if proposal else "no_action",
                            "compile_rejection_reason": proposal.rejection_reason if proposal else "no_action_detected",
                            "validation_trace": list(proposal.validation_trace) if proposal else [],
                            "action_plan_alignment": alignment_score,
                            "action_plan_alignment_details": alignment_details,
                            "selected_text_excerpt": text[:180],
                        },
                    )
                    if phase_action_policy.get("action_mode", "execute") == "execute":
                        runtime.ledger.append_action_proposal(proposal)

                if base_condition != "engine_controller":
                    inferred_traits = estimate_actor_traits_from_turns(
                        runtime.visible_turns_for_actor(actor_id, max_turns=999),
                        actor.display_name,
                    )
                    runtime.ledger.apply_state_delta(
                        actor_id=actor_id,
                        last_inferred_traits=inferred_traits,
                        rolling_trait_estimate=inferred_traits,
                        drift_score=persona_drift_mae(actor.actor_spec.personality_prior, inferred_traits),
                    )

            if ablation_config.use_action_layer and runtime.script.phase_action_policy(phase.name).get("action_mode", "execute") == "execute":
                approved, rejected = arbitrate_phase_actions(
                    runtime.script,
                    phase.name,
                    runtime.ledger.phase_action_proposals(phase.name),
                )
                for proposal in approved:
                    runtime.ledger.update_action_proposal_status(proposal.proposal_id, status="approved")
                    runtime.ledger.update_action_audit(
                        proposal.proposal_id,
                        arbitration_status="approved",
                        arbitration_reason=None,
                    )
                for proposal in rejected:
                    runtime.ledger.update_action_proposal_status(
                        proposal.proposal_id,
                        status="rejected",
                        rejection_reason=proposal.rejection_reason,
                    )
                    runtime.ledger.update_action_audit(
                        proposal.proposal_id,
                        arbitration_status="rejected",
                        arbitration_reason=proposal.rejection_reason,
                    )
                current_snapshot = runtime.ledger.latest_world_state()
                executed_rows = []
                for proposal in approved:
                    executed, next_snapshot, rejection_reason = apply_transition_rule(
                        runtime.script,
                        proposal,
                        current_snapshot,
                    )
                    if executed is None or next_snapshot is None:
                        runtime.ledger.update_action_proposal_status(
                            proposal.proposal_id,
                            status="rejected",
                            rejection_reason=rejection_reason or "transition_failed",
                        )
                        runtime.ledger.update_action_audit(
                            proposal.proposal_id,
                            execution_status="rejected",
                            execution_rejection_reason=rejection_reason or "transition_failed",
                        )
                        continue
                    runtime.ledger.apply_executed_action(executed, next_snapshot)
                    runtime.ledger.update_action_audit(
                        proposal.proposal_id,
                        execution_status="executed",
                        execution_rejection_reason=None,
                        executed_action=executed.to_dict(),
                        pre_state=dict(current_snapshot.global_state),
                        post_state=dict(next_snapshot.global_state),
                    )
                    current_snapshot = next_snapshot
                    executed_rows.append(executed)
                runtime.ledger.record_phase_feedback(
                    phase.name,
                    executed_rows,
                    runtime.ledger.latest_world_state(),
                )

            runtime.advance_phase()

        selection_audits = [
            audit
            for controller in controllers.values()
            for audit in controller.selection_audits
        ]
        return BenchmarkRunResult(
            condition=condition,
            simulation_id=script.simulation_id,
            runtime_summary=runtime.to_runtime_summary(),
            metrics=compute_runtime_metrics(runtime),
            selection_audits=selection_audits,
        )

    async def run_suite(
        self,
        conditions: list[BenchmarkCondition] | None = None,
        repetitions: int = 1,
        script_ids: list[str] | None = None,
        checkpoint_dir: str | None = None,
    ) -> dict[str, Any]:
        conditions = conditions or ["naive", "engine", "engine_controller"]
        invalid = sorted(set(conditions).difference(ALL_BENCHMARK_CONDITIONS))
        if invalid:
            raise ValueError(f"Unknown benchmark conditions: {', '.join(invalid)}")
        scripts = load_mvp_policy_scripts()
        if script_ids:
            allowed = set(script_ids)
            scripts = [script for script in scripts if script.simulation_id in allowed]
            missing = sorted(allowed.difference(script.simulation_id for script in scripts))
            if missing:
                raise ValueError(f"Unknown simulation script ids: {', '.join(missing)}")

        run_results: list[BenchmarkRunResult] = []
        total_runs = len(scripts) * len(conditions) * repetitions
        completed_runs = 0
        checkpoint_path = Path(checkpoint_dir) if checkpoint_dir else None
        existing_run_counts: dict[tuple[str, str], int] = {}
        if checkpoint_path is not None:
            checkpoint_path.mkdir(parents=True, exist_ok=True)
            run_results, existing_run_counts = _load_checkpoint_results(
                checkpoint_path=checkpoint_path,
                scripts=scripts,
                conditions=conditions,
                repetitions=repetitions,
                style_slots=self.style_slots,
            )
            completed_runs = len(run_results)
            if completed_runs:
                print(
                    f"[benchmark] resumed from checkpoint: {completed_runs}/{total_runs} runs already completed",
                    flush=True,
                )
                with open(checkpoint_path / "progress.json", "w") as handle:
                    json.dump(
                        {
                            "completed_runs": completed_runs,
                            "total_runs": total_runs,
                            "last_script_id": run_results[-1].simulation_id,
                            "last_condition": run_results[-1].condition,
                        },
                        handle,
                        indent=2,
                    )

        for script in scripts:
            for condition in conditions:
                already_done = existing_run_counts.get((script.simulation_id, condition), 0)
                for rep_idx in range(repetitions):
                    if rep_idx < already_done:
                        continue
                    run_results.append(await self.run_single(script, condition))
                    completed_runs += 1
                    print(
                        f"[benchmark] completed {completed_runs}/{total_runs}: "
                        f"{script.simulation_id} | {condition}",
                        flush=True,
                    )
                    partial_results = {
                        "config": {
                            "conditions": conditions,
                            "repetitions": repetitions,
                            "script_ids": [item.simulation_id for item in scripts],
                            "style_slots": list(self.style_slots),
                        },
                        "runs": [result.to_dict() for result in run_results],
                        "aggregate": aggregate_benchmark_runs(run_results),
                        "aggregate_by_script": aggregate_benchmark_runs_by_script(run_results),
                        "aggregate_by_mode": aggregate_benchmark_runs_by_mode(run_results),
                        "aggregate_by_family": aggregate_benchmark_runs_by_family(run_results),
                    }
                    if checkpoint_path is not None:
                        save_benchmark_outputs(partial_results, checkpoint_path)
                        progress_payload = {
                            "completed_runs": completed_runs,
                            "total_runs": total_runs,
                            "last_script_id": script.simulation_id,
                            "last_condition": condition,
                        }
                        with open(checkpoint_path / "progress.json", "w") as handle:
                            json.dump(progress_payload, handle, indent=2)

        return {
            "config": {
                "conditions": conditions,
                "repetitions": repetitions,
                "script_ids": [script.simulation_id for script in scripts],
                "style_slots": list(self.style_slots),
            },
            "runs": [result.to_dict() for result in run_results],
            "aggregate": aggregate_benchmark_runs(run_results),
            "aggregate_by_script": aggregate_benchmark_runs_by_script(run_results),
            "aggregate_by_mode": aggregate_benchmark_runs_by_mode(run_results),
            "aggregate_by_family": aggregate_benchmark_runs_by_family(run_results),
        }


def aggregate_benchmark_runs(run_results: list[BenchmarkRunResult]) -> dict[str, Any]:
    grouped: dict[str, list[BenchmarkRunResult]] = {}
    for result in run_results:
        grouped.setdefault(result.condition, []).append(result)

    return _aggregate_grouped_runs(grouped)


def aggregate_benchmark_runs_by_script(run_results: list[BenchmarkRunResult]) -> dict[str, Any]:
    grouped: dict[str, list[BenchmarkRunResult]] = {}
    for result in run_results:
        key = f"{result.simulation_id}:{result.condition}"
        grouped.setdefault(key, []).append(result)

    return _aggregate_grouped_runs(grouped)


def aggregate_benchmark_runs_by_mode(run_results: list[BenchmarkRunResult]) -> dict[str, Any]:
    grouped: dict[str, list[BenchmarkRunResult]] = {}
    for result in run_results:
        mode = str(result.runtime_summary.get("simulation_mode", "unknown"))
        key = f"{mode}:{result.condition}"
        grouped.setdefault(key, []).append(result)
    return _aggregate_grouped_runs(grouped)


def aggregate_benchmark_runs_by_family(run_results: list[BenchmarkRunResult]) -> dict[str, Any]:
    grouped: dict[str, list[BenchmarkRunResult]] = {}
    for result in run_results:
        family = str(result.runtime_summary.get("scenario_family", "generic"))
        key = f"{family}:{result.condition}"
        grouped.setdefault(key, []).append(result)
    return _aggregate_grouped_runs(grouped)


def _aggregate_grouped_runs(grouped: dict[str, list[BenchmarkRunResult]]) -> dict[str, Any]:
    aggregate: dict[str, Any] = {}
    for group_key, rows in grouped.items():
        aggregate[group_key] = _summarize_rows(rows)
    return aggregate


def _summarize_rows(rows: list[BenchmarkRunResult]) -> dict[str, Any]:
    drift_values = [row.metrics.persona_drift_mae for row in rows]
    relation_values = [row.metrics.relationship_inconsistency for row in rows]
    commitment_values = [row.metrics.commitment_contradiction_rate for row in rows]
    envelope_values = [row.metrics.envelope_violations for row in rows]
    turn_counts = [row.runtime_summary["turn_count"] for row in rows]
    per_trait_error_mean = {
        trait: round(
            mean(row.metrics.per_trait_error_mean.get(trait, 0.0) for row in rows),
            4,
        )
        for trait in ("O", "C", "E", "A", "N")
    }
    action_validity = [row.metrics.structured_action_validity_rate for row in rows]
    owner_resolution = [row.metrics.owner_resolution_rate for row in rows]
    action_contradiction = [row.metrics.executed_action_contradiction_rate for row in rows]
    transition_coherence = [row.metrics.state_transition_coherence for row in rows]
    feedback_utilization = [row.metrics.action_feedback_utilization for row in rows]
    action_plan_alignment = [row.metrics.action_plan_alignment_mean for row in rows]
    planned_action_coverage = [row.metrics.planned_action_coverage_rate for row in rows]
    action_family_convergence = [row.metrics.action_family_convergence_rate for row in rows]
    role_action_diversity = [row.metrics.role_action_diversity_score for row in rows]
    negotiation_uniqueness = [row.metrics.negotiation_uniqueness_rate for row in rows]
    fallback_rates = [row.metrics.fallback_utterance_rate for row in rows]
    fallback_type_keys = sorted(
        {
            key
            for row in rows
            for key in (row.metrics.fallback_type_rates or {}).keys()
        }
    )
    fallback_type_rate_mean = {
        key: round(mean((row.metrics.fallback_type_rates or {}).get(key, 0.0) for row in rows), 4)
        for key in fallback_type_keys
    }
    clean_rows = [row for row in rows if row.metrics.fallback_utterance_rate < 0.30]
    contaminated_rows = [row for row in rows if row.metrics.fallback_utterance_rate >= 0.30]
    trajectory_variance = aggregate_phase_end_state_variance([row.metrics for row in rows])

    summary = {
        "num_runs": len(rows),
        "clean_run_count": len(clean_rows),
        "contaminated_run_count": len(contaminated_rows),
        "persona_drift_mae_mean": round(mean(drift_values), 4),
        "persona_drift_mae_std": round(pstdev(drift_values), 4) if len(drift_values) > 1 else 0.0,
        "relationship_inconsistency_mean": round(mean(relation_values), 4),
        "commitment_contradiction_mean": round(mean(commitment_values), 4),
        "envelope_violations_mean": round(mean(envelope_values), 4),
        "structured_action_validity_rate_mean": round(mean(action_validity), 4),
        "owner_resolution_rate_mean": round(mean(owner_resolution), 4),
        "executed_action_contradiction_rate_mean": round(mean(action_contradiction), 4),
        "state_transition_coherence_mean": round(mean(transition_coherence), 4),
        "action_feedback_utilization_mean": round(mean(feedback_utilization), 4),
        "action_plan_alignment_mean": round(mean(action_plan_alignment), 4),
        "planned_action_coverage_rate_mean": round(mean(planned_action_coverage), 4),
        "action_family_convergence_rate_mean": round(mean(action_family_convergence), 4),
        "role_action_diversity_score_mean": round(mean(role_action_diversity), 4),
        "negotiation_uniqueness_rate_mean": round(mean(negotiation_uniqueness), 4),
        "fallback_utterance_rate_mean": round(mean(fallback_rates), 4),
        "fallback_type_rate_mean": fallback_type_rate_mean,
        "state_trajectory_variance_mean": trajectory_variance,
        "per_trait_error_mean": per_trait_error_mean,
        "turn_count_mean": round(mean(turn_counts), 2),
    }
    if clean_rows:
        summary["clean_persona_drift_mae_mean"] = round(
            mean(row.metrics.persona_drift_mae for row in clean_rows),
            4,
        )
        summary["clean_envelope_violations_mean"] = round(
            mean(row.metrics.envelope_violations for row in clean_rows),
            4,
        )
        summary["clean_commitment_contradiction_mean"] = round(
            mean(row.metrics.commitment_contradiction_rate for row in clean_rows),
            4,
        )
    return summary


def run_benchmark_sync(
    gen_client,
    conditions: list[BenchmarkCondition] | None = None,
    repetitions: int = 1,
    script_ids: list[str] | None = None,
) -> dict[str, Any]:
    return asyncio.run(
        SimulationBenchmarkRunner(gen_client=gen_client).run_suite(
            conditions=conditions,
            repetitions=repetitions,
            script_ids=script_ids,
        )
    )


def _load_checkpoint_results(
    checkpoint_path: Path,
    scripts: list[Any],
    conditions: list[str],
    repetitions: int,
    style_slots: list[str],
) -> tuple[list[BenchmarkRunResult], dict[tuple[str, str], int]]:
    runs_path = checkpoint_path / "benchmark_runs.json"
    if not runs_path.exists():
        return [], {}

    try:
        payload = json.loads(runs_path.read_text())
    except json.JSONDecodeError:
        return [], {}

    expected_script_ids = [script.simulation_id for script in scripts]
    expected_config = {
        "conditions": conditions,
        "repetitions": repetitions,
        "script_ids": expected_script_ids,
        "style_slots": list(style_slots),
    }
    existing_config = payload.get("config", {})
    if existing_config != expected_config:
        print("[benchmark] checkpoint config mismatch; starting a fresh run", flush=True)
        return [], {}

    run_results: list[BenchmarkRunResult] = []
    run_counts: dict[tuple[str, str], int] = {}
    valid_script_ids = set(expected_script_ids)
    valid_conditions = set(conditions)
    for row in payload.get("runs", []):
        simulation_id = row.get("simulation_id")
        condition = row.get("condition")
        if simulation_id not in valid_script_ids or condition not in valid_conditions:
            continue
        key = (simulation_id, condition)
        if run_counts.get(key, 0) >= repetitions:
            continue
        metrics_data = row.get("metrics")
        runtime_summary = row.get("runtime_summary")
        if not isinstance(metrics_data, dict) or not isinstance(runtime_summary, dict):
            continue
        try:
            metrics = BenchmarkRunMetrics(**metrics_data)
        except TypeError:
            continue
        run_results.append(
            BenchmarkRunResult(
                condition=condition,
                simulation_id=simulation_id,
                runtime_summary=runtime_summary,
                metrics=metrics,
                selection_audits=row.get("selection_audits", []),
            )
        )
        run_counts[key] = run_counts.get(key, 0) + 1
    return run_results, run_counts
