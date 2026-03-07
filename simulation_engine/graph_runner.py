"""Runner for the stakeholder simulation LangGraph runtime."""

from __future__ import annotations

from typing import Any

from .ablation import resolve_benchmark_condition
from .graphs import build_stakeholder_simulation_graph


class StakeholderSimulationGraphRunner:
    """Run a single stakeholder simulation through the product-oriented graph runtime."""

    def __init__(self, gen_client, style_slots: list[str]):
        self.gen_client = gen_client
        self.style_slots = list(style_slots)
        self.graph = build_stakeholder_simulation_graph()

    async def run(self, script, condition: str) -> dict[str, Any]:
        base_condition, ablation_config = resolve_benchmark_condition(condition)
        initial_state = {
            "script": script,
            "gen_client": self.gen_client,
            "condition": condition,
            "base_condition": base_condition,
            "style_slots": list(self.style_slots),
            "ablation_config": ablation_config,
        }
        final_state = await self.graph.ainvoke(
            initial_state,
            {"recursion_limit": 256},
        )
        return final_state["result"]
