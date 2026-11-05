# Lesson 11.2: Make task dependencies inspectable

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## A tiny configuration-driven workflow

We will represent a staged investigation using dictionaries and functions. This is not a reimplementation of CrewAI. It isolates the idea that a task receives named predecessor results and must return an inspectable output. No model, database or external tool is used.

```python
def collect(context):
    return {"source_ids": ["order-17"], "reported_difference": 2}

def assess(context):
    evidence = context["collect"]
    return {
        "source_ids": evidence["source_ids"],
        "finding": "Customer and shipment accounts require reconciliation"
    }

def draft(context):
    finding = context["assess"]
    return {"source_ids": finding["source_ids"], "text": finding["finding"]}

TASKS = [
    {"id": "collect", "needs": [], "run": collect},
    {"id": "assess", "needs": ["collect"], "run": assess},
    {"id": "draft", "needs": ["assess"], "run": draft},
]

def run_tasks(tasks):
    results = {}
    for task in tasks:
        task_id = task["id"]
        if task_id in results:
            raise ValueError("Duplicate task ID")
        missing = [name for name in task["needs"] if name not in results]
        if missing:
            raise ValueError(f"Unfinished dependencies: {missing}")
        context = {name: results[name] for name in task["needs"]}
        output = task["run"](context)
        if not isinstance(output, dict) or not output.get("source_ids"):
            raise ValueError("Task result lacks source references")
        results[task_id] = output
    return results

results = run_tasks(TASKS)
print(results["draft"]["text"])
print(results["draft"]["source_ids"])
```

Expected output:

```text
Customer and shipment accounts require reconciliation
['order-17']
```

## Read the configuration as a contract

`TASKS` is an ordered list of dictionaries. Each dictionary names a task, lists earlier results it requires and supplies a function to run. These are ordinary Python values. A framework can provide richer scheduling and validation, but it still needs equivalent information somewhere.

The first task has no predecessors. The second requires `collect`; the third requires `assess`. This does not give the third function direct access to `collect` through its context dictionary. It receives the assessment, which has carried forward source identifiers. Choosing that boundary affects what the drafter can check.

The `run_tasks` loop stores completed outputs under task IDs. The missing-dependency check runs before invoking the task. Reordering the list to put `draft` first therefore raises an error instead of inventing absent context. The implementation expects an already valid order; it does not calculate an execution order for an arbitrary graph.

The dictionary comprehension builds a smaller context from named predecessors. It creates a new outer dictionary but shares the contained result objects. A task that mutates a nested predecessor result could affect later work. Immutable records or deliberate copies are alternatives when that risk matters.

## What the output check does and does not establish

The check requires a dictionary with non-empty `source_ids`. That catches an omitted evidence field. It does not prove that the IDs exist, that the sources are permitted or that the finding follows from them. A fabricated reference would pass this small check.

This illustrates a recurring distinction: a **data contract** governs representation; an **evidence contract** governs support. An operating system needs both, plus rules about authority and external effects. Calling a field `verified` would not perform verification.

The fake assessment uses fixed wording to make the mechanics predictable. It does not actually interpret the reported difference. To test judgement, replace the fake with an implementation and evaluate cases where records agree, conflict or are incomplete. Keep the deterministic wiring check separate from that assessment.

## Read the original crew and task files together

Open the original [researcher crew](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/researcher/src/researcher/crew.py) and its [task settings](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/researcher/src/researcher/config/tasks.yaml). Follow a configured task into its Python `Task` object, then into the crew's selected process. The reporting task writes a file; that write is a side effect beyond returning text.

For a larger example, compare the engineering team's [task configuration](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/engineering_team/src/engineering_team/config/tasks.yaml) with its [crew class](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/engineering_team/src/engineering_team/crew.py). `context` names the predecessor outputs. The backend tester is instructed to test backend code, not the frontend. A backend test summary is consequently not a certificate that the whole application works.

The [sandbox tools](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/engineering_team/src/engineering_team/tools/sandbox_tools.py) show how generated programs can be written and executed in a constrained environment. Reading the tool implementation reveals actual capabilities. A role description saying “test engineer” would not reveal those effects by itself.

## Alternatives and extensions

Direct function calls are simpler when the sequence is short and stable. Configuration becomes useful when task definitions are reused, inspected by several people or changed independently of a runner. Its flexibility also makes configuration changes part of the review process.

A graph scheduler could find ready tasks and run independent ones together. It would need cycle detection, failure propagation and a policy for partially completed work. A manager agent could select tasks dynamically, but its choices would need to satisfy any mandatory dependencies enforced by the application.

**Try it:** Put `draft` first, remove `source_ids` from `assess`, and create two tasks with the same ID, one change at a time. Explain the three failures. Then describe a result that passes every code check above but is still unacceptable as evidence for a credit decision.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A task graph makes prerequisites visible, but shared-resource and meaning problems can remain. The research chapter explains [dependency management](../../reference/research/02-coordination.md#identify-what-depends-on-what).
