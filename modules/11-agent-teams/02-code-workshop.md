# Lesson 11.2: Schedule tasks through their dependencies

[Download the matching notebook](/downloads/11-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Adding specialists can improve local expertise while increasing integration work. The first design question is what depends on what, not how many named agents can be created.

The implementation lives in `src/ai_orgdesign/labs/m11.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

order_tasks receives a mapping from task names to prerequisite names. It first rejects unknown prerequisites. At each pass it finds tasks whose prerequisites are already done, sorts them to make the displayed order reproducible, and removes them from the remaining graph. If no task is ready while tasks remain, the graph has a cycle. This topological ordering exposes feasible precedence; it does not assign people, schedule elapsed time or create autonomous agents.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m11 import order_tasks, demo
print(demo())
assert order_tasks({"a":[], "b":["a"]}) == ["a", "b"]
```

Records and policy preparation precede comparison, which precedes review. Both preparation tasks are independent in this graph, so a runtime could execute them concurrently. The printed sorted sequence is one valid order, not evidence that concurrency occurred.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Make policy preparation depend on review while review already depends on compare and compare on policy. Explain why adding a faster worker cannot repair the resulting graph.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The dependencies form a cycle. No task can become ready under the stated rules. The design must change: supply an initial policy, permit an explicit iterative cycle with a stopping rule, or separate preliminary review from final review. Faster execution cannot remove a logical prerequisite contradiction.

## Consider the alternative

A single generalist may reduce handoffs for small cases. Parallel specialists are useful when inputs are separable and outputs can be integrated. Reciprocal interdependence needs continuing adjustment rather than pretending every task fits a one-pass dependency graph.

The [organisation design reading](../../reference/research/01-organisation-design.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
