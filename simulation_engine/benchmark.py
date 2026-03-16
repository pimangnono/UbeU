"""Benchmark harness for naive vs engine stakeholder simulation runs."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
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
    action_family,
    action_plan_alignment_score,
    apply_transition_rule,
    arbitrate_phase_actions,
    compile_action_proposal,
    normalize_planned_action_artifact,
)
from .controller import PersonaStateController
from .graph_runner import StakeholderSimulationGraphRunner
from .manual_scripts import load_mvp_policy_scripts
from .script import SimulationScript
from .metrics import (
    BenchmarkRunMetrics,
    aggregate_phase_end_state_variance,
    compute_runtime_metrics,
    estimate_actor_traits_from_turns,
    persona_drift_mae,
)
from .runtime import RuntimeTurnView, StakeholderSimulationRuntime
from .reporting import atomic_write_json, save_benchmark_outputs

DEFAULT_STYLE_SLOTS = ["integrator", "planner", "challenger", "skeptic"]


@dataclass
class BenchmarkRunResult:
    condition: str
    simulation_id: str
    runtime_summary: dict[str, Any]
    metrics: BenchmarkRunMetrics
    selection_audits: list[dict[str, Any]]
    suite_id: str = ""
    track_id: str = ""
    run_id: str = ""
    repetition_index: int = 0
    trace_bundle_path: str = ""
    builder_trace_ref: str = ""
    script_id: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "condition": self.condition,
            "simulation_id": self.simulation_id,
            "script_id": self.script_id,
            "runtime_summary": self.runtime_summary,
            "metrics": self.metrics.to_dict(),
            "selection_audits": self.selection_audits,
            "suite_id": self.suite_id,
            "track_id": self.track_id,
            "run_id": self.run_id,
            "repetition_index": self.repetition_index,
            "trace_bundle_path": self.trace_bundle_path,
            "builder_trace_ref": self.builder_trace_ref,
        }


def _suite_id_for_config(config: dict[str, Any]) -> str:
    canonical = json.dumps(
        {
            "conditions": list(config.get("conditions", [])),
            "repetitions": int(config.get("repetitions", 1)),
            "script_ids": list(config.get("script_ids", [])),
            "style_slots": list(config.get("style_slots", [])),
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    digest = hashlib.sha1(canonical.encode("utf-8")).hexdigest()[:12]
    return f"suite_{digest}"


def _decorate_run_identity(
    result: BenchmarkRunResult,
    *,
    suite_id: str,
    repetition_index: int,
) -> BenchmarkRunResult:
    track_id = str(result.runtime_summary.get("simulation_mode", "unknown"))
    run_id = f"{suite_id}:{track_id}:{result.simulation_id}:{result.condition}:{repetition_index}"
    builder_trace_ref = str(
        dict(result.runtime_summary.get("builder_trace", {})).get("builder_trace_id")
        or f"manual:{result.simulation_id}"
    )
    result.suite_id = suite_id
    result.track_id = track_id
    result.run_id = run_id
    result.repetition_index = repetition_index
    result.builder_trace_ref = builder_trace_ref
    result.runtime_summary["suite_id"] = suite_id
    result.runtime_summary["track_id"] = track_id
    result.runtime_summary["run_id"] = run_id
    result.runtime_summary["repetition_index"] = repetition_index
    result.runtime_summary["builder_trace_ref"] = builder_trace_ref
    return result


def _serialize_run_result(result: BenchmarkRunResult) -> dict[str, Any]:
    payload = dict(result.to_dict())
    suite_id = str(getattr(result, "suite_id", "") or "")
    track_id = str(getattr(result, "track_id", "") or "")
    run_id = str(getattr(result, "run_id", "") or "")
    repetition_index = int(getattr(result, "repetition_index", 0) or 0)
    trace_bundle_path = str(getattr(result, "trace_bundle_path", "") or "")
    builder_trace_ref = str(getattr(result, "builder_trace_ref", "") or "")
    script_id = str(getattr(result, "script_id", "") or result.simulation_id)
    payload["suite_id"] = suite_id
    payload["track_id"] = track_id
    payload["run_id"] = run_id
    payload["repetition_index"] = repetition_index
    payload["trace_bundle_path"] = trace_bundle_path
    payload["builder_trace_ref"] = builder_trace_ref
    payload["script_id"] = script_id
    runtime_summary = dict(payload.get("runtime_summary", {}))
    runtime_summary["suite_id"] = suite_id
    runtime_summary["track_id"] = track_id
    runtime_summary["run_id"] = run_id
    runtime_summary["repetition_index"] = repetition_index
    runtime_summary["builder_trace_ref"] = builder_trace_ref
    payload["runtime_summary"] = runtime_summary
    return payload


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
                script_id=graph_result.get("script_id", graph_result["simulation_id"]),
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
                elif base_condition == "naive_informed":
                    # Generate 4 candidates (same as engine) but select by
                    # drift-only scoring — no controller intelligence.
                    pool = await actor.generate_candidate_pool_styles(
                        turns=context["turns"],
                        phase_style=phase.style,
                        style_slots=runtime.script.style_slots_for_phase(phase.name, self.style_slots),
                        actor_snapshot=None,
                        phase_name=phase.name,
                        phase_cues=phase.cues,
                    )
                    if not pool:
                        # Fallback: generate a single naive response
                        response_payload = await actor.generate_response_payload(
                            turns=context["turns"],
                            phase_style=phase.style,
                            actor_snapshot=None,
                            phase_name=phase.name,
                            phase_cues=phase.cues,
                        )
                        text = response_payload["text"]
                        selected_meta = {
                            "mode": "naive_informed",
                            "pool_size": 0,
                            "selected_drift": 0.0,
                            "generation_meta": dict(response_payload.get("generation_meta", {})),
                            "used_fallback": True,
                        }
                    else:
                        best_candidate = pool[0]
                        best_drift = float("inf")
                        candidate_landscape = []
                        for candidate in pool:
                            preview_turns = list(context["turns"]) + [
                                RuntimeTurnView(
                                    turn_number=len(context["turns"]),
                                    speaker_name=actor.display_name,
                                    content=candidate["text"],
                                )
                            ]
                            inferred = estimate_actor_traits_from_turns(preview_turns, actor.display_name)
                            drift = persona_drift_mae(actor.actor_spec.personality_prior, inferred)
                            candidate_landscape.append({
                                "slot": candidate.get("slot"),
                                "drift": drift,
                                "inferred_traits": inferred,
                            })
                            if drift < best_drift:
                                best_drift = drift
                                best_candidate = candidate
                        text = best_candidate["text"]
                        selected_meta = {
                            "mode": "naive_informed",
                            "pool_size": len(pool),
                            "selected_drift": best_drift,
                            "candidate_landscape": candidate_landscape,
                            "slot": best_candidate.get("slot"),
                            "generation_meta": dict(best_candidate.get("generation_meta", {})),
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
                    candidate_kwargs = {
                        "turns": context["turns"],
                        "phase_style": phase.style,
                        "style_slots": runtime.script.style_slots_for_phase(phase.name, self.style_slots),
                        "actor_snapshot": context["snapshot"] if base_condition != "naive" else None,
                        "phase_name": phase.name,
                        "phase_cues": phase.cues,
                        "policy_plan": policy_plan,
                        "enable_trait_execution": (base_condition == "engine_controller"),
                        "max_concurrency_override": runtime.script.pool_max_concurrency_for_phase(
                            phase.name,
                            default=2,
                        ),
                    }
                    try:
                        pool = await actor.generate_candidate_pool_styles(**candidate_kwargs)
                    except TypeError as exc:
                        if "max_concurrency_override" not in str(exc):
                            raise
                        candidate_kwargs.pop("max_concurrency_override", None)
                        pool = await actor.generate_candidate_pool_styles(**candidate_kwargs)
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
                            "current_actor_phase_family_counts": runtime.ledger.phase_actor_action_family_counts(
                                phase.name,
                                actor_id,
                            ),
                            "phase_action_family_counts_for_guardrail": runtime.ledger.phase_action_audit_family_counts(
                                phase.name,
                                exclude_actor_id=actor_id,
                            ),
                            "current_actor_phase_family_counts_for_guardrail": runtime.ledger.phase_actor_action_audit_family_counts(
                                phase.name,
                                actor_id,
                            ),
                            "turn_index": runtime.turn_index + 1,
                            "use_action_aware_scoring": bool(
                                ablation_config.use_action_aware_scoring
                                and phase_action_policy.get("action_mode", "execute") == "execute"
                            ),
                            "use_dialogue_family_guardrail": bool(
                                ablation_config.use_action_layer and not ablation_config.use_action_aware_scoring
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
                            turn_index=runtime.turn_index + 1,
                            phase_name=phase.name,
                            cause_type="candidate_selection",
                        )

                runtime.append_actor_turn(
                    actor_id=actor_id,
                    content=text,
                    metadata=selected_meta,
                )
                turn_trace_id = str(runtime.ledger.turns[-1].metadata.get("turn_trace_id", ""))
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
                            "turn_trace_id": turn_trace_id,
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
                            "planned_action_family": action_family(
                                (selected_meta.get("planned_action_artifact") or {}).get("action_type")
                            ),
                            "selected_action_family": action_family(
                                (selected_meta.get("action_hint") or {}).get("action_type")
                            ),
                            "compiled_action_family": action_family(
                                (proposal.to_dict() if proposal else {}).get("action_type")
                            ),
                            "phase_action_family_counts_before_compile": runtime.ledger.phase_action_family_counts(
                                phase.name,
                                exclude_actor_id=actor_id,
                            ),
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
                        turn_index=runtime.turn_index,
                        phase_name=phase.name,
                        cause_type="post_turn_metric",
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
            script_id=script.simulation_id,
        )

    async def run_suite(
        self,
        conditions: list[BenchmarkCondition] | None = None,
        repetitions: int = 1,
        script_ids: list[str] | None = None,
        checkpoint_dir: str | None = None,
        scripts: list[SimulationScript] | None = None,
    ) -> dict[str, Any]:
        conditions = conditions or ["naive", "engine", "engine_controller"]
        invalid = sorted(set(conditions).difference(ALL_BENCHMARK_CONDITIONS))
        if invalid:
            raise ValueError(f"Unknown benchmark conditions: {', '.join(invalid)}")
        if scripts is None:
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
        config = {
            "conditions": conditions,
            "repetitions": repetitions,
            "script_ids": [script.simulation_id for script in scripts],
            "style_slots": list(self.style_slots),
        }
        suite_id = _suite_id_for_config(config)
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
            counter: dict[tuple[str, str], int] = {}
            decorated_runs: list[BenchmarkRunResult] = []
            for row in run_results:
                key = (row.simulation_id, row.condition)
                counter[key] = counter.get(key, 0) + 1
                decorated_runs.append(
                    _decorate_run_identity(row, suite_id=suite_id, repetition_index=counter[key])
                )
            run_results = decorated_runs
            completed_runs = len(run_results)
            if completed_runs:
                print(
                    f"[benchmark] resumed from checkpoint: {completed_runs}/{total_runs} runs already completed",
                    flush=True,
                )
                atomic_write_json(
                    checkpoint_path / "progress.json",
                    {
                        "completed_runs": completed_runs,
                        "total_runs": total_runs,
                        "last_script_id": run_results[-1].simulation_id,
                        "last_condition": run_results[-1].condition,
                    },
                    indent=2,
                )

        # How many runs were loaded from the old checkpoint (0 if fast resume)
        _prior_checkpoint_runs = len(run_results)
        _new_runs_since_merge = 0
        _FULL_MERGE_INTERVAL = 30  # full save every N new runs

        for script in scripts:
            for condition in conditions:
                already_done = existing_run_counts.get((script.simulation_id, condition), 0)
                for rep_idx in range(repetitions):
                    if rep_idx < already_done:
                        continue
                    run_result = await self.run_single(script, condition)
                    run_result = _decorate_run_identity(
                        run_result,
                        suite_id=suite_id,
                        repetition_index=rep_idx + 1,
                    )
                    run_results.append(run_result)
                    completed_runs += 1
                    _new_runs_since_merge += 1
                    print(
                        f"[benchmark] completed {completed_runs}/{total_runs}: "
                        f"{script.simulation_id} | {condition}",
                        flush=True,
                    )
                    if checkpoint_path is not None:
                        # Always: fast append to delta JSONL + update progress
                        _append_run_to_delta(checkpoint_path, run_result)
                        atomic_write_json(
                            checkpoint_path / "progress.json",
                            {
                                "completed_runs": completed_runs,
                                "total_runs": total_runs,
                                "last_script_id": script.simulation_id,
                                "last_condition": condition,
                            },
                            indent=2,
                        )
                        # Periodic full merge: every N runs, merge old+delta
                        if _new_runs_since_merge >= _FULL_MERGE_INTERVAL:
                            _do_full_checkpoint_merge(
                                checkpoint_path, run_results, config,
                                suite_id, _prior_checkpoint_runs,
                            )
                            _new_runs_since_merge = 0

        # Final full merge at end
        if checkpoint_path is not None and _new_runs_since_merge > 0:
            _do_full_checkpoint_merge(
                checkpoint_path, run_results, config,
                suite_id, _prior_checkpoint_runs,
            )

        # If fast-resumed, run_results only has new runs. Load complete
        # data from the just-saved merged file for the return value.
        if _prior_checkpoint_runs == 0 and checkpoint_path is not None:
            merged_path = checkpoint_path / "benchmark_runs.json"
            if merged_path.exists():
                try:
                    full_payload = json.loads(merged_path.read_text())
                    return {
                        "config": full_payload.get("config", {**config, "suite_id": suite_id}),
                        "suite_id": suite_id,
                        "runs": full_payload.get("runs", []),
                        "aggregate": full_payload.get("aggregate", {}),
                        "aggregate_by_script": full_payload.get("aggregate_by_script", {}),
                        "aggregate_by_mode": full_payload.get("aggregate_by_mode", {}),
                        "aggregate_by_family": full_payload.get("aggregate_by_family", {}),
                    }
                except (json.JSONDecodeError, OSError):
                    pass  # fall through to return new-only results

        return {
            "config": {**config, "suite_id": suite_id},
            "suite_id": suite_id,
            "runs": [_serialize_run_result(result) for result in run_results],
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
    relation_shift_values = [row.metrics.relationship_shift_rate for row in rows]
    relation_overshoot_values = [row.metrics.relationship_overshoot_rate for row in rows]
    commitment_values = [row.metrics.commitment_contradiction_rate for row in rows]
    envelope_values = [row.metrics.envelope_violations for row in rows]
    turn_counts = [row.runtime_summary.get("turn_count", 0) for row in rows]
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
    dialogue_coherence = [row.metrics.dialogue_coherence_score for row in rows]
    repetition = [row.metrics.repetition_rate for row in rows]
    topic_drift = [row.metrics.topic_drift_rate for row in rows]
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
    # Aggregate phase_quality across runs
    phase_quality_agg: dict[str, dict[str, list[float]]] = {}
    phase_feature_agg: dict[str, dict[str, list[float]]] = {}
    for row in rows:
        pq = row.metrics.phase_quality or {}
        for phase_name, quality in pq.items():
            if phase_name not in phase_quality_agg:
                phase_quality_agg[phase_name] = {"drift": [], "convergence": [], "diversity": []}
            for metric_key in ("drift", "convergence", "diversity"):
                phase_quality_agg[phase_name][metric_key].append(quality.get(metric_key, 0.0))
            # Aggregate per-phase mean features
            mean_feats = quality.get("mean_features", {})
            if mean_feats:
                if phase_name not in phase_feature_agg:
                    phase_feature_agg[phase_name] = {}
                for feat, val in mean_feats.items():
                    phase_feature_agg[phase_name].setdefault(feat, []).append(float(val))
    phase_quality_mean: dict[str, dict[str, float]] = {}
    for phase_name, metrics_lists in phase_quality_agg.items():
        phase_quality_mean[phase_name] = {
            k: round(mean(v), 4) if v else 0.0
            for k, v in metrics_lists.items()
        }
        # Include aggregated mean features per phase
        if phase_name in phase_feature_agg:
            phase_quality_mean[phase_name]["mean_features"] = {
                feat: round(mean(vals), 4)
                for feat, vals in sorted(phase_feature_agg[phase_name].items())
            }

    trajectory_variance = aggregate_phase_end_state_variance([row.metrics for row in rows])
    zero_variance_metrics = [
        name
        for name, values in {
            "persona_drift_mae": drift_values,
            "relationship_inconsistency": relation_values,
            "relationship_shift_rate": relation_shift_values,
            "relationship_overshoot_rate": relation_overshoot_values,
            "commitment_contradiction": commitment_values,
            "envelope_violations": envelope_values,
            "action_family_convergence": action_family_convergence,
            "role_action_diversity": role_action_diversity,
            "negotiation_uniqueness": negotiation_uniqueness,
            "fallback_utterance_rate": fallback_rates,
            "dialogue_coherence_score": dialogue_coherence,
            "repetition_rate": repetition,
            "topic_drift_rate": topic_drift,
        }.items()
        if len(values) > 1 and pstdev(values) == 0.0
    ]

    def _mean_ci(values: list[float]) -> list[float]:
        if not values:
            return [0.0, 0.0]
        mean_value = mean(values)
        if len(values) == 1:
            return [round(mean_value, 4), round(mean_value, 4)]
        spread = pstdev(values)
        margin = 1.96 * (spread / (len(values) ** 0.5))
        return [round(mean_value - margin, 4), round(mean_value + margin, 4)]

    summary = {
        "num_runs": len(rows),
        "clean_run_count": len(clean_rows),
        "contaminated_run_count": len(contaminated_rows),
        "persona_drift_mae_mean": round(mean(drift_values), 4),
        "persona_drift_mae_std": round(pstdev(drift_values), 4) if len(drift_values) > 1 else 0.0,
        "relationship_inconsistency_mean": round(mean(relation_values), 4),
        "relationship_shift_rate_mean": round(mean(relation_shift_values), 4),
        "relationship_overshoot_rate_mean": round(mean(relation_overshoot_values), 4),
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
        "dialogue_coherence_score_mean": round(mean(dialogue_coherence), 4),
        "repetition_rate_mean": round(mean(repetition), 4),
        "topic_drift_rate_mean": round(mean(topic_drift), 4),
        "phase_quality_mean": phase_quality_mean,
        "fallback_type_rate_mean": fallback_type_rate_mean,
        "semantic_identity_consistency_mean": round(mean(row.metrics.semantic_identity_consistency for row in rows), 4),
        "commitment_fulfillment_rate_mean": round(mean(row.metrics.commitment_fulfillment_rate for row in rows), 4),
        "state_trajectory_variance_mean": trajectory_variance,
        "per_trait_error_mean": per_trait_error_mean,
        "turn_count_mean": round(mean(turn_counts), 2),
        "ci_95": {
            "persona_drift_mae": _mean_ci(drift_values),
            "relationship_inconsistency": _mean_ci(relation_values),
            "relationship_shift_rate": _mean_ci(relation_shift_values),
            "relationship_overshoot_rate": _mean_ci(relation_overshoot_values),
            "commitment_contradiction": _mean_ci(commitment_values),
            "envelope_violations": _mean_ci([float(value) for value in envelope_values]),
            "dialogue_coherence_score": _mean_ci(dialogue_coherence),
            "repetition_rate": _mean_ci(repetition),
            "topic_drift_rate": _mean_ci(topic_drift),
        },
        "ci_width": {
            "persona_drift_mae": round(_mean_ci(drift_values)[1] - _mean_ci(drift_values)[0], 4),
            "relationship_inconsistency": round(_mean_ci(relation_values)[1] - _mean_ci(relation_values)[0], 4),
            "relationship_shift_rate": round(_mean_ci(relation_shift_values)[1] - _mean_ci(relation_shift_values)[0], 4),
            "relationship_overshoot_rate": round(_mean_ci(relation_overshoot_values)[1] - _mean_ci(relation_overshoot_values)[0], 4),
            "commitment_contradiction": round(_mean_ci(commitment_values)[1] - _mean_ci(commitment_values)[0], 4),
            "envelope_violations": round(_mean_ci([float(value) for value in envelope_values])[1] - _mean_ci([float(value) for value in envelope_values])[0], 4),
            "dialogue_coherence_score": round(_mean_ci(dialogue_coherence)[1] - _mean_ci(dialogue_coherence)[0], 4),
            "repetition_rate": round(_mean_ci(repetition)[1] - _mean_ci(repetition)[0], 4),
            "topic_drift_rate": round(_mean_ci(topic_drift)[1] - _mean_ci(topic_drift)[0], 4),
        },
        "metric_confidence": {
            "persona_drift_mae": "high",
            "relationship_inconsistency": "medium",
            "relationship_shift_rate": "medium",
            "relationship_overshoot_rate": "medium",
            "commitment_contradiction": "medium",
            "envelope_violations": "medium",
        },
        "zero_variance_metrics": zero_variance_metrics,
        "evidence_refs": [row.run_id for row in rows],
        "top_driver_refs": [row.run_id for row in rows[: min(3, len(rows))]],
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

    # Aggregate feature breakdowns: mean raw features across all actors/runs
    feature_totals: dict[str, list[float]] = {}
    for row in rows:
        if not row.metrics.actor_feature_breakdowns:
            continue
        for actor_id, breakdown in row.metrics.actor_feature_breakdowns.items():
            for feat, val in (breakdown.get("raw_features") or {}).items():
                feature_totals.setdefault(feat, []).append(float(val))
    if feature_totals:
        summary["mean_raw_features"] = {
            feat: round(mean(vals), 4) for feat, vals in sorted(feature_totals.items())
        }

    # Aggregate per-archetype trait errors
    archetype_errors: dict[str, list[dict[str, float]]] = {}
    for row in rows:
        labels = row.metrics.actor_labels
        errors = row.metrics.actor_trait_errors
        for actor_id, label in labels.items():
            error_map = errors.get(actor_id, {})
            if error_map:
                archetype_errors.setdefault(label, []).append(error_map)
    if archetype_errors:
        archetype_summary: dict[str, dict[str, float]] = {}
        for label, error_list in sorted(archetype_errors.items()):
            trait_means = {}
            for trait in ("O", "C", "E", "A", "N"):
                vals = [e.get(trait, 0.0) for e in error_list]
                trait_means[trait] = round(mean(vals), 4) if vals else 0.0
            trait_means["mae"] = round(mean(trait_means.values()), 4)
            trait_means["n"] = len(error_list)
            archetype_summary[label] = trait_means
        summary["per_archetype_trait_error"] = archetype_summary

    # Aggregate influence attribution stats
    dp_counts = []
    concentrations = []
    for row in rows:
        ia = row.metrics.influence_attribution
        if not ia:
            continue
        dp_counts.append(ia.get("summary", {}).get("total_decision_points", 0))
        concentrations.append(ia.get("summary", {}).get("mean_influence_concentration", 0.0))
    if dp_counts:
        summary["influence_attribution_summary"] = {
            "mean_decision_points_per_run": round(mean(dp_counts), 2),
            "mean_influence_concentration": round(mean(concentrations), 3) if concentrations else 0.0,
        }

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


def _deserialize_run_lightweight(row: dict) -> "BenchmarkRunResult":
    """Reconstruct BenchmarkRunResult from serialized dict (metrics only, skip heavy data)."""
    metrics_data = row.get("metrics", {})
    if not isinstance(metrics_data, dict):
        metrics_data = {}
    metrics = BenchmarkRunMetrics(**metrics_data)
    sim_id = row.get("simulation_id", "")
    return BenchmarkRunResult(
        condition=row.get("condition", ""),
        simulation_id=sim_id,
        runtime_summary={},
        metrics=metrics,
        selection_audits=[],
        suite_id=str(row.get("suite_id") or ""),
        track_id=str(row.get("track_id") or ""),
        run_id=str(row.get("run_id") or ""),
        repetition_index=int(row.get("repetition_index") or 0),
        trace_bundle_path=str(row.get("trace_bundle_path") or ""),
        builder_trace_ref=str(row.get("builder_trace_ref") or ""),
        script_id=str(row.get("script_id") or sim_id),
    )


def _do_full_checkpoint_merge(
    checkpoint_path: Path,
    run_results: list["BenchmarkRunResult"],
    config: dict,
    suite_id: str,
    prior_checkpoint_runs: int,
) -> None:
    """Merge old checkpoint data + new in-memory runs → full save.

    If prior_checkpoint_runs == 0 (fast resume), run_results only has new runs.
    We load old runs from benchmark_runs.json, combine, and compute correct aggregates.
    """
    if prior_checkpoint_runs == 0 and (checkpoint_path / "benchmark_runs.json").exists():
        # Fast-resumed: old data is on disk, new runs are in run_results
        try:
            old_payload = json.loads((checkpoint_path / "benchmark_runs.json").read_text())
            old_serialized = old_payload.get("runs", [])
        except (json.JSONDecodeError, OSError):
            old_serialized = []
        all_serialized = old_serialized + [_serialize_run_result(r) for r in run_results]
        # Reconstruct lightweight BenchmarkRunResult objects for aggregation
        old_results = []
        for row in old_serialized:
            try:
                old_results.append(_deserialize_run_lightweight(row))
            except (TypeError, KeyError):
                continue
        all_results_for_agg = old_results + list(run_results)
    else:
        # All data is in memory (fresh run or slow-path resume)
        all_serialized = [_serialize_run_result(r) for r in run_results]
        all_results_for_agg = list(run_results)

    full_results = {
        "config": {**config, "suite_id": suite_id},
        "suite_id": suite_id,
        "runs": all_serialized,
        "aggregate": aggregate_benchmark_runs(all_results_for_agg),
        "aggregate_by_script": aggregate_benchmark_runs_by_script(all_results_for_agg),
        "aggregate_by_mode": aggregate_benchmark_runs_by_mode(all_results_for_agg),
        "aggregate_by_family": aggregate_benchmark_runs_by_family(all_results_for_agg),
    }
    save_benchmark_outputs(full_results, checkpoint_path)

    # Clear delta JSONL after successful merge
    delta_path = checkpoint_path / "benchmark_runs_delta.jsonl"
    if delta_path.exists():
        delta_path.unlink()


def _reconstruct_run_counts_from_progress(
    checkpoint_path: Path,
    scripts: list[Any],
    conditions: list[str],
    repetitions: int,
) -> dict[tuple[str, str], int] | None:
    """Reconstruct which runs are done from progress.json + deterministic ordering.

    Since runs execute in strict order (scripts × conditions × reps), we can
    reconstruct the full skip map from just the completed_runs count.
    Returns None if progress.json is missing or invalid.
    """
    progress_path = checkpoint_path / "progress.json"
    if not progress_path.exists():
        return None
    try:
        progress = json.loads(progress_path.read_text())
    except (json.JSONDecodeError, OSError):
        return None

    completed = progress.get("completed_runs", 0)
    if completed <= 0:
        return None

    run_counts: dict[tuple[str, str], int] = {}
    count = 0
    for script in scripts:
        for condition in conditions:
            key = (script.simulation_id, condition)
            for _rep in range(repetitions):
                if count >= completed:
                    return run_counts
                run_counts[key] = run_counts.get(key, 0) + 1
                count += 1
    return run_counts


def _append_run_to_delta(checkpoint_path: Path, run_result: "BenchmarkRunResult") -> None:
    """Append a single run result to the delta JSONL file (fast, append-only)."""
    delta_path = checkpoint_path / "benchmark_runs_delta.jsonl"
    row = json.dumps(_serialize_run_result(run_result), default=str, separators=(",", ":"))
    with open(delta_path, "a") as f:
        f.write(row + "\n")
        f.flush()
        os.fsync(f.fileno())


def _merge_old_and_delta(checkpoint_path: Path) -> list[dict]:
    """Merge runs from old benchmark_runs.json + delta JSONL into one list."""
    old_runs: list[dict] = []
    runs_path = checkpoint_path / "benchmark_runs.json"
    if runs_path.exists():
        try:
            payload = json.loads(runs_path.read_text())
            old_runs = payload.get("runs", [])
        except (json.JSONDecodeError, OSError):
            pass

    delta_path = checkpoint_path / "benchmark_runs_delta.jsonl"
    if delta_path.exists():
        try:
            for line in delta_path.read_text().splitlines():
                line = line.strip()
                if line:
                    old_runs.append(json.loads(line))
        except (json.JSONDecodeError, OSError):
            pass

    return old_runs


def _load_checkpoint_results(
    checkpoint_path: Path,
    scripts: list[Any],
    conditions: list[str],
    repetitions: int,
    style_slots: list[str],
) -> tuple[list[BenchmarkRunResult], dict[tuple[str, str], int]]:
    # ── Fast path: reconstruct skip counts from progress.json ──────────
    fast_counts = _reconstruct_run_counts_from_progress(
        checkpoint_path, scripts, conditions, repetitions
    )
    if fast_counts is not None:
        completed = sum(fast_counts.values())
        print(
            f"[benchmark] fast resume: reconstructed {completed} completed run counts from progress.json",
            flush=True,
        )
        return [], fast_counts

    # ── Slow fallback: load full benchmark_runs.json ───────────────────
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
    existing_config = {
        "conditions": list(dict(payload.get("config", {})).get("conditions", [])),
        "repetitions": int(dict(payload.get("config", {})).get("repetitions", 0)),
        "script_ids": list(dict(payload.get("config", {})).get("script_ids", [])),
        "style_slots": list(dict(payload.get("config", {})).get("style_slots", [])),
    }
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
                suite_id=str(row.get("suite_id") or ""),
                track_id=str(row.get("track_id") or ""),
                run_id=str(row.get("run_id") or ""),
                repetition_index=int(row.get("repetition_index") or 0),
                trace_bundle_path=str(row.get("trace_bundle_path") or ""),
                builder_trace_ref=str(row.get("builder_trace_ref") or ""),
                script_id=str(row.get("script_id") or simulation_id),
            )
        )
        run_counts[key] = run_counts.get(key, 0) + 1
    return run_results, run_counts
