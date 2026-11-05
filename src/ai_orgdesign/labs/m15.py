"""Turn examples into executable acceptance decisions before adding generation."""

from ai_orgdesign.business import fingerprint

REQUIREMENTS = [
    {"id": "R1", "case": "mismatched quantities", "expected": "review", "owner": "operations"},
    {"id": "R2", "case": "wrong tenant", "expected": "deny", "owner": "security"},
    {"id": "R3", "case": "missing source", "expected": "needs_evidence", "owner": "record owner"},
]


def route(record):
    if record.get("tenant") != "north":
        return "deny"
    if not record.get("source"):
        return "needs_evidence"
    return "review" if record["ordered"] != record["reported"] else "compare_policy"


def demo():
    inputs = [
        {"tenant": "north", "ordered": 12, "reported": 10, "source": "c17"},
        {"tenant": "south", "ordered": 12, "reported": 10, "source": "c18"},
        {"tenant": "north", "ordered": 12, "reported": 10},
    ]
    actual = [route(record) for record in inputs]
    return {
        "requirements": REQUIREMENTS,
        "actual": actual,
        "matches": actual == [r["expected"] for r in REQUIREMENTS],
        "dataset_hash": fingerprint(inputs),
    }
