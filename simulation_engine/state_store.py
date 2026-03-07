"""State store abstraction for future backend swaps."""

from __future__ import annotations

from typing import Protocol

from .state_ledger import SimulationStateLedger


class StateStore(Protocol):
    """Minimal protocol for the authoritative simulation state backend."""

    @property
    def ledger(self) -> SimulationStateLedger: ...


class InMemoryStateStore:
    """Current v0 backend backed by the in-process state ledger."""

    def __init__(self, ledger: SimulationStateLedger):
        self._ledger = ledger

    @property
    def ledger(self) -> SimulationStateLedger:
        return self._ledger


class GraphStateStore:
    """Reserved for a future graph-backed state backend."""

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "GraphStateStore is intentionally deferred until actor count, horizon, and query complexity require it."
        )
