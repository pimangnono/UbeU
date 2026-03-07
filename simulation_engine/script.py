"""Schema objects for pre-injected stakeholder simulation scripts."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


TRAIT_KEYS = ("O", "C", "E", "A", "N")


def _clip_trait(value: float) -> float:
    return max(0.0, min(1.0, round(float(value), 4)))


def normalize_personality_vector(vector: dict[str, float] | None) -> dict[str, float]:
    """Return a complete OCEAN vector with clipped values."""
    vector = vector or {}
    return {
        trait: _clip_trait(vector.get(trait, 0.5))
        for trait in TRAIT_KEYS
    }


def default_personality_envelope(
    prior: dict[str, float],
    radius: float = 0.18,
) -> dict[str, tuple[float, float]]:
    """Build a bounded envelope around the actor's personality prior."""
    prior = normalize_personality_vector(prior)
    return {
        trait: (_clip_trait(value - radius), _clip_trait(value + radius))
        for trait, value in prior.items()
    }


@dataclass
class StakeholderActorSpec:
    """A first-class stakeholder definition for a simulation script."""

    actor_id: str
    display_name: str
    role: str
    identity_core: dict[str, Any] = field(default_factory=dict)
    personality_prior: dict[str, float] = field(default_factory=dict)
    personality_envelope: dict[str, tuple[float, float]] = field(default_factory=dict)
    incentives: list[str] = field(default_factory=list)
    concerns: list[str] = field(default_factory=list)
    communication_style: dict[str, Any] = field(default_factory=dict)
    experience_summary: str = ""
    salient_memories: list[str] = field(default_factory=list)
    private_context: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self.personality_prior = normalize_personality_vector(self.personality_prior)
        if not self.personality_envelope:
            self.personality_envelope = default_personality_envelope(self.personality_prior)
        else:
            self.personality_envelope = {
                trait: tuple(bounds)
                for trait, bounds in self.personality_envelope.items()
            }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StakeholderActorSpec":
        return cls(
            actor_id=data["actor_id"],
            display_name=data["display_name"],
            role=data["role"],
            identity_core=dict(data.get("identity_core", {})),
            personality_prior=dict(data.get("personality_prior", {})),
            personality_envelope=dict(data.get("personality_envelope", {})),
            incentives=list(data.get("incentives", [])),
            concerns=list(data.get("concerns", [])),
            communication_style=dict(data.get("communication_style", {})),
            experience_summary=data.get("experience_summary", ""),
            salient_memories=list(data.get("salient_memories", [])),
            private_context=dict(data.get("private_context", {})),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def analysis_label(self) -> str:
        """Return the role-first label used in reports and benchmark outputs."""
        return self.role


@dataclass
class SimulationPhase:
    """One phase in a policy or stakeholder simulation."""

    name: str
    goal: str
    style: str = "neutral"
    max_turns: int = 4
    cues: list[str] = field(default_factory=list)
    target_actor_ids: list[str] = field(default_factory=list)
    visibility: str = "public"
    description: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SimulationPhase":
        return cls(
            name=data["name"],
            goal=data.get("goal", ""),
            style=data.get("style", "neutral"),
            max_turns=int(data.get("max_turns", 4)),
            cues=list(data.get("cues", [])),
            target_actor_ids=list(data.get("target_actor_ids", [])),
            visibility=data.get("visibility", "public"),
            description=data.get("description", ""),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class WorldEvent:
    """An exogenous event or signal injected into the simulation."""

    event_id: str
    title: str
    description: str
    trigger_phase: str | None = None
    trigger_turn: int | None = None
    visibility: str = "public"
    affected_actor_ids: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "WorldEvent":
        return cls(
            event_id=data["event_id"],
            title=data["title"],
            description=data["description"],
            trigger_phase=data.get("trigger_phase"),
            trigger_turn=data.get("trigger_turn"),
            visibility=data.get("visibility", "public"),
            affected_actor_ids=list(data.get("affected_actor_ids", [])),
            metadata=dict(data.get("metadata", {})),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SimulationScript:
    """Serializable input contract for a stakeholder simulation run."""

    simulation_id: str
    title: str
    objective: str
    brief: str
    stakeholders: list[StakeholderActorSpec]
    phases: list[SimulationPhase]
    world_events: list[WorldEvent] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    evaluation_targets: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.validate()

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SimulationScript":
        return cls(
            simulation_id=data["simulation_id"],
            title=data["title"],
            objective=data["objective"],
            brief=data.get("brief", ""),
            stakeholders=[
                StakeholderActorSpec.from_dict(actor)
                for actor in data.get("stakeholders", [])
            ],
            phases=[
                SimulationPhase.from_dict(phase)
                for phase in data.get("phases", [])
            ],
            world_events=[
                WorldEvent.from_dict(event)
                for event in data.get("world_events", [])
            ],
            metadata=dict(data.get("metadata", {})),
            evaluation_targets=list(data.get("evaluation_targets", [])),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "simulation_id": self.simulation_id,
            "title": self.title,
            "objective": self.objective,
            "brief": self.brief,
            "stakeholders": [actor.to_dict() for actor in self.stakeholders],
            "phases": [phase.to_dict() for phase in self.phases],
            "world_events": [event.to_dict() for event in self.world_events],
            "metadata": dict(self.metadata),
            "evaluation_targets": list(self.evaluation_targets),
        }

    @property
    def actor_ids(self) -> list[str]:
        return [actor.actor_id for actor in self.stakeholders]

    @property
    def actor_map(self) -> dict[str, StakeholderActorSpec]:
        return {actor.actor_id: actor for actor in self.stakeholders}

    def get_actor(self, actor_id: str) -> StakeholderActorSpec:
        try:
            return self.actor_map[actor_id]
        except KeyError as exc:
            raise KeyError(f"Unknown actor_id: {actor_id}") from exc

    @property
    def actor_role_map(self) -> dict[str, str]:
        return {actor.actor_id: actor.role for actor in self.stakeholders}

    @property
    def actor_display_name_map(self) -> dict[str, str]:
        return {actor.actor_id: actor.display_name for actor in self.stakeholders}

    @property
    def actor_analysis_label_map(self) -> dict[str, str]:
        return {actor.actor_id: actor.analysis_label for actor in self.stakeholders}

    def validate(self):
        if not self.stakeholders:
            raise ValueError("SimulationScript requires at least one stakeholder")
        if not self.phases:
            raise ValueError("SimulationScript requires at least one phase")

        actor_ids = self.actor_ids
        if len(actor_ids) != len(set(actor_ids)):
            raise ValueError("Stakeholder actor_id values must be unique")

        for phase in self.phases:
            for actor_id in phase.target_actor_ids:
                if actor_id not in actor_ids:
                    raise ValueError(f"Phase {phase.name} references unknown actor_id {actor_id}")

        for event in self.world_events:
            for actor_id in event.affected_actor_ids:
                if actor_id not in actor_ids:
                    raise ValueError(
                        f"World event {event.event_id} references unknown actor_id {actor_id}"
                    )
