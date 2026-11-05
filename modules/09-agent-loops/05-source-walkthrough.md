# Lesson 9.5: Test repeated calls and independent stopping limits

[Download the matching notebook](/downloads/09-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m09.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

run receives a planner function instead of constructing a hidden model client. Each iteration supplies accumulated observations and expects either a final answer or a structured tool request. The application validates the decision, rejects repeated call identifiers, invokes the same scoped dispatcher used in Module 2 and records the observation. A positive integer budget bounds iterations. scripted_planner supplies deterministic decisions for reproducible tests; it is not called an LLM. The optional live adapter in ai_orgdesign.live uses the provider protocol while retaining the dispatcher and a separate tool-call limit.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Supply a planner that always asks for the same call. Then change the call identifier on every step. Which independent bound remains necessary?

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m09 import run
request = {"kind":"tool", "id":"one", "name":"lookup_case", "arguments":{"case_id":"H-17"}}
assert run(lambda observations: request)["stop"] == "repeated_call"
print("Repeated call stopped")
```

**Interpretation.** The repeated-identifier check catches the first planner. Unique identifiers evade that check, so the iteration budget remains essential. A live service also needs timeouts, token and cost limits, cancellation and recovery. Tool checks still apply on every execution; a model instruction to behave carefully is not a substitute.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The supplied planner first reads H-17 and then returns an investigation statement. With a budget of one, the tool can run but the loop stops at budget before a final answer. Repeated call identifiers stop the loop instead of executing indefinitely. Reaching a stop condition does not mean the business case is resolved.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A fixed workflow is often easier to verify when the route is known. An adaptive loop is justified when observations genuinely determine the next action. Framework runners can implement the loop, but the application still owns permissions, budgets and accepted completion.

The [research connection](../../reference/research/03-decisions.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
