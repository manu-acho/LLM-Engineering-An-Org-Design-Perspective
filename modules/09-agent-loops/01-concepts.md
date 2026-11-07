# Lesson 9.1: An agent chooses steps inside an application

[Download the matching notebook](/downloads/09-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Business context: Harbour

Explain what the agent may contribute and when it must return control to the investigator.

[Company and supply-chain context](../../HARBOUR.md) · [Module 9 business situation](../../reference/harbour-learning-journey.md#module-9)

## From answering a question to investigating a case

Harbour's assistant can summarise a delivery complaint. An account manager now asks it to investigate: find the order, compare the quantities, look for the applicable rule and prepare a response. The necessary next step depends on what the earlier steps reveal. If the order number is missing, searching policy first may accomplish little.

An **agent loop** lets a model propose a next action, lets an application carry it out, and returns the result to the model. The cycle repeats until the application receives an answer or reaches a limit. An agent is therefore not just a long prompt. There is a program deciding which requests can execute and when work stops.

Module 8 introduced bounded workflows. Here we open the loop itself and examine how apparently autonomous behaviour is produced. The engineering pattern can be useful without granting the model the organisation's authority to resolve the case.

## Four parts of the loop

A **goal** states what is being attempted. **Context** supplies the information available now. A **tool** exposes a particular operation, such as retrieving an order. **Control flow** determines what happens after a model response.

Suppose the model requests `lookup_order` with order ID `O-17`. The application checks that the name is permitted, the argument has the expected form and the current user may read that record. It calls the function and returns the result as a tool message. The model can then use that evidence in its next response.

The tool description is an explanation of an available operation. It is not the operation itself. A model can request a function that fails, request the wrong record or draw an unsupported conclusion from a successful result. Each failure belongs to a different part of the system.

## Why the result goes back into context

The model needs to see what happened. A tool-call identifier connects a result to the request it answers. In a conversation containing several calls, that identity prevents a returned quantity being mistaken for the answer to another question.

The evolving message list becomes a working record for the run. It may include the request, the model's proposed calls, their results and the final answer. This is context assembly, not retraining. A different model call can behave differently because the available evidence changed, even though the model's learned parameters did not.

Context also has limits. If a result is shortened, exceptions may disappear. If a tool returns a whole customer file, unrelated information may become visible. Choosing what the model sees is both an engineering choice and a choice about the information on which later decisions depend.

## A plan is a representation of intended work

The course's extra foundations lab lets an agent create a checklist and mark items complete. That makes its intended sequence visible. It does not independently show that the work was completed correctly. A model can call a completion tool after doing too little, or describe a successful action whose receipt was never checked.

Separate **planned**, **attempted**, **acknowledged** and **verified**. A plan says “check delivery”. A trace records a lookup attempt. A tool receipt records a response. Verification asks whether the response supports the relevant conclusion. These are four useful records, with different meanings.

## Where the loop ends

A **stopping condition** tells the program when to return control. It might be a final model answer, a maximum number of steps, a missing permission or a need for clarification. A request such as “keep trying until successful” is insufficient as the only boundary: success may be ambiguous and the loop can spend money or repeat actions.

Define a step budget and an outcome for exhaustion. Returning “needs a person to investigate” can be a valid result. It should not be disguised as successful resolution. Likewise, a timeout must leave the case somewhere visible rather than silently abandoning it.

A model's own assessment can help decide whether to continue. This is often called **reflection** or an **evaluator loop**. It adds another fallible judgement. Independent records and checks still matter, particularly when the evaluator receives only the worker's account of its performance.

## Start with the least complicated design that fits

A fixed sequence is easier to inspect when every case needs the same steps. A rule can route a missing order number to clarification without a model. An agent loop becomes attractive when the evidence genuinely changes the useful next action and the flexibility is worth the extra uncertainty.

An inspectable loop separates the planner, the tool registry, permission checks, observations and stopping rules. The supplied implementation exposes those components directly, with a scripted planner for repeatable tests and a separately gated live-model adapter.

**Explain it back:** An assistant reports “investigation complete” after three calls. What records would let you distinguish correct investigation from a plausible completion story? Include the original question, actual call results, unresolved evidence and an accountable next step.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

The application bounds available steps while organisational authority remains a separate question. The research chapter explains [permission and authority](../../reference/research/03-decisions.md#permission-and-authority).

## Practical activity: Observe the difference between a scripted planner and a model proposal.





The exercise code below runs from a prepared course checkout. In the matching notebook, the setup cell already supplies ROOT and RUN_LIVE. If following the code here, run this setup first:

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

Was scripted_planner a live language model?

```python
from ai_orgdesign.labs.m09 import run, scripted_planner
result = run(scripted_planner)
print(result)
assert result["stop"] == "final"
```

No. It is controlled code that makes the loop repeatable for tests. The live activity replaces the planner, not the application checks.

### Complete the exercise

Write the prediction before consulting the worked answer: Was scripted_planner a live language model?

**Worked answer.** No. It is controlled code that makes the loop repeatable for tests. The live activity replaces the planner, not the application checks.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
