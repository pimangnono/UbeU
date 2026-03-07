"""Actor-symmetric runtime state ledger for stakeholder simulations."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from experiment.memory_backend import Commitment, extract_commitments

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

        actor_ids = script.actor_ids
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
        self.turns.append(turn)
        self.add_commitments_from_text(actor_id, content, turn.turn_index, phase_name)
        self.update_relationships_from_text(actor_id, content, turn.turn_index)
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
    ):
        edge = self.relationships[(source_actor_id, target_actor_id)]
        edge.sentiment = sentiment
        edge.trust = _clip_unit(edge.trust + trust_delta)
        edge.tension = _clip_unit(edge.tension + tension_delta)
        edge.last_turn = turn_index
        if evidence:
            edge.evidence.append(evidence)
        self.relationship_events.append({
            "source_actor_id": source_actor_id,
            "target_actor_id": target_actor_id,
            "sentiment": sentiment,
            "trust": edge.trust,
            "tension": edge.tension,
            "trust_delta": round(trust_delta, 4),
            "tension_delta": round(tension_delta, 4),
            "turn_index": turn_index,
            "evidence": evidence or "",
        })

        actor_state = self.actor_states[source_actor_id]
        actor_state.trust_map[target_actor_id] = edge.trust
        actor_state.stance_map[target_actor_id] = round(0.5 - edge.tension, 4)

    def update_relationships_from_text(
        self,
        actor_id: str,
        content: str,
        turn_index: int,
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
    ):
        actor_state = self.actor_states[actor_id]
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
        }
