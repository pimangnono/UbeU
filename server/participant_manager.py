"""
Participant Manager: Handles participant registration, counterbalancing, and persistence.

Within-subject design:
- Each participant completes BOTH modes (Case Study + Group Discussion)
- Order is counterbalanced: odd IDs get case first, even IDs get group first
- Scenarios are round-robin assigned within each mode
"""

import json
import threading
from pathlib import Path
from typing import Optional

from server.models import (
    ParticipantRecord,
    StudyCondition,
    StudyPhase,
)
from config.case_studies import get_all_case_ids
from config.group_scenarios import get_all_scenario_ids


class ParticipantManager:
    """
    Manages participant registration and study flow.

    - Sequential IDs: P001, P002, ...
    - Counterbalanced condition assignment
    - Round-robin scenario assignment for each mode
    - Persistent storage in outputs/participants/{pid}/
    """

    def __init__(self, base_dir: Optional[str] = None):
        self._base_dir = Path(base_dir) if base_dir else Path("outputs/participants")
        self._base_dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

        # Available scenarios
        self._case_ids = get_all_case_ids()
        self._group_ids = get_all_scenario_ids()

        # Discover next ID
        self._counter = self._discover_next_id()

    def _discover_next_id(self) -> int:
        """Scan existing directories to find the next participant number."""
        max_num = 0
        for d in self._base_dir.iterdir():
            if d.is_dir() and d.name.startswith("P"):
                try:
                    num = int(d.name[1:])
                    max_num = max(max_num, num)
                except ValueError:
                    continue
        return max_num + 1

    def create_participant(self, name: str, email: Optional[str] = None) -> ParticipantRecord:
        """
        Create a new participant with counterbalanced condition assignment.

        Args:
            name: Participant's name for the interview
            email: Optional email for follow-up

        Returns:
            ParticipantRecord with assigned condition and scenarios
        """
        with self._lock:
            pid = f"P{self._counter:03d}"

            # Counterbalance: odd IDs get case first, even IDs get group first
            if self._counter % 2 == 1:
                condition = StudyCondition.CASE_FIRST
            else:
                condition = StudyCondition.GROUP_FIRST

            # Round-robin scenario assignment
            case_idx = (self._counter - 1) % len(self._case_ids)
            group_idx = (self._counter - 1) % len(self._group_ids)

            self._counter += 1

        record = ParticipantRecord(
            participant_id=pid,
            name=name,
            email=email,
            condition=condition,
            current_phase=StudyPhase.CONSENT,
            case_scenario_id=self._case_ids[case_idx],
            group_scenario_id=self._group_ids[group_idx],
        )

        # Create directory and save
        self._get_dir(pid).mkdir(parents=True, exist_ok=True)
        self._save_record(record)

        return record

    def get_participant(self, pid: str) -> Optional[ParticipantRecord]:
        """Load a participant record from disk."""
        record_path = self._get_dir(pid) / "record.json"
        if not record_path.exists():
            return None
        with open(record_path) as f:
            data = json.load(f)
        return ParticipantRecord.model_validate(data)

    def update_participant(self, record: ParticipantRecord) -> None:
        """Save an updated participant record."""
        self._save_record(record)

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
            # Start first mode based on condition
            if record.condition == StudyCondition.CASE_FIRST:
                record.current_phase = StudyPhase.MODE_1_INTERVIEW
            else:
                record.current_phase = StudyPhase.MODE_2_INTERVIEW
        elif current == StudyPhase.MODE_1_INTERVIEW:
            record.current_phase = StudyPhase.MODE_1_COMPLETE
        elif current == StudyPhase.MODE_1_COMPLETE:
            # Check if second mode needed
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

        self._save_record(record)
        return record.current_phase

    def list_participants(self) -> list[str]:
        """List all participant IDs."""
        pids = []
        for d in sorted(self._base_dir.iterdir()):
            if d.is_dir() and d.name.startswith("P"):
                pids.append(d.name)
        return pids

    def list_completed_participants(self) -> list[ParticipantRecord]:
        """List all participants who completed both modes."""
        completed = []
        for pid in self.list_participants():
            record = self.get_participant(pid)
            if record and record.case_completed and record.group_completed:
                completed.append(record)
        return completed

    def _get_dir(self, pid: str) -> Path:
        """Get the data directory for a participant."""
        return self._base_dir / pid

    def _save_record(self, record: ParticipantRecord) -> None:
        """Save participant record to disk."""
        dir_path = self._get_dir(record.participant_id)
        dir_path.mkdir(parents=True, exist_ok=True)
        record_path = dir_path / "record.json"
        with open(record_path, "w") as f:
            f.write(record.model_dump_json(indent=2))

    def save_session_output(self, pid: str, mode: str, session_data: dict) -> Path:
        """Save session output for a participant."""
        dir_path = self._get_dir(pid)
        dir_path.mkdir(parents=True, exist_ok=True)
        output_path = dir_path / f"{mode}_session.json"
        with open(output_path, "w") as f:
            json.dump(session_data, f, indent=2, default=str)
        return output_path

    def get_condition_counts(self) -> dict[str, int]:
        """Get count of participants in each condition."""
        counts = {
            StudyCondition.CASE_FIRST.value: 0,
            StudyCondition.GROUP_FIRST.value: 0,
        }
        for pid in self.list_participants():
            record = self.get_participant(pid)
            if record:
                counts[record.condition.value] += 1
        return counts
