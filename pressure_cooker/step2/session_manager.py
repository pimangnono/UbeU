"""
Session Manager: manages concurrent LiveSession objects and persistence.

Each LiveSession wraps a LiveEngine with participant metadata and timing.
State is saved to disk after every turn exchange for reconnection support.
"""

import json
import threading
from pathlib import Path
from typing import Optional, TYPE_CHECKING

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.scenarios import get_scenario
from step2.live_engine import LiveEngine
from step2.models import SessionState

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient


class LiveSession:
    """Wraps a LiveEngine with participant metadata."""

    def __init__(
        self,
        engine: LiveEngine,
        participant_id: str,
    ):
        self.engine = engine
        self.participant_id = participant_id

    @property
    def session_id(self) -> str:
        return self.engine.session_id

    @property
    def state(self) -> SessionState:
        return self.engine.state


class SessionManager:
    """
    Manages concurrent live interview sessions.

    - In-memory dict of session_id -> LiveSession
    - Persists state after every turn exchange
    - Supports session reconnection via participant ID
    """

    def __init__(
        self,
        client: "GeminiClient | MockGeminiClient",
        persist_dir: Optional[str] = None,
    ):
        self.client = client
        self._sessions: dict[str, LiveSession] = {}
        self._pid_to_sid: dict[str, str] = {}  # participant_id -> session_id
        self._lock = threading.Lock()
        self._persist_dir = Path(persist_dir) if persist_dir else Path("outputs/step2/sessions")
        self._persist_dir.mkdir(parents=True, exist_ok=True)

    def create_session(
        self,
        participant_id: str,
        scenario_id: str,
        participant_name: str,
    ) -> LiveSession:
        """
        Create a new live interview session.

        Args:
            participant_id: ID of the participant.
            scenario_id: ID of the scenario to use.
            participant_name: Participant's display name.

        Returns:
            The created LiveSession.
        """
        scenario = get_scenario(scenario_id)

        engine = LiveEngine(
            client=self.client,
            scenario=scenario,
            participant_name=participant_name,
        )

        session = LiveSession(engine=engine, participant_id=participant_id)

        with self._lock:
            self._sessions[session.session_id] = session
            self._pid_to_sid[participant_id] = session.session_id

        return session

    def get_session(self, session_id: str) -> Optional[LiveSession]:
        """Get a session by session ID."""
        return self._sessions.get(session_id)

    def get_session_by_participant(self, participant_id: str) -> Optional[LiveSession]:
        """Get a session by participant ID."""
        sid = self._pid_to_sid.get(participant_id)
        if sid:
            return self._sessions.get(sid)
        return None

    def persist_session(self, session_id: str) -> None:
        """Save session state to disk for reconnection."""
        session = self._sessions.get(session_id)
        if session is None:
            return

        state = {
            "participant_id": session.participant_id,
            "engine_state": session.engine.to_state_dict(),
        }

        path = self._persist_dir / f"{session_id}.json"
        with open(path, "w") as f:
            json.dump(state, f, indent=2, default=str)

    def restore_session(self, session_id: str) -> Optional[LiveSession]:
        """
        Restore a session from disk.

        Returns:
            The restored LiveSession, or None if not found.
        """
        path = self._persist_dir / f"{session_id}.json"
        if not path.exists():
            return None

        with open(path) as f:
            state = json.load(f)

        engine_state = state["engine_state"]
        scenario = get_scenario(engine_state["scenario_id"])

        engine = LiveEngine(
            client=self.client,
            scenario=scenario,
            participant_name=engine_state["participant_name"],
        )
        engine.session_id = engine_state["session_id"]
        engine.restore_from_state(engine_state)

        session = LiveSession(
            engine=engine,
            participant_id=state["participant_id"],
        )

        with self._lock:
            self._sessions[session.session_id] = session
            self._pid_to_sid[session.participant_id] = session.session_id

        return session

    def list_active_sessions(self) -> list[str]:
        """List session IDs of active sessions."""
        return [
            sid for sid, s in self._sessions.items()
            if s.state not in (SessionState.ENDED,)
        ]

    def remove_session(self, session_id: str) -> None:
        """Remove a session from memory (keeps disk state)."""
        with self._lock:
            session = self._sessions.pop(session_id, None)
            if session:
                self._pid_to_sid.pop(session.participant_id, None)
