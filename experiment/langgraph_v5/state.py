"""Typed state for the BCFC v5 LangGraph runtime."""

from __future__ import annotations

from typing import Any, Optional, TypedDict


class BCFCV5GraphState(TypedDict, total=False):
    """Shared mutable state across the LangGraph session runtime."""

    spec: Any
    gen_client: Any
    eval_client: Any
    quality_audit: dict[str, Any]
    session_start: float

    scenario: Any
    system_prompt: Optional[str]
    assigned_vector: Optional[dict[str, float]]

    engine: Any
    candidate: Any
    controller: Any
    memory_backend: Any

    max_candidate_turns: int
    candidate_turn_count: int
    current_nudge: Optional[str]

    phase_name: str
    phase_style: str
    phase_cues: list[str]
    target_traits: list[str]
    style_slots: list[str]

    memory_context: dict[str, Any]
    opportunity_scores: dict[str, float]
    activation_mask: dict[str, float]
    policy_plan: dict[str, Any]

    slot_candidates: list[dict[str, Any]]
    scored_candidates: list[dict[str, Any]]
    selection_audit: dict[str, Any]
    selected_candidate: dict[str, Any]
    selected_candidate_text: str
    selected_candidate_index: int

    candidate_pool_logs: list[dict[str, Any]]
    environment_action: str
    environment_turns: list[Any]
    environment_primary_speaker: Optional[str]

    stats: Any
    features: Any
    rule_based_vector: dict[str, float]

    assessment: Any
    inferred_vector: dict[str, float]
    judge_diagnostics: dict[str, Any]
    uncertain_rows: list[dict[str, Any]]

    trajectory_scores: dict[str, Any]
    pressure_metrics: dict[str, Any]
    trajectory_diagnostics: dict[str, Any]

    result: dict[str, Any]
