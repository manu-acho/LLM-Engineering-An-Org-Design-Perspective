# Lesson 17.2: Limit concurrent work and recover an expired lease

[Download the matching notebook](/downloads/17-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Preparing more cases per minute can overload the people who accept or investigate them. Harbour therefore examines technical concurrency and human review capacity together, while preserving ownership when workers fail or become slow.

The implementation lives in `src/ai_orgdesign/labs/m17.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

bounded_work uses an asyncio semaphore to limit the number of active coroutines. Each coroutine enters the semaphore, increments a counter, awaits a short artificial delay and decrements the counter in finally. gather collects results in input order. The separate SQLite job exercise gives a worker a time-limited lease through one conditional UPDATE. Another worker may reclaim an expired lease, but finish accepts only the current owner with an unexpired lease. The supplied clock values make expiration tests deterministic.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m17 import bounded_work, demo
result = await bounded_work(list(range(6)), limit=2)
assert result["peak"] <= 2
print(result)
print(demo())
```

At concurrency two, the peak counter never exceeds two. The first worker can claim job-1 at time zero; a second cannot claim it at time five, but can reclaim it at eleven after a ten-second lease. A former owner cannot finish after the transfer. These are local ownership tests, not a benchmark of distributed throughput.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Assume thirty cases per hour enter review and reviewers can finish twenty per hour. What changes if agent preparation becomes twice as fast? How should a lease handle an external action completed just before a worker fails?

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The review backlog grows by ten cases each hour under the stated steady rates. Faster preparation does not increase review capacity and may expose the bottleneck sooner. A lease alone cannot establish whether an external action happened. Use a stable command identity, the external service's idempotency facilities where available, and reconciliation before retrying an uncertain action.

## Consider the alternative

A serial queue is easier to reason about and may be adequate at low volume. More concurrency can hide waiting but adds contention and ordering problems. Distributed brokers and worker pools introduce acknowledgements, redelivery and operational responsibilities that an in-process semaphore does not supply.

The [organisation design reading](../../reference/research/02-coordination.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
