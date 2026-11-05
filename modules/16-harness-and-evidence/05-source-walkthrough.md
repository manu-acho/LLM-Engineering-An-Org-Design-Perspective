# Lesson 16.5: Trace instruction identity, time and assumed cost

[Download the matching notebook](/downloads/16-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m16.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

harness wraps the bounded loop from Module 9. It hashes a fixed instruction string, measures elapsed time with perf_counter, counts recorded tool calls and preserves the stop reason. It explicitly leaves provider_usage as None because the scripted planner makes no model request. estimate_cost multiplies token counts by assumed prices per million tokens and rejects negative inputs. The resulting number is illustrative arithmetic, not billed cost.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Suppose a run stopped after reading the case but before writing its final response. Decide which trace fields distinguish that failure from a denied tool call and from an unresolved business investigation.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m16 import harness
from ai_orgdesign.labs.m09 import scripted_planner
print(harness(scripted_planner))
```

**Interpretation.** A step-level record should distinguish requested, authorised, started, completed and failed operations, with bounded identifiers and exception categories. A final loop stop reason is not a full audit trail. An unresolved business case can coexist with a technically successful run; an execution error can coexist with a correct earlier read.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The supplied loop uses one tool call and stops with final. Elapsed time is measured at runtime and will vary. The assumed cost calculation for one thousand input tokens at one unit per million and two hundred output tokens at four units per million is 0.0018 currency units. No actual provider usage is claimed.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. Structured local logs are sufficient for the first experiment. A tracing service can correlate distributed spans and evaluations, but needs retention, access and redaction rules. Recording hidden reasoning is neither required nor an adequate explanation of evidence support.

The [research connection](../../reference/research/05-routines.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
