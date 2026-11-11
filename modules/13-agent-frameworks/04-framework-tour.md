# Lesson 13.4: Compare runtime responsibilities through a common task

[Download the matching notebook](/downloads/13-04-framework-tour.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## What you'll learn and why it matters

Compare what different runtimes supply for the same task. State a condition that must stay true when the implementation changes.

## Business context: Harbour

An invariant is a condition that should remain true when the implementation changes. For example, the brief must keep the customer's report separate from confirmed receipt. Write down that expectation, then compare which part of each runtime checks it and what happens when a result breaks it.

Run the Agents SDK path with the same explicit evidence and output requirements.

[Company and supply-chain context](../../HARBOUR.md) · [Module 13 business situation](../../reference/harbour-learning-journey.md#module-13)

## Begin with the invariant

A runtime is the software that executes and coordinates operations. Plain Python executes ordinary function calls. LangGraph executes named nodes and transitions over state. Both can implement the same business contribution. Neither makes that contribution autonomous merely by running it.

State is a TypedDict describing named fields for tooling; it does not validate them at runtime. inspect_record reads the scoped fictional case and returns only the updated difference and status. plain merges those updates with the input dictionary. graph registers the same function as a LangGraph node, links START to inspect and inspect to END, then compiles the graph. invoke runs the compiled graph. Comparing both results isolates execution packaging while holding the business function constant.

## State shape and runtime validation

TypedDict documents expected field names and types for development tools. Python does not enforce that description automatically. Pydantic can check an incoming structure, but a valid field can still name the wrong case. The application must retain scope and semantic acceptance checks in either runtime.

## Compare features with tests

The two routes are compared on returned fields and scope rejection. More demanding replacement decisions should also test persistence, retries, cancellation, streaming, resource cleanup and identity propagation. Describe the observable contract for each feature before selecting a framework.

A remote agent adds a service boundary. Requests can time out, the remote service may be unavailable and a response may arrive after a caller cancels. Agent-to-agent protocols can describe capabilities and task states, but business acceptance and authority still need explicit ownership. This course does not claim that the local graph exercise tests a remote protocol.

## Choose the smallest useful runtime

The course implements one framework and one plain runtime rather than assuming identical behaviour across many SDKs. Other frameworks can be evaluated through the same contract suite. A remote agent interface adds network, identity and partial-failure obligations that a second local function does not have.

**Exercise.** List three features that would require additional comparison tests before replacing an established runtime. Explain why passing this one equivalence check is useful but insufficient.

**Worked answer.** Persistence across interruption, treatment of a failed tool and cancellation of concurrent work are three candidates. Authentication propagation, ordering, tracing and nested budgets may also differ. The small equivalence check catches changed task results, but only tests the behaviours actually exercised.

For the actual API used here, consult the [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart). The official example is optional further reading; the complete local graph is included in the course package.

## Practical activity: Run the same evidence contract through the OpenAI Agents SDK.

 An asynchronous operation can suspend while compatible work proceeds. The notebook uses await to obtain its result; this is different from a business acceptance acknowledgement.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

```python
from ai_orgdesign.workspace import project_root, live_mode
ROOT = project_root()
RUN_LIVE = live_mode()
if RUN_LIVE:
    from ai_orgdesign.provider import Gateway
    gateway = Gateway(max_requests=12, max_output_tokens=1000)
print("Live mode:", RUN_LIVE)
```

### Predict and follow the values

Is a framework's valid output automatically evidence-supported?

```python
from ai_orgdesign.investigation import Brief
print("Shared output fields:",list(Brief.model_fields))
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.frameworks import agents_sdk_run
    result=await agents_sdk_run(gateway)
    print(result["brief"])
    print(result["sdk_usage"])
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. The same application checks still compare case facts and source membership.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A stable condition such as keeping reported and confirmed quantities separate gives the comparison a basis. State and failure handling can vary even when successful outputs look alike.

## What this means for the business process

Test the shared condition in each runtime, including missing and conflicting evidence. Require a useful refusal that reaches the case owner, so a framework substitution does not quietly change what the service promises.

For the research behind this design choice, read [Four questions for a usable contribution](../../reference/research/02-coordination.md#four-questions-for-a-usable-contribution).

## Next lesson

The next workshop compares returned factual fields and failures from actual runtime paths. [Lesson 13.5: Compare runtime outputs and failure boundaries](05-source-walkthrough.md).
