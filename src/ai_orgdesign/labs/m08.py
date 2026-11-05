"""A local service operating record and simulated remedy decision."""

import tempfile
from pathlib import Path

from ai_orgdesign.business import CaseStore


def demo():
    with tempfile.TemporaryDirectory() as folder:
        store = CaseStore(Path(folder) / "cases.db")
        store.seed()
        pending = store.read("H-17", "north")
        decided = store.decide("H-17", "north", "manager-a", "manager", 1, "approve", "command-1")
        retry = store.decide("H-17", "north", "manager-a", "manager", 1, "approve", "command-1")
        return {
            "pending": pending,
            "decision": decided,
            "retry_same": decided == retry,
            "service_owner": "customer operations",
            "money_moved": False,
        }
