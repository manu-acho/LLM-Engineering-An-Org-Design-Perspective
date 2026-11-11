# Lesson 17.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/17-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## Business context: Harbour

If automation prepares more briefs per hour than advisers can review, work piles up after drafting. Trace arrivals and completions at the review stage, then compare adding review capacity, limiting arrivals or narrowing scope. The best response depends on where the waiting occurs.

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


### Predict and follow the values

Which case risks remaining hidden if only easy completions are celebrated?

```python
queue=[{"case":"easy","age_hours":1},{"case":"difficult","age_hours":48}]
oldest=max(queue,key=lambda row:row["age_hours"])
print("Oldest case:",oldest)
```

### Complete the exercise

**Worked answer.** difficult. A queue policy should state how ageing and unresolved cases are handled.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Calculate capacity for the receiving team

The existing lease example uses thirty arrivals and twenty reviews per hour. Give those numbers an explicit business basis: one reviewer has sixty minutes available in the hour and each case needs three minutes of active review. The implied capacity is `60 / 3 = 20` cases per hour. **Available review minutes** exclude time assigned to other work; they are not automatically the whole shift.

The separate scenario below assumes homogeneous cases, constant arrivals, no rework and independent reviewers whose capacities add. It compares average workload with capacity. It does not predict queue waiting time or guarantee that a backlog disappears. Even where capacity exceeds arrivals, variation, specialist dependencies and an existing backlog can still cause delay.

```python
def review_capacity(arrivals_per_hour, reviewers, minutes_available_each, minutes_per_case):
    if arrivals_per_hour < 0 or reviewers < 1 or minutes_available_each < 0 or minutes_per_case <= 0:
        raise ValueError("Use valid non-negative workload and positive review inputs")
    capacity = reviewers * minutes_available_each / minutes_per_case
    return {
        "capacity_per_hour": capacity,
        "unserved_growth_per_hour": max(0, arrivals_per_hour - capacity),
    }

one_reviewer = review_capacity(30, 1, 60, 3)
two_reviewers = review_capacity(30, 2, 60, 3)
assert one_reviewer["capacity_per_hour"] == 20
assert one_reviewer["unserved_growth_per_hour"] == 10
assert two_reviewers["capacity_per_hour"] == 40
assert two_reviewers["unserved_growth_per_hour"] == 0
print(one_reviewer, two_reviewers)

```

### Independent application

Keep one reviewer but reserve only thirty minutes of the hour for review. Calculate capacity and incoming work left unserved. Then compare adding review time with improving evidence completeness; do not assume additional agent concurrency supplies human review capacity.

### Worked comparison

The reviewer can handle ten cases, leaving twenty incoming cases per hour beyond this simplified capacity. Providing a second machine worker does not change those available review minutes. More reviewer time, clearer intake, fewer returns or a narrower pilot may change the workload-capacity relationship in different ways. Each option needs evidence about quality and where work moves.

Record the arrival population, available human time, assumed effort, return/rework treatment and escalation owner. The calculation informs the decision; it does not select staffing or delegated authority automatically.

```python
half_hour = review_capacity(30, 1, 30, 3)
assert half_hour["capacity_per_hour"] == 10
assert half_hour["unserved_growth_per_hour"] == 20
print(half_hour)

```

## Independent Harbour design record

Harbour may receive several complaints while investigators and warehouse contacts are already busy. Faster concurrent preparation can increase the queue waiting for acceptance. A worker that finishes late must also be prevented from overwriting work another worker has legitimately taken over.

**Task:** Create a capacity and recovery plan with preparation rate, human review limits, queue owner and response to overdue cases.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Limit concurrent work and observe receiving-team capacity. Distinguish a queued technical job from ownership of the commercial case. Expired workers must not commit stale results; any external physical or financial action would need its own reconciliation.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.

## Research extension: examine the wider arrangement

[Process architecture](../../reference/research/09-process-architecture.md#what-event-logs-can-reveal). An event timestamp may record receipt rather than occurrence. Examine delayed records, case correlation and missing work before interpreting queue performance.
