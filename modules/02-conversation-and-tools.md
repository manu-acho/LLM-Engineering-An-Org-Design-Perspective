# Module 2: Conversational applications and tools

[Previous module](01-foundations-and-pipelines.md) · [Guide index](../README.md) · [Next module](03-open-models-and-inference.md)

## What you should be able to do

Trace a chat turn through UI, history, model and database; explain callbacks and generators; distinguish model-requested actions from application-authorised execution; and compare a chatbot with a form or fixed workflow.

**Course walkthrough:** [day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day1.ipynb), [day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day2.ipynb), [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day3.ipynb), [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day4.ipynb), [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day5.ipynb). The sequence compares providers and abstractions, builds Gradio interfaces, introduces history, connects an airline assistant to SQLite, and adds image and speech outputs.

## 1. Concepts: a conversation is an application protocol

A useful assistant combines language generation with state and access to authoritative information. The model can interpret “How much is Paris?”, but the current price belongs in a database, not in a guess derived from model parameters.

**Tool calling** lets the model request a named function with arguments. The surrounding application receives the request, decides whether it is permitted, executes the function if appropriate, and returns the result. The model then generates a reply using that result. The model's request is not itself permission. [Official function-calling explanation](https://developers.openai.com/api/docs/guides/function-calling).

Three contracts matter: the UI's callback signature, the model API's message/event format, and the business tool's inputs/outputs. Many integration errors arise when two contracts are confused.

**Streaming** delivers intermediate text for responsiveness. It can reduce perceived waiting without reducing total generation time. **Caching** can reuse some computation for repeated context, depending on the service; it is distinct from durable user memory and does not prove that a document is current.

An assistant is **multimodal** when it handles more than text. The course chains text, speech and generated imagery. Chaining separate services differs from a single model processing all modalities together. Each boundary adds latency and another possible failure.

## 2. What the code does

### Day 1: compare interfaces and providers

Several clients expose a similar `chat.completions.create` call through different base URLs. Native provider SDKs, LangChain's `invoke`, and LiteLLM's `completion` illustrate different abstraction levels. The code extracts text, usage and cost-related fields, then experiments with repeated long context and model-to-model conversation.

Read provider examples as examples from this snapshot. Supported parameters and models vary. A common method name does not mean that caching, reasoning controls or tool schemas are interchangeable. Accessing `_hidden_params` also couples code to an implementation detail.

The adversarial conversation uses `zip` to rebuild each model's perspective from two lists. `zip` stops at the shorter list. This makes list lengths and append order part of the program's correctness. Multi-model dialogue is a demonstration of role-conditioned conversation, not proof that debate yields reliable truth.

### Days 2–3: callbacks, history and streaming

`gr.Interface(fn=shout, ...)` registers a Python function as a callback: the UI invokes it when the user submits. Replacing `shout` with `message_gpt` changes the computation behind the same interaction.

In `stream_gpt`, `yield result` pauses the function and exposes the accumulated string. The caller can render each new prefix. Replacing it with `return result` would finish the function immediately at that point. This is a Python generator, not a background thread.

The chat callback receives a current message and previous history. It normalises each history record into a role/content pair, prepends the system message and appends the current user message. The model call receives that newly constructed conversation. Keep state scoped to the user session; a shared global conversation could mix users' content.

### Day 4: read a database through a model-selected tool

`get_ticket_price(city)` opens a SQLite connection in a `with` block, creates a cursor and executes a parameterised query. The `?` placeholder supplies the city as data rather than concatenating it into SQL. The `(city.lower(),)` expression is a one-element tuple; its comma matters.

The schema calls the argument `destination_city`, while the Python function accepts `city`. `handle_tool_calls` translates between those names explicitly. Schemas describe interfaces; they do not invoke Python by magic.

Trace a tool turn:

1. The request includes tool descriptions.
2. A response may contain `tool_calls` rather than a final answer.
3. The dispatcher loops through requests and parses argument strings using `json.loads`.
4. It calls the recognised local function.
5. It returns a tool message with the matching `tool_call_id`.
6. The application appends the assistant's request and all tool results before asking the model again.

The `while` loop supports successive rounds. It needs a round/time/cost limit for an operational service. Unsupported tools, bad arguments, empty choices and failed requests need explicit outcomes rather than silent omission.

### Day 5: decode media and wire events

