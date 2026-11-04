# Part II: Agent engineering for organisational work

[Guide index](README.md) · [Start here](START-HERE.md) · [Agents source guide](reference/agents-source-guide.md)

An assistant that answers questions is different from a system that selects steps, uses tools, waits for review and passes work to other services. That shift creates new engineering problems and new organisational choices. Who may act? What counts as completion? Who owns a case when a step fails?

Part II develops those questions through six modules inspired by [Ed Donner's Agents course](https://github.com/ed-donner/agents). It builds on the first part of this guide and keeps the same connection between concepts, code and business application. Frameworks are studied as ways to implement work, not as substitutes for designing the work itself.

## Choose a route

| Module | Understand | Inspect | Apply |
|---|---|---|---|
| [9. Agent loops](modules/09-agent-loops/README.md) | Goals, context, tools and stopping conditions | A bounded dispatch loop | Intake promises and accepted responsibility |
| [10. Orchestration](modules/10-agent-orchestration/README.md) | SDK runs, parallel work, specialists and handoffs | Required evidence and separate authorisation | Receiving ownership and review capacity |
| [11. Agent teams](modules/11-agent-teams/README.md) | CrewAI roles, tasks and processes | Configuration and task dependencies | Integration, independence and local fit |
| [12. Stateful agents](modules/12-stateful-agents/README.md) | Graphs, memory, checkpoints and interrupts | Proposal versions and resumption | Waiting, discretion and recovery ownership |
| [13. Frameworks](modules/13-agent-frameworks/README.md) | Runtime interfaces, shared state and A2A | A task board, six frameworks and an orchestrated worker comparison | Common contracts across organisational boundaries |
| [14. Business integration](modules/14-agent-integration/README.md) | MCP capabilities, context and access | Discovery, scope and source-backed operations | Service ownership and an end-to-end pilot plan |

Each module has six or seven lessons: introductory concepts and code, an organisational discussion, focused technical depth, a source or library walkthrough and a completed design case. Frameworks and integration also include additional comparative or service lessons. The [local lab guide](reference/local-labs.md) separates exercises that run without external services from integrations requiring model access. Follow the complete module route before treating a small mechanism as an operating application.

## Build on what you already understand

If you are new to programming and models, begin with [Part I](README.md#part-i-ai-engineering-foundations). The most direct preparation is [Module 2](modules/02-conversation/README.md) on tools and permissions, [Module 4](modules/04-evaluation/README.md) on evaluation, [Module 5](modules/05-rag/README.md) on evidence retrieval and [Module 8](modules/08-agents/README.md) on workflow and recovery.

If you already know those mechanisms, start with Module 9. Use the earlier lessons when a term needs more explanation. The additional material goes deeper into agent execution; it does not assume that creating more agents is the right answer to every business problem.

## Follow Harbour into an operating service

Harbour Services remains fictional. Its disputed delivery now passes through a service that collects evidence, requests specialist advice, pauses for review and connects to shared capabilities. Each new technical pattern lets us ask a sharper question about the design of work.

| Technical mechanism | Organisation-design question |
|---|---|
| Tool registry and bounded loop | Which actions may the assistant attempt, and what promise does the user understand? |
| Specialist call or handoff | Who retains the case, and who has accepted the next contribution? |
| Task context and reviewer | Which evidence crosses a boundary, and can the review challenge it independently? |
| Checkpoint and approval version | What exactly was agreed, and who owns work while it waits? |
| Shared board and adapter | Do different teams mean the same thing by complete? |
| MCP service and context selection | Who owns capability semantics, source authority and permitted effects? |

These questions draw on literature from organisation design research. The [literature guide](reference/literature-guide.md) explains the concepts and links directly to the reviews. Their application to Harbour is a reasoned interpretation, not an observed business outcome.

## Finish with an integration decision

The [final integration plan](modules/14-agent-integration/04-integration-plan.md) brings the parts together. It asks for a bounded service problem, an appropriate technical design, explicit responsibilities, a simpler alternative and evidence that could support or challenge a pilot.

A successful learning outcome is being able to explain both what the code does and why that operation would, or would not, help particular people accomplish their work.
