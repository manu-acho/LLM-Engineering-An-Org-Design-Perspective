"""Immutable local configuration proposals, explicit promotion and rollback."""

import json
from pathlib import Path

from ai_orgdesign.business import fingerprint
from ai_orgdesign.labs.m20 import gate


class Versions:
    def __init__(self, path):
        self.path = Path(path)
        if not self.path.exists():
            self._write(
                {
                    "current": "baseline",
                    "previous": None,
                    "versions": {
                        "baseline": {"instructions": "Use supplied evidence", "status": "approved"}
                    },
                }
            )

    def read(self):
        return json.loads(self.path.read_text())

    def _write(self, value):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(json.dumps(value, indent=2) + "\n")
        temporary.replace(self.path)

    def propose(self, name, instructions):
        state = self.read()
        if not name or name in state["versions"]:
            raise ValueError("A new immutable version name is required")
        state["versions"][name] = {
            "instructions": instructions,
            "hash": fingerprint(instructions),
            "status": "candidate",
        }
        self._write(state)

    def promote(self, name, baseline, candidate, *, human_approved=False):
        state = self.read()
        if name not in state["versions"] or state["versions"][name]["status"] != "candidate":
            raise ValueError("Select a pending candidate")
        if baseline.get("cost_unit") != candidate.get("cost_unit"):
            raise ValueError("Resource units differ")
        decision = gate(baseline, candidate, human_approved)
        if decision["promote"]:
            state["previous"] = state["current"]
            state["current"] = name
            state["versions"][name]["status"] = "approved"
            self._write(state)
        return decision

    def rollback(self, *, human_approved=False):
        if human_approved is not True:
            raise PermissionError("Explicit human rollback decision required")
        state = self.read()
        if state["previous"] is None:
            raise ValueError("No previous approved version")
        state["current"], state["previous"] = state["previous"], state["current"]
        self._write(state)
        return state["current"]


def propose_instruction(gateway, development_errors):
    schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {"instruction_addition": {"type": "string"}, "rationale": {"type": "string"}},
        "required": ["instruction_addition", "rationale"],
    }
    return gateway.generate(
        json.dumps(development_errors),
        instructions="Propose a small clarification for an evidence-preparation instruction. Do not change tools, authority or access. These are development cases, not the final confirmation set.",
        schema=schema,
    ).value
