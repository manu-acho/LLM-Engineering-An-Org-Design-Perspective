# Lesson 2.5: Trace a complete tool call and interface callback

[Module route](README.md) · [Next: decide where discretion belongs](06-design-lab.md)

## What you'll learn and why it matters

Follow a tool request, its identifier and the interface callback through the original implementation. Learn to locate a failure between lookup, response and display.

A model might ask for a lookup and wait for the result before it answers. A call identifier lets the application match that result to the particular request. Follow it back into the conversation, then read how a callback, a function run in response to an interface event, lets the screen use the resulting answer.

[Open the companion workshop notebook](../../notebooks/02-conversation.ipynb).

## Inspect the actual exchange

Open [the airline assistant notebook](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day4.ipynb). Find the tool description, `get_ticket_price`, the tool-call handler and the final `chat` callback. Read them as one route. A tool description alone does not implement an operation.

The schema tells the model that a named operation accepts a destination city. The Python function queries a database. The handler translates the schema's argument into the function call. The callback sends conversation messages and available tools to the model, handles returned requests and asks the model to continue with the results.

The sequence has six observable objects:

| Step | Object | Meaning |
|---|---|---|
| 1 | User question and history | What the application supplies now |
| 2 | Tool schema | Operations the model may propose |
| 3 | Assistant tool request | A proposed operation and argument text |
| 4 | Parsed and checked arguments | Values the application may execute |
| 5 | Tool result with matching call ID | Evidence returned for that particular request |
| 6 | Final assistant message | Generated interpretation of the evidence |

## Why the call identifier matters

Imagine the model requests two prices, London and Paris. Results can arrive in a different order. A call identifier connects each result with its request. Attaching the Paris result to the London call produces a syntactically plausible but substantively wrong answer. Matching by list position is fragile once concurrency is introduced.

The following new fragment shows the central Chat Completions pattern used by the course. It is an integration function requiring a configured client, model, schemas and dispatcher. It makes external requests if called and was not executed here. `dispatch` must enforce the checks introduced in Lesson 2.2.

```python
def complete_with_tools(client, model, messages, tools, dispatch, max_rounds=4):
    import json

    working = list(messages)
    for _ in range(max_rounds):
        response = client.chat.completions.create(
            model=model, messages=working, tools=tools
        )
        message = response.choices[0].message
        if not message.tool_calls:
            return message.content
        working.append(message.model_dump(exclude_none=True))
        for call in message.tool_calls:
            arguments = json.loads(call.function.arguments)
            result = dispatch(call.function.name, arguments)
            working.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result),
            })
    raise RuntimeError("Tool round budget exhausted")
```

`working` is a new outer list so the function does not append directly to the caller's history. Its nested dictionaries remain shared. The assistant request must be retained before appending its tool results, because the conversation needs the request/result relationship. `json.loads` converts argument text to values; it does not validate business permission. `json.dumps` converts the result to text the interface can carry.

The next iteration supplies the growing exchange to the model. The model may answer or request another tool. The bound counts model rounds, not individual tool calls, so one round can contain several operations. Time, spending and per-operation limits require additional policy.

## Database values and interface events

The source query uses an SQL placeholder rather than interpolating the destination directly into SQL. Parameters keep ordinary values distinct from query syntax. A missing row needs an explicit unavailable result. It should not silently become a zero price.

A Gradio chat component invokes the callback when the user submits a message. The callback's signature must match what that configured component supplies. History format can differ by library version, so inspect actual records before adapting them into API messages. Preserve system instructions separately from user-editable conversation.

The following optional adapter needs `gradio`. It constructs an interface only when called. It accepts an application function with a defined `(message, history)` contract; that function can be a local fake or the connected tool-loop application. Creating the interface is separate from calling its `launch` method.

```python
def build_chat_interface(answer_question):
    import gradio as gr

    def chat(message, history):
        return answer_question(message, history)

    return gr.ChatInterface(fn=chat)
```

The nested function keeps access to `answer_question`; this is a closure. Registering it supplies behaviour for a future event. The application can test the answering function without starting the interface. A streaming version returns or yields the format expected by its component, which is why the prefix/delta distinction matters.

## Follow a failure through the route

Suppose `json.loads` raises because the argument string is malformed. No lookup has yet run. The application can expose a structured tool error, request correction or stop with a visible failure. Suppose the lookup instead times out after reaching a remote system. The uncertainty is different: the request may have reached that service. A read can often be retried; a record-changing operation needs duplicate protection and reconciliation.

**Practice with feedback:** A generated answer says “the lookup succeeded”, but the database returned `not_found`. Which object should determine the factual claim? The tool result is the evidence available from that lookup. Preserve it in the trace and evaluate whether the final message respects it. The assistant's own success sentence is not an independent confirmation.

The [function-calling documentation](https://developers.openai.com/api/docs/guides/function-calling) describes the request/result relationship. Responses uses different item shapes, so do not mix its fields into this Chat Completions example.

## Read the organisational connection

A complete tool exchange still needs a defensible allocation of action rights. The research chapter explains [permission and authority](../../reference/research/03-decisions.md#permission-and-authority).

## What to remember

The identifier matches a result to a request. The application returns that result to the conversation, then a callback lets the interface display an outcome.

## What this means for the business process

Retain the case and call identifiers through the callback and expose a lookup failure to the adviser. The next person needs to know whether a record was unavailable or the interface failed to show it.

For the research behind this design choice, read [Four questions for a usable contribution](../../reference/research/02-coordination.md#four-questions-for-a-usable-contribution).

## Next lesson

The next lesson turns these checks into a design choice about how much freedom the assistant and advisers should have. [Lesson 2.6: Allocate discretion across a conversational service](06-design-lab.md).
