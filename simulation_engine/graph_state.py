"""Typed state for the stakeholder simulation LangGraph runtime."""

from __future__ import annotations

from typing import Any, Optional, TypedDict


class StakeholderGraphState(TypedDict, total=False):
    script: Any
    gen_client: Any
    condition: str
    base_condition: str
    style_slots: list[str]
    ablation_config: Any

    runtime: Any
    controllers: dict[str, Any]
    actor_name_map: dict[str, str]

    phase_turn_index: int
    last_turn_index: int
    simulation_complete: bool
    injected_events: list[str]

    active_actor_id: str
    active_actor_name: str
    actor_context: dict[str, Any]
    drift_nudge: Optional[str]

    policy_plan: dict[str, Any]
    planned_action_artifact: dict[str, Any] | None
    candidate_pool: list[dict[str, Any]]
    scored_candidates: list[dict[str, Any]]
    selected_candidate: dict[str, Any]
    selected_candidate_text: str
    selected_meta: dict[str, Any]
    selected_action_proposal: dict[str, Any] | None
    selected_action_audit: dict[str, Any] | None
    approved_phase_actions: list[dict[str, Any]]
    rejected_phase_actions: list[dict[str, Any]]
    executed_phase_actions: list[dict[str, Any]]
    phase_feedback: dict[str, Any]
    phase_boundary_reached: bool

    result: dict[str, Any]
