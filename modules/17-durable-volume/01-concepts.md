# Lesson 17.1: Durable case handling at volume

[Download the matching notebook](/downloads/17-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## Business context: Harbour

When many requests arrive together, one worker can start a case that another worker finishes. Concurrency allows work on more than one case during the same period. A lease gives one worker a temporary right to act on a job. Follow how that right changes if a worker stops responding, and distinguish which job started first from which finished first.

Relate technical throughput to investigator, warehouse and review capacity.

[Company and supply-chain context](../../HARBOUR.md) · [Module 17 business situation](../../reference/harbour-learning-journey.md#module-17)

## Work arrives faster than it can be accepted

A queue holds work awaiting a resource. Harbour can prepare briefs much faster than investigators can review them. If thirty cases arrive each hour and twenty leave review, the queue grows by ten per hour under those assumed steady rates. Faster preparation may change where the waiting becomes visible rather than remove it.

**Concurrency** means that several activities are in progress during overlapping periods. **Parallelism** means that computation happens simultaneously on multiple execution resources. Python coroutines can overlap waiting without executing Python instructions at the same instant. This distinction matters when choosing a mechanism for network-bound and computation-heavy work.

The asynchronous lab uses a semaphore, a counter-like permission mechanism, to permit at most a chosen number of active tasks. A task waits to enter the protected region, performs a short artificial wait and releases its place. The demonstration checks the maximum overlap; the delay is not a model-latency benchmark.

## Completion order and business order differ

A runtime can return results in input order even if operations finish in a different order. asyncio.gather uses this behaviour in the exercise. A business process may instead need events processed according to a case version or dependency. Do not infer business ordering from the shape of a returned Python list.

Suppose H-17 begins first but waits for a record, while H-18 starts later and finishes quickly. The list returned to the caller can still put H-17 first. To tell which finished first, inspect the completion events. To know which can be acted on, check the case's dependencies and current version. These are separate notions of order.

A faster worker can overtake an earlier slow worker. If both update the same case, an optimistic version check or another concurrency control must prevent a stale result from overwriting current state. More workers make this boundary more consequential; they do not eliminate it.

## Ownership must survive a worker failure

A **lease** gives one worker a temporary right to attempt a job. The lease expires unless renewed or completed. Expiration allows recovery when a worker disappears, but also permits overlap if the original worker is merely slow and continues after another takes ownership.

The local job table records state, owner and expiry. claim uses a conditional database update to obtain ownership only when the job is queued or its existing lease has expired. finish checks the owner and unexpired lease again. That final check prevents the former owner from marking a reclaimed job complete.

In a larger system a fencing token, often a monotonically increasing generation, can help downstream resources reject operations from an older lease. The local exercise checks ownership at its own database boundary. It does not fence an external payment provider or a service that ignores those tokens.

## Retry is a decision under uncertainty

A timeout does not necessarily mean an operation failed. A server might commit an action and lose the response. Retrying can then repeat the action unless the operation has a stable identity and the receiving service recognises it. **Idempotency** means that repeating an operation under its stated contract has the same effect as applying it once.

An idempotency key must be linked to the command content. Reusing the same key for a different action should fail. Keep deduplication and the business transition in one transaction when they share a database. When the external side effect cannot join that transaction, an outbox, acknowledgement tracking and reconciliation can help, but no label creates a distributed exactly-once guarantee.

## Capacity includes the work of exceptions

Do not size a review team only from average successful cases. Missing evidence, failed calls, disputes, rework and leave change effective capacity. Backpressure means slowing or refusing additional intake before an overloaded downstream stage becomes unsafe. It should produce a visible service response and ownership route, not silently drop work.

The module's numerical queue example is an illustrative steady-rate calculation. Real arrival and service variability require measurements and a suitable queueing model. Little's law relates average work in a stable system to throughput and average time, but should not be applied as though an ever-growing backlog were already stable.

## Work a stable-flow calculation

Little's law can be written as average work in the system = average throughput × average time in the system, under its applicable stable-flow conditions. If a stable review process completes twenty cases per hour and each case spends an average of half an hour there, average work in that process is ten cases. Keep the units consistent: cases per hour multiplied by hours produces cases.

This is not the earlier example with arrivals of thirty and capacity of twenty, where the backlog keeps growing. It also does not predict a waiting-time distribution or explain why particular cases are delayed. Use measured boundaries and conditions before applying the relationship.

## Practical activity: Identify where an arrival rate exceeds completion capacity.


### Predict and follow the values

How many additional cases accumulate after three hours under these assumptions?

```python
arrivals,capacity,hours=30,20,3
backlog_growth=(arrivals-capacity)*hours
print("Illustrative additional queued cases:",backlog_growth)
```

### Complete the exercise

**Worked answer.** Thirty. Variability and exceptions need separate evidence in a real queue.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
