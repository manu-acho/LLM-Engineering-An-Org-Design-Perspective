"""Governed candidate evaluation with an explicit human promotion condition."""

import math

from ai_orgdesign.business import fingerprint


def gate(baseline, candidate, human_approved=False):
    if type(human_approved) is not bool:
        raise ValueError("Explicit boolean approval required")
    required = {"accuracy", "unsafe", "cost", "n", "dataset_hash"}
    if not required <= baseline.keys() or not required <= candidate.keys():
        raise ValueError("Incomplete evaluation record")
    for record in [baseline, candidate]:
        if type(record["n"]) is not int or type(record["unsafe"]) is not int:
            raise ValueError("Counts must be integers")
        if not 0 <= record["unsafe"] <= record["n"]:
            raise ValueError("Unsafe count must fit sample size")
        if not all(
            type(record[field]) in (int, float) and math.isfinite(record[field])
            for field in ["accuracy", "cost"]
        ):
            raise ValueError("Finite numeric metrics required")
        if not 0 <= record["accuracy"] <= 1 or record["cost"] < 0 or not record["dataset_hash"]:
            raise ValueError("Invalid metric range or dataset identity")
    if (
        baseline["n"] <= 0
        or baseline["n"] != candidate["n"]
        or baseline["dataset_hash"] != candidate["dataset_hash"]
    ):
        raise ValueError("Comparable nonempty evaluation evidence required")
    reasons = []
    if candidate["unsafe"] > baseline["unsafe"]:
        reasons.append("more unsafe decisions")
    if candidate["accuracy"] < baseline["accuracy"]:
        reasons.append("lower accuracy")
    if candidate["cost"] > baseline["cost"] * 1.1:
        reasons.append("cost exceeds agreed tolerance")
    if not human_approved:
        reasons.append("approval absent")
    return {
        "promote": not reasons,
        "reasons": reasons,
        "boundary": "Teaching gate, not a significance test",
    }


def demo():
    identity = fingerprint([f"fictional-held-out-{i}" for i in range(10)])
    baseline = {"accuracy": 0.8, "unsafe": 1, "cost": 1.0, "n": 10, "dataset_hash": identity}
    candidate = {**baseline, "accuracy": 0.9, "unsafe": 0, "cost": 1.05}
    return {
        "without_approval": gate(baseline, candidate),
        "approved": gate(baseline, candidate, True),
        "rollback_target": "previous approved immutable version",
    }
