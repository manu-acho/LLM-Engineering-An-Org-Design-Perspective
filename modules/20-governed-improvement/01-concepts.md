# Lesson 20.1: Governed improvement and integration capstone

[Download the matching notebook](/downloads/20-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## Business context: Harbour

Explain which changes a governed improvement process may propose and who may approve them.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## Improvement needs a declared object

A service can change its model, prompt, tool schema, source collection, routing rules or review arrangement. These are different interventions. An improvement proposal should identify exactly what changes, which failure it addresses and why the proposed mechanism could address that failure.

Harbour's candidate might preserve source labels more consistently. That is a testable claim about a particular behaviour. “Make the agent smarter” is too broad to identify a comparison or a rollback target. Keep the candidate immutable during evaluation so its results refer to a stable artefact.

## Separate proposal from promotion

A model or coding agent can propose a change without holding the authority to release it. A proposal may include a diff, rationale, expected effect and a test plan. Promotion is the decision to make a candidate the active configuration for a defined population. That decision should identify who accepts the risks and how operation will be monitored.

The gate function embodies a small declared policy: comparable cases, no increase in unsafe outcomes, no accuracy decrease, cost within an agreed tolerance and explicit human approval. These thresholds are teaching choices. They are not universal business rules or a substitute for an appropriate statistical analysis.

## Keep development and confirmation apart

A development set supports diagnosis and iteration. A final confirmation set should examine a candidate after the selection process. Repeatedly querying the same held-out scores can turn that set into another development signal, even when its labels are never shown to the proposer. Record evaluation rounds and protect the final comparison from continuous optimisation.

Compare the candidate with both the current system and a simpler alternative where appropriate. The candidate can outperform an old model while remaining inferior to a revised intake form. A useful result is a justified choice among arrangements, not merely a positive difference against one convenient baseline.

## Interpret variation before claiming progress

Small samples and stochastic generation can produce different scores across runs. Fix the declared dataset, retain relevant settings and report the sample size. Repeated runs can help estimate execution variation, but they do not correct a biased population. Differences in time or cost should be interpreted alongside failure rates and human effort.

A promotion gate is a decision rule, not proof of statistical significance. A confidence interval requires a suitable method and assumptions. A business decision may also depend on rare severe errors that an average score obscures. Keep those conditions visible rather than reducing every consideration to one composite grade.

## Recover from a released mistake

Versioning records which configuration was used. Rollback selects a previous configuration for new work. Neither automatically undoes messages already sent, records already changed or expectations already created. Recovery needs an affected-case query, responsible owners and a correction route.

The capstone therefore joins the technical service and its operating model. A defensible proposal explains the contribution, the data and model boundaries, who accepts outputs, how exceptions move, what was tested and which claims remain unsupported. Completion is the ability to reason across these layers, not merely obtaining a green test suite.

## Practical activity: Separate a configuration proposal from the active version.





The exercise code below runs from a prepared course checkout. In the matching notebook, the setup cell already supplies ROOT and RUN_LIVE. If following the code here, run this setup first:

```python
from ai_orgdesign.workspace import project_root, live_mode
ROOT = project_root()
RUN_LIVE = live_mode()
if RUN_LIVE:
    from ai_orgdesign.provider import Gateway
    gateway = Gateway(max_requests=12, max_output_tokens=1000)
print("Live mode:", RUN_LIVE)
```

### Predict and follow the values

Which version remains active after a proposal is recorded?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.governance import Versions
with TemporaryDirectory() as directory:
    registry=Versions(Path(directory)/"versions.json")
    registry.propose("candidate","Preserve report status explicitly")
    print(registry.read())
    assert registry.read()["current"]=="baseline"
```

baseline. Recording a proposed change does not release it.

### Complete the exercise

Write the prediction before consulting the worked answer: Which version remains active after a proposal is recorded?

**Worked answer.** baseline. Recording a proposed change does not release it.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
