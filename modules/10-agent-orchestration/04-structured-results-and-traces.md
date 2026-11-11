# Lesson 10.4: Structure the contribution and read the execution trace

[Module route](README.md) · [Next: run a small SDK application](05-source-walkthrough.md)

## What you'll learn and why it matters

Read the structure of a specialist result and follow it through an execution trace. Learn which events show that it was returned, checked or accepted.

A free-text specialist report may hide the source number inside a sentence. A structured result gives the source and the claim named places. A trace records events such as a call, a returned result and a check. Follow one contribution through the trace to see whether it was returned, checked and accepted.

## A paragraph is difficult to combine reliably

Two specialists return advice. One writes “probably ready”; the other supplies a long policy explanation. A coordinator cannot safely treat those as equivalent approval records. A structured contract separates contribution, evidence, uncertainty and status.

```python
from pydantic import BaseModel, Field

class EvidenceContribution(BaseModel):
    case_id: str
    source_ids: list[str] = Field(min_length=1)
    finding: str
    missing_information: list[str]
    ready_for_review: bool
```

This example needs `pydantic`. The type declaration lets a validator check expected fields and values under its configuration. `min_length=1` requires at least one source ID. A fabricated source can still satisfy it. The application must check that IDs refer to permitted records and that the finding is supported.

## Separate shape, evidence and authority

Shape asks whether the record can be consumed. Evidence asks whether it faithfully represents sources. Authority asks whether a particular actor may approve or execute the proposed action. A structured result addresses the first; it can carry information needed for the other two without performing them automatically.

A guardrail's position matters. An output check after an agent run can reject a final answer. It cannot undo an earlier tool effect. A tool boundary can check arguments and permission before a change. A human review interrupt can request a decision. These mechanisms have different timing and evidence.

## Read a trace as a chain of events

An illustrative trace contains: coordinator started, order specialist called, policy specialist called, policy lookup failed, order result returned, draft withheld, incomplete outcome returned. The failure policy is visible because the coordinator did not silently convert one successful branch into a complete case.

Trace events should retain a run ID, parent relationship, operation name, status and timing. Store sensitive inputs only when needed and appropriately protected. Business records may additionally need case identity, proposal revision, approval and acknowledged effect. A technical trace and a business record can refer to the same run while serving different purposes.

## Concurrency has more than a happy path

If a branch fails, decide whether the whole group stops, remaining work continues or a partial result is returned. Cancellation is cooperative in asynchronous programs. A request to cancel does not establish that an external system received nothing. A branch that sends email is different from a branch that only reads policy.

For independent reads, an all-required policy can collect results and withhold the draft if any required source fails. For optional enrichment, a partial result may be appropriate. Name that distinction in the task contract before implementing `gather`.

**Worked check:** A trace shows that both specialists returned results, and the final Pydantic object validates. Is the recommendation verified? No. Inspect returned evidence, support and decision conditions. The trace establishes an execution path; the schema establishes representation. Neither alone establishes the truth of the business conclusion.

**Source connection:** The course [structured-output and guardrail lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/2_openai/3_lab3.ipynb) supplies concrete implementations for comparison.

## Read the organisational connection

An execution trace records selected events without showing every judgement or off-system contribution. The research chapter explains [the limits of logs](../../reference/research/05-routines.md#what-logs-can-show).

## What to remember

Named fields make a contribution easier to combine. A trace records selected events. Field shape, evidence support and authority remain separate checks.

## What this means for the business process

Record each status with a case identifier, and expose the gap between a returned output and an accepted handoff. Check the receiver's record before using the trace to claim that business ownership changed.

For the research behind this design choice, read [What logs can show](../../reference/research/05-routines.md#what-logs-can-show).

## Next lesson

Next follow an actual SDK configuration into a run and inspect what the returned result lets the application verify. [Lesson 10.5: Configure an agent, run it and inspect its result](05-source-walkthrough.md).
