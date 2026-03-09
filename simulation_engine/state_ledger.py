"""Actor-symmetric runtime state ledger for stakeholder simulations."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from experiment.memory_backend import Commitment, extract_commitments

from .action_layer import (
    ActionProposal,
    ExecutedAction,
    WorldStateSnapshot,
    action_family,
    build_phase_feedback,
    default_local_state,
)
from .script import SimulationScript


_POSITIVE_REL = (
    "good point",
    "agree",
    "you are right",
    "you're right",
    "makes sense",
    "thanks",
    "appreciate",
    "love that",
    "great idea",
    "aligned",
    "fair point",
    "valid concern",
    "see your point",
    "hear your concern",
)
_NEGATIVE_REL = (
    "disagree",
    "that is wrong",
    "that's wrong",
    "no way",
    "doesn't work",
    "problem with",
    "push back",
    "challenge that",
    "i don't think",
    "i am not sure",
    "i'm not sure",
    "won't work",
    "too risky",
    "not convinced",
)
_CHALLENGE_REL = (
    "but",
    "however",
    "still",
    "yet",
    "at the same time",
    "before we expand",
    "i need evidence",
    "i want evidence",
    "need more proof",
    "push back",
    "challenge",
)


def _clip_unit(value: float) -> float:
    return max(0.0, min(1.0, round(float(value), 4)))


@dataclass
class LedgerTurn:
    """Canonical turn record stored by the simulation runtime."""

    turn_index: int
    actor_id: str
    display_name: str
    content: str
    phase_name: str
    visible_to: list[str] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RelationshipEdge:
    """Directed relationship state from one actor to another."""

    source_actor_id: str
    target_actor_id: str
    sentiment: str = "neutral"
    trust: float = 0.5
    tension: float = 0.0
    last_turn: int = 0
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class EventExposure:
    """Record of which actors saw which world event and when."""

    event_id: str
    actor_ids: list[str]
    turn_index: int
    event_title: str = ""
    event_description: str = ""
    visibility: str = "public"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ActorDynamicState:
    """Mutable per-actor state that may change during a run."""

    actor_id: str
    beliefs: dict[str, float] = field(default_factory=dict)
    issue_salience: dict[str, float] = field(default_factory=dict)
    stress: float = 0.0
    trust_map: dict[str, float] = field(default_factory=dict)
    stance_map: dict[str, float] = field(default_factory=dict)
    open_commitments: list[str] = field(default_factory=list)
    recent_reflections: list[str] = field(default_factory=list)
    last_inferred_traits: dict[str, float] = field(default_factory=dict)
    rolling_trait_estimate: dict[str, float] = field(default_factory=dict)
    drift_score: float = 0.0
    trait_drift_map: dict[str, float] = field(default_factory=dict)
    drift_history: list[dict[str, float]] = field(default_factory=list)
    sycophancy_risk: float = 0.0
    sycophancy_signals: dict[str, int] = field(default_factory=dict)
    unfulfilled_persona_acts: dict[str, list[str]] = field(default_factory=dict)
    goals: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class SimulationStateLedger:
    """Shared multi-actor state ledger for the product runtime."""

    def __init__(self, script: SimulationScript):
        self.script = script
        self.turns: list[LedgerTurn] = []
        self.actor_states: dict[str, ActorDynamicState] = {}
        self.commitments_by_actor: dict[str, list[Commitment]] = {}
        self.relationships: dict[tuple[str, str], RelationshipEdge] = {}
        self.event_exposures: list[EventExposure] = []
        self.relationship_events: list[dict[str, Any]] = []
        self.actor_state_events: list[dict[str, Any]] = []
        self.action_proposals: list[ActionProposal] = []
        self.executed_actions: list[ExecutedAction] = []
        self.action_audits: dict[str, dict[str, Any]] = {}
        self.world_state_history: list[WorldStateSnapshot] = []
        self.phase_state_feedback: dict[str, dict[str, dict[str, Any]]] = {}

        actor_ids = script.actor_ids
        self.world_state_history.append(
            WorldStateSnapshot(
                phase_name="BOOTSTRAP",
                turn_index=0,
                global_state=dict(script.initial_world_state),
                local_state_by_actor=default_local_state(actor_ids),
                executed_action_ids=[],
            )
        )
        for actor_id in actor_ids:
            trust_map = {
                other_id: 0.5
                for other_id in actor_ids
                if other_id != actor_id
            }
            stance_map = {
                other_id: 0.0
                for other_id in actor_ids
                if other_id != actor_id
            }
            self.actor_states[actor_id] = ActorDynamicState(
                actor_id=actor_id,
                trust_map=trust_map,
                stance_map=stance_map,
                last_inferred_traits=dict(script.get_actor(actor_id).personality_prior),
                rolling_trait_estimate=dict(script.get_actor(actor_id).personality_prior),
                trait_drift_map={
                    trait: 0.0
                    for trait in script.get_actor(actor_id).personality_prior
                },
                goals=list(script.get_actor(actor_id).incentives[:2]),
            )
            self.commitments_by_actor[actor_id] = []
            for other_id in actor_ids:
                if other_id == actor_id:
                    continue
                self.relationships[(actor_id, other_id)] = RelationshipEdge(
                    source_actor_id=actor_id,
                    target_actor_id=other_id,
                )

    def append_turn(
        self,
        actor_id: str,
        content: str,
        phase_name: str,
        visible_to: Optional[list[str]] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> LedgerTurn:
        actor = self.script.get_actor(actor_id)
        turn = LedgerTurn(
            turn_index=len(self.turns) + 1,
            actor_id=actor_id,
            display_name=actor.display_name,
            content=content,
            phase_name=phase_name,
            visible_to=list(visible_to) if visible_to else None,
            metadata=dict(metadata or {}),
        )
        turn.metadata.setdefault(
            "turn_trace_id",
            f"{self.script.simulation_id}:{phase_name}:{turn.turn_index}:{actor_id}",
        )
        self.turns.append(turn)
        self.add_commitments_from_text(actor_id, content, turn.turn_index, phase_name)
        self.update_relationships_from_text(
            actor_id,
            content,
            turn.turn_index,
            turn_trace_id=str(turn.metadata.get("turn_trace_id", "")) or None,
        )
        return turn

    def add_commitments_from_text(
        self,
        actor_id: str,
        content: str,
        turn_index: int,
        phase_name: str,
    ) -> list[Commitment]:
        commitments = extract_commitments(content, turn_index, phase_name)
        if not commitments:
            return []
        self.commitments_by_actor[actor_id].extend(commitments)
        self.actor_states[actor_id].open_commitments.extend(
            commitment.commitment_id for commitment in commitments
        )
        return commitments

    def record_event_exposure(
        self,
        event_id: str,
        actor_ids: list[str],
        turn_index: int,
        visibility: str = "public",
        event_title: str = "",
        event_description: str = "",
    ) -> EventExposure:
        exposure = EventExposure(
            event_id=event_id,
            event_title=event_title,
            event_description=event_description,
            actor_ids=list(actor_ids),
            turn_index=turn_index,
            visibility=visibility,
        )
        self.event_exposures.append(exposure)
        return exposure

    def update_relationship(
        self,
        source_actor_id: str,
        target_actor_id: str,
        sentiment: str,
        trust_delta: float,
        tension_delta: float,
        turn_index: int,
        evidence: str | None = None,
        turn_trace_id: str | None = None,
        cause_type: str = "text_reference",
    ):
        edge = self.relationships[(source_actor_id, target_actor_id)]
        prior_sentiment = edge.sentiment
        prior_trust = edge.trust
        prior_tension = edge.tension
        edge.sentiment = sentiment
        edge.trust = _clip_unit(edge.trust + trust_delta)
        edge.tension = _clip_unit(edge.tension + tension_delta)
        edge.last_turn = turn_index
        if evidence:
            edge.evidence.append(evidence)
        self.relationship_events.append({
            "source_actor_id": source_actor_id,
            "target_actor_id": target_actor_id,
            "prior_sentiment": prior_sentiment,
            "new_sentiment": sentiment,
            "sentiment": sentiment,
            "prior_trust": round(prior_trust, 4),
            "new_trust": edge.trust,
            "trust": edge.trust,
            "prior_tension": round(prior_tension, 4),
            "new_tension": edge.tension,
            "tension": edge.tension,
            "trust_delta": round(trust_delta, 4),
            "tension_delta": round(tension_delta, 4),
            "turn_index": turn_index,
            "evidence": evidence or "",
            "turn_trace_id": turn_trace_id,
            "cause_type": cause_type,
        })

        actor_state = self.actor_states[source_actor_id]
        actor_state.trust_map[target_actor_id] = edge.trust
        actor_state.stance_map[target_actor_id] = round(0.5 - edge.tension, 4)

    def update_relationships_from_text(
        self,
        actor_id: str,
        content: str,
        turn_index: int,
        turn_trace_id: str | None = None,
    ) -> list[RelationshipEdge]:
        lowered = content.lower()
        updates: list[RelationshipEdge] = []
        actor_map = self.script.actor_map

        for target_actor_id, actor in actor_map.items():
            if target_actor_id == actor_id:
                continue
            name = actor.display_name.lower()
            if name not in lowered:
                continue

            positive_hit = any(token in lowered for token in _POSITIVE_REL)
            negative_hit = any(token in lowered for token in _NEGATIVE_REL)
            challenge_hit = any(token in lowered for token in _CHALLENGE_REL)

            sentiment = "neutral"
            trust_delta = 0.0
            tension_delta = 0.0
            if positive_hit and challenge_hit and not negative_hit:
                sentiment = "challenging"
                trust_delta = 0.04
                tension_delta = 0.11
            elif negative_hit and positive_hit:
                sentiment = "challenging"
                trust_delta = -0.04
                tension_delta = 0.13
            elif negative_hit:
                sentiment = "negative"
                trust_delta = -0.12
                tension_delta = 0.16
            elif challenge_hit:
                sentiment = "challenging"
                trust_delta = -0.03
                tension_delta = 0.09
            elif positive_hit:
                sentiment = "positive"
                trust_delta = 0.12
                tension_delta = -0.05
            else:
                continue

            self.update_relationship(
                source_actor_id=actor_id,
                target_actor_id=target_actor_id,
                sentiment=sentiment,
                trust_delta=trust_delta,
                tension_delta=tension_delta,
                turn_index=turn_index,
                evidence=content[:140],
                turn_trace_id=turn_trace_id,
            )
            updates.append(self.relationships[(actor_id, target_actor_id)])

        return updates

    def apply_state_delta(
        self,
        actor_id: str,
        beliefs: Optional[dict[str, float]] = None,
        issue_salience: Optional[dict[str, float]] = None,
        stress_delta: float = 0.0,
        reflection: Optional[str] = None,
        last_inferred_traits: Optional[dict[str, float]] = None,
        rolling_trait_estimate: Optional[dict[str, float]] = None,
        drift_score: Optional[float] = None,
        sycophancy_risk: Optional[float] = None,
        sycophancy_signals: Optional[dict[str, int]] = None,
        unfulfilled_persona_acts: Optional[dict[str, list[str]]] = None,
        goals: Optional[list[str]] = None,
        turn_index: Optional[int] = None,
        phase_name: Optional[str] = None,
        cause_type: str = "state_update",
    ):
        actor_state = self.actor_states[actor_id]
        prior_state = {
            "beliefs": dict(actor_state.beliefs),
            "issue_salience": dict(actor_state.issue_salience),
            "stress": actor_state.stress,
            "last_inferred_traits": dict(actor_state.last_inferred_traits),
            "rolling_trait_estimate": dict(actor_state.rolling_trait_estimate),
            "drift_score": actor_state.drift_score,
            "trait_drift_map": dict(actor_state.trait_drift_map),
            "sycophancy_risk": actor_state.sycophancy_risk,
            "unfulfilled_persona_acts": {
                key: list(value)
                for key, value in actor_state.unfulfilled_persona_acts.items()
            },
            "goals": list(actor_state.goals),
        }
        if beliefs:
            actor_state.beliefs.update(beliefs)
        if issue_salience:
            actor_state.issue_salience.update(issue_salience)
        if stress_delta:
            actor_state.stress = _clip_unit(actor_state.stress + stress_delta)
        if reflection:
            actor_state.recent_reflections.append(reflection)
            actor_state.recent_reflections = actor_state.recent_reflections[-5:]
        if last_inferred_traits:
            actor_state.last_inferred_traits = dict(last_inferred_traits)
        if rolling_trait_estimate:
            actor_state.rolling_trait_estimate = dict(rolling_trait_estimate)
        elif last_inferred_traits:
            if actor_state.rolling_trait_estimate:
                actor_state.rolling_trait_estimate = {
                    trait: _clip_unit(
                        (0.6 * actor_state.rolling_trait_estimate.get(trait, value))
                        + (0.4 * value)
                    )
                    for trait, value in last_inferred_traits.items()
                }
            else:
                actor_state.rolling_trait_estimate = dict(last_inferred_traits)
        if drift_score is not None:
            actor_state.drift_score = _clip_unit(drift_score)
        if last_inferred_traits:
            prior = self.script.get_actor(actor_id).personality_prior
            trait_drift_map = {
                trait: _clip_unit(abs(last_inferred_traits.get(trait, prior[trait]) - prior[trait]))
                for trait in prior
            }
            actor_state.trait_drift_map = trait_drift_map
            actor_state.drift_history.append(dict(trait_drift_map))
            actor_state.drift_history = actor_state.drift_history[-6:]
        if sycophancy_risk is not None:
            actor_state.sycophancy_risk = _clip_unit(
                (0.65 * actor_state.sycophancy_risk) + (0.35 * sycophancy_risk)
            )
        if sycophancy_signals:
            merged = dict(actor_state.sycophancy_signals)
            for key, value in sycophancy_signals.items():
                merged[key] = merged.get(key, 0) + int(value)
            actor_state.sycophancy_signals = merged
        if unfulfilled_persona_acts is not None:
            actor_state.unfulfilled_persona_acts = {
                key: list(value)
                for key, value in unfulfilled_persona_acts.items()
            }
        if goals is not None:
            actor_state.goals = list(goals)
        self.actor_state_events.append({
            "actor_id": actor_id,
            "turn_index": turn_index if turn_index is not None else len(self.turns),
            "phase_name": phase_name or (self.turns[-1].phase_name if self.turns else "BOOTSTRAP"),
            "cause_type": cause_type,
            "prior_state": prior_state,
            "new_state": actor_state.to_dict(),
        })

    def resolve_commitment(self, actor_id: str, commitment_id: str):
        for commitment in self.commitments_by_actor.get(actor_id, []):
            if commitment.commitment_id == commitment_id:
                commitment.status = "resolved"
                break
        actor_state = self.actor_states[actor_id]
        actor_state.open_commitments = [
            cid for cid in actor_state.open_commitments
            if cid != commitment_id
        ]

    def visible_turns_for(self, actor_id: str, max_turns: int = 8) -> list[LedgerTurn]:
        visible: list[LedgerTurn] = []
        for turn in self.turns:
            if turn.visible_to is None or actor_id in turn.visible_to:
                visible.append(turn)
        return visible[-max_turns:]

    def append_action_proposal(self, proposal: ActionProposal | None) -> ActionProposal | None:
        if proposal is None:
            return None
        self.action_proposals.append(proposal)
        return proposal

    def upsert_action_audit(self, trace_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        existing = dict(self.action_audits.get(trace_id, {}))
        existing.update(payload)
        self.action_audits[trace_id] = existing
        return existing

    def update_action_audit(self, trace_id: str, **updates: Any) -> dict[str, Any] | None:
        if trace_id not in self.action_audits:
            return None
        self.action_audits[trace_id].update(updates)
        return dict(self.action_audits[trace_id])

    def ordered_action_audits(self) -> list[dict[str, Any]]:
        return [
            audit
            for _, audit in sorted(
                self.action_audits.items(),
                key=lambda item: (
                    int(item[1].get("turn_index", 0)),
                    str(item[0]),
                ),
            )
        ]

    def update_action_proposal_status(
        self,
        proposal_id: str,
        *,
        status: str,
        rejection_reason: str | None = None,
    ) -> ActionProposal | None:
        for proposal in self.action_proposals:
            if proposal.proposal_id == proposal_id:
                proposal.status = status
                proposal.rejection_reason = rejection_reason
                return proposal
        return None

    def phase_action_proposals(self, phase_name: str) -> list[ActionProposal]:
        return [proposal for proposal in self.action_proposals if proposal.phase_name == phase_name]

    def phase_action_family_counts(
        self,
        phase_name: str,
        *,
        exclude_actor_id: str | None = None,
    ) -> dict[str, int]:
        counts: dict[str, int] = {}
        for proposal in self.phase_action_proposals(phase_name):
            if proposal.status not in {"proposed", "approved", "executed"}:
                continue
            if exclude_actor_id and proposal.actor_id == exclude_actor_id:
                continue
            family = action_family(proposal.action_type)
            counts[family] = counts.get(family, 0) + 1
        return counts

    def phase_actor_action_families(
        self,
        phase_name: str,
        *,
        exclude_actor_id: str | None = None,
    ) -> dict[str, list[str]]:
        actor_families: dict[str, list[str]] = {}
        for proposal in self.phase_action_proposals(phase_name):
            if proposal.status not in {"proposed", "approved", "executed"}:
                continue
            if exclude_actor_id and proposal.actor_id == exclude_actor_id:
                continue
            actor_families.setdefault(proposal.actor_id, [])
            family = action_family(proposal.action_type)
            if family not in actor_families[proposal.actor_id]:
                actor_families[proposal.actor_id].append(family)
        return actor_families

    def phase_actor_action_family_counts(
        self,
        phase_name: str,
        actor_id: str,
    ) -> dict[str, int]:
        counts: dict[str, int] = {}
        for proposal in self.phase_action_proposals(phase_name):
            if proposal.actor_id != actor_id:
                continue
            if proposal.status not in {"proposed", "approved", "executed"}:
                continue
            family = action_family(proposal.action_type)
            counts[family] = counts.get(family, 0) + 1
        return counts

    def apply_executed_action(
        self,
        executed_action: ExecutedAction,
        world_snapshot: WorldStateSnapshot,
    ) -> ExecutedAction:
        self.executed_actions.append(executed_action)
        self.world_state_history.append(world_snapshot)
        proposal = self.update_action_proposal_status(executed_action.proposal_id, status="executed")
        if proposal and proposal.commitment_id:
            self.resolve_commitment(proposal.actor_id, proposal.commitment_id)
        return executed_action

    def latest_world_state(self) -> WorldStateSnapshot:
        return self.world_state_history[-1]

    def latest_phase_feedback(self, actor_id: str) -> dict[str, Any]:
        if not self.phase_state_feedback:
            return {}
        last_phase_name = list(self.phase_state_feedback.keys())[-1]
        return dict(self.phase_state_feedback.get(last_phase_name, {}).get(actor_id, {}))

    def unresolved_action_proposals_for(self, actor_id: str) -> list[dict[str, Any]]:
        rows = [
            proposal.to_dict()
            for proposal in self.action_proposals
            if proposal.actor_id == actor_id and proposal.status in {"proposed", "approved"}
        ]
        return rows[-4:]

    def visible_state_summary_for(self, actor_id: str) -> dict[str, Any]:
        latest_world = self.latest_world_state()
        feedback = self.latest_phase_feedback(actor_id)
        recent_actions = [
            action.to_dict()
            for action in self.executed_actions
            if action.owner_actor_id == actor_id or action.target_actor_id == actor_id
        ][-2:]
        return {
            "global_state": dict(latest_world.global_state),
            "local_state": dict(latest_world.local_state_by_actor.get(actor_id, {})),
            "phase_feedback": feedback,
            "recent_executed_actions": recent_actions,
            "unresolved_actions": self.unresolved_action_proposals_for(actor_id),
        }

    def record_phase_feedback(
        self,
        phase_name: str,
        executed_actions: list[ExecutedAction],
        world_snapshot: WorldStateSnapshot,
    ):
        self.phase_state_feedback[phase_name] = {
            actor_id: build_phase_feedback(world_snapshot, executed_actions, actor_id)
            for actor_id in self.script.actor_ids
        }

    def get_open_commitments(self, actor_id: str) -> list[Commitment]:
        return [
            commitment
            for commitment in self.commitments_by_actor.get(actor_id, [])
            if commitment.status == "open"
        ]

    def get_relationships_for(self, actor_id: str) -> list[RelationshipEdge]:
        return [
            edge
            for (source_actor_id, _), edge in self.relationships.items()
            if source_actor_id == actor_id
        ]

    def state_trajectory_summary(self) -> str:
        """Compare last 2 WorldStateSnapshot entries and produce a 1-2 sentence delta description."""
        if len(self.world_state_history) < 2:
            return ""
        prev = self.world_state_history[-2]
        curr = self.world_state_history[-1]
        changes: list[str] = []
        for key in curr.global_state:
            prev_val = float(prev.global_state.get(key, 0.5))
            curr_val = float(curr.global_state.get(key, 0.5))
            delta = curr_val - prev_val
            if abs(delta) >= 0.03:
                direction = "rose" if delta > 0 else "fell"
                changes.append(f"{key} {direction} {abs(delta):.2f}")
        if not changes:
            return ""
        return f"Since last phase: {'; '.join(changes[:4])}."

    def trait_divergence_score(self) -> float:
        """Mean pairwise absolute difference between all actors' rolling trait estimates."""
        actor_ids = list(self.actor_states.keys())
        if len(actor_ids) < 2:
            return 0.0
        pair_diffs: list[float] = []
        for i in range(len(actor_ids)):
            for j in range(i + 1, len(actor_ids)):
                traits_i = self.actor_states[actor_ids[i]].rolling_trait_estimate
                traits_j = self.actor_states[actor_ids[j]].rolling_trait_estimate
                if traits_i and traits_j:
                    shared_traits = set(traits_i.keys()) & set(traits_j.keys())
                    if shared_traits:
                        diff = sum(
                            abs(traits_i[t] - traits_j[t]) for t in shared_traits
                        ) / len(shared_traits)
                        pair_diffs.append(diff)
        if not pair_diffs:
            return 0.0
        return round(sum(pair_diffs) / len(pair_diffs), 4)

    def snapshot_actor_context(self, actor_id: str, max_turns: int = 8) -> dict[str, Any]:
        return {
            "actor_state": self.actor_states[actor_id].to_dict(),
            "open_commitments": [asdict(item) for item in self.get_open_commitments(actor_id)],
            "relationships": [edge.to_dict() for edge in self.get_relationships_for(actor_id)],
            "visible_turns": [turn.to_dict() for turn in self.visible_turns_for(actor_id, max_turns=max_turns)],
            "recent_event_exposures": [
                exposure.to_dict()
                for exposure in self.event_exposures
                if actor_id in exposure.actor_ids
            ][-5:],
            "world_state": dict(self.latest_world_state().global_state),
            "local_state": dict(self.latest_world_state().local_state_by_actor.get(actor_id, {})),
            "phase_feedback": self.latest_phase_feedback(actor_id),
            "recent_executed_actions": [
                action.to_dict()
                for action in self.executed_actions
                if action.owner_actor_id == actor_id or action.target_actor_id == actor_id
            ][-2:],
            "unresolved_actions": self.unresolved_action_proposals_for(actor_id),
            "recent_action_audits": [
                audit
                for audit in self.ordered_action_audits()
                if audit.get("actor_id") == actor_id
            ][-2:],
        }
