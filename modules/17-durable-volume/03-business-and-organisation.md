# Lesson 17.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/17-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## Business context: Harbour

Examine where increased automation shifts waiting or effort to another function.

[Company and supply-chain context](../../HARBOUR.md) · [Module 17 business situation](../../reference/harbour-learning-journey.md#module-17)

## More prepared work is not necessarily more completed work

Harbour doubles its preparation capacity and celebrates a larger daily number of briefs. Investigators then face a growing review queue. The activity improved locally while the wider service still waits. The case illustrates a dependency: preparation outputs become useful only when the next contribution can be accepted and acted on.

Malone and Crowston (1994) frame coordination as managing dependencies among activities. Their framework encourages examining the dependency and possible mechanisms rather than assuming that another technical link solves coordination. See the [coordination chapter](../../reference/research/02-coordination.md) and the original [publication](https://doi.org/10.1145/174666.174668).

## Analyse the receiving stage

For each prepared brief, ask which team receives it, what information makes it usable, how acceptance is acknowledged and what happens if it cannot be accepted. A message delivered to an inbox is a transport event. Acceptance into an accountable work queue is a different event. The local job lease demonstrates machine ownership of an attempt; it does not establish business ownership of the customer problem.

If investigators repeatedly return briefs for a missing document, the apparent capacity shortfall may partly reflect intake quality. If every brief needs managerial approval, the authority design may be the bottleneck. These possibilities imply different interventions. Increasing worker count before diagnosing them can create more unusable work.

## Choose a capacity response

Possible responses include narrowing the pilot, improving evidence completeness, allocating more review capacity, changing batching or delegating a bounded class of decisions. Delegation changes authority and therefore needs a separate policy decision. It should not happen as an accidental consequence of a throughput target.

Prioritisation also has distributive effects. Always favouring easy cases may improve average completion time while leaving difficult customers waiting. A queue policy should specify what receives priority, why, and how long unresolved cases can wait before escalation. Record age and case type alongside throughput.

## Work a recovery example

Worker A prepares a case and loses its lease while waiting for another system. Worker B reclaims the job. If A later returns, the authoritative state must reject its attempt to mark the new owner's job complete. The lab tests that local ownership rule. If A already sent a customer message, database rejection cannot unsend it. Recovery must distinguish prevented state changes from external consequences requiring correction.

The same principle applies to people. A case handed to a new investigator should retain the prior work and unresolved questions without implying that the former investigator still owns the next decision. Explicit acceptance and a current work record can reduce ambiguity, while situated communication may still be necessary for difficult cases.

## Worked service decision

Harbour caps preparation concurrency, exposes review backlog and age, and records reasons for return. It compares changes to intake quality before increasing reviewer headcount. The plan defines an escalation owner for lease failures and a business owner for delayed cases. These are hypotheses about a coherent arrangement, to be examined in use.

The [organisation design chapter](../../reference/research/01-organisation-design.md) explains why task division creates integration work and why several coherent responses may exist. The [routines chapter](../../reference/research/05-routines.md) adds a warning: a configured queue is an artefact, and repeated coordination must still be studied.

## Practical activity: Distinguish priority policy from average throughput.





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

Which case risks remaining hidden if only easy completions are celebrated?

```python
queue=[{"case":"easy","age_hours":1},{"case":"difficult","age_hours":48}]
oldest=max(queue,key=lambda row:row["age_hours"])
print("Oldest case:",oldest)
```

difficult. A queue policy should state how ageing and unresolved cases are handled.

### Complete the exercise

Write the prediction before consulting the worked answer: Which case risks remaining hidden if only easy completions are celebrated?

**Worked answer.** difficult. A queue policy should state how ageing and unresolved cases are handled.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour may receive several complaints while investigators and warehouse contacts are already busy. Faster concurrent preparation can increase the queue waiting for acceptance. A worker that finishes late must also be prevented from overwriting work another worker has legitimately taken over.

**Task:** Create a capacity and recovery plan with preparation rate, human review limits, queue owner and response to overdue cases.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Limit concurrent work and observe receiving-team capacity. Distinguish a queued technical job from ownership of the commercial case. Expired workers must not commit stale results; any external physical or financial action would need its own reconciliation.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
