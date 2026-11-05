# Lesson 15.6: Complete a defensible service decision

[Download the matching notebook](/downloads/15-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Research chapter](../../reference/research/04-implementation.md)

## Prepare the decision record

The fictional Harbour case is an opportunity to connect an executable pattern with the organisation around it. The technical walkthrough supplies the mechanism. This exercise asks what contribution should be accepted, by whom and under which conditions.

Write a one-page decision record with a stated population and exclusions, the proposed contribution, authoritative sources, the people or services involved, acceptance conditions, refusal conditions, recovery and a comparison against an alternative. Keep unsupported assumptions visible. Do not fill a missing business rule by quietly turning a convenient software default into policy.

## Work the difficult case first

Add an acceptance example with equal quantities but a damaged box. Identify which missing input and policy rule are needed before the pilot can handle that case.

Before running a variation, predict the result and its business implication. An exception is not necessarily a defect: denying a forbidden read or rejecting a stale approval can be the intended behaviour. Explain which distinction matters in this case.

**Worked reasoning.** Quantity comparison cannot recognise condition or contractual remedy. The pilot needs an explicit damage report, supporting evidence and an agreed review route. Expanding the schema and examples changes scope; changing a prompt alone would hide that change. Keep damaged-goods cases outside automated handling until the revised specification is tested.

## Separate the technical claim from the service claim

The three routes are review, deny and needs_evidence. matches is true for the supplied examples. Agreement between quantities produces compare_policy rather than automatic closure. This deliberately avoids using numerical agreement as sufficient evidence that the customer problem is resolved.

The code checks support that local claim under the supplied fictional inputs. A service-level claim needs a defined comparison population, an observation period, a reference process and evidence about the surrounding work. Record failed and referred cases as well as successful ones. Omitting them can change both the denominator and the apparent benefit.

## Worked choice among alternatives

An intake form, a record-comparison script or a better source feed may solve the first problem without generation. A coding agent can help implement the agreed slice, but its proposed code must face the same acceptance cases and review as manually written code.

A defensible decision can retain the simpler alternative, narrow the contribution, request more evidence or authorise a bounded pilot. It need not select the most technically elaborate arrangement. The reason should connect observed difficulties with an intervention that can plausibly address them.

## Check the completed explanation

A strong response defines unfamiliar terms, names the relevant owner rather than a vague human-in-the-loop, explains what the code establishes and identifies at least one rival explanation for a favourable result. It should also state what new evidence could change the decision. The linked research chapter supplies the theoretical argument and scholarly references; the case here is an application, not a finding from that literature.
