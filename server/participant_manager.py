"""
Participant Manager: Handles participant registration, counterbalancing, and persistence.

V4: Backed by Supabase instead of JSON files.
Within-subject design:
- Each participant completes BOTH modes (Case Study + Group Discussion)
- Order is counterbalanced: odd IDs get case first, even IDs get group first
- Scenarios are round-robin assigned within each mode
"""

import json
import logging
from dataclasses import asdict
from datetime import datetime
from typing import Optional, Any

from server.supabase_client import get_supabase
from server.models import (
    ParticipantRecord,
    StudyCondition,
    StudyPhase,
    PostSessionSurvey,
)
from config.case_studies import get_all_case_ids
from config.group_scenarios import get_all_scenario_ids

logger = logging.getLogger(__name__)


def _serialize(obj: Any) -> Any:
    """Serialize a dataclass or Pydantic model to a JSON-compatible dict."""
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    if hasattr(obj, "__dataclass_fields__"):
        return _dataclass_to_dict(obj)
    return obj


def _dataclass_to_dict(obj: Any) -> dict:
    """Recursively convert a dataclass to a dict, handling nested dataclasses and enums."""
    if hasattr(obj, "__dataclass_fields__"):
        result = {}
        for k, v in obj.__dict__.items():
            result[k] = _dataclass_to_dict(v)
        return result
    elif isinstance(obj, list):
        return [_dataclass_to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: _dataclass_to_dict(v) for k, v in obj.items()}
    elif hasattr(obj, "value"):  # Enum
        return obj.value
    elif isinstance(obj, datetime):
        return obj.isoformat()
    return obj


