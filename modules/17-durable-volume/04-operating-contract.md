# Lesson 17.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/17-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

A job can be waiting, claimed or finished; those states have different consequences for the next worker. An operating contract specifies who can change a state and under what conditions. Read the example for when work can be claimed again and what prevents two results being accepted for one claim.

Use a job lease to inspect temporary ownership and reject an expired worker.

[Company and supply-chain context](../../HARBOUR.md) · [Module 17 business situation](../../reference/harbour-learning-journey.md#module-17)

## Start with a concrete contribution

Preparing more cases per minute can overload the people who accept or investigate them. Harbour therefore examines technical concurrency and human review capacity together, while preserving ownership when workers fail or become slow.

An operating contract states what information is required, what contribution is promised, what counts as acceptance and who owns the next step. It also names refusal and failure outcomes. A contract is useful when another person can apply it to a case without guessing what a success label means.

## Follow the included implementation

Imagine two places at a workbench. If both are occupied, the next job waits for a place. In Python, a **semaphore** provides those places. The lab function `bounded_work` runs tasks that can pause while another task proceeds. Each task takes a place, adds one to the active count and waits briefly to imitate work. A `finally` block subtracts one even if the task encounters a problem. `gather` returns the results in the order the tasks were supplied, which may differ from the order in which they finished.

The separate exercise records jobs in a local SQLite database. A worker claims a job by changing its record, but the database applies the change only if the job is still available. Another worker can reclaim it when the lease runs out. The `finish` operation checks both the current owner and the expiry time before accepting a result. The test supplies the clock values so the same example can be repeated without waiting.

Open `src/ai_orgdesign/labs/m17.py` and follow each call into its supporting function. Ordinary Python functions receive values and return values; a class groups state and operations; a context manager controls a resource's lifetime. The [programming reference](../../reference/python-patterns.md) explains these patterns with small examples, and the [technical foundations](../../reference/technical-foundations.md) introduces transactions, concurrency and neural calculations before their use.

## Write acceptance and rejection conditions

At concurrency two, the peak counter never exceeds two. The first worker can claim job-1 at time zero; a second cannot claim it at time five, but can reclaim it at eleven after a ten-second lease. A former owner cannot finish after the transfer. These are local ownership tests, not a benchmark of distributed throughput.

Acceptance conditions should be observable. “The system handles errors” is too vague. Specify which input is refused, whether the attempt changes state, what the caller sees and who receives unresolved work. A failed test is useful information about the contract; suppressing an exception merely to obtain a successful notebook run destroys that information.

## Compare another arrangement

A serial queue is easier to reason about and may be adequate at low volume. More concurrency can hide waiting but adds contention and ordering problems. Distributed brokers and worker pools introduce acknowledgements, redelivery and operational responsibilities that an in-process semaphore does not supply.

Compare the alternatives on the same task boundary. Include work transferred to another person or service, information that becomes unavailable and new maintenance obligations. A component-level speed gain can be real while the complete service remains slower or harder to investigate.

## Exercise and worked answer

Assume thirty cases per hour enter review and reviewers can finish twenty per hour. What changes if agent preparation becomes twice as fast? How should a lease handle an external action completed just before a worker fails?

**Worked answer.** The review backlog grows by ten cases each hour under the stated steady rates. Faster preparation does not increase review capacity and may expose the bottleneck sooner. A lease alone cannot establish whether an external action happened. Use a stable command identity, the external service's idempotency facilities where available, and reconciliation before retrying an uncertain action.

Carry that answer into the design record: required input, permitted contribution, acceptance owner, escalation trigger, recovery route and evidence for any benefit claim. The design record describes who will do the work and what rules they will follow. Observing actual cases shows whether those roles and rules work as planned.

## Practical activity: Check whether a stable-flow calculation is applicable.


### Predict and follow the values

What is average work under these declared stable-flow assumptions?

```python
throughput_per_hour=20
average_hours=.5
average_work=throughput_per_hour*average_hours
print("Stable-flow illustrative work:",average_work)
```

### Complete the exercise

**Worked answer.** Ten cases. This calculation does not describe the separate example with a continually growing backlog.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

### Programming practice

Write growth(arrivals, completions, hours) for the stated constant-rate illustration.

Start with the placeholder in the notebook, then compare with this worked solution. The contrasting checks are part of understanding the contract.

```python
def growth(arrivals, completions, hours):
    return (arrivals-completions)*hours

assert growth(30,20,3) == 30
assert growth(20,20,3) == 0
```

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
