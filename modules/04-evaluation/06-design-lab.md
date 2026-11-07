# Lesson 4.6: Decide whether a measured improvement changes the organisation

[Download the matching notebook](/downloads/04-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../05-rag/README.md)

## Business context: Harbour

Decide whether the evidence supports a bounded pilot, further investigation or no change.

[Company and supply-chain context](../../HARBOUR.md) · [Module 4 business situation](../../reference/harbour-learning-journey.md#module-4)

## Put the entire case into the measurement

**Fictional comparison.** Harbour evaluates two drafting systems on 100 comparable delivery complaints. Both reduce drafting time. System A is cheaper per request; System B preserves qualifications more consistently. The decision concerns completed work, so the team records effort after generation as well.

| Per-case measure | Existing process | System A | System B |
|---|---|---|---|
| Preparation | 10 minutes | 3 minutes | 4 minutes |
| Review | 2 minutes | 6 minutes | 3 minutes |
| Expected rework effort | 1 minute | 3 minutes | 1 minute |
| Total recorded effort | 13 minutes | 12 minutes | 8 minutes |

These are illustrative averages, not empirical findings. A's seven-minute preparation gain becomes a one-minute total gain. B saves five minutes despite generating more slowly. Compare software cost against those complete effort differences.

## Explain why local metrics can conflict

The account manager's preparation target rewards submitting quickly. Operations needs usable evidence. Finance needs a justified remedy. Each role can meet its local target while the case moves poorly across the process. The decision-premise lens explains how a measure directs attention and behaviour, rather than simply describing it afterwards.

Harbour therefore uses a small set of connected measures: supported draft, accepted handoff, total effort, elapsed resolution and harmful error. It retains the local measures for diagnosis. The aim is not one universal score in which consequential failures can be hidden by many quick successes.

## Hold alternative explanations open

During the pilot, Harbour also introduces a clearer intake form. That may explain some of the gain. A three-way comparison can help: existing process, improved intake alone, and improved intake plus system B. Where assignment is not random, document differences in case difficulty, staff experience and workload. A before/after average alone cannot isolate the model's contribution.

Suppose the improved form saves four minutes and the model adds one more. The business case should recognise both contributions. This does not make the model useless. It establishes a smaller, better-supported claim about its incremental value.

## Check fit among the design elements

The [organisation design review](../../reference/research/01-organisation-design.md) describes interdependent configurations. Better source access, reviewer skill, workload and incentives can complement a referenced draft. They can also be inconsistent: rewarding submission count while expecting careful evidence checking gives staff competing signals.

There may be more than one coherent design. A central specialist pool can support rare, difficult cases. Trained frontline resolution can support a standardised population. This is the practical significance of **equifinality**: different configurations can produce an appropriate result under different conditions. It does not imply that every arrangement is equally good.

## Reach a decision with explicit conditions

Harbour chooses system B for the defined population, keeps human authorisation for remedies and retains the improved intake form. It postpones expansion to urgent and ambiguous cases until those groups have their own evaluation. The service owner reviews unsupported claims and effort by role weekly during stabilisation.

A scale decision requires both technical quality and an operating arrangement. If B generates twice as many drafts but finance cannot review them, capacity becomes the binding constraint. In that case a scope limit or a different division of work may be preferable to another model upgrade.

**Exercise with a worked response:** Suppose B saves five staff minutes per case but resolution still takes two days. Can the pilot claim improved customer responsiveness? It can claim the measured effort reduction under its comparison assumptions. To claim responsiveness, it needs evidence of changed elapsed time or another defined customer outcome. The next redesign should investigate waiting and dependencies, using the [coordination review](../../reference/research/02-coordination.md).

## Read the organisational connection

The effect of a measured improvement depends on information, capacity, roles and incentives around it. The research chapter explains [fit among design choices](../../reference/research/01-organisation-design.md#fit-is-a-relationship-among-choices).

## Practical activity: Make a release decision conditional on more than a mean score.





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

Does passing the three local cases establish a real business benefit?

```python
decision = {"technical_cases_checked":3,"business_outcome_observed":False,"release_scope":"learning only"}
print(decision)
assert not decision["business_outcome_observed"]
```

No. An outcome comparison needs observations of the complete work, including failures and review effort.

### Complete the exercise

Write the prediction before consulting the worked answer: Does passing the three local cases establish a real business benefit?

**Worked answer.** No. An outcome comparison needs observations of the complete work, including failures and review effort.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
