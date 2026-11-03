# Python patterns to recognise in the course

[Guide index](../README.md)

This reference explains the programming vocabulary used by the modules. Examples here are original teaching examples. They do not require model access.

## Read a function as a contract

For any function, identify its input, output, side effects and failures. `summarize(url)` returns text but also fetches a remote page and invokes inference. `make_messages(text)` can be a pure transformation if it depends only on the supplied arguments. Keeping pure transformations separate from I/O makes a system easier to inspect.

```python
def make_record(text, source_id):
    return {"text": text.strip(), "source_id": source_id}

record = make_record("  A handoff occurs here.  ", "interview-01")
```

The function's name alone does not reveal a contract. Look at its body, returned values and exceptions.

## Containers and transformations

| Syntax | Meaning | Course use |
|---|---|---|
| `[]` | Ordered list | Conversation messages, chunks, predictions |
| `{key: value}` | Dictionary | Message fields, metadata, tool registries |
| `set()` | Unique members | Duplicate detection, already-processed IDs |
| `(value,)` | One-element tuple | SQL parameters |
| `[f(x) for x in xs]` | Transform each element | Convert items into records |
| `[x for x in xs if condition]` | Filter elements | Keep valid items |
| `"\n".join(texts)` | Combine strings with a separator | Assemble evidence context |
| `xs[:k]` | First k elements, excluding index k | Candidate selection or truncation |
| `enumerate(xs)` | Produce index/value pairs | Chunk IDs and batch records |
| `zip(xs, ys)` | Pair corresponding elements | Compare predictions and targets |

`zip` stops at the shorter input, so validate lengths before evaluating. `sorted` returns a new list; `.sort()` mutates the existing list. `append(x)` adds one element; `extend(xs)` adds every element from an iterable.

Avoid clever side effects in comprehensions when an explicit loop communicates intent better:

```python
def unique_by_id(records):
    seen = set()
    result = []
    for record in records:
        if record["id"] not in seen:
            seen.add(record["id"])
            result.append(record)
    return result
```

This defines duplicates by ID, not by meaning. Near-duplicate detection requires another rule.

## Functions as values: callbacks and strategies

```python
def normalise(text):
    return text.strip().lower()

def apply_transform(text, transform):
    return transform(text)

result = apply_transform(" OPERATIONS ", normalise)
```

Passing `normalise` passes the function itself. Writing `normalise(...)` calls it immediately. UI libraries register functions for later calls. Provider adapters and predictor functions use the same idea: pass behaviour through a defined interface.

## Generators: `yield` versus `return`

```python
def prefixes(parts):
    text = ""
    for part in parts:
        text += part
        yield text

updates = list(prefixes(["Hello", " ", "team"]))
# ["Hello", "Hello ", "Hello team"]
```

`yield` produces a value and preserves local execution state for the next iteration. This is useful for UI updates and progress. It does not create a thread or automatically overlap I/O.

Some consumers expect deltas (`"team"`), others the complete current value (`"Hello team"`). Confirm the consumer's contract; appending full prefixes as if they were deltas duplicates text.

## Classes, instances and methods

A class defines behaviour and attributes. An instance is one object with its own state. `self` refers to that instance. In the capstone, the planner holds scanner, estimator and messenger instances; this is **composition**. Shared base-agent logging illustrates **inheritance**.

Class-level mutable objects can be shared across instances or notebook calls. The batch registry is an example worth inspecting. Use instance state when each run needs isolation.

`@classmethod` receives the class (`cls`) and can construct instances of that class. `@staticmethod` receives no automatic instance/class argument. `@decorator` replaces or wraps a function/class at definition time; retry and remote-service decorators use this mechanism.

## Keyword arguments and unpacking

```python
def label_request(team, urgent=False):
    return f"{team}:{'urgent' if urgent else 'normal'}"

arguments = {"team": "operations", "urgent": True}
label = label_request(**arguments)
```

`**arguments` expands dictionary entries into named arguments. Tool dispatchers use this after parsing model output. Validate argument keys, values and authority before unpacking into a callable.

Type hints such as `list[str]` document expected types and support tooling. Python does not automatically enforce ordinary hints at runtime. Pydantic validation checks a declared data contract, subject to its configuration; it still cannot establish truth, source fidelity or permission.

## Context managers and cleanup

`with open(...) as f` manages the file's lifetime. Database connections and no-gradient contexts use the same syntax for different resources. `try/except/finally` separates the attempted work, error handling and required cleanup.

Catching every error and returning a plausible default can conceal a failed system. Prefer explicit error records when a failure changes how a business result should be interpreted.

## Serialization and representation boundaries

JSON turns structured values into interoperable text; JSONL stores one JSON value per line. `json.dumps` serializes; `json.loads` parses. Pydantic `model_dump` makes a dictionary; `model_validate` validates input data; `model_validate_json` parses and validates JSON text.

Serialization is not semantic verification. `{ "price": 100 }` can be well formed and wrong. Keep stable source IDs through transformations so an output can be traced back to evidence.

## Mutation and defaults

```python
def add_turn(history, text):
    return history + [{"role": "user", "content": text}]
```

This creates a new outer list. `.append(...)` would mutate the original. A shallow copy does not copy nested dictionaries. Decide whether sharing nested state is intended.

Avoid `def f(history=[])` for functions that might mutate that list: the default is created once, not once per call. Use `None` and initialise inside the function. Several course functions use empty-list defaults without mutating them directly; this is a pattern to improve, not proof that every such function currently corrupts history.

## Three meanings of parallel work

Threads can overlap blocking API calls; processes can run independent Python computations; `async`/`await` coordinates compatible non-blocking operations. Remote batch jobs run elsewhere and can complete after the submitting process ends. These are different mechanisms.

Concurrency introduces ordering, cancellation, rate-limit and partial-failure questions. A queue can safely transfer messages between workers, but it does not by itself provide durable completion tracking. See [Python tasks and cancellation](https://docs.python.org/3/library/asyncio-task.html).

## A repeatable code-reading routine

1. Find the entry point: notebook call, UI callback or `main` guard.
2. Trace one small input through each function.
3. Write down representation changes: URL → HTML → text → messages → response.
4. Mark side effects: network, files, database changes, notifications.
5. Inspect global state and imported helpers.
6. Ask how each failure becomes visible.
7. Replace one dependency with a fake to understand the wiring.
8. Compare one simpler alternative before adding an abstraction.
