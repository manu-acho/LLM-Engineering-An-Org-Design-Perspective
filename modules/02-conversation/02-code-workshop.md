# Lesson 2.2: A conversation, a dispatcher and a visible result

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## Start with two messages

This example uses synthetic data and no model service. We will imitate a tool request so every step remains visible. In a connected application, a model could propose the same request, but the execution boundary remains the application's responsibility.

```python
history = [
    {"role": "user", "content": "Check order O-17"},
    {"role": "assistant", "content": "I will retrieve the order record."},
]
current_message = {"role": "user", "content": "What quantities are recorded?"}
messages = history + [current_message]
```

The last line creates a new list containing the earlier turns and the current one. It does not update `history` in place. The application needs to decide when a successful exchange becomes part of saved history. Adding it repeatedly can duplicate turns.

The content of the assistant's second record is a statement of intended work. It is not evidence that the lookup occurred. The next example actually performs a lookup against a local dictionary.

## Define a small tool

```python
orders = {"O-17": {"ordered": 12, "reported_received": 10}}

def lookup_order(order_id):
    record = orders.get(order_id)
    if record is None:
        return {"status": "not_found", "order_id": order_id}
    return {"status": "found", "order_id": order_id, "record": record}

def dispatch(tool_name, arguments, permitted_order_ids):
    tools = {"lookup_order": lookup_order}
    if tool_name not in tools:
        raise ValueError("Unknown tool")
    if set(arguments) != {"order_id"}:
        raise ValueError("Expected only order_id")
    order_id = arguments["order_id"]
    if not isinstance(order_id, str):
        raise ValueError("order_id must be text")
    if order_id not in permitted_order_ids:
        raise PermissionError("Order is outside the permitted scope")
    return tools[tool_name](order_id)

request = {"name": "lookup_order", "arguments": {"order_id": "O-17"}}
result = dispatch(request["name"], request["arguments"], {"O-17"})
```

`orders.get(order_id)` attempts a dictionary lookup but returns `None` for a missing key. `None` is Python's value for an absent result in this example. We return an explicit status, so missing data does not become a plausible empty order.

`tools` maps an allowed name to a function. This is a **dispatch table**. A name received from outside the application can select only entries that were deliberately placed there. The program does not evaluate arbitrary text as Python code.

The first `if` checks whether the requested tool exists. The next compares argument keys with the expected set. A **set** stores unique values; here it lets us reject extra or missing fields. `isinstance` checks the type of the supplied value. Finally, the permission check asks whether the order ID belongs to the provided scope.

In this small example, the caller supplies that scope. In a real service, trusted identity and policy must determine it. It should not be accepted from the model or an untrusted user field.

Only after these checks does `tools[tool_name](order_id)` run the selected function. Reading the nested expression from left to right helps: retrieve the function, then call it with the ID.

## Inspect the result

The expected `result` contains `status: found`, the requested ID and the two quantities. This is an execution result from the local function. A service-backed version would additionally need to handle network and remote-system errors. The model may then turn the record into a sentence, but that sentence is a later transformation.

If the user may access no orders, pass an empty set. The program raises `PermissionError` before reading the record. This demonstrates an authority boundary that exists independently of how politely or confidently the request was phrased.

## A generator makes incremental output understandable

```python
def render_in_parts(parts):
    current = ""
    for part in parts:
        current = current + part
        yield current

updates = list(render_in_parts(["Order O-17: ", "12 ordered; ", "10 reported received."]))
```

Calling the generator does not immediately produce one final string. Iterating asks it for values. It returns three successive prefixes. `list(...)` collects those values for inspection. A UI expecting the whole answer so far can replace its display with each prefix. A UI expecting only new text must instead receive individual pieces.

This generator is synchronous: it performs one step at a time. It does not create a background worker merely because `yield` appears.

## Connect to the original notebooks

In [week2/day4.ipynb](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day4.ipynb), `get_ticket_price` uses SQLite rather than our dictionary. A connection opens the database; a cursor executes a query; `fetchone` retrieves a matching row. The `?` placeholder keeps the city value separate from SQL syntax. The model schema names the input `destination_city`, and the dispatcher translates it to the Python function's argument.

The notebook loops through model tool requests, returns matching tool results and asks the model to continue. Its UI registers `chat` as a callback. Look for the same separation we used: prepare conversation, request or imitate a tool call, validate/dispatch, collect evidence, present a result.

## Alternatives and an exercise

For a form with a mandatory order ID, the application could call `lookup_order` directly, without asking a model to choose the tool. Use model selection when it helps interpret varied requests, not because every lookup needs generation.

Add a second tool, `draft_handoff`, which returns a proposed message without sending it. Define permitted arguments and a clear status. Then predict what happens for an unknown tool, an extra argument and an unpermitted order.

**Worked explanation:** Each invalid request should fail before the business operation. The draft tool should return a draft receipt, not `sent`. The distinction prevents a user or later program from treating prepared text as an acknowledged external action.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.
