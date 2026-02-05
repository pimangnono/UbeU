"""
Participant management: ID generation, counterbalanced scenario assignment,
and data directory management.
"""

import json
import threading
from pathlib import Path
from typing import Optional

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from step2.consulting_scenarios import get_all_consulting_scenario_ids
from step2.models import ParticipantRecord


class ParticipantManager:
    """
    Manages participant IDs, scenario assignment, and persistence.

    - IDs are sequential: P001, P002, ...
    - Scenarios are counterbalanced via round-robin across the 4 consulting scenarios.
    - Each participant's data is stored in outputs/step2/participants/{pid}/
    """

    def __init__(self, base_dir: Optional[str] = None):
        self._base_dir = Path(base_dir) if base_dir else Path("outputs/step2/participants")
        self._base_dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._scenario_ids = get_all_consulting_scenario_ids()
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

    def create_participant(self, name: str) -> ParticipantRecord:
        """
        Create a new participant with counterbalanced scenario assignment.

        Args:
            name: Participant's first name for the interview.

        Returns:
            ParticipantRecord with assigned ID and scenario.
        """
        with self._lock:
            pid = f"P{self._counter:03d}"
            # Round-robin scenario assignment
            scenario_idx = (self._counter - 1) % len(self._scenario_ids)
            scenario_id = self._scenario_ids[scenario_idx]
            self._counter += 1

        record = ParticipantRecord(
            participant_id=pid,
            name=name,
            assigned_scenario=scenario_id,
        )

        # Create data directory and save record
        self._get_dir(pid).mkdir(parents=True, exist_ok=True)
        self._save_record(record)

        return record

    def get_participant(self, pid: str) -> Optional[ParticipantRecord]:
        """Load a participant record from disk."""
        record_path = self._get_dir(pid) / "record.json"
        if not record_path.exists():
            return None
        with open(record_path) as f:
            return ParticipantRecord.model_validate_json(f.read())

    def update_participant(self, record: ParticipantRecord) -> None:
        """Save an updated participant record."""
        self._save_record(record)

    def list_participants(self) -> list[str]:
        """List all participant IDs."""
        pids = []
        for d in sorted(self._base_dir.iterdir()):
            if d.is_dir() and d.name.startswith("P"):
                pids.append(d.name)
        return pids

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

    def save_session_output(self, pid: str, session_data: dict) -> Path:
        """Save session output JSON for a participant."""
        dir_path = self._get_dir(pid)
        dir_path.mkdir(parents=True, exist_ok=True)
        output_path = dir_path / "session_output.json"
        with open(output_path, "w") as f:
            json.dump(session_data, f, indent=2, default=str)
        return output_path
