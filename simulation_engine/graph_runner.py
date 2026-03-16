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
        self._shared_semantic_scorer = None  # lazy-init, reused across runs

    def _get_semantic_scorer(self):
        """Return a shared SemanticScorer instance (loaded once)."""
        if self._shared_semantic_scorer is None:
            try:
                from .semantic_scorer import SemanticScorer
                self._shared_semantic_scorer = SemanticScorer()
            except ImportError:
                self._shared_semantic_scorer = False  # sentinel: not available
        return self._shared_semantic_scorer if self._shared_semantic_scorer is not False else None

    async def run(self, script, condition: str) -> dict[str, Any]:
        base_condition, ablation_config = resolve_benchmark_condition(condition)
        # Pass shared semantic scorer to avoid reloading model every run
        shared_semantic_scorer = None
        if ablation_config.use_structural_adaptation:
            shared_semantic_scorer = self._get_semantic_scorer()
        initial_state = {
            "script": script,
            "gen_client": self.gen_client,
            "condition": condition,
            "base_condition": base_condition,
            "style_slots": list(self.style_slots),
            "ablation_config": ablation_config,
            "shared_semantic_scorer": shared_semantic_scorer,
        }
        final_state = await self.graph.ainvoke(
            initial_state,
            {"recursion_limit": 256},
        )
        return final_state["result"]
