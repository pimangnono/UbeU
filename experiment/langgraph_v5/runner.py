"""Runners for the BCFC v5 LangGraph runtime."""

from __future__ import annotations

from typing import Any

from experiment.batch_runner import BatchRunner

from .graphs import build_bcfc_v5_session_graph


class LangGraphV5SessionRunner:
    """Run a single BCFC v5 session through the LangGraph runtime."""

    def __init__(self, gen_client, eval_client, quality_audit: dict[str, Any]):
        self.gen_client = gen_client
        self.eval_client = eval_client
        self.quality_audit = quality_audit
        self.graph = build_bcfc_v5_session_graph()

    async def run_session(self, spec) -> tuple[dict[str, Any], list[dict[str, Any]]]:
        initial_state = {
            "spec": spec,
            "gen_client": self.gen_client,
            "eval_client": self.eval_client,
            "quality_audit": self.quality_audit,
        }
        final_state = await self.graph.ainvoke(initial_state)
        return final_state["result"], final_state.get("uncertain_rows", [])


class LangGraphBatchRunner(BatchRunner):
    """Batch runner that routes LangGraph-enabled interventions to the graph runtime."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._langgraph_v5_runner = LangGraphV5SessionRunner(
            gen_client=self.gen_client,
            eval_client=self.eval_client,
            quality_audit=self._quality_audit,
        )

    async def _run_single_session(self, spec) -> dict[str, Any]:
        if spec.intervention == "bcfc_v5_langgraph":
            result, uncertain_rows = await self._langgraph_v5_runner.run_session(spec)
            if uncertain_rows:
                self.uncertain_rows.extend(uncertain_rows)
            return result
        return await super()._run_single_session(spec)