class ParticipantManager:
    """
    Manages participant registration and study flow.

    - Sequential IDs: P001, P002, ...
    - Counterbalanced condition assignment
    - Round-robin scenario assignment for each mode
    - Persistent storage in Supabase
    """

    def __init__(self):
        self._db = get_supabase()
        self._case_ids = get_all_case_ids()
        self._group_ids = get_all_scenario_ids()

    def _get_next_id(self) -> tuple[str, int]:
        """Get the next sequential participant ID."""
        result = (
            self._db.table("participants")
            .select("id")
            .order("created_at", desc=True)
            .limit(1)
            .execute()
        )
        if not result.data:
            return "P001", 1

        last_id = result.data[0]["id"]
        try:
            num = int(last_id[1:]) + 1
        except (ValueError, IndexError):
            num = 1
        return f"P{num:03d}", num

    def create_participant(self, name: str, email: Optional[str] = None) -> ParticipantRecord:
        """
        Create a new participant with counterbalanced condition assignment.

        Args:
            name: Participant's name for the interview
            email: Optional email for follow-up

        Returns:
            ParticipantRecord with assigned condition and scenarios
        """
        pid, num = self._get_next_id()

        # Counterbalance: odd IDs get case first, even IDs get group first
        if num % 2 == 1:
            condition = StudyCondition.CASE_FIRST
        else:
            condition = StudyCondition.GROUP_FIRST

        # Round-robin scenario assignment
        case_idx = (num - 1) % len(self._case_ids)
        group_idx = (num - 1) % len(self._group_ids)

        row = {
            "id": pid,
            "name": name,
            "email": email,
            "status": "pending",
            "current_phase": StudyPhase.CONSENT.value,
            "condition": condition.value,
            "case_scenario_id": self._case_ids[case_idx],
            "group_scenario_id": self._group_ids[group_idx],
        }

        self._db.table("participants").insert(row).execute()

        return ParticipantRecord(
            participant_id=pid,
            name=name,
            email=email,
            condition=condition,
            current_phase=StudyPhase.CONSENT,
            case_scenario_id=self._case_ids[case_idx],
            group_scenario_id=self._group_ids[group_idx],
        )

    def get_participant(self, pid: str) -> Optional[ParticipantRecord]:
        """Load a participant record from Supabase."""
        result = self._db.table("participants").select("*").eq("id", pid).execute()
        if not result.data:
            return None

        row = result.data[0]

        # Load BFI-44 data if available
        bfi_result = (
            self._db.table("bfi44_results")
            .select("*")
            .eq("participant_id", pid)
            .execute()
        )

        bfi44_raw = None
        bfi44_scores = None
        bfi44_duration = None
        if bfi_result.data:
            bfi = bfi_result.data[0]
            bfi44_raw = bfi.get("raw_responses")
            # Convert string keys back to int keys
            if bfi44_raw and isinstance(bfi44_raw, dict):
                bfi44_raw = {int(k): v for k, v in bfi44_raw.items()}
            bfi44_scores = bfi.get("scores")
            bfi44_duration = bfi.get("duration_seconds")

        # Build record data
        record_data = {
            "participant_id": row["id"],
            "name": row["name"],
            "email": row.get("email"),
            "consent_given": row.get("consent_given", False),
            "consent_timestamp": row.get("consent_at"),
            "condition": row.get("condition", "case_first"),
            "current_phase": row.get("current_phase", "consent"),
            "case_scenario_id": row.get("case_scenario_id"),
            "group_scenario_id": row.get("group_scenario_id"),
            "case_completed": row.get("case_completed", False),
            "case_session_id": row.get("case_session_id"),
            "case_assessment": row.get("case_assessment"),
            "case_stats": row.get("case_stats"),
            "group_completed": row.get("group_completed", False),
            "group_session_id": row.get("group_session_id"),
            "group_assessment": row.get("group_assessment"),
            "group_stats": row.get("group_stats"),
            "survey": row.get("survey"),
            "created_at": row.get("created_at"),
            "completed_at": row.get("completed_at"),
            "bfi44_raw": bfi44_raw,
            "bfi44_scores": bfi44_scores,
            "bfi44_duration_seconds": bfi44_duration,
        }

        return ParticipantRecord.model_validate(record_data)

    def update_participant(self, record: ParticipantRecord) -> None:
        """Save an updated participant record to Supabase."""
        data = {
            "name": record.name,
            "email": record.email,
            "consent_given": record.consent_given,
            "consent_at": record.consent_timestamp.isoformat() if record.consent_timestamp else None,
            "condition": record.condition.value,
            "current_phase": record.current_phase.value,
            "case_scenario_id": record.case_scenario_id,
            "group_scenario_id": record.group_scenario_id,
            "case_completed": record.case_completed,
            "case_session_id": record.case_session_id,
            "case_assessment": _serialize(record.case_assessment),
            "case_stats": _serialize(record.case_stats),
            "group_completed": record.group_completed,
            "group_session_id": record.group_session_id,
            "group_assessment": _serialize(record.group_assessment),
            "group_stats": _serialize(record.group_stats),
            "survey": _serialize(record.survey),
            "completed_at": record.completed_at.isoformat() if record.completed_at else None,
        }

        self._db.table("participants").update(data).eq("id", record.participant_id).execute()

        # Upsert BFI-44 data if present
        if record.bfi44_raw is not None:
            bfi_data = {
                "participant_id": record.participant_id,
                "raw_responses": {str(k): v for k, v in record.bfi44_raw.items()},
                "scores": _serialize(record.bfi44_scores),
                "duration_seconds": record.bfi44_duration_seconds,
            }
            self._db.table("bfi44_results").upsert(bfi_data).execute()

    def advance_phase(self, pid: str) -> StudyPhase:
        """
        Advance participant to the next study phase.

        Returns:
            The new phase
        """
        record = self.get_participant(pid)
        if record is None:
            raise ValueError(f"Participant {pid} not found")

        current = record.current_phase

        # Phase transitions
        if current == StudyPhase.CONSENT:
            record.current_phase = StudyPhase.BFI44
        elif current == StudyPhase.BFI44:
            if record.condition == StudyCondition.CASE_FIRST:
                record.current_phase = StudyPhase.MODE_1_INTERVIEW
            else:
                record.current_phase = StudyPhase.MODE_2_INTERVIEW
        elif current == StudyPhase.MODE_1_INTERVIEW:
            record.current_phase = StudyPhase.MODE_1_COMPLETE
        elif current == StudyPhase.MODE_1_COMPLETE:
            if record.condition == StudyCondition.CASE_FIRST:
                record.current_phase = StudyPhase.MODE_2_INTERVIEW
            else:
                record.current_phase = StudyPhase.SURVEY
        elif current == StudyPhase.MODE_2_INTERVIEW:
            record.current_phase = StudyPhase.MODE_2_COMPLETE
        elif current == StudyPhase.MODE_2_COMPLETE:
            if record.condition == StudyCondition.GROUP_FIRST:
                record.current_phase = StudyPhase.MODE_1_INTERVIEW
            else:
                record.current_phase = StudyPhase.SURVEY
        elif current == StudyPhase.SURVEY:
            record.current_phase = StudyPhase.COMPLETE

        # Update only the phase and status
        update_data = {"current_phase": record.current_phase.value}
        if record.current_phase == StudyPhase.BFI44:
            update_data["status"] = "in_progress"
        elif record.current_phase == StudyPhase.COMPLETE:
            update_data["status"] = "completed"

        self._db.table("participants").update(update_data).eq("id", pid).execute()

        return record.current_phase

    def list_participants(self) -> list[str]:
        """List all participant IDs."""
        result = (
            self._db.table("participants")
            .select("id")
            .order("id")
            .execute()
        )
        return [row["id"] for row in result.data]

    def list_completed_participants(self) -> list[ParticipantRecord]:
        """List all participants who completed both modes."""
        result = (
            self._db.table("participants")
            .select("*")
            .eq("case_completed", True)
            .eq("group_completed", True)
            .execute()
        )

        records = []
        for row in result.data:
            try:
                record = self.get_participant(row["id"])
                if record:
                    records.append(record)
            except Exception as e:
                logger.warning(f"Failed to load participant {row['id']}: {e}")

        return records

    def save_session_output(self, pid: str, mode: str, session_data: dict) -> None:
        """Save session output to Supabase sessions table."""
        session_id = session_data.get("session_id", "")
        if not session_id:
            return

        # Upsert session record
        session_row = {
            "id": session_id,
            "participant_id": pid,
            "mode": mode,
            "scenario_id": session_data.get("scenario_id"),
            "status": "ended",
            "duration_seconds": session_data.get("duration_seconds", 0),
        }
        self._db.table("sessions").upsert(session_row).execute()

        # Insert turns
        turns = session_data.get("turns", [])
        if turns:
            turn_rows = [
                {
                    "session_id": session_id,
                    "turn_number": t.get("turn_number", i),
                    "speaker_name": t.get("speaker_name", ""),
                    "speaker_role": t.get("speaker_role", ""),
                    "content": t.get("content", ""),
                }
                for i, t in enumerate(turns)
            ]
            # Delete existing turns for this session before inserting
            self._db.table("turns").delete().eq("session_id", session_id).execute()
            self._db.table("turns").insert(turn_rows).execute()

    def get_condition_counts(self) -> dict[str, int]:
        """Get count of participants in each condition."""
        result = self._db.table("participants").select("condition").execute()

        counts = {
            StudyCondition.CASE_FIRST.value: 0,
            StudyCondition.GROUP_FIRST.value: 0,
        }
        for row in result.data:
            cond = row.get("condition")
            if cond in counts:
                counts[cond] += 1
        return counts
