# Lesson 13.4: Compare runtime responsibilities through a common task

[Download the matching notebook](/downloads/13-04-framework-tour.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

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
