"""Ablation condition parsing for stakeholder simulation benchmarks."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal


BaseBenchmarkCondition = Literal["naive", "engine", "engine_controller"]
BenchmarkCondition = Literal[
    "naive",
    "engine",
    "engine_controller",
    "naive_action_baseline",
    "engine_dialogue_only",
    "engine_action_v0",
    "engine_controller_no_trait_poles",
    "engine_controller_no_banded_target_matching",
    "engine_controller_no_extended_ledger",
    "engine_controller_no_tie_routing",
]


@dataclass(frozen=True)
class SimulationAblationConfig:
    """Runtime feature toggles for product-MVP ablation studies."""

    use_trait_expression_prior: bool = True
    use_banded_target_matching: bool = True
    use_extended_ledger_context: bool = True
    use_tie_routing: bool = True
    use_action_layer: bool = False
    use_action_aware_scoring: bool = False

    def to_dict(self) -> dict[str, bool]:
        return asdict(self)


DEFAULT_ABLATION_CONFIG = SimulationAblationConfig()

ALL_BENCHMARK_CONDITIONS: list[str] = [
    "naive",
    "engine",
    "engine_controller",
    "naive_action_baseline",
    "engine_dialogue_only",
    "engine_action_v0",
    "engine_controller_no_trait_poles",
    "engine_controller_no_banded_target_matching",
    "engine_controller_no_extended_ledger",
    "engine_controller_no_tie_routing",
]


def resolve_benchmark_condition(
    condition: str,
) -> tuple[BaseBenchmarkCondition, SimulationAblationConfig]:
    """Map a benchmark condition label to its base runtime mode and toggles."""
    mapping: dict[str, tuple[BaseBenchmarkCondition, SimulationAblationConfig]] = {
        "naive": ("naive", DEFAULT_ABLATION_CONFIG),
        "engine": ("engine", DEFAULT_ABLATION_CONFIG),
        "engine_controller": ("engine_controller", DEFAULT_ABLATION_CONFIG),
        "naive_action_baseline": (
            "naive",
            SimulationAblationConfig(use_action_layer=True),
        ),
        "engine_dialogue_only": (
            "engine_controller",
            SimulationAblationConfig(use_action_layer=True),
        ),
        "engine_action_v0": (
            "engine_controller",
            SimulationAblationConfig(use_action_layer=True, use_action_aware_scoring=True),
        ),
        "engine_controller_no_trait_poles": (
            "engine_controller",
            SimulationAblationConfig(use_trait_expression_prior=False),
        ),
        "engine_controller_no_banded_target_matching": (
            "engine_controller",
            SimulationAblationConfig(use_banded_target_matching=False),
        ),
        "engine_controller_no_extended_ledger": (
            "engine_controller",
            SimulationAblationConfig(use_extended_ledger_context=False),
        ),
        "engine_controller_no_tie_routing": (
            "engine_controller",
            SimulationAblationConfig(use_tie_routing=False),
        ),
    }
    if condition not in mapping:
        raise ValueError(f"Unknown benchmark condition: {condition}")
    return mapping[condition]
