# Lesson 11.5: Find missing prerequisites and task cycles

[Download the matching notebook](/downloads/11-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m11.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

order_tasks receives a mapping from task names to prerequisite names. It first rejects unknown prerequisites. At each pass it finds tasks whose prerequisites are already done, sorts them to make the displayed order reproducible, and removes them from the remaining graph. If no task is ready while tasks remain, the graph has a cycle. This topological ordering exposes feasible precedence; it does not assign people, schedule elapsed time or create autonomous agents.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Make policy preparation depend on review while review already depends on compare and compare on policy. Explain why adding a faster worker cannot repair the resulting graph.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m11 import order_tasks
try:
    order_tasks({"a":["b"], "b":["a"]})
except ValueError:
    print("Cycle rejected")
else:
    raise AssertionError("Cycle not detected")
```

**Interpretation.** The dependencies form a cycle. No task can become ready under the stated rules. The design must change: supply an initial policy, permit an explicit iterative cycle with a stopping rule, or separate preliminary review from final review. Faster execution cannot remove a logical prerequisite contradiction.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

Records and policy preparation precede comparison, which precedes review. Both preparation tasks are independent in this graph, so a runtime could execute them concurrently. The printed sorted sequence is one valid order, not evidence that concurrency occurred.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A single generalist may reduce handoffs for small cases. Parallel specialists are useful when inputs are separable and outputs can be integrated. Reciprocal interdependence needs continuing adjustment rather than pretending every task fits a one-pass dependency graph.

The [research connection](../../reference/research/01-organisation-design.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
