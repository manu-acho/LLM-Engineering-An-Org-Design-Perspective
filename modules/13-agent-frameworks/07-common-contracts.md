# Lesson 13.7: Write an adapter that preserves uncertainty

[Download the matching notebook](/downloads/13-07-common-contracts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../14-agent-integration/README.md)

## A common shape needs explicit meanings

One runtime returns an object with `output`; another exposes a last message. The application can adapt both into one result record. The dangerous shortcut is to label every non-empty text result `done`. An adapter should preserve what is actually known.

This dependency-free exercise uses invented runtime responses. It tests the application contract, not either framework. The local plain-Python and LangGraph invocation paths are examined in Lesson 13.5.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Contribution:
    task_id: str
    input_revision: int
    status: str
    text: str
    output_id: str | None

def adapt(task_id, revision, response):
    text = response.get("output", "")
    error = response.get("error")
    if error:
        return Contribution(task_id, revision, "failed", str(error), None)
    if not isinstance(text, str) or not text.strip():
        return Contribution(task_id, revision, "invalid", "No text contribution", None)
    return Contribution(task_id, revision, "reported_done", text, response.get("output_id"))

def accept(contribution, current_revision, inspected_output_ids):
    if contribution.status != "reported_done":
        return "not_ready"
    if contribution.input_revision != current_revision:
        return "needs_revision"
    if contribution.output_id not in inspected_output_ids:
        return "awaiting_validation"
    return "eligible_for_business_acceptance"

draft = adapt("T-17", 1, {"output": "Translation complete", "output_id": "file:v1"})
assert accept(draft, 1, set()) == "awaiting_validation"
assert accept(draft, 2, {"file:v1"}) == "needs_revision"
assert accept(draft, 1, {"file:v1"}) == "eligible_for_business_acceptance"
```

`frozen=True` prevents reassignment of dataclass fields through ordinary attribute assignment. It is not an authentication mechanism. The caller still needs trusted work identity and revision information. The set of inspected output IDs is supplied by the example, not established by the adapter.

The acceptance function stops short of accepting business quality. An inspected file may exist and still contain a poor translation. A later check must apply the agreed criteria. Preserving this intermediate state prevents a storage observation from becoming a stronger claim.

## Follow a lease and an old worker

If a worker crashes after claiming a task, a lease can eventually let another worker take it. The returning old worker must not overwrite the new owner's result. A monotonically changing claim token or version can make its stale update fail. Timeout by itself does not revoke the old process's ability to write.

The SQLite conditional update in Lesson 13.2 demonstrates expected-state checking. Extend that idea with claim identity when ownership can move. Do not infer that write-ahead logging, a busy timeout or a common database automatically creates the right business transition rule.

## Contract tests should reveal lost meaning

Test an empty result, explicit error, stale input revision, missing output and an inspected but unaccepted artefact. These cases examine actual boundaries. A test merely repeating the adapter's happy-path field mapping adds little confidence.

**Worked extension:** Add a separate `accepted_by` record with decision, task revision and criteria version. Explain why that record belongs to a receiving actor or service, rather than being filled automatically by whichever worker produced the text. The contract now carries work across an organisational boundary instead of hiding that boundary behind a successful function return.

## Read the organisational connection

An adapter that replaces unknown with a definite value changes the basis of later choices. The research chapter explains [decision premises](../../reference/research/03-decisions.md#decision-premises).
