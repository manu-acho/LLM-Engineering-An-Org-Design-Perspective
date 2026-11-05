# Lesson 13.2: Run the same task in Python and LangGraph

[Download the matching notebook](/downloads/13-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Frameworks package execution conventions. A framework change should not silently change what counts as evidence, how errors are represented or who accepts an output. A plain-Python baseline makes those invariants visible.

The implementation lives in `src/ai_orgdesign/labs/m13.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

State is a TypedDict describing named fields for tooling; it does not validate them at runtime. inspect_record reads the scoped fictional case and returns only the updated difference and status. plain merges those updates with the input dictionary. graph registers the same function as a LangGraph node, links START to inspect and inspect to END, then compiles the graph. invoke runs the compiled graph. Comparing both results isolates execution packaging while holding the business function constant.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m13 import plain, graph
inputs = {"case_id":"H-17", "tenant":"north"}
assert plain(inputs) == graph().invoke(inputs)
print(graph().invoke(inputs))
```

Both routes return case H-17 in north, difference two and status review. Equality checks observable output for this one contract. It does not establish equivalent persistence, retries, streaming or remote-service behaviour. This is a real framework run with deterministic nodes, not a framework-generated language answer.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** List three features that would require additional comparison tests before replacing an established runtime. Explain why passing this one equivalence check is useful but insufficient.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** Persistence across interruption, treatment of a failed tool and cancellation of concurrent work are three candidates. Authentication propagation, ordering, tracing and nested budgets may also differ. The small equivalence check catches changed task results, but only tests the behaviours actually exercised.

## Consider the alternative

The course implements one framework and one plain runtime rather than assuming identical behaviour across many SDKs. Other frameworks can be evaluated through the same contract suite. A remote agent interface adds network, identity and partial-failure obligations that a second local function does not have.

The [organisation design reading](../../reference/research/02-coordination.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
