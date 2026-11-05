# Lesson 9.2: Run a bounded investigation loop

[Download the matching notebook](/downloads/09-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

An agent loop chooses another step after observing an earlier result. That flexibility can help an investigation, but also creates repeated calls, unexpected branches and uncertain completion. The application must bound the execution independently of the planner.

The implementation lives in `src/ai_orgdesign/labs/m09.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

run receives a planner function instead of constructing a hidden model client. Each iteration supplies accumulated observations and expects either a final answer or a structured tool request. The application validates the decision, rejects repeated call identifiers, invokes the same scoped dispatcher used in Module 2 and records the observation. A positive integer budget bounds iterations. scripted_planner supplies deterministic decisions for reproducible tests; it is not called an LLM. The optional live adapter in ai_orgdesign.live uses the provider protocol while retaining the dispatcher and a separate tool-call limit.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m09 import run, scripted_planner
assert run(scripted_planner)["stop"] == "final"
assert run(scripted_planner, budget=1)["stop"] == "budget"
print(run(scripted_planner))
```

The supplied planner first reads H-17 and then returns an investigation statement. With a budget of one, the tool can run but the loop stops at budget before a final answer. Repeated call identifiers stop the loop instead of executing indefinitely. Reaching a stop condition does not mean the business case is resolved.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Supply a planner that always asks for the same call. Then change the call identifier on every step. Which independent bound remains necessary?

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The repeated-identifier check catches the first planner. Unique identifiers evade that check, so the iteration budget remains essential. A live service also needs timeouts, token and cost limits, cancellation and recovery. Tool checks still apply on every execution; a model instruction to behave carefully is not a substitute.

## Consider the alternative

A fixed workflow is often easier to verify when the route is known. An adaptive loop is justified when observations genuinely determine the next action. Framework runners can implement the loop, but the application still owns permissions, budgets and accepted completion.

The [organisation design reading](../../reference/research/03-decisions.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
