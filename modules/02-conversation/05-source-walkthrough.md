# Lesson 2.5: Trace call identity, scope and incremental output

[Download the matching notebook](/downloads/02-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m02.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

The conversation function creates a fresh history list for each call. A scripted call carries an identifier, a capability name and an arguments dictionary. dispatch permits only lookup_case with exactly one case_id field, then lookup checks the tenant before returning a copy of the record. Serialising that result makes the tool observation inspectable without changing the authoritative record. stream_words yields one word at a time; it demonstrates incremental delivery without pretending that a model produced the words.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Request H-18 while keeping the north scope. Predict whether the record will be returned and whether changing a name inside a model message should alter that decision.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.business import dispatch
try:
    dispatch("lookup_case", {"case_id": "H-18"}, "north")
except PermissionError:
    print("Expected: cross-scope read denied")
else:
    raise AssertionError("Scope boundary failed")
```

**Interpretation.** lookup raises PermissionError because H-18 belongs to south. Identity and scope enter through the application, not the request text. A real authentication system would supply that trusted scope; this local function parameter is a teaching boundary, not authentication.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The selected case is H-17, its ordered quantity is twelve and its reported quantity is ten. The tool observation has call_id equal to call-1. Joining the stream pieces reconstructs Evidence awaits review, with a trailing space. Nothing approves a remedy.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A form with a required case identifier may be more dependable than extracting it from chat. A provider adapter can propose the same tool call, but should not bypass dispatch. Streaming can improve perceived responsiveness while adding partial-output and cancellation problems.

The [research connection](../../reference/research/03-decisions.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
