"""Schema objects for pre-injected stakeholder simulation scripts."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from .action_layer import ACTION_TYPES, DEFAULT_LOCAL_STATE_KEYS

TRAIT_KEYS = ("O", "C", "E", "A", "N")
DEFAULT_GLOBAL_WORLD_STATE_KEYS = (
    "alignment",
    "trust",
    "uncertainty",
    "execution_confidence",
    "risk",
)
DEFAULT_STATE_VISIBILITY_RULES = {
    "global_keys": ["alignment", "uncertainty", "risk"],
    "local_keys": ["trust", "execution_confidence", "alignment"],
    "max_recent_actions": 2,
}


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
    world_state_schema: list[str] = field(default_factory=list)
    initial_world_state: dict[str, float] = field(default_factory=dict)
    allowed_action_types: list[str] = field(default_factory=list)
    transition_rules: dict[str, dict[str, Any]] = field(default_factory=dict)
    state_visibility_rules: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    evaluation_targets: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.world_state_schema:
            self.world_state_schema = list(DEFAULT_GLOBAL_WORLD_STATE_KEYS)
        else:
            self.world_state_schema = list(dict.fromkeys(self.world_state_schema))
        if not self.initial_world_state:
            self.initial_world_state = {key: 0.5 for key in self.world_state_schema}
        else:
            self.initial_world_state = {
                key: _clip_trait(self.initial_world_state.get(key, 0.5))
                for key in self.world_state_schema
            }
        if not self.allowed_action_types:
            self.allowed_action_types = []
        else:
            self.allowed_action_types = list(dict.fromkeys(self.allowed_action_types))
        if not self.state_visibility_rules:
            self.state_visibility_rules = dict(DEFAULT_STATE_VISIBILITY_RULES)
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
            world_state_schema=list(data.get("world_state_schema", [])),
            initial_world_state=dict(data.get("initial_world_state", {})),
            allowed_action_types=list(data.get("allowed_action_types", [])),
            transition_rules={
                phase_name: dict(rules)
                for phase_name, rules in dict(data.get("transition_rules", {})).items()
            },
            state_visibility_rules=dict(data.get("state_visibility_rules", {})),
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
            "world_state_schema": list(self.world_state_schema),
            "initial_world_state": dict(self.initial_world_state),
            "allowed_action_types": list(self.allowed_action_types),
            "transition_rules": dict(self.transition_rules),
            "state_visibility_rules": dict(self.state_visibility_rules),
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

    @property
    def local_state_keys(self) -> list[str]:
        return list(dict.fromkeys(self.state_visibility_rules.get("local_keys", DEFAULT_LOCAL_STATE_KEYS)))

    def transition_rule_for(self, phase_name: str, action_type: str) -> dict[str, Any]:
        return dict(self.transition_rules.get(phase_name, {}).get(action_type, {}))

    def allowed_action_types_for_phase(self, phase_name: str) -> list[str]:
        phase_rules = self.transition_rules.get(phase_name, {})
        if not phase_rules:
            return list(self.allowed_action_types)
        phase_actions = list(phase_rules.keys())
        ordered = [action for action in self.allowed_action_types if action in phase_actions]
        return ordered or phase_actions

    def target_keys_for_phase(self, phase_name: str) -> list[str]:
        phase_rules = self.transition_rules.get(phase_name, {})
        keys: list[str] = []
        for rule in phase_rules.values():
            for state_key in dict(rule.get("global_deltas", {})).keys():
                if state_key not in keys:
                    keys.append(state_key)
        return keys or list(self.world_state_schema)

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

        invalid_action_types = sorted(set(self.allowed_action_types).difference(ACTION_TYPES))
        if invalid_action_types:
            raise ValueError(
                f"SimulationScript allowed_action_types contains unknown entries: {', '.join(invalid_action_types)}"
            )

        if not set(DEFAULT_GLOBAL_WORLD_STATE_KEYS).issubset(set(self.world_state_schema)):
            raise ValueError(
                "SimulationScript world_state_schema must include all default global state keys"
            )

        for key, value in self.initial_world_state.items():
            if key not in self.world_state_schema:
                raise ValueError(f"Initial world state key {key} is not in world_state_schema")
            if not 0.0 <= float(value) <= 1.0:
                raise ValueError(f"Initial world state value for {key} must be within [0, 1]")

        for phase_name, rules in self.transition_rules.items():
            if phase_name not in {phase.name for phase in self.phases}:
                raise ValueError(f"Transition rules reference unknown phase {phase_name}")
            for action_type, rule in rules.items():
                if action_type not in self.allowed_action_types:
                    raise ValueError(
                        f"Transition rule {phase_name}:{action_type} uses an action not in allowed_action_types"
                    )
                for state_key in rule.get("global_deltas", {}):
                    if state_key not in self.world_state_schema:
                        raise ValueError(
                            f"Transition rule {phase_name}:{action_type} references unknown global state key {state_key}"
                        )
