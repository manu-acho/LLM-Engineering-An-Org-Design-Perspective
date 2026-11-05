# Lesson 13.4: Read six frameworks through one repeated task

[Module route](README.md) · [Code workshop](02-code-workshop.md) · [Next module](../14-agent-integration/README.md)

## Keep the task in view

The course's comparison week begins with a worker translating a file and recording steps on a small board. The final project combines workers to build a language-game site. These deliberately visible outputs help us ask where a framework supplies machinery and where application code supplies the contract.

This tour explains the inspected course implementations. It is not a ranking, a complete account of each framework or a promise that the examples run unchanged with every later release. Follow the pinned source links to inspect the exact wiring.

## Google ADK: an agent, runner and session

In the [worker definition](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/1_google_adk_a2a/task_worker/agent.py), an `LlmAgent` receives instructions and tools for board operations and files. The [entry point](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/1_google_adk_a2a/worker.py) creates an `InMemoryRunner` and starts a run. Creating the agent is configuration; running it starts work.

The [remote concierge](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/1_google_adk_a2a/a2a_demo/spanish_concierge/agent.py) uses `RemoteA2aAgent` with a remote agent-card address. That is an example of a service boundary rather than a second function in the same process. Availability, identity and task responsibility must be considered at that boundary.

The [ADK documentation](https://adk.dev/agents/) provides current framework concepts. The organisational question remains which service is responsible for the returned translation and what happens if it cannot complete the request.

## Pydantic AI: functions, toolsets and a result object

The [Pydantic AI worker](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/2_strands_pydantic/pydantic_worker.py) passes ordinary board functions as tools, adds a filesystem toolset and calls `worker.run`. It opens the worker with `async with`, allowing managed resources to be cleaned up when the block exits. The application reads `result.output`.

The [official agent guide](https://ai.pydantic.dev/agents/) describes the framework's agent interface. Do not infer that this particular worker has a structured business output merely because the framework name includes Pydantic. Inspect the configured output type and the values returned by tools.

## AWS Strands: tool registration and invocation

The [Strands worker](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/2_strands_pydantic/strands_worker.py) registers board operations, attaches a filesystem MCP client and awaits `invoke_async`. The output is connected to the same board-and-file objective as the other workers.

The lesson to carry across is that a consistent task can be implemented through a different invocation interface. A model-generated completion sentence is still weaker evidence than an inspected file and an acceptance check. Compare the evidence returned to the caller, not only the ease of constructing an agent.

## Microsoft Agent Framework: a client and a managed tool connection

The [Microsoft worker](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/3_maf_agno/maf_worker.py) supplies a client, instructions and tools to its agent. Its filesystem connection is opened within an asynchronous resource block. Follow where that connection begins and ends: a tool becoming unavailable after cleanup is a resource-lifetime issue, not a change in what the model knows.

A business integration needs similar clarity about session ownership. Who starts the service, who can cancel it, and what task record remains if the process stops? Those responsibilities do not disappear behind a framework client.

## Agno: run the worker, then inspect the application record

The [Agno worker](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/3_maf_agno/agno_worker.py) connects filesystem tools, creates an `Agent`, and awaits `arun`. It uses the same board functions and can receive a task identity from the shared orchestrator.

That common record is what permits application-level comparison. The returned object and framework lifecycle may differ, but the business still needs to know whether the expected output exists, whether it is correct and who accepted it. An adapter should retain failure and uncertainty rather than convert every returned response into success.

## Mastra: the same ideas in TypeScript

[Step 1](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/4_mastra/step1.ts) creates an agent using a configuration object. `const` declares a binding and `new Agent` creates an instance. The code is TypeScript, which adds static type information to JavaScript; its `import` syntax and runtime setup differ from Python.

The [tools file](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/4_mastra/tools.ts) defines board tools using `createTool`. `inputSchema` declares accepted input structure, while `execute` contains the operation. An arrow function such as `async (...) => ...` defines asynchronous behaviour. A schema describes shape; it does not authenticate the caller or validate the truth of a completion claim.

The source also attaches a filesystem MCP client. Sharing a protocol lets different programming ecosystems use an interface, while each runtime still needs compatible resource handling and application controls.

## The hand-written loop and the orchestrator

The [final entry point](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/5_agent_loop/agent_loop.py) discovers worker implementations and assigns a common board path. The [orchestrator](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/5_agent_loop/orchestrator.py) exposes actions such as launch, wait, test and bounded repair to an ADK coordinator. “Hand-written” describes application orchestration around reusable framework components, not a system with no libraries.

The distinction matters when explaining an outcome. A successful site depends on task selection, file conventions, worker execution, checks and fallback behaviour, not a framework label alone. The same approach can help a business compare specialised components without letting each redefine completion.

## Use the tour to ask better questions

For any implementation, trace one task ID from creation to output and acceptance. Mark the model boundary, tool boundary, storage boundary and service boundary. Then ask what a failure at each point means for the people waiting on the work.

The most useful comparison may end with one shared runtime, a mix behind stable interfaces or a simpler application with no multi-agent coordination. The choice should follow the work, evidence and maintenance capacity rather than a requirement to use every framework encountered.

## Read the organisational connection

Different technical arrangements can distribute and reconnect contributions in different ways. The research chapter explains [division and integration](../../reference/research/01-organisation-design.md#division-creates-a-need-for-integration).
