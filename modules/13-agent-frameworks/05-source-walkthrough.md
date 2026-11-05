# Lesson 13.5: Compare runtime outputs and failure boundaries

[Download the matching notebook](/downloads/13-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m13.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

State is a TypedDict describing named fields for tooling; it does not validate them at runtime. inspect_record reads the scoped fictional case and returns only the updated difference and status. plain merges those updates with the input dictionary. graph registers the same function as a LangGraph node, links START to inspect and inspect to END, then compiles the graph. invoke runs the compiled graph. Comparing both results isolates execution packaging while holding the business function constant.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

List three features that would require additional comparison tests before replacing an established runtime. Explain why passing this one equivalence check is useful but insufficient.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m13 import plain
try:
    plain({"case_id":"H-18", "tenant":"north"})
except PermissionError:
    print("The shared scope rule survives the runtime boundary")
else:
    raise AssertionError("Scope check failed")
```

**Interpretation.** Persistence across interruption, treatment of a failed tool and cancellation of concurrent work are three candidates. Authentication propagation, ordering, tracing and nested budgets may also differ. The small equivalence check catches changed task results, but only tests the behaviours actually exercised.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

Both routes return case H-17 in north, difference two and status review. Equality checks observable output for this one contract. It does not establish equivalent persistence, retries, streaming or remote-service behaviour. This is a real framework run with deterministic nodes, not a framework-generated language answer.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. The course implements one framework and one plain runtime rather than assuming identical behaviour across many SDKs. Other frameworks can be evaluated through the same contract suite. A remote agent interface adds network, identity and partial-failure obligations that a second local function does not have.

The [research connection](../../reference/research/02-coordination.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
