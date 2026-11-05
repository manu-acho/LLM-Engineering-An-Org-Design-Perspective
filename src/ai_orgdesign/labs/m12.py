"""Persist pending work, recreate a process-facing store, reject stale approval."""

import tempfile
from pathlib import Path

from ai_orgdesign.business import CaseStore


def demo():
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "state.db"
        first_process = CaseStore(path)
        first_process.seed()
        snapshot = first_process.read("H-17", "north")
        resumed = CaseStore(path)
        decision = resumed.decide(
            "H-17", "north", "manager-a", "manager", snapshot["version"], "return", "resume-1"
        )
        return {
            "before_restart": snapshot,
            "after_resume": decision,
            "boundary": "Database reopen, not a real process crash or distributed checkpoint test",
        }
