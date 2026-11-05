# Lesson 17.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/17-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## Start with a concrete contribution

Preparing more cases per minute can overload the people who accept or investigate them. Harbour therefore examines technical concurrency and human review capacity together, while preserving ownership when workers fail or become slow.

An operating contract states what information is required, what contribution is promised, what counts as acceptance and who owns the next step. It also names refusal and failure outcomes. A contract is useful when another person can apply it to a case without guessing what a success label means.

## Follow the included implementation

bounded_work uses an asyncio semaphore to limit the number of active coroutines. Each coroutine enters the semaphore, increments a counter, awaits a short artificial delay and decrements the counter in finally. gather collects results in input order. The separate SQLite job exercise gives a worker a time-limited lease through one conditional UPDATE. Another worker may reclaim an expired lease, but finish accepts only the current owner with an unexpired lease. The supplied clock values make expiration tests deterministic.

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

Carry that answer into the design record: required input, permitted contribution, acceptance owner, escalation trigger, recovery route and evidence for any benefit claim. A design record describes the proposed arrangement. Repeated observation and outcome comparisons are needed to examine what it becomes in practice.
