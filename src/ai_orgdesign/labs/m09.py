"""Bounded loop with injected planner, explicit tool budgets and replayable calls."""

from ai_orgdesign.business import dispatch


def run(planner, tenant="north", budget=2):
    if type(budget) is not int or budget < 1:
        raise ValueError("Positive integer budget required")
    observations = []
    seen = set()
    for step in range(budget):
        decision = planner(list(observations))
        if decision.get("kind") == "final":
            return {"stop": "final", "answer": decision["text"], "observations": observations}
        if decision.get("kind") != "tool" or not isinstance(decision.get("id"), str):
            raise ValueError("Invalid planner decision")
        if decision["id"] in seen:
            return {"stop": "repeated_call", "observations": observations}
        seen.add(decision["id"])
        result = dispatch(decision["name"], decision["arguments"], tenant)
        observations.append({"call_id": decision["id"], "result": result, "step": step})
    return {"stop": "budget", "observations": observations}


def scripted_planner(observations):
    if observations:
        return {"kind": "final", "text": "Records need investigation; no remedy authorised."}
    return {"kind": "tool", "id": "read-1", "name": "lookup_case", "arguments": {"case_id": "H-17"}}


def demo():
    return run(scripted_planner)
