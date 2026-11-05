# Lesson 11.5: Follow a CrewAI project from settings to returned artefact

[Module route](README.md) · [Next: redesign the division of work](06-design-lab.md)

## Open the files that cooperate

Read the source [researcher crew](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/researcher/src/researcher/crew.py) with its [tasks](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/researcher/src/researcher/config/tasks.yaml). `@CrewBase` supplies project conventions. Methods marked `@agent` construct configured agents; methods marked `@task` construct tasks. `@crew` assembles them with `Process.sequential` in the inspected implementation.

The reporting task writes `report.md`. Writing a file is a side effect in addition to returning an object. Its existence does not establish source quality. The file, raw task outputs and run status are different artefacts to inspect.

## A complete minimal crew

This new integration requires `crewai`, configured provider access and an accessible `OPENAI_MODEL`. Running kickoff makes model requests and may incur charges. It uses only supplied fictional evidence, no search or execution tools. It was not run against a model while authoring.

```python
import os
from crewai import Agent, Crew, Process, Task

def investigate_delivery():
    researcher = Agent(
        role="Evidence reader", goal="Preserve supplied facts and uncertainty",
        backstory="A careful reader of delivery records",
        llm=os.environ["OPENAI_MODEL"], allow_delegation=False,
    )
    analyst = Agent(
        role="Case analyst", goal="Prepare a bounded review proposal",
        backstory="An analyst who distinguishes reports from verification",
        llm=os.environ["OPENAI_MODEL"], allow_delegation=False,
    )
    collect = Task(
        description=(
            "For {case_id}, read only this supplied evidence: {evidence}. "
            "Retain source IDs and identify what remains unverified."
        ),
        expected_output="A factual evidence record with sources and uncertainty",
        agent=researcher,
    )
    assess = Task(
        description="Propose the next evidence check. Do not authorise a credit.",
        expected_output="A draft proposal with its sources and limits",
        agent=analyst, context=[collect],
    )
    crew = Crew(
        agents=[researcher, analyst], tasks=[collect, assess],
        process=Process.sequential, verbose=False,
    )
    return crew.kickoff(inputs={
        "case_id": "C-17",
        "evidence": "[order-17] Ordered 12; customer reports receiving 10; no recount.",
    })
```

The function returns the crew result instead of printing it immediately. Its task outputs can be inspected separately from the final raw response. `context=[collect]` explicitly passes the predecessor contribution. It does not give the analyst independent source verification. `allow_delegation=False` keeps this example's contribution route bounded.

This code uses direct Python construction so the full wiring is visible in one place. The reference project separates similar information into YAML and decorated methods. Compare the two approaches field by field before assuming that one requires different business semantics.

## Trace the larger engineering crew

The source [engineering crew](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/engineering_team/src/engineering_team/crew.py) constructs design, backend, frontend and test tasks. Its selected process is sequential. A hierarchical alternative appears in comments; commented configuration is not active execution.

The task settings give frontend work both design and code context. The test task receives backend and design context and is instructed to test the backend, not `app.py`. A backend test summary therefore cannot establish complete application quality. The frontend has a separate construction-check instruction.

Inspect the [sandbox tools](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/engineering_team/src/engineering_team/tools/sandbox_tools.py) to understand how file writing and code execution occur. A role label does not show those effects. No original generated program is executed by this lesson.

## Compare process behaviour fairly

For a sequential/hierarchical comparison, hold task, source evidence, model access and acceptance criteria stable. Record scheduling, calls, errors, review corrections and cost. A manager producing more messages is not a quality improvement by itself.

**Worked diagnosis:** The analyst confidently recommends a credit, although collection only contained a customer report. Inspect whether the expected-output wording encouraged a remedy, whether the evidence qualification survived and whether the final acceptance check catches unsupported authority. Adding another similarly prompted reviewer may preserve the same mistake.

**Documentation:** [CrewAI crews](https://docs.crewai.com/en/concepts/crews), alongside the pinned reference project. Current documentation and source dependency versions can differ.

## Read the organisational connection

A configuration and returned artefact do not establish recurrent organisational performance. The research chapter explains [artefacts and patterns of action](../../reference/research/05-routines.md#designing-an-artefact-and-designing-a-pattern).
