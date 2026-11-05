# Lesson 17.5: Inspect ownership, waiting and completion

[Download the matching notebook](/downloads/17-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m17.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

bounded_work uses an asyncio semaphore to limit the number of active coroutines. Each coroutine enters the semaphore, increments a counter, awaits a short artificial delay and decrements the counter in finally. gather collects results in input order. The separate SQLite job exercise gives a worker a time-limited lease through one conditional UPDATE. Another worker may reclaim an expired lease, but finish accepts only the current owner with an unexpired lease. The supplied clock values make expiration tests deterministic.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Assume thirty cases per hour enter review and reviewers can finish twenty per hour. What changes if agent preparation becomes twice as fast? How should a lease handle an external action completed just before a worker fails?

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m17 import bounded_work
serial = await bounded_work([1,2,3], limit=1)
assert serial["peak"] == 1
print(serial)
```

**Interpretation.** The review backlog grows by ten cases each hour under the stated steady rates. Faster preparation does not increase review capacity and may expose the bottleneck sooner. A lease alone cannot establish whether an external action happened. Use a stable command identity, the external service's idempotency facilities where available, and reconciliation before retrying an uncertain action.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

At concurrency two, the peak counter never exceeds two. The first worker can claim job-1 at time zero; a second cannot claim it at time five, but can reclaim it at eleven after a ten-second lease. A former owner cannot finish after the transfer. These are local ownership tests, not a benchmark of distributed throughput.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A serial queue is easier to reason about and may be adequate at low volume. More concurrency can hide waiting but adds contention and ordering problems. Distributed brokers and worker pools introduce acknowledgements, redelivery and operational responsibilities that an in-process semaphore does not supply.

The [research connection](../../reference/research/02-coordination.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
