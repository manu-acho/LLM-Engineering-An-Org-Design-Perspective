# Lesson 17.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/17-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Use a job lease to inspect temporary ownership and reject an expired worker.

[Company and supply-chain context](../../HARBOUR.md) · [Module 17 business situation](../../reference/harbour-learning-journey.md#module-17)

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

## Practical activity: Check whether a stable-flow calculation is applicable.





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

What is average work under these declared stable-flow assumptions?

```python
throughput_per_hour=20
average_hours=.5
average_work=throughput_per_hour*average_hours
print("Stable-flow illustrative work:",average_work)
```

Ten cases. This calculation does not describe the separate example with a continually growing backlog.

### Complete the exercise

Write the prediction before consulting the worked answer: What is average work under these declared stable-flow assumptions?

**Worked answer.** Ten cases. This calculation does not describe the separate example with a continually growing backlog.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

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
