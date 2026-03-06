import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiment.batch_runner import SessionSpec
from experiment.langgraph_v5 import LangGraphBatchRunner, build_bcfc_v5_session_graph
from experiment.run_experiment import _build_bcfc_v5_mini_sessions


class _DummyClient:
    def reset_usage(self):
        return None

    def get_usage(self):
        return {}


def test_build_bcfc_v5_langgraph_sessions():
    sessions = _build_bcfc_v5_mini_sessions(
        condition="mini_v5_langgraph",
        intervention="bcfc_v5_langgraph",
        session_prefix="bcfc_v5_langgraph",
    )

    assert len(sessions) == 12
    assert all(session.condition == "mini_v5_langgraph" for session in sessions)
    assert all(session.intervention == "bcfc_v5_langgraph" for session in sessions)
    assert all(session.session_key.startswith("bcfc_v5_langgraph_") for session in sessions)


def test_langgraph_session_graph_compiles():
    graph = build_bcfc_v5_session_graph()
    assert graph is not None
    assert hasattr(graph, "ainvoke")


def test_langgraph_batch_runner_routes_langgraph_sessions(monkeypatch, tmp_path):
    async def _fake_run_session(self, spec):
        return {"session_key": spec.session_key, "stats": {"candidate_turns": 3}}, [{"trait": "O"}]

    monkeypatch.setattr(
        "experiment.langgraph_v5.runner.LangGraphV5SessionRunner.run_session",
        _fake_run_session,
    )

    runner = LangGraphBatchRunner(
        gen_client=_DummyClient(),
        eval_client=_DummyClient(),
        output_dir=str(tmp_path),
        shuffle=False,
    )

    spec = SessionSpec(
        session_key="bcfc_v5_langgraph_anxious_perfectionist_strategy_pivot_r1",
        condition="mini_v5_langgraph",
        profile_id="anxious_perfectionist",
        scenario_id="strategy_pivot",
        rep=1,
        intervention="bcfc_v5_langgraph",
    )

    result = asyncio.run(runner._run_single_session(spec))

    assert result["session_key"] == spec.session_key
    assert runner.uncertain_rows == [{"trait": "O"}]
