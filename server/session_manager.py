"""
Session Manager: Manages concurrent interview sessions for both modes.

Handles:
- CaseEngine sessions (Mode 1)
- GroupEngine sessions (Mode 2)
- Session persistence for reconnection
"""

import json
import threading
from pathlib import Path
from typing import Optional, Union, TYPE_CHECKING

from engines.case_engine import CaseEngine
from engines.group_engine import GroupEngine
from utils.models import InterviewMode, SessionState
from config.case_studies import create_case_study
from config.group_scenarios import create_scenario

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


class Session:
    """Wraps an engine with participant metadata."""

    def __init__(
        self,
        engine: Union[CaseEngine, GroupEngine],
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

    @property
    def mode(self) -> InterviewMode:
        return self.engine.mode


class SessionManager:
    """
    Manages concurrent interview sessions for both modes.

    - In-memory dict of session_id -> Session
    - Supports Mode 1 (CaseEngine) and Mode 2 (GroupEngine)
    - Persists state after every turn
    - Supports session reconnection
    """

    def __init__(
        self,
        client: "LLMClient",
        persist_dir: Optional[str] = None,
    ):
        self.client = client
        self._sessions: dict[str, Session] = {}
        self._pid_to_sid: dict[str, dict[str, str]] = {}  # pid -> {mode: sid}
        self._lock = threading.Lock()
        self._persist_dir = Path(persist_dir) if persist_dir else Path("outputs/sessions")
        self._persist_dir.mkdir(parents=True, exist_ok=True)

    def create_case_session(
        self,
        participant_id: str,
        participant_name: str,
        case_id: str,
    ) -> Session:
        """
        Create a new Mode 1 (Case Study) session.

        Args:
            participant_id: Participant ID
            participant_name: Display name
            case_id: ID of the case study to use

        Returns:
            The created Session
        """
        case_study = create_case_study(case_id)

        engine = CaseEngine(
            client=self.client,
            participant_id=participant_id,
            participant_name=participant_name,
            case_study=case_study,
        )

        session = Session(engine=engine, participant_id=participant_id)

        with self._lock:
            self._sessions[session.session_id] = session
            if participant_id not in self._pid_to_sid:
                self._pid_to_sid[participant_id] = {}
            self._pid_to_sid[participant_id]["case"] = session.session_id

        return session

    def create_group_session(
        self,
        participant_id: str,
        participant_name: str,
        scenario_id: str,
    ) -> Session:
        """
        Create a new Mode 2 (Group Discussion) session.

        Args:
            participant_id: Participant ID
            participant_name: Display name
            scenario_id: ID of the group scenario to use

        Returns:
            The created Session
        """
        scenario = create_scenario(scenario_id)

        engine = GroupEngine(
            client=self.client,
            participant_id=participant_id,
            participant_name=participant_name,
            scenario=scenario,
        )

        session = Session(engine=engine, participant_id=participant_id)

        with self._lock:
            self._sessions[session.session_id] = session
            if participant_id not in self._pid_to_sid:
                self._pid_to_sid[participant_id] = {}
            self._pid_to_sid[participant_id]["group"] = session.session_id

        return session

    def get_session(self, session_id: str) -> Optional[Session]:
        """Get a session by session ID."""
        return self._sessions.get(session_id)

    def get_session_by_participant(
        self,
        participant_id: str,
        mode: str,
    ) -> Optional[Session]:
        """Get a session by participant ID and mode."""
        mode_sids = self._pid_to_sid.get(participant_id, {})
        sid = mode_sids.get(mode)
        if sid:
            return self._sessions.get(sid)
        return None

    def persist_session(self, session_id: str) -> None:
        """Save session state to disk for reconnection."""
        session = self._sessions.get(session_id)
        if session is None:
            return

        engine = session.engine
        state = {
            "participant_id": session.participant_id,
            "mode": engine.mode.value,
            "session_id": engine.session_id,
            "turns": [
                {
                    "turn_number": t.turn_number,
                    "speaker_role": t.speaker_role.value,
                    "speaker_name": t.speaker_name,
                    "content": t.content,
                    "timestamp": t.timestamp.isoformat(),
                }
                for t in engine.turns
            ],
            "state": engine.state.value,
            "elapsed_seconds": engine.elapsed_seconds,
        }

        # Mode-specific state
        if isinstance(engine, CaseEngine):
            state["case_id"] = engine.case_study.id
            state["revealed_categories"] = list(engine.facilitator.revealed_categories)
        elif isinstance(engine, GroupEngine):
            state["scenario_id"] = engine.scenario.id
            state["current_phase_index"] = engine.current_phase_index

        path = self._persist_dir / f"{session_id}.json"
        with open(path, "w") as f:
            json.dump(state, f, indent=2, default=str)

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
                pid = session.participant_id
                mode = "case" if session.mode == InterviewMode.CASE_STUDY else "group"
                if pid in self._pid_to_sid:
                    self._pid_to_sid[pid].pop(mode, None)
