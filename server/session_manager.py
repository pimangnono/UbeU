"""
Session Manager: Manages concurrent interview sessions for both modes.

V4: Persists session state and turns to Supabase.
Keeps engines in memory for active sessions (LLM context).

Handles:
- CaseEngine sessions (Mode 1)
- GroupEngine sessions (Mode 2)
- Session persistence to Supabase for crash recovery
"""

import logging
import threading
from typing import Optional, Union, TYPE_CHECKING

from server.supabase_client import get_supabase
from engines.case_engine import CaseEngine
from engines.group_engine import GroupEngine
from utils.models import InterviewMode, SessionState
from config.case_studies import create_case_study
from config.group_scenarios import create_scenario

if TYPE_CHECKING:
    from clients.llm_client import LLMClient

logger = logging.getLogger(__name__)


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

    - In-memory dict of session_id -> Session (active engines)
    - Persists session state and turns to Supabase
    - Supports Mode 1 (CaseEngine) and Mode 2 (GroupEngine)
    """

    def __init__(self, client: "LLMClient"):
        self.client = client
        self._sessions: dict[str, Session] = {}
        self._pid_to_sid: dict[str, dict[str, str]] = {}  # pid -> {mode: sid}
        self._lock = threading.Lock()
        self._db = get_supabase()

    def create_case_session(
        self,
        participant_id: str,
        participant_name: str,
        case_id: str,
    ) -> Session:
        """Create a new Mode 1 (Case Study) session."""
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

        # Persist session record to Supabase
        self._create_session_record(session, case_id)

        return session

    def create_group_session(
        self,
        participant_id: str,
        participant_name: str,
        scenario_id: str,
    ) -> Session:
        """Create a new Mode 2 (Group Discussion) session."""
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

        # Persist session record to Supabase
        self._create_session_record(session, scenario_id)

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
        """Save session state and turns to Supabase."""
        session = self._sessions.get(session_id)
        if session is None:
            return

        engine = session.engine

        # Update session status
        update_data = {
            "status": "active" if engine.state != SessionState.ENDED else "ended",
            "duration_seconds": int(engine.elapsed_seconds),
        }
        if engine.state == SessionState.ENDED:
            from datetime import datetime
            update_data["ended_at"] = datetime.now().isoformat()

        try:
            self._db.table("sessions").update(update_data).eq("id", session_id).execute()
        except Exception as e:
            logger.error(f"Failed to update session {session_id}: {e}")

        # Persist turns (delete + reinsert for simplicity)
        try:
            turn_rows = [
                {
                    "session_id": session_id,
                    "turn_number": t.turn_number,
                    "speaker_name": t.speaker_name,
                    "speaker_role": t.speaker_role.value,
                    "content": t.content,
                }
                for t in engine.turns
            ]
            if turn_rows:
                self._db.table("turns").delete().eq("session_id", session_id).execute()
                self._db.table("turns").insert(turn_rows).execute()
        except Exception as e:
            logger.error(f"Failed to persist turns for session {session_id}: {e}")

    def list_active_sessions(self) -> list[str]:
        """List session IDs of active sessions."""
        return [
            sid for sid, s in self._sessions.items()
            if s.state not in (SessionState.ENDED,)
        ]

    def remove_session(self, session_id: str) -> None:
        """Remove a session from memory (keeps Supabase state)."""
        with self._lock:
            session = self._sessions.pop(session_id, None)
            if session:
                pid = session.participant_id
                mode = "case" if session.mode == InterviewMode.CASE_STUDY else "group"
                if pid in self._pid_to_sid:
                    self._pid_to_sid[pid].pop(mode, None)

    def _create_session_record(self, session: Session, scenario_id: str) -> None:
        """Create a session record in Supabase."""
        try:
            row = {
                "id": session.session_id,
                "participant_id": session.participant_id,
                "mode": session.mode.value,
                "scenario_id": scenario_id,
                "status": "active",
            }
            self._db.table("sessions").insert(row).execute()
        except Exception as e:
            logger.error(f"Failed to create session record: {e}")
