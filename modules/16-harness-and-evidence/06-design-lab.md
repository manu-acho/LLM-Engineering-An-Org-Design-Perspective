# Lesson 16.6: Complete a defensible service decision

[Download the matching notebook](/downloads/16-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Research chapter](../../reference/research/05-routines.md)

## What you'll learn and why it matters

Build an operational review that combines execution evidence and evidence about the work people do. Use the comparison to choose an intervention.

## Business context: Harbour

Suppose Harbour can see a slow run but cannot tell which instruction produced it or whether it finished. Decide what evidence is missing before recommending a change to the service. Recording run details is useful only if someone can interpret them and act on the result.

Connect a technical incident to affected cases without declaring every case resolved when the service recovers.

[Company and supply-chain context](../../HARBOUR.md) · [Module 16 business situation](../../reference/harbour-learning-journey.md#module-16)

## Prepare the decision record

The fictional Harbour case is an opportunity to connect an executable pattern with the organisation around it. The technical walkthrough supplies the mechanism. This exercise asks what contribution should be accepted, by whom and under which conditions.

Write a one-page decision record with a stated population and exclusions, the proposed contribution, authoritative sources, the people or services involved, acceptance conditions, refusal conditions, recovery and a comparison against an alternative. Keep unsupported assumptions visible. Do not fill a missing business rule by quietly turning a convenient software default into policy.

## Work the difficult case first

Suppose a run stopped after reading the case but before writing its final response. Decide which trace fields distinguish that failure from a denied tool call and from an unresolved business investigation.

Before running a variation, predict the result and its business implication. An exception is not necessarily a defect: denying a forbidden read or rejecting a stale approval can be the intended behaviour. Explain which distinction matters in this case.

**Worked reasoning.** A step-level record should distinguish requested, authorised, started, completed and failed operations, with bounded identifiers and exception categories. A final loop stop reason is not a full audit trail. An unresolved business case can coexist with a technically successful run; an execution error can coexist with a correct earlier read.

## Separate the technical claim from the service claim

The supplied loop uses one tool call and stops with final. Elapsed time is measured at runtime and will vary. The assumed cost calculation for one thousand input tokens at one unit per million and two hundred output tokens at four units per million is 0.0018 currency units. No actual provider usage is claimed.

The code checks support that local claim under the supplied fictional inputs. A service-level claim needs a defined comparison population, an observation period, a reference process and evidence about the surrounding work. Record failed and referred cases as well as successful ones. Omitting them can change both the denominator and the apparent benefit.

## Worked choice among alternatives

Structured local logs are sufficient for the first experiment. A tracing service can correlate distributed spans and evaluations, but needs retention, access and redaction rules. Recording hidden reasoning is neither required nor an adequate explanation of evidence support.

A defensible decision can retain the simpler alternative, narrow the contribution, request more evidence or authorise a bounded pilot. It need not select the most technically elaborate arrangement. The reason should connect observed difficulties with an intervention that can plausibly address them.

## Check the completed explanation

A strong response defines unfamiliar terms, names the relevant owner rather than a vague human-in-the-loop, explains what the code establishes and identifies at least one rival explanation for a favourable result. It should also state what new evidence could change the decision. The linked research chapter supplies the theoretical argument and scholarly references; the case here is an application, not a finding from that literature.

## Practical activity: Define an operational review from recorded failures and work outcomes.


### Predict and follow the values

Does an execution trace alone show why the whole organisation improved?

```python
review={"execution":["stop reason","duration","source version"],"work":["rework","waiting","unsupported closure"],"decision_owner":"service manager"}
print(review)
```

### Complete the exercise

**Worked answer.** No. It records selected operations; organisational consequences require observations at the appropriate task boundary.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A trace can show that a step started or stopped. Waiting, rework and unsupported closure require information about the process around that step.

## What this means for the business process

Review failures with the owners of the affected tools and the teams receiving the work. Add observations of queueing and correction, because a successful trace can coexist with an unresolved customer case.

For the research behind this design choice, read [Connected routines and hidden work](../../reference/research/05-routines.md#connected-routines-and-hidden-work).

## Next lesson

Module 17 asks what changes when cases arrive together and waiting, ownership and recovery become regular operating concerns. [Lesson 17.1: Durable case handling at volume](../17-durable-volume/01-concepts.md).
