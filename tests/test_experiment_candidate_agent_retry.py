import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import asyncio

from experiment.candidate_agent import ExperimentCandidateAgent
from utils.models import Turn


class _FlakyClient:
    def __init__(self, failures_before_success: int, error_text: str):
        self.failures_before_success = failures_before_success
        self.error_text = error_text
        self.calls = 0

    async def generate(self, **kwargs):
        self.calls += 1
        if self.calls <= self.failures_before_success:
            raise RuntimeError(self.error_text)
        return 'Candidate: "We should run a pilot first."'


class _TimeoutThenSuccessClient:
    def __init__(self, timeouts_before_success: int):
        self.timeouts_before_success = timeouts_before_success
        self.calls = 0

    async def generate(self, **kwargs):
        self.calls += 1
        if self.calls <= self.timeouts_before_success:
            await asyncio.sleep(0.05)
            return "late response"
        return 'Candidate: "We should run a pilot first."'


class _ConcurrentProbeClient:
    def __init__(self, delay_seconds: float = 0.02):
        self.delay_seconds = delay_seconds
        self.active_calls = 0
        self.max_active_calls = 0
        self.calls = 0

    async def generate(self, **kwargs):
        self.calls += 1
        self.active_calls += 1
        self.max_active_calls = max(self.max_active_calls, self.active_calls)
        try:
            await asyncio.sleep(self.delay_seconds)
            return 'Candidate: "We should run a pilot first."'
        finally:
            self.active_calls -= 1


class _AlwaysFailClient:
    def __init__(self, error_text: str):
        self.error_text = error_text
        self.calls = 0

    async def generate(self, **kwargs):
        self.calls += 1
        raise RuntimeError(self.error_text)


def _sample_turns() -> list[Turn]:
    return [
        Turn(turn_number=1, speaker_name="Alex", speaker_role="Ops", content="We need a launch plan.")
    ]


def test_generate_response_retries_on_transient_connection_errors():
    client = _FlakyClient(failures_before_success=2, error_text="Connection error.")
    agent = ExperimentCandidateAgent(client=client, candidate_name="Candidate")
    agent._response_retry_base_delay = 0.0
    agent._response_retry_max_delay = 0.0

    response = asyncio.run(
        agent.generate_response(
            turns=_sample_turns(),
            scenario_brief="Test scenario",
            phase_style="neutral",
        )
    )

    assert response == "We should run a pilot first."
    assert client.calls == 3


def test_generate_response_skips_retry_for_non_transient_errors():
    client = _FlakyClient(failures_before_success=10, error_text="Invalid request payload.")
    agent = ExperimentCandidateAgent(client=client, candidate_name="Candidate")
    agent._response_retry_base_delay = 0.0
    agent._response_retry_max_delay = 0.0

    response = asyncio.run(
        agent.generate_response(
            turns=_sample_turns(),
            scenario_brief="Test scenario",
            phase_style="neutral",
        )
    )

    assert response == "I think we should consider all the options before deciding."
    assert client.calls == 1


def test_generate_response_retries_on_timeout_then_succeeds():
    client = _TimeoutThenSuccessClient(timeouts_before_success=2)
    agent = ExperimentCandidateAgent(client=client, candidate_name="Candidate")
    agent._response_retry_base_delay = 0.0
    agent._response_retry_max_delay = 0.0
    agent._response_request_timeout_seconds = 0.01

    response = asyncio.run(
        agent.generate_response(
            turns=_sample_turns(),
            scenario_brief="Test scenario",
            phase_style="neutral",
        )
    )

    assert response == "We should run a pilot first."
    assert client.calls == 3


def test_generate_response_payload_records_timeout_fallback_type():
    client = _AlwaysFailClient("timeout while waiting for upstream")
    agent = ExperimentCandidateAgent(client=client, candidate_name="Candidate")
    agent._response_retry_attempts = 1
    agent._response_retry_base_delay = 0.0
    agent._response_retry_max_delay = 0.0

    payload = asyncio.run(
        agent.generate_response_payload(
            turns=_sample_turns(),
            scenario_brief="Test scenario",
            phase_style="neutral",
        )
    )

    assert payload.text == "I think we should consider all the options before deciding."
    assert payload.generation_meta["used_fallback"] is True
    assert payload.generation_meta["fallback_type"] == "timeout_fallback"


def test_generate_candidate_pool_styles_keeps_non_fallback_candidates():
    client = _FlakyClient(failures_before_success=1, error_text="Connection error.")
    agent = ExperimentCandidateAgent(client=client, candidate_name="Candidate")
    agent._response_retry_attempts = 1
    agent._response_retry_base_delay = 0.0
    agent._response_retry_max_delay = 0.0

    async def _run():
        return await agent.generate_candidate_pool_styles(
            turns=_sample_turns(),
            scenario_brief="Test scenario",
            phase_style="neutral",
            style_slots=["planner", "skeptic"],
            policy_plan={"stance": "synthesize"},
        )

    pool = asyncio.run(_run())

    assert len(pool) == 1
    assert pool[0]["generation_meta"]["used_fallback"] is False


def test_generate_candidate_pool_styles_collapses_all_fallbacks_into_empty_pool_marker():
    client = _AlwaysFailClient("Connection error.")
    agent = ExperimentCandidateAgent(client=client, candidate_name="Candidate")
    agent._response_retry_attempts = 1
    agent._response_retry_base_delay = 0.0
    agent._response_retry_max_delay = 0.0

    async def _run():
        return await agent.generate_candidate_pool_styles(
            turns=_sample_turns(),
            scenario_brief="Test scenario",
            phase_style="neutral",
            style_slots=["planner", "skeptic"],
            policy_plan={"stance": "synthesize"},
        )

    pool = asyncio.run(_run())

    assert len(pool) == 1
    assert pool[0]["generation_meta"]["used_fallback"] is True
    assert pool[0]["generation_meta"]["fallback_type"] == "empty_pool_fallback"


def test_generate_candidate_pool_respects_max_concurrency_cap():
    client = _ConcurrentProbeClient()
    agent = ExperimentCandidateAgent(client=client, candidate_name="Candidate")
    agent._pool_max_concurrency = 2

    responses = asyncio.run(
        agent.generate_candidate_pool(
            turns=_sample_turns(),
            scenario_brief="Test scenario",
            phase_style="neutral",
            n=6,
        )
    )

    assert len(responses) == 6
    assert all(item == "We should run a pilot first." for item in responses)
    assert client.calls == 6
    assert client.max_active_calls <= 2
