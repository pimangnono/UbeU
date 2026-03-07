"""Foundations for the product-oriented stakeholder simulation engine."""

from .ablation import ALL_BENCHMARK_CONDITIONS, SimulationAblationConfig, resolve_benchmark_condition
from .action_layer import (
    ACTION_TYPES,
    ActionProposal,
    ExecutedAction,
    TransitionRule,
    WorldStateSnapshot,
    apply_transition_rule,
    arbitrate_phase_actions,
    compile_action_proposal,
)
from .actor import StakeholderActor
from .benchmark import SimulationBenchmarkRunner, aggregate_benchmark_runs, run_benchmark_sync
from .controller import PersonaStateController
from .graph_runner import StakeholderSimulationGraphRunner
from .graphs import build_stakeholder_simulation_graph
from .manual_scripts import load_mvp_policy_script_map, load_mvp_policy_scripts
from .metrics import BenchmarkRunMetrics, compute_runtime_metrics, estimate_actor_traits_from_turns
from .reporting import build_benchmark_report, save_benchmark_outputs
from .runtime import StakeholderSimulationRuntime
from .script import (
    SimulationPhase,
    SimulationScript,
    StakeholderActorSpec,
    WorldEvent,
    default_personality_envelope,
    normalize_personality_vector,
)
from .state_ledger import (
    ActorDynamicState,
    EventExposure,
    LedgerTurn,
    RelationshipEdge,
    SimulationStateLedger,
)
from .state_store import GraphStateStore, InMemoryStateStore, StateStore

__all__ = [
    "ActorDynamicState",
    "ALL_BENCHMARK_CONDITIONS",
    "ACTION_TYPES",
    "EventExposure",
    "LedgerTurn",
    "ActionProposal",
    "BenchmarkRunMetrics",
    "build_benchmark_report",
    "build_stakeholder_simulation_graph",
    "compile_action_proposal",
    "apply_transition_rule",
    "arbitrate_phase_actions",
    "ExecutedAction",
    "WorldStateSnapshot",
    "TransitionRule",
    "PersonaStateController",
    "RelationshipEdge",
    "SimulationPhase",
    "SimulationBenchmarkRunner",
    "SimulationAblationConfig",
    "SimulationScript",
    "SimulationStateLedger",
    "StakeholderSimulationGraphRunner",
    "StakeholderActor",
    "StakeholderActorSpec",
    "StakeholderSimulationRuntime",
    "StateStore",
    "InMemoryStateStore",
    "GraphStateStore",
    "WorldEvent",
    "aggregate_benchmark_runs",
    "compute_runtime_metrics",
    "default_personality_envelope",
    "estimate_actor_traits_from_turns",
    "load_mvp_policy_script_map",
    "load_mvp_policy_scripts",
    "normalize_personality_vector",
    "run_benchmark_sync",
    "resolve_benchmark_condition",
    "save_benchmark_outputs",
]
