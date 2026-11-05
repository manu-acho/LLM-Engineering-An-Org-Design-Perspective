"""Dependency scheduling for deterministic specialist work, not autonomous agents."""


def order_tasks(tasks):
    remaining = {name: set(dependencies) for name, dependencies in tasks.items()}
    if any(not deps <= tasks.keys() for deps in remaining.values()):
        raise ValueError("Unknown dependency")
    done = []
    while remaining:
        ready = sorted(name for name, deps in remaining.items() if deps <= set(done))
        if not ready:
            raise ValueError("Cyclic task dependency")
        for name in ready:
            done.append(name)
            del remaining[name]
    return done


def demo():
    tasks = {"records": [], "policy": [], "compare": ["records", "policy"], "review": ["compare"]}
    return {
        "order": order_tasks(tasks),
        "dependency_edges": sum(map(len, tasks.values())),
        "design": "Parallel preparation, integrated comparison, accountable review",
    }
