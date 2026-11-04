# Lesson 13.2: A shared task board needs a precise claim rule

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## Stop two workers from both claiming the same task

The source course uses a SQLite board across its framework examples. This small independent example focuses on the claim transition. It uses an in-memory database, so no file survives after the program closes. It calls no agents and writes no external output.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("""CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    status TEXT NOT NULL,
    owner TEXT,
    result TEXT
)""")
connection.execute("INSERT INTO tasks (id, status) VALUES (?, ?)", (17, "pending"))
connection.commit()

def claim(connection, task_id, worker):
    with connection:
        changed = connection.execute(
            "UPDATE tasks SET status = ?, owner = ? WHERE id = ? AND status = ?",
            ("in_progress", worker, task_id, "pending")
        ).rowcount
    return changed == 1

def report(connection, task_id, worker, result):
    with connection:
        changed = connection.execute(
            "UPDATE tasks SET status = ?, result = ? "
            "WHERE id = ? AND owner = ? AND status = ?",
            ("reported_done", result, task_id, worker, "in_progress")
        ).rowcount
    if changed != 1:
        raise ValueError("Task is not held by this worker in the expected state")

print(claim(connection, 17, "worker-a"))
print(claim(connection, 17, "worker-b"))
report(connection, 17, "worker-a", "Draft prepared for review")
print(connection.execute("SELECT status, owner FROM tasks WHERE id = 17").fetchone())
connection.close()
```

Expected output:

```text
True
False
('reported_done', 'worker-a')
```

## The condition is part of the operation

`sqlite3.connect(":memory:")` creates a database for this connection. `execute` sends an SQL statement to it. The question marks are parameter placeholders. Values are supplied separately rather than inserted into SQL text, preventing ordinary values from being interpreted as SQL instructions.

The `claim` function does not first read the task and then unconditionally write a new owner. Its `WHERE` clause makes the expected state part of the update. The second claim finds no pending row because the first has already changed it. `rowcount` tells the caller whether the transition actually took place.

This two-call example demonstrates the condition. A real concurrent system must also handle transaction conflicts, locks, timeouts and retries appropriately. It should not infer exclusive ownership merely because an earlier read showed `pending`.

`with connection` commits or rolls back the relevant transaction; it does not close the connection. The explicit final `close` releases it. Persistence and cleanup are different responsibilities.

## Reported completion is deliberately separate

`report` checks both the worker and the current state. A different worker cannot report this task complete through this function. The status becomes `reported_done`, not `verified` or `accepted`.

This distinction preserves an evidence boundary. A worker report can record its claim. A file validator, a test or a receiving reviewer may be needed before the business accepts it. If the acceptance check fails, define how the task returns for correction and who owns that transition.

The worker name is only a string here. An operating system must bind it to trusted process or service identity rather than accept whichever name a caller chooses.

## Compare the original board

The course's [board implementation](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/1_google_adk_a2a/board.py) creates goals and steps with `parent_id`, records task status and stores result text. Its `claim_todo` sets `in_progress` by ID. It is intended to show progress for a selected worker; that statement does not implement the conditional exclusive claim demonstrated above.

The source configures SQLite's write-ahead logging mode and a busy timeout. These help manage access by several processes, but they do not invent missing business conditions in an update. Database machinery and the task-ownership rule solve different problems.

The [ADK worker](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/1_google_adk_a2a/worker.py) seeds a goal, marks it in progress and starts the framework runner. The [Pydantic AI worker](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/2_strands_pydantic/pydantic_worker.py) can either seed its own task or take a task ID supplied by an orchestrator. Follow the source of the task ID before interpreting a board status as worker discovery or independent allocation.

## The multi-framework orchestrator

The course's [orchestrator](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/5_agent_loop/orchestrator.py) launches workers, waits for tasks, checks outputs and allows a bounded repair attempt. The [entry point](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/5_agent_frameworks/5_agent_loop/agent_loop.py) sets a common board path and passes runtime configuration to workers.

These are application-level integration choices. The frameworks do not coordinate merely because they all have an `Agent` class. A shared record, agreed interfaces and an explicit orchestrator connect them. The fallback that creates a basic hub when the orchestrator stops early also illustrates a useful recovery design: leave an inspectable partial result rather than pretending the full agent plan succeeded.

## Further operating requirements

If a worker crashes after claiming, someone must reclaim or review the task. A **lease** is ownership that expires unless renewed; it is one possible design. It needs a rule preventing an old worker from later reporting a result after ownership has moved.

If completion depends on a file, retain the output identity and version. If a reviewer accepts the file, record that separate decision. If two systems use different meanings of complete, an adapter must preserve the difference rather than collapse both into `done`.

**Try it:** Attempt to report as `worker-b`, and attempt to report the same task again after `reported_done`. Then describe what the board should show when the worker produced a file but crashed before recording its result. Which evidence would permit safe recovery?

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.
