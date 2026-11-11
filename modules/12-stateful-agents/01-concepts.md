# Lesson 12.1: State lets a workflow pause, recover and continue

[Module route](README.md) · [Next lesson](02-code-workshop.md)

A claim may wait overnight for a human decision. The next day, the program needs a saved account of what it knows and where the work stopped. That account is state. A graph describes the steps and paths between them; a checkpoint saves state at a boundary where work can later continue. Follow the case from drafting to the point it waits for review.

## A review that takes until tomorrow

Harbour's assistant has gathered evidence and prepared a proposal. Finance cannot review it until the next morning. The application needs to remember which case is waiting, what version was proposed and what happens after a reviewer responds. Keeping a Python function running overnight is a fragile way to do that.

**State** is the recorded information describing where work stands. A stateful workflow makes that information explicit so execution can pause and resume. It also makes choices visible: what is remembered, which updates replace earlier values and what must be rechecked after a delay.

## Graphs connect functions and decisions

LangGraph represents work through nodes and edges. A **node** performs a step and returns state updates. An **edge** connects steps. A **conditional edge** chooses a route based on the current result, such as returning from a tool to the model or sending an incomplete case for clarification.

On paper the path could be “prepare brief → check evidence → request review”. A failed evidence check could instead take the case to “ask for clarification”. Those steps are nodes; the arrows are edges. At review, record the case identifier and draft in saved state. The next day's run needs both the stored facts and the point where work stopped.

A node need not call a model. The course begins with a graph producing a simple sentence, then adds model calls, tools and memory. This order exposes the underlying scheduling pattern before introducing probabilistic behaviour.

The graph is a program representation. Its arrows say which transitions are possible in that version. They do not establish that a receiving employee has accepted responsibility or that an external action succeeded.

## A reducer decides how updates combine

Suppose one node returns a new message. Should that message replace the entire conversation or be combined with earlier messages? A **reducer** supplies the update rule for a state field.

The course uses `Annotated` with `add_messages` to associate message state with a reducer. Conceptually, the annotation tells the framework how to apply an update. Plain type hints alone do not perform validation or define all runtime behaviour. The function associated with the field matters.

Combination rules can also create business consequences. Appending every assessment may preserve disagreements but require later reconciliation. Replacing a record may remove useful history. Adding two monetary values is sensible only if they represent distinct contributions rather than duplicate reports of one transaction.

## Checkpoints, threads and longer-term memory

A **checkpoint** records graph state at an execution boundary. A **thread identifier** associates successive runs with a particular conversation or work item. Using the wrong thread can mix cases; creating a new one unexpectedly can lose continuity.

The course shows an in-memory checkpointer and also discusses file-backed storage. An in-memory store can support continuation while its process lives, but it does not survive a process restart. **Durability** means records remain available after the failure conditions the design is meant to withstand. A persistent database needs its own access, retention, recovery and migration arrangements.

The [LangGraph persistence guide](https://docs.langchain.com/oss/python/langgraph/persistence) distinguishes thread-scoped checkpoints from stores for application-defined information across threads. “Memory” is therefore not one universal feature and does not mean retraining the model.

## Interrupt and resume

An **interrupt** pauses work and surfaces a request for external input. A later command supplies a review result and resumes the workflow. The application must ensure that the response belongs to the right case, proposal and reviewer.

On resumption, some node code may execute again. External effects before an interruption need careful design so replay does not repeat them. The [interrupt documentation](https://docs.langchain.com/oss/python/langgraph/interrupts) explains this behaviour. Checkpointing and exactly-once business effects are separate problems.

A stale approval is another risk. If the proposal changes while review is pending, an approval of the earlier version must not silently authorise the new one. Preserve version identity and decide what changes require renewed review.

## Layers of abstraction in the course

The inspected week distinguishes lower-level model/tool building blocks, LangGraph orchestration, LangChain's `create_agent`, and Deep Agents. A higher layer can supply repeated machinery such as planning, filesystem access or subagent delegation. It also chooses defaults that deserve inspection.

The Sidekick application wraps a worker with an evaluator, attempt limits and middleware. **Middleware** is code that intercepts or augments a step, for example to apply a call limit or pause a named tool. The application configures an in-memory checkpointer; its evaluator sees selected evidence rather than every aspect of the outside world.

## Choose state for the business question

Store the case identity, relevant source versions, proposal revision, pending action and authority evidence when those are needed for continuation. Avoid treating a long chat transcript as the only business record. Conversation text may be helpful context while leaving essential commitments ambiguous.

**Check:** A vendor says its agent has memory and human approval. Ask what is stored, how cases are separated, what survives a restart, which actions pause and which proposal version an approval covers. Explain why each answer affects the operating design.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Saved state preserves selected information rather than the entire situation in which work occurred. The research chapter explains [the limits of recorded evidence](../../reference/research/05-routines.md#what-logs-can-show).
