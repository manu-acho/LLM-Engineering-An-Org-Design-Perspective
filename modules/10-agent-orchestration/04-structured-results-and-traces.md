# Lesson 10.4: Structure the contribution and read the execution trace

[Download the matching notebook](/downloads/10-04-structured-results-and-traces.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: run a small SDK application](05-source-walkthrough.md)

## Business context: Harbour

Design a contract that preserves meaning and uncertainty when components exchange data.

[Company and supply-chain context](../../HARBOUR.md) · [Module 10 business situation](../../reference/harbour-learning-journey.md#module-10)

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

## Read the organisational connection

An execution trace records selected events without showing every judgement or off-system contribution. The research chapter explains [the limits of logs](../../reference/research/05-routines.md#what-logs-can-show).

## Practical activity: Reject well-shaped content that cites an invented source.





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

Is schema validation alone sufficient for factual support?

```python
from ai_orgdesign.investigation import validate_specialist
from ai_orgdesign.case_data import get_case
case=get_case()
try:
    validate_specialist({"case_id":"H-17","findings":["Claim"],"sources":["invented"],"unresolved":["receipt"]},case,case["source_ids"])
except ValueError:
    print("Unsupported source rejected")
else:
    raise AssertionError("Unsupported contribution accepted")
```

No. This second check rejects unsupported source membership; it still cannot prove every sentence follows from an allowed source.

### Complete the exercise

Write the prediction before consulting the worked answer: Is schema validation alone sufficient for factual support?

**Worked answer.** No. This second check rejects unsupported source membership; it still cannot prove every sentence follows from an allowed source.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
