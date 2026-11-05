# Lesson 17.6: Complete a defensible service decision

[Download the matching notebook](/downloads/17-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Research chapter](../../reference/research/02-coordination.md)

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
