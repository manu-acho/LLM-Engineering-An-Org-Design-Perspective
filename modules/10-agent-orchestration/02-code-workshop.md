# Lesson 10.2: Validate and accept a specialist contribution

[Download the matching notebook](/downloads/10-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

A specialist can return a well-formed object about the wrong case. Orchestration therefore needs both a structural contract and acceptance rules linking the contribution to the task that requested it.

The implementation lives in `src/ai_orgdesign/labs/m10.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

Contribution is a Pydantic model. Its fields require a case identifier, at least one source, a conclusion and at least one unresolved item; extra fields are forbidden. model_validate checks the payload against that structure. accept then checks that the case identifier is the expected one and every cited source belongs to the allowed set. A successful result is labelled accepted_for_review. That status deliberately stops short of verifying the conclusion or authorising a remedy.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m10 import accept
payload = {"case_id":"H-17", "sources":["order-17"], "conclusion":"Quantities require comparison", "unresolved":["receipt"]}
assert accept(payload)["state"] == "accepted_for_review"
print(accept(payload))
```

The supplied H-17 contribution passes the structural and case/source membership checks. An invented source or another case identifier raises ValueError. A conclusion that is false but cites an allowed source may still pass, exposing the distinction between membership validation and factual support.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Write a false conclusion using order-17 as its source and determine whether the current acceptance function detects the falsehood. Propose the next check rather than claiming schema validation solved it.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The function cannot judge entailment. A deterministic quantity comparison, a reviewer or a separately evaluated evidence-support check must examine whether the source supports the conclusion. Each additional checker has its own error modes. An acceptance contract should state exactly which checks were applied and what remains for review.

## Consider the alternative

A specialist-as-tool returns a contribution to its coordinator. A handoff transfers the active interaction to another role. Neither pattern should leave ownership implicit. Plain functions are adequate for many fixed routes and make a useful comparison before introducing a model-driven coordinator.

The [organisation design reading](../../reference/research/02-coordination.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
