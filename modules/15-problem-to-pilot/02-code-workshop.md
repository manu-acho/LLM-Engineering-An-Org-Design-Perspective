# Lesson 15.2: Turn requirements into executable acceptance cases

[Download the matching notebook](/downloads/15-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Harbour wants to reduce the effort of investigating delivery discrepancies. That is a business problem, not yet a requirement for an agent. A useful pilot tests a bounded contribution against an explicit alternative and preserves the case owner's ability to investigate exceptions.

The implementation lives in `src/ai_orgdesign/labs/m15.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

REQUIREMENTS pairs three cases with expected outcomes and named owners. route applies scope before evidence checks, then distinguishes a discrepancy from an apparently matching record. demo constructs the three inputs, evaluates them and computes a hash of the exact input data. The hash identifies the examples; it does not validate their quality. Keeping the expected outcomes separate from route makes it possible to detect an implementation that disagrees with the specification.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m15 import demo, route
result = demo()
assert result["matches"]
assert route({"tenant":"north", "ordered":12, "reported":12, "source":"c17"}) == "compare_policy"
print(result)
```

The three routes are review, deny and needs_evidence. matches is true for the supplied examples. Agreement between quantities produces compare_policy rather than automatic closure. This deliberately avoids using numerical agreement as sufficient evidence that the customer problem is resolved.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Add an acceptance example with equal quantities but a damaged box. Identify which missing input and policy rule are needed before the pilot can handle that case.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** Quantity comparison cannot recognise condition or contractual remedy. The pilot needs an explicit damage report, supporting evidence and an agreed review route. Expanding the schema and examples changes scope; changing a prompt alone would hide that change. Keep damaged-goods cases outside automated handling until the revised specification is tested.

## Consider the alternative

An intake form, a record-comparison script or a better source feed may solve the first problem without generation. A coding agent can help implement the agreed slice, but its proposed code must face the same acceptance cases and review as manually written code.

The [organisation design reading](../../reference/research/04-implementation.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
