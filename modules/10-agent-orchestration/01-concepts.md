# Lesson 10.1: Orchestration decides how pieces of work connect

[Download the matching notebook](/downloads/10-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Business context: Harbour

Identify the dependency between obtaining evidence, interpreting policy and accepting a combined brief.

[Company and supply-chain context](../../HARBOUR.md) · [Module 10 business situation](../../reference/harbour-learning-journey.md#module-10)

## Three specialists do not yet make a service

Harbour now has an assistant that checks order evidence, another that reads policy and a third that drafts a customer response. The team calls them a multi-agent system. But who combines their answers? Can they run together? What happens when policy lookup fails? Who owns the final response?

**Orchestration** is how an application coordinates those steps. It determines their order, what information passes between them, which results are required and what happens after a failure. The OpenAI Agents SDK supplies runtime components for this work; the organisation must still decide what work is appropriate and who can authorise effects.

## Defining an agent and running it are different acts

In the course, `Agent(...)` creates a configuration containing a name, instructions, a model and optional tools or other settings. `Runner.run(...)` starts a run. The runner manages the repeated model/tool interaction introduced in Module 9. A final result contains an output and other run information; it is more than a bare text string.

An **SDK**, or software development kit, is reusable code that helps applications use a platform. It removes repeated implementation work. It does not decide whether a credit should be permitted, which policy version is authoritative or how a reviewer should investigate a disagreement.

The [official SDK overview](https://developers.openai.com/api/docs/guides/agents/sdk) separates the SDK's loop from the application's deployment, tools, state and approval responsibilities. Here the typed contribution and acceptance checks make that boundary concrete.

## Fixed sequence and parallel work

Order evidence and policy retrieval might be independent once the request is identified. They can overlap. Drafting depends on both, so it should wait until the required results are available.

**Asynchronous** code can pause while an operation waits and allow other suitable work to proceed. `async def` defines a coroutine function; `await` waits for an asynchronous result without requiring the whole application to sit idle. It does not make ordinary Python calculations magically parallel.

`asyncio.gather` can await several coroutine operations together. The default exception behaviour matters: a failure is propagated to the caller, while other submitted operations may still be running. “The group failed” does not necessarily mean “nothing happened”. This becomes important when any branch sends messages or changes records.

## Specialists as tools, or a handoff?

A **specialist-as-tool** pattern lets a main agent request help and use the returned result. The main agent retains responsibility for composing the final answer within that workflow. In the course, `as_tool` exposes another agent through a tool interface.

A **handoff** transfers the active conversation branch to another agent. That specialist continues with a different configuration. It is a runtime change in who handles the model conversation, not proof that a human department has accepted a business case.

The [official orchestration guide](https://developers.openai.com/api/docs/guides/agents/orchestration) distinguishes those control patterns. Prefer a specialist call when the original coordinator needs an answer back. Consider a handoff when a specialist should continue the conversation. A fixed application route may be clearer when the category and ownership rule are already explicit.

## Structured results and guardrails

A **structured output** has fields that software can inspect, such as `supported`, `source_ids` and `missing_information`. Validation can check the expected shape and types. It cannot establish that the supporting source really says what the answer claims.

A **guardrail** is an automatic check placed at a defined boundary. Some checks use ordinary code; others ask a model to assess an output. A model-based professionalism check is evidence about wording, not a business authorisation.

Position matters. A final-output check cannot undo an email already sent by an earlier tool. Agent-level checks should not be assumed to wrap every nested operation. The [official guardrail guidance](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) distinguishes automatic validation, tool checks and approval pauses. Inspect what is checked, when it is checked and which path could bypass it.

## Traces help explain events

A **trace** connects events within a run, such as specialist calls and returned results. It helps answer “where did this failure begin?” It does not establish that the business process achieved its purpose. A trace may record successful drafting while the receiving team rejects the handoff.

Decide which data belongs in traces and who may inspect it. Context useful for debugging can contain customer or employee information. A business audit trail additionally needs evidence linking a request, approval, action and acknowledged result.

**Check:** Choose between parallel calls, a specialist-as-tool and a handoff for three cases: independent evidence gathering, asking a policy expert a bounded question, and transferring an unresolved conversation to a specialist service. Explain the dependency and ownership assumptions behind each choice.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Orchestration is assessable when the connected contributions and their dependencies are explicit. The research chapter explains [dependency management](../../reference/research/02-coordination.md#identify-what-depends-on-what).

## Practical activity: Define the receiving contract before naming a specialist.





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

Which required field identifies the evidential basis?

```python
from ai_orgdesign.investigation import Specialist
print(Specialist.model_json_schema()["required"])
assert "sources" in Specialist.model_json_schema()["required"]
```

sources identifies the returned basis, whose membership and meaning still need checking.

### Complete the exercise

Write the prediction before consulting the worked answer: Which required field identifies the evidential basis?

**Worked answer.** sources identifies the returned basis, whose membership and meaning still need checking.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
