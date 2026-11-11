# Lesson 9.2: Follow a tool request around a bounded loop

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

An investigation might look up an order, then decide whether the result is enough for a draft. The scripted responder below gives the same lookup request each time it sees the opening question. Follow the request, the access check and the record that returns to the loop before the final draft appears.

[Open the companion workshop notebook](../../notebooks/09-agent-loops.ipynb).

## Make the moving parts visible

The original course moves from a single model response to a loop over tool requests. We will use a scripted response provider instead of a model, so the sequence is predictable. This example makes no network calls and changes no business records. It demonstrates dispatch and evidence flow, not model competence.

```python
ORDERS = {"O-17": {"ordered": 12, "reported_received": 10}}

def lookup_order(order_id):
    return dict(ORDERS[order_id])

TOOLS = {"lookup_order": lookup_order}

def scripted_model(messages):
    if messages[-1]["role"] == "tool":
        record = messages[-1]["result"]
        difference = record["ordered"] - record["reported_received"]
        return {"kind": "final", "text": f"Reported difference: {difference}"}
    return {
        "kind": "tool", "name": "lookup_order",
        "arguments": {"order_id": "O-17"}, "call_id": "call-1"
    }

def investigate(question, choose, permitted_ids, max_steps=3):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        proposal = choose(messages)
        if proposal["kind"] == "final":
            return {"status": "draft", "text": proposal["text"], "trace": messages}
        if proposal["kind"] != "tool" or proposal["name"] not in TOOLS:
            raise ValueError("Unsupported action")
        arguments = proposal["arguments"]
        if set(arguments) != {"order_id"}:
            raise ValueError("Unexpected argument fields")
        order_id = arguments["order_id"]
        if not isinstance(order_id, str) or order_id not in permitted_ids:
            raise PermissionError("Order is outside the permitted scope")
        result = TOOLS[proposal["name"]](order_id=order_id)
        messages.append({"role": "assistant", "proposal": proposal})
        messages.append({"role": "tool", "call_id": proposal["call_id"], "result": result})
    return {"status": "needs_review", "reason": "Step budget exhausted", "trace": messages}

answer = investigate("Investigate O-17", scripted_model, {"O-17"})
print(answer["status"], answer["text"])
```

Expected output:

```text
draft Reported difference: 2
```

## Read from the final call

`investigate` receives a question, a function that chooses the next response, and a set of permitted order IDs. Passing a function makes it possible to replace a real service with a fake. This is the dependency-injection pattern from Module 1.

The first call to `choose` receives a message list ending in a user question. Our fake returns a dictionary describing a lookup. Nothing has been looked up yet. `proposal` is data about an intended operation.

The program checks the proposal before dispatch. A **registry** is the `TOOLS` dictionary: it maps an allowed name to a particular function. It keeps the callable surface explicit. The code does not search all available Python functions for a matching name.

`set(arguments)` collects the dictionary's keys. Comparing that set with `{"order_id"}` rejects missing or additional fields. The next check requires a string and membership in the permitted scope. In a real application, that scope must come from trusted identity and access rules, not a model's request or an editable user field.

`TOOLS[proposal["name"]](order_id=order_id)` retrieves the function and calls it. Nested brackets select values; the final parentheses perform the operation. `lookup_order` returns a copy of the stored record so this caller cannot change the original dictionary through the returned outer object.

## Follow the second iteration

The application appends a proposal record and its result to `messages`. On the next iteration, `scripted_model` sees a tool result, calculates the reported difference and returns a final response. The application labels it `draft`. It has neither verified the delivery nor authorised compensation.

The fake does arithmetic in Python to make the path inspectable. A real model may instead generate the arithmetic and wording. That difference matters: a valid loop does not establish that generated calculations are reliable. Put exact calculations in a trusted function when the business rule permits it.

The `for` loop permits at most three calls to `choose`. A model that repeatedly asks for tools cannot continue forever. With `max_steps=1`, the lookup runs but there is no second turn to compose the draft, so the function returns `needs_review`. Budget design changes what counts as a completed run.

## Connect the example to the course

In [foundations lab 3](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/1_foundations/3_lab3.ipynb), the final `chat` definition loops while the provider reports tool calls. It appends the assistant message, executes each request, appends results with `tool_call_id`, and calls the model again. Reading only the first `chat` definition would miss the more complete version later in the notebook.

[Lab 4](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/1_foundations/4_lab4.ipynb) shows both explicit `if` dispatch and a version using `globals().get`. The latter looks up a name in Python's global namespace. Our explicit registry is an alternative that exposes fewer functions and makes permissions easier to inspect. The course's [application tools](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/1_foundations/twin/tools.py) provide another source-reading anchor. We have not run their notification operations.

## Failure handling and alternatives

A missing stored order raises an error here. A real service also needs to distinguish “not found”, “temporarily unavailable” and “not permitted”. Those should not all become an empty record, because they support different conclusions.

This small loop assumes a correctly shaped proposal and handles one tool request per turn. A provider adapter would need to validate the full response, handle multiple calls, serialize results and preserve matching identifiers. It would also need time and cost limits, appropriate retry rules and a policy for external effects.

**Try it:** Change the permitted set to empty and predict where execution stops. Then use `max_steps=1`. Explain why permission failure and unfinished investigation require different responses. Finally, sketch a fixed two-step lookup-and-format function. When would that be sufficient?

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A tool request and its execution result should not be treated as the same event. The research chapter explains [distinct acts in a workflow](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow).
