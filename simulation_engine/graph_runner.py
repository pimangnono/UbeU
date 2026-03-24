"""Runner for the stakeholder simulation LangGraph runtime."""

from __future__ import annotations

from typing import Any, Callable, Awaitable, Optional

from .ablation import resolve_benchmark_condition
from .graphs import build_stakeholder_simulation_graph

# Callback type: called with (event_data, phase_name)
StreamCallback = Callable[[dict[str, Any], str], Awaitable[None]]


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

    def _build_initial_state(self, script, condition: str) -> dict[str, Any]:
        base_condition, ablation_config = resolve_benchmark_condition(condition)
        shared_semantic_scorer = None
        if ablation_config.use_structural_adaptation:
            shared_semantic_scorer = self._get_semantic_scorer()
        return {
            "script": script,
            "gen_client": self.gen_client,
            "condition": condition,
            "base_condition": base_condition,
            "style_slots": list(self.style_slots),
            "ablation_config": ablation_config,
            "shared_semantic_scorer": shared_semantic_scorer,
        }

    async def run(self, script, condition: str) -> dict[str, Any]:
        initial_state = self._build_initial_state(script, condition)
        final_state = await self.graph.ainvoke(
            initial_state,
            {"recursion_limit": 256},
        )
        return final_state["result"]

    async def run_streaming(
        self,
        script,
        condition: str,
        on_event: Optional[StreamCallback] = None,
    ) -> dict[str, Any]:
        """Run simulation with real-time event callbacks via astream."""
        initial_state = self._build_initial_state(script, condition)
        last_turn_count = 0
        last_rel_count = 0
        last_phase = ""
        result = None

        async for state_chunk in self.graph.astream(
            initial_state,
            {"recursion_limit": 256},
            stream_mode="values",
        ):
            runtime = state_chunk.get("runtime")
            if runtime and on_event:
                turns = runtime.ledger.turns
                rel_events = runtime.ledger.relationship_events

                # Emit newly committed turns
                while last_turn_count < len(turns):
                    turn = turns[last_turn_count]
                    phase = turn.phase_name
                    display_name = turn.display_name or turn.actor_id
                    if phase != last_phase:
                        await on_event({"_type": "phase_change", "from": last_phase, "to": phase}, phase)
                        last_phase = phase
                    await on_event({
                        "_type": "turn",
                        "actor_id": turn.actor_id,
                        "display_name": display_name,
                        "content": turn.content,
                        "turn_index": turn.turn_index,
                        "phase": phase,
                    }, phase)
                    last_turn_count += 1

                # Emit newly created relationship events
                while last_rel_count < len(rel_events):
                    rev = rel_events[last_rel_count]
                    await on_event({
                        "_type": "relationship",
                        "source": rev.get("source_actor_id", ""),
                        "target": rev.get("target_actor_id", ""),
                        "sentiment": rev.get("sentiment", "neutral"),
                        "trust_delta": rev.get("trust_delta", 0),
                        "tension_delta": rev.get("tension_delta", 0),
                        "evidence": rev.get("evidence", ""),
                        "turn_index": rev.get("turn_index", 0),
                    }, last_phase)
                    last_rel_count += 1

            if "result" in state_chunk and state_chunk["result"]:
                result = state_chunk["result"]

        return result
