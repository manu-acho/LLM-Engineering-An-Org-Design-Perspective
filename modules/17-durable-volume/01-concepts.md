# Lesson 17.1: Durable case handling at volume

[Download the matching notebook](/downloads/17-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## Work arrives faster than it can be accepted

A queue holds work awaiting a resource. Harbour can prepare briefs much faster than investigators can review them. If thirty cases arrive each hour and twenty leave review, the queue grows by ten per hour under those assumed steady rates. Faster preparation may change where the waiting becomes visible rather than remove it.

**Concurrency** means that several activities are in progress during overlapping periods. **Parallelism** means that computation happens simultaneously on multiple execution resources. Python coroutines can overlap waiting without executing Python instructions at the same instant. This distinction matters when choosing a mechanism for network-bound and computation-heavy work.

The asynchronous lab uses a semaphore, a counter-like permission mechanism, to permit at most a chosen number of active tasks. A task waits to enter the protected region, performs a short artificial wait and releases its place. The demonstration checks the maximum overlap; the delay is not a model-latency benchmark.

## Completion order and business order differ

A runtime can return results in input order even if operations finish in a different order. asyncio.gather uses this behaviour in the exercise. A business process may instead need events processed according to a case version or dependency. Do not infer business ordering from the shape of a returned Python list.

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

How many additional cases accumulate after three hours under these assumptions?

```python
arrivals,capacity,hours=30,20,3
backlog_growth=(arrivals-capacity)*hours
print("Illustrative additional queued cases:",backlog_growth)
```

Thirty. Variability and exceptions need separate evidence in a real queue.

### Complete the exercise

Write the prediction before consulting the worked answer: How many additional cases accumulate after three hours under these assumptions?

**Worked answer.** Thirty. Variability and exceptions need separate evidence in a real queue.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
