# Lesson 13.1: Compare frameworks by the work they help you organise

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## The same goal, different machinery

Harbour has teams experimenting with different agent frameworks. One prefers Google ADK, another Pydantic AI, and a third wants a TypeScript implementation. They all demonstrate a worker that reads a task, creates steps, writes an output and marks the task complete.

A useful comparison holds the task reasonably stable and inspects the differences in execution, context, tool access, state and recovery. A popularity list or a count of successful demonstrations cannot tell Harbour which design fits its operating requirements.

The course's fifth week deliberately repeats a small board-and-file task across frameworks, then combines workers. That gives us a concrete basis for understanding both common patterns and important differences.

## Separate model, framework, protocol and application

A **model** generates predictions or text. A **framework** supplies reusable machinery for tools, loops, messages and other runtime behaviour. A **protocol** defines how components exchange particular kinds of requests and responses. An **application** combines those parts with a user-facing purpose and operating controls.

Changing the framework does not necessarily change the model. Two frameworks can call the same model with different prompts or tool descriptions, producing different results for reasons unrelated to the framework's scheduler. Likewise, a protocol can connect components built with different frameworks without making their business meanings agree.

Keep these variables separate when comparing results. Record model and prompt versions, source access, task definitions, iteration limits and the way success is assessed.

## What an adapter does

An **adapter** translates between interfaces. Suppose one framework returns `result.output` and another produces messages whose last item contains the answer. An adapter can convert both into an application record such as `status`, `text` and `source_ids`.

That common shape helps the application use either implementation. It does not guarantee identical semantics. A result labelled `done` may mean a final answer was generated, a file was written or a recipient accepted the work. Define the common contract before treating workers as interchangeable.

This is the same representation problem encountered in Module 5's retrieval sources, now applied to runtime results.

## A shared board provides a coordination mechanism

The course uses SQLite, a database stored in a local file, for goals and steps. A goal has no parent; a step names a parent goal. Status and result fields make progress visible across processes.

A database can coordinate access to records, but individual statements still need the right conditions. An unconditional update to `in_progress` records a claim without necessarily preventing another worker from claiming the same task. A stronger claim operation can update only a still-pending record and check whether it succeeded.

A **transaction** groups database work under defined consistency rules. It can protect a state transition without guaranteeing that an external file write or remote message happened exactly once. Those effects may sit outside the transaction.

## Agent-to-agent communication

**A2A**, or Agent2Agent, supplies a protocol for communicating with remote agents. The course includes a local concierge that delegates translation through a remote agent's advertised interface. The concierge uses an agent card describing that service.

A2A concerns communication between agent services. MCP, developed in Module 14, concerns interfaces to tools and context. They can be used together. Neither protocol establishes that one business unit has a mandate to act for another. The [A2A overview](https://a2a-protocol.org/latest/topics/what-is-a2a/) explains the communication scope; business ownership and service agreements remain application and organisational choices.

A direct function call may be simpler inside one application. A remote service interface becomes useful when the components need separate deployment, ownership or interaction across boundaries. It adds network failure, compatibility and access questions that a local call does not have in the same form.

## What the comparison should include

| Question | What to inspect |
|---|---|
| How does a run begin and end? | Invocation, event stream, stopping conditions |
| What does a tool expose? | Input schema, execution path, returned result |
| Where is state stored? | Session, checkpoint, database, file or remote service |
| How is authority applied? | Identity, scope, approvals and execution checks |
| What happens on failure? | Timeouts, partial results, retries and recovery ownership |
| How is completion established? | Self-report, file check, tests, receipt or recipient acceptance |
| Can the team maintain it? | Skills, debugging, compatibility and operating responsibilities |

A framework that produces a promising output but cannot fit the organisation's approval or recovery requirements is not yet a suitable deployment choice. A more elaborate framework is not inherently more useful than a small, inspectable loop.

## A comparison is an experiment

Use representative cases, including ambiguous and failing ones. Keep the relevant conditions consistent and record unavoidable differences. The course examples are a source of implementation patterns, not benchmark evidence that one framework is best for every organisation.

**Check:** Two workers both finish the translation task. One validates a written file; the other only returns a completion sentence. What additional checks would make their outcomes comparable? Explain why standardising the result dictionary is necessary but insufficient.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.
