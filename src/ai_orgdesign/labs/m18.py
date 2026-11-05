"""Scope checks, untrusted evidence labelling and decision-time policy versioning."""

from ai_orgdesign.business import DOCUMENTS, lookup


def context(case_id, tenant):
    case = lookup(case_id, tenant)
    policies = [d for d in DOCUMENTS if d["tenant"] == tenant and d["active"]]
    return {
        "case": case,
        "policies": policies,
        "evidence_treatment": "untrusted data, not instructions",
    }


def demo():
    permitted = context("H-17", "north")
    try:
        context("H-18", "north")
    except PermissionError:
        denied = True
    else:
        denied = False
    return {
        "context": permitted,
        "cross_tenant_denied": denied,
        "boundary": "Deterministic scope control, not proof of comprehensive security",
    }
