# Lesson 20.1: Governed improvement and integration capstone

[Download the matching notebook](/downloads/20-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## What you'll learn and why it matters

Distinguish a proposed configuration from the active one and explain what should justify a release. Harbour needs to improve the service without judging candidates on the same cases used to design them.

## Business context: Harbour

Suppose Harbour changes an instruction to preserve the word “reported” in more briefs. The candidate is the proposed version; promotion makes it the version the service uses. Evaluate the candidate on cases that did not guide its design and decide beforehand what it must improve without making other outcomes worse.

Explain which changes a governed improvement process may propose and who may approve them.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## Improvement needs a declared object

A service can change its model, prompt, tool schema, source collection, routing rules or review arrangement. These are different interventions. An improvement proposal should identify exactly what changes, which failure it addresses and why the proposed mechanism could address that failure.

Harbour's candidate might preserve source labels more consistently. That is a testable claim about a particular behaviour. “Make the agent smarter” is too broad to identify a comparison or a rollback target. Keep the candidate immutable during evaluation so its results refer to a stable artefact.

## Separate proposal from promotion

A model or coding agent can propose a change without holding the authority to release it. A proposal may include a diff, rationale, expected effect and a test plan. Promotion is the decision to make a candidate the active configuration for a defined population. That decision should identify who accepts the risks and how operation will be monitored.

A new instruction is tested because the old one sometimes turns “reported” into “confirmed”. The proposed instruction remains a candidate while the tests run. Even if it improves that result, Harbour should check what happened to other required behaviours. Only after the stated checks and an authorised decision does it become the active version.

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

### Complete the exercise

**Worked answer.** baseline. Recording a proposed change does not release it.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A candidate is a proposed version. Promotion selects what the service will use. Development and confirmation answer different questions about its performance.

## What this means for the business process

Assign release authority and agree the checks before tuning the candidate. Hold some cases for confirmation so a promising development result does not silently become the basis of approval.

For the research behind this design choice, read [Select controls for the work that can actually be assessed](../../reference/research/08-governance-and-accountability.md#select-controls-for-the-work-that-can-actually-be-assessed).

## Next lesson

The next workshop compares the current and proposed instructions on the same declared cases against those checks. [Lesson 20.2: Evaluate a candidate against a promotion gate](02-code-workshop.md).
