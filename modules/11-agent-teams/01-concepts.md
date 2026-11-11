# Lesson 11.1: Roles, tasks and dependencies in an agent team

[Module route](README.md) · [Next lesson](02-code-workshop.md)

Imagine one specialist checking dispatch and another checking the delivery report. A role specifies the kind of contribution expected; a task asks for a particular piece of work. A dependency appears if one task needs another task's result. Draw those relationships for the case before deciding who or what should coordinate the work.

## Dividing an investigation

Harbour separates a difficult delivery case into evidence gathering, policy interpretation and response preparation. Instead of writing one large prompt, the team defines a specialist for each contribution. This may make instructions clearer. It also creates a new problem: how do the contributions fit together?

CrewAI offers a way to describe agents, tasks and the process connecting them. The original course uses research, debate, stock-selection and software-building projects to explore these ideas. Here we use them to examine the design of a small team of software components and its relationship to the organisation around it.

## An agent role is a configuration

An agent configuration can describe a role, goal, background instructions, model and tools. “Researcher” helps express the intended contribution. The name does not supply expertise or independent knowledge by itself. Two differently named agents can use the same model and repeat the same misconception.

The warehouse specialist can read the dispatch record without waiting for the policy specialist. A third task that combines both reports must wait for both. That is the division of work. The next design question is what the combined report should do if one specialist returns nothing or the two reports use “received” differently.

A **task** describes work to be done and the output expected. The task may specify which agent handles it, which earlier results it needs and where the result should be written. Separating agent and task lets a reusable capability serve several activities without making every activity a new software persona.

A **crew** brings agents and tasks together under a process. It is useful to ask what the program actually schedules rather than imagining a human team with all its informal coordination already present.

## Sequential and hierarchical processes

A **sequential process** arranges tasks in an order. Evidence is prepared before a report is written. The course's researcher and engineering-team reference projects use this pattern in their inspected configuration.

A **hierarchical process** introduces a manager agent to coordinate work. The stock-picker reference supplies `manager_agent` and uses the hierarchical process. This changes runtime coordination; it does not establish a universally better organisational form. Nor should every crew containing a role called “lead” be described as hierarchical. Inspect the selected process.

The [CrewAI process documentation](https://docs.crewai.com/en/concepts/processes) explains the distinction. When the required sequence is stable, a fixed process can make dependencies easier to see. Model-managed allocation adds flexibility but also requires evaluating whether the manager obtains and integrates the necessary contributions.

## Task context is an information boundary

A task can name earlier tasks as its **context**. In the engineering-team example, coding uses the design, frontend work uses code and design, and backend testing uses code and design. Those declarations help determine which outputs a task receives.

A dependency graph describes these relationships: each task is a node, and an arrow means that one needs something from another. A **directed acyclic graph**, or DAG, has arrows with no route back to the starting task. It can represent a staged process. A revision loop is a different structure and needs an explicit policy for returning work.

More context is not always better. Passing a report rather than its supporting records may hide uncertainty. Passing every file may expose unrelated information and overwhelm the next prompt. Choose what the task needs, including evidence for checking its predecessor's claims.

## Configuration files are part of the program

The course stores many role and task descriptions in **YAML**, a text format for nested settings. Indentation groups fields. A placeholder such as `{requirements}` is filled with supplied input. A small change to task wording can alter what information is considered, which output is expected or when work is treated as complete.

The Python crew class connects these settings to runtime objects. A **decorator**, written with `@`, wraps or registers a definition. In the course, decorators identify agent-producing and task-producing methods and assemble their objects into a crew. They reduce repetitive wiring, but the configuration is still consequential code-adjacent material that needs review and versioning.

## Expected output is not verified output

A task field saying “tested code” expresses a requirement. It does not prove that tests ran or that they addressed the important failure cases. Similarly, a structured record validates its fields without confirming that the research behind them is sound.

The engineering project includes tools for writing and checking generated code in a Docker sandbox. **Isolation** limits where an operation runs and what it can access. It is distinct from correctness: a safely isolated program can still calculate the wrong result. It is also distinct from business permission: a test passing does not authorise publication or use of confidential records.

## Compare another division of work

One model with a clear staged prompt may be sufficient for a small evidence-to-brief task. A deterministic program may perform calculations and formatting more reliably. Several agents become useful when specialised instructions, tools or context boundaries improve the task enough to justify coordination overhead.

The original [researcher crew](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/researcher/src/researcher/crew.py), [engineering crew](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/engineering_team/src/engineering_team/crew.py) and [stock-picker crew](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/stock_picker/src/stock_picker/crew.py) make the process differences visible.

**Check:** A diagram has four boxes labelled researcher, analyst, manager and reviewer. What additional information would you need to describe its actual control flow and independence? Include models, task dependencies, evidence access, evaluation and authority.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Agent role names do not establish independence among the tasks they perform. The research chapter explains [interdependence](../../reference/research/01-organisation-design.md#dependencies-before-departments).
