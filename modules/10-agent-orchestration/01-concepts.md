# Lesson 10.1: Orchestration decides how pieces of work connect

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Three specialists do not yet make a service

Harbour now has an assistant that checks order evidence, another that reads policy and a third that drafts a customer response. The team calls them a multi-agent system. But who combines their answers? Can they run together? What happens when policy lookup fails? Who owns the final response?

**Orchestration** is how an application coordinates those steps. It determines their order, what information passes between them, which results are required and what happens after a failure. The OpenAI Agents SDK supplies runtime components for this work; the organisation must still decide what work is appropriate and who can authorise effects.

## Defining an agent and running it are different acts

In the course, `Agent(...)` creates a configuration containing a name, instructions, a model and optional tools or other settings. `Runner.run(...)` starts a run. The runner manages the repeated model/tool interaction introduced in Module 9. A final result contains an output and other run information; it is more than a bare text string.

An **SDK**, or software development kit, is reusable code that helps applications use a platform. It removes repeated implementation work. It does not decide whether a credit should be permitted, which policy version is authoritative or how a reviewer should investigate a disagreement.

The [official SDK overview](https://developers.openai.com/api/docs/guides/agents/sdk) separates the SDK's loop from the application's deployment, tools, state and approval responsibilities. Here we examine the inspected Python course examples rather than treating a framework name as a guarantee of an operating design.

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
