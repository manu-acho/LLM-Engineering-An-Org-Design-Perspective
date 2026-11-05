# Lesson 13.5: Follow the same worker through two real framework implementations

[Module route](README.md) · [Next: design shared ownership](06-design-lab.md)

## Hold the task constant

The source comparison uses a visible task: read `notes.txt`, translate it into Spanish, write `spanish.txt` and record progress on a board. The task crosses model, storage, filesystem and process boundaries. Following it closely is more informative than comparing framework names in a feature list.

This is a source-reading walkthrough, not an instruction to launch the original worker. Its seed path resets the teaching board and removes an earlier output. Model runs can also create paid requests and launch a filesystem server. No original worker is executed by this lesson.

## Google ADK: find configuration before invocation

Open [the agent definition](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/1_google_adk_a2a/task_worker/agent.py). `LlmAgent` receives model, instructions and tools. Board functions list work, add steps and mark tasks complete. `McpToolset` supplies filesystem operations through a subprocess configured with a workspace directory.

The tool connection specifies an executable, arguments and working directory. That is a real process boundary. The agent's instructions describe the desired sequence, but the model chooses particular tool requests within the available surface.

Now read [worker.py](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/1_google_adk_a2a/worker.py). `seed` prepares the board and returns a goal ID. The entry point marks it in progress, then `asyncio.run` enters a coroutine that creates `InMemoryRunner` and calls `run_debug`. Afterwards, the script displays the board and reads the output file if it exists.

The final file-existence branch is an observation after execution. It is not a full translation-quality test. An in-memory runner also does not establish durable recovery after process failure.

## Pydantic AI: follow startup arguments before imports

The [Pydantic worker](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/2_strands_pydantic/pydantic_worker.py) has two modes. Standalone mode seeds its own task. Orchestrated mode receives a task ID and shared board path from command-line arguments.

It sets `BOARD_PATH` before importing the board module because that module chooses its path at import time. Reordering imports could silently connect the worker to another board. Configuration timing is part of execution semantics, not cosmetic style.

The worker creates an `Agent` with board functions and a filesystem toolset. `async with worker` manages resources around `await worker.run(message)`. The application then reads `result.output`. Returning from that call and cleaning up the tool connection are related but different lifecycle events.

In orchestrated mode, it works one supplied task rather than resetting the entire board. A task ID therefore carries a coordination contract from caller to worker. The source of that ID matters as much as the framework invocation.

## Compare the concrete boundaries

| Concern | ADK source path | Pydantic AI source path |
|---|---|---|
| Agent definition | `LlmAgent` and tools | `Agent` and tools/toolsets |
| Run machinery | `InMemoryRunner.run_debug` | `await worker.run` |
| Tool lifecycle | MCP toolset configuration | Managed worker resource block |
| Work identity | Seeded goal in the standalone entry point | Seeded goal or caller-supplied task ID |
| Result observation | Board and file read | Framework output plus board/file observation |

Different interfaces do not imply different organisational outcomes. Hold source text, task, model conditions and acceptance criteria as consistent as feasible, then inspect failure and resource behaviour.

## Extend to the remaining frameworks

Use the [six-framework tour](04-framework-tour.md) for Strands, Microsoft Agent Framework, Agno and Mastra. For each, mark agent construction, invocation, tool resources, task identity and returned result. TypeScript's promises and `await` serve a comparable asynchronous role, but its runtime and package environment differ from Python.

**Worked diagnosis:** A worker marks a task done but the file is absent. Do not rewrite every framework adapter first. Check the task's working directory, tool output, board transition and acceptance policy. The shared task contract must distinguish self-reported completion from an inspected and accepted artefact.

## Read the organisational connection

A framework comparison should distinguish an available interface from selected configuration and actual use. The research chapter explains [capability, configuration, practice and outcome](../../reference/research/04-implementation.md#capability-configuration-practice-and-outcome).
