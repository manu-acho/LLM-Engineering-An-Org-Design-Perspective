# Lesson 17.6: Complete a defensible service decision

[Download the matching notebook](/downloads/17-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Research chapter](../../reference/research/02-coordination.md)

## Business context: Harbour

Test Harbour's design with a worker that stops and a queue that keeps growing. Decide who notices, who can recover the waiting work and what the customer should be told. A result showing successful recovery for one job does not measure whether Harbour has enough capacity for sustained demand.

Design handling for partial failure, denied regional access and growing review queues.

[Company and supply-chain context](../../HARBOUR.md) · [Module 17 business situation](../../reference/harbour-learning-journey.md#module-17)

## Prepare the decision record

The fictional Harbour case is an opportunity to connect an executable pattern with the organisation around it. The technical walkthrough supplies the mechanism. This exercise asks what contribution should be accepted, by whom and under which conditions.

Write a one-page decision record with a stated population and exclusions, the proposed contribution, authoritative sources, the people or services involved, acceptance conditions, refusal conditions, recovery and a comparison against an alternative. Keep unsupported assumptions visible. Do not fill a missing business rule by quietly turning a convenient software default into policy.

## Work the difficult case first

Assume thirty cases per hour enter review and reviewers can finish twenty per hour. What changes if agent preparation becomes twice as fast? How should a lease handle an external action completed just before a worker fails?

Before running a variation, predict the result and its business implication. An exception is not necessarily a defect: denying a forbidden read or rejecting a stale approval can be the intended behaviour. Explain which distinction matters in this case.

**Worked reasoning.** The review backlog grows by ten cases each hour under the stated steady rates. Faster preparation does not increase review capacity and may expose the bottleneck sooner. A lease alone cannot establish whether an external action happened. Use a stable command identity, the external service's idempotency facilities where available, and reconciliation before retrying an uncertain action.

## Separate the technical claim from the service claim

At concurrency two, the peak counter never exceeds two. The first worker can claim job-1 at time zero; a second cannot claim it at time five, but can reclaim it at eleven after a ten-second lease. A former owner cannot finish after the transfer. These are local ownership tests, not a benchmark of distributed throughput.

The code checks support that local claim under the supplied fictional inputs. A service-level claim needs a defined comparison population, an observation period, a reference process and evidence about the surrounding work. Record failed and referred cases as well as successful ones. Omitting them can change both the denominator and the apparent benefit.

## Worked choice among alternatives

A serial queue is easier to reason about and may be adequate at low volume. More concurrency can hide waiting but adds contention and ordering problems. Distributed brokers and worker pools introduce acknowledgements, redelivery and operational responsibilities that an in-process semaphore does not supply.

A defensible decision can retain the simpler alternative, narrow the contribution, request more evidence or authorise a bounded pilot. It need not select the most technically elaborate arrangement. The reason should connect observed difficulties with an intervention that can plausibly address them.

## Check the completed explanation

A strong response defines unfamiliar terms, names the relevant owner rather than a vague human-in-the-loop, explains what the code establishes and identifies at least one rival explanation for a favourable result. It should also state what new evidence could change the decision. The linked research chapter supplies the theoretical argument and scholarly references; the case here is an application, not a finding from that literature.

## Practical activity: Inspect actual batch failures as a receiving-work problem.

 An asynchronous operation can suspend while compatible work proceeds. The notebook uses await to obtain its result; this is different from a business acceptance acknowledgement.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

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

Should unresolved cases be excluded from the denominator?

```python
statuses=["prepared","needs_investigation","prepared"]
print("Prepared:",statuses.count("prepared"),"Unresolved:",statuses.count("needs_investigation"))
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import batch
    rows=await batch(gateway,["H-17","H-18"],concurrency=1)
    print(rows)
    assert rows[1]["status"]=="needs_investigation"
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. Their handling is part of the service and capacity assessment.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
