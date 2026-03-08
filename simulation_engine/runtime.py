"""Minimal generalized runtime scaffold for stakeholder simulations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from .actor import StakeholderActor
from .ablation import DEFAULT_ABLATION_CONFIG, SimulationAblationConfig
from .script import SimulationPhase, SimulationScript
from .state_ledger import SimulationStateLedger
from .state_store import InMemoryStateStore


@dataclass
class RuntimeTurnView:
    """Lightweight view object compatible with the existing generator interfaces."""

    turn_number: int
    speaker_name: str
    content: str


class StakeholderSimulationRuntime:
    """
    Product-oriented runtime foundation.

    This is intentionally smaller than the current BCFC experiment runner.
    It provides the object model needed for the next refactor:
    - data-first simulation scripts
    - actor-symmetric state ledger
    - reusable stakeholder actors
    """

    def __init__(
        self,
        script: SimulationScript,
        gen_client,
        ablation_config: SimulationAblationConfig | None = None,
    ):
        self.script = script
        self.gen_client = gen_client
        self.ablation_config = ablation_config or DEFAULT_ABLATION_CONFIG
        self.state_store = InMemoryStateStore(SimulationStateLedger(script))
        self.ledger = self.state_store.ledger
        self.actors = {
            actor.actor_id: StakeholderActor(
                client=gen_client,
                actor_spec=actor,
                world_brief=script.brief,
                ablation_config=self.ablation_config,
            )
            for actor in script.stakeholders
        }
        self.phase_index = 0
        self.turn_index = 0
        self._last_actor_id: Optional[str] = None

    @classmethod
    def from_dict(
        cls,
        script_data: dict[str, Any],
        gen_client,
        ablation_config: SimulationAblationConfig | None = None,
    ) -> "StakeholderSimulationRuntime":
        return cls(
            script=SimulationScript.from_dict(script_data),
            gen_client=gen_client,
            ablation_config=ablation_config,
        )

    @property
    def current_phase(self) -> SimulationPhase:
        return self.script.phases[min(self.phase_index, len(self.script.phases) - 1)]

    def bootstrap_state(self) -> dict[str, Any]:
        return {
            "simulation_id": self.script.simulation_id,
            "phase_name": self.current_phase.name,
            "actor_order": list(self.actors.keys()),
            "world_events": [event.to_dict() for event in self.script.world_events],
        }

    def select_next_actor_round_robin(self) -> str:
        actor_order = self.current_phase.target_actor_ids or list(self.actors.keys())
        if not actor_order:
            raise ValueError("Simulation runtime has no actors to schedule")

        if self._last_actor_id not in actor_order:
            next_actor_id = actor_order[0]
        else:
            current_index = actor_order.index(self._last_actor_id)
            next_actor_id = actor_order[(current_index + 1) % len(actor_order)]

        self._last_actor_id = next_actor_id
        return next_actor_id

    def visible_turns_for_actor(self, actor_id: str, max_turns: int = 8) -> list[RuntimeTurnView]:
        return [
            RuntimeTurnView(
                turn_number=turn.turn_index,
                speaker_name=turn.display_name,
                content=turn.content,
            )
            for turn in self.ledger.visible_turns_for(actor_id, max_turns=max_turns)
        ]

    def actor_context(self, actor_id: str, max_turns: int = 8) -> dict[str, Any]:
        return {
            "phase": self.current_phase.to_dict(),
            "turns": self.visible_turns_for_actor(actor_id, max_turns=max_turns),
            "snapshot": self.ledger.snapshot_actor_context(actor_id, max_turns=max_turns),
        }

    def append_actor_turn(
        self,
        actor_id: str,
        content: str,
        visible_to: Optional[list[str]] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        turn = self.ledger.append_turn(
            actor_id=actor_id,
            content=content,
            phase_name=self.current_phase.name,
            visible_to=visible_to,
            metadata=metadata,
        )
        self.turn_index = turn.turn_index
        return turn

    def record_world_event(
        self,
        event_id: str,
        actor_ids: Optional[list[str]] = None,
        visibility: str = "public",
    ):
        actor_ids = actor_ids or list(self.actors.keys())
        event = next(
            (item for item in self.script.world_events if item.event_id == event_id),
            None,
        )
        return self.ledger.record_event_exposure(
            event_id=event_id,
            event_title=event.title if event else "",
            event_description=event.description if event else "",
            actor_ids=actor_ids,
            turn_index=max(self.turn_index, 1),
            visibility=visibility,
        )

    def advance_phase(self):
        if self.phase_index < len(self.script.phases) - 1:
            self.phase_index += 1

    def to_runtime_summary(self) -> dict[str, Any]:
        latest_world = self.ledger.latest_world_state()
        action_status_counts: dict[str, int] = {}
        action_rejection_reason_counts: dict[str, int] = {}
        for proposal in self.ledger.action_proposals:
            action_status_counts[proposal.status] = action_status_counts.get(proposal.status, 0) + 1
            if proposal.rejection_reason:
                action_rejection_reason_counts[proposal.rejection_reason] = (
                    action_rejection_reason_counts.get(proposal.rejection_reason, 0) + 1
                )
        return {
            "simulation_id": self.script.simulation_id,
            "title": self.script.title,
            "objective": self.script.objective,
            "scenario_family": self.script.scenario_family,
            "simulation_mode": self.script.simulation_mode,
            "outcome_spec": dict(self.script.outcome_spec),
            "phase_name": self.current_phase.name,
            "turn_count": len(self.ledger.turns),
            "actor_ids": list(self.actors.keys()),
            "actor_labels": dict(self.script.actor_analysis_label_map),
            "actor_display_names": dict(self.script.actor_display_name_map),
            "action_proposal_count": len(self.ledger.action_proposals),
            "executed_action_count": len(self.ledger.executed_actions),
            "phase_count": len(self.script.phases),
            "latest_world_state": dict(latest_world.global_state),
            "action_status_counts": action_status_counts,
            "action_rejection_reason_counts": action_rejection_reason_counts,
            "action_proposals": [proposal.to_dict() for proposal in self.ledger.action_proposals],
            "executed_actions": [action.to_dict() for action in self.ledger.executed_actions],
            "action_audits": self.ledger.ordered_action_audits(),
            "world_state_history": [snapshot.to_dict() for snapshot in self.ledger.world_state_history],
            "phase_state_feedback": dict(self.ledger.phase_state_feedback),
        }