`artist(city)` receives base64 image data, decodes it to bytes, wraps those bytes in `BytesIO`, and opens them as a PIL image. These are different representations of one asset: transport text, binary content, file-like object, image object.

`talker(reply)` sends the answer to speech synthesis. `chat(history)` returns three values: updated history, audio and optional image. Their order must match the UI output component list.

In Gradio Blocks, `.submit(...).then(...)` wires a sequence: first add the user's turn to the visible conversation, then perform generation and update the outputs. An image failure should not necessarily erase an otherwise valid textual answer.

## 3. Learn the coding patterns

**Teaching example: dependency-free, read-only dispatcher:**

```python
def lookup_owner(team):
    return {"team": team, "owner": {"operations": "Service lead"}.get(team)}

def dispatch(name, arguments):
    allowed = {"lookup_owner": lookup_owner}
    if name not in allowed:
        raise ValueError("Unknown tool")
    if set(arguments) != {"team"}:
        raise ValueError("Expected only a team argument")
    team = arguments["team"]
    if not isinstance(team, str) or not team.strip():
        raise ValueError("Team must be non-empty text")
    return allowed[name](team.strip().lower())

result = dispatch("lookup_owner", {"team": "Operations"})
```

This is a **dispatch table**: a dictionary maps allowed names to callables. It is more inspectable than evaluating a model-generated Python expression. Input validation happens before execution. A real service must additionally check the authenticated user's access to the requested record.

Other reusable patterns are **event-driven programming** (callbacks react to UI events), **generator-based streaming**, **context managers** (database/file lifetime), and **protocol continuation** (return every tool result with its request ID).

| Pattern in the lessons | Alternative | Trade-off |
|---|---|---|
| Chat interface | Structured form | Less flexible language, clearer required fields |
| Model selects a lookup tool | Fixed route to lookup after deterministic parsing | Less autonomy; easier evaluation for narrow requests |
| Compatibility SDK | Native SDK | More provider-specific code; direct access to native features |
| Framework wrapper | Small application adapter | Less machinery; more responsibility for retries and telemetry |
| Image and voice on every answer | Optional media after text | Lower latency and cost when media adds little value |
| Repeated full history | Scoped summary plus relevant recent turns | Lower context load; summary omissions must be managed |

The course uses Chat Completions-shaped tools and streams. OpenAI's Responses API has different tool/output item shapes and typed streaming events; migration requires changing parsers and state handling, not simply renaming the client method. [Official migration guide](https://developers.openai.com/api/docs/guides/migrate-to-responses).

## 4. Business application and organisation design

For Harbour, begin with an assistant that answers “Who owns this request?” and retrieves approved status records. Separate **observe**, **recommend**, **draft** and **execute** authority. An accurate lookup does not imply permission to change the owner or send a customer message.

Map escalation as an actual handoff: named receiving role, required context, expected response and fallback when the person is unavailable. A button labelled “escalate” is insufficient if no team accepts the work.

Useful measures include correct resolution, appropriate escalation, unnecessary escalation, time to completion and correction effort. Classify errors by consequence: a slightly awkward sentence is different from a wrong delivery commitment. Conversation satisfaction alone can reward confident misinformation.

A conversational interface also reallocates coordination work. Users may stop searching policy pages and start relying on the assistant. Knowledge owners then need a workable mechanism for updating records and contesting wrong answers.

## 5. Experiment, diagnose and reflect

**Exercise:** Use a synthetic table of three teams and owners. Implement `lookup_owner`; then add a separate `propose_assignment` tool that returns a draft without changing state. Draw the message sequence for a lookup followed by a proposed assignment. Identify the point at which a human must authorise an actual change.

Create cases for an unknown team, a missing argument, an unauthorised record, a database outage and repeated tool requests. Define expected behaviour before trying the assistant.

**Common failures:** duplicated user turns come from history construction; an unmatched tool ID breaks the conversation protocol; mismatched return/output order breaks the UI; an infinite loop points to missing termination controls. A model's statement that a change succeeded is not a tool execution receipt.

**Check your understanding:** Why does a SQL placeholder matter? What does `yield` change? Why does a tool schema not establish authority? When would a form be better than chat?

**Answer cues:** values stay separate from SQL syntax; execution pauses and resumes; permission comes from application policy and user scope; forms suit constrained inputs and predictable workflows.

**Decision note:** Write the assistant's permitted actions, forbidden transitions, escalation owner and success measures. Explain why chat is appropriate for this task.
