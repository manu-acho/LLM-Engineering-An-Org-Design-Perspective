# Lesson 11.4: Read configuration as an executable division of work

[Module route](README.md) · [Next: follow a real crew](05-source-walkthrough.md)

A configuration is a set of settings that tells software what to run and how. A task listed below another one is not necessarily dependent on it; the dependency exists when it requires the earlier result. Read the settings as instructions for an actual case and identify where the result passes from one task to the next.

## Configuration changes behaviour

A YAML file is structured text. Indentation groups fields. A key such as `agent` identifies a configured contributor; a `context` list names earlier outputs. A folded block introduced with `>` combines multiple written lines into a text value. The file is not Python, but the program can load it and use its values to construct Python objects.

In the course's reference projects, agent configuration describes role, goal and backstory. Task configuration describes work, expected output and assigned agent. An `expected_output` description tells a model what is wanted. It does not independently test whether the output exists or is correct.

## A dependency is more than an ordering preference

```yaml
collect:
  description: Collect the supplied delivery evidence without adding facts.
  expected_output: A record containing source IDs and unresolved differences.
  agent: researcher

assess:
  description: Assess the evidence against the supplied policy.
  expected_output: A supported finding with missing information identified.
  agent: analyst
  context:
    - collect
```

This is an illustrative task configuration, not a standalone application. A loader or framework still has to create agents and task objects, resolve names and execute a process. The dependency says the assessment needs collection output. It does not necessarily provide the original evidence in full: inspect what the predecessor actually returns.

If `collect` compresses away “customer reports”, the analyst may receive a stronger claim than the source supports. A reviewer consuming the same compressed result can repeat the error. Additional agents do not create independent evidence automatically.

## Sequential and hierarchical are process choices

A sequential process executes the declared task route. A hierarchical process gives a manager role machinery to allocate and review work. The latter can adapt to a varying task but introduces another model-mediated coordination layer. It still needs explicit tools, evidence, stopping rules and result checking.

Neither process is inherently an organisation design. A software manager choosing a task does not establish authority over finance staff. A sequential task pipeline can support a highly collaborative human process. Analyse technical scheduling and organisational allocation separately, then connect them deliberately.

## Make hidden inputs visible

Task strings can contain placeholders such as `{requirements}`. Values supplied at kickoff become part of the task. A prompt can therefore change even when its YAML file is unchanged. Record the template revision and substituted values in an experiment.

Likewise, a source project's tool list determines whether an agent can read, write or execute files. A role description saying “researcher” does not reveal those powers. Inspect tool registration and execution paths alongside the configuration.

**Worked check:** The YAML names a `test_task` and asks for a test summary. What establishes that testing occurred? Inspect executed tools, test artefacts, outcomes and scope. A generated summary alone establishes that text was produced. It does not establish backend correctness or frontend behaviour.

**Source connection:** The [engineering task settings](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/3_crewai/reference/engineering_team/src/engineering_team/config/tasks.yaml) make these boundaries especially visible.

## Read the organisational connection

Configuration encodes categories, permitted contributions and criteria before execution starts. The research chapter explains [decision premises](../../reference/research/03-decisions.md#decision-premises).
