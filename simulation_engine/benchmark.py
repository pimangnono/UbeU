"""Benchmark harness for naive vs engine stakeholder simulation runs."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from statistics import mean, pstdev
from typing import Any

from .ablation import (
    ALL_BENCHMARK_CONDITIONS,
    BenchmarkCondition,
    resolve_benchmark_condition,
)
from .action_layer import apply_transition_rule, arbitrate_phase_actions, compile_action_proposal
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

                if base_condition == "naive":
                    text = await actor.generate_response(
                        turns=context["turns"],
                        phase_style=phase.style,
                        actor_snapshot=None,
                        phase_name=phase.name,
                        phase_cues=phase.cues,
                    )
                    selected_meta = {"mode": "naive"}
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
                    )
                    pool = await actor.generate_candidate_pool_styles(
                        turns=context["turns"],
                        phase_style=phase.style,
                        style_slots=self.style_slots,
                        actor_snapshot=context["snapshot"] if base_condition != "naive" else None,
                        phase_name=phase.name,
                        phase_cues=phase.cues,
                        policy_plan=policy_plan,
                        enable_trait_execution=(base_condition == "engine_controller"),
                    )
                    if base_condition == "engine":
                        selected = pool[0]
                        selected_meta = {
                            "mode": "engine_first_candidate",
                            "policy_plan": policy_plan,
                            "slot": selected["slot"],
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
                                "valid_target_keys": list(runtime.script.world_state_schema),
                                "allowed_action_types": list(runtime.script.allowed_action_types),
                                "global_state": dict(runtime.ledger.latest_world_state().global_state),
                                "turn_index": runtime.turn_index + 1,
                                "use_action_aware_scoring": bool(ablation_config.use_action_aware_scoring),
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
                    )
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

            if ablation_config.use_action_layer:
                approved, rejected = arbitrate_phase_actions(
                    runtime.script,
                    phase.name,
                    runtime.ledger.phase_action_proposals(phase.name),
                )
                for proposal in approved:
                    runtime.ledger.update_action_proposal_status(proposal.proposal_id, status="approved")
                for proposal in rejected:
                    runtime.ledger.update_action_proposal_status(
                        proposal.proposal_id,
                        status="rejected",
                        rejection_reason=proposal.rejection_reason,
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
                        continue
                    runtime.ledger.apply_executed_action(executed, next_snapshot)
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
        for script in scripts:
            for condition in conditions:
                for _ in range(repetitions):
                    run_results.append(await self.run_single(script, condition))

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
    trajectory_variance = aggregate_phase_end_state_variance([row.metrics for row in rows])

    return {
        "num_runs": len(rows),
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
        "state_trajectory_variance_mean": trajectory_variance,
        "per_trait_error_mean": per_trait_error_mean,
        "turn_count_mean": round(mean(turn_counts), 2),
    }


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
