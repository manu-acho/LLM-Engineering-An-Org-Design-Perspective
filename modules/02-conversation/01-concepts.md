# Lesson 2.1: How a conversation becomes a controlled interaction

[Download the matching notebook](/downloads/02-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## What you'll learn and why it matters

Explain what an application must retain for a follow-up to refer to the right case. This helps Harbour handle short questions without silently switching orders.

## Business context: Harbour

When a customer writes “What about the other order?”, the missing order number may be clear to a person who remembers the previous turn. A model request needs enough of that earlier exchange supplied again to make sense of it. History is the exchange so far; state is the information the application currently relies on, such as the selected case. The application must decide what to carry into the next request and when to ask which order the customer intends.

Preserve which delivery the adviser is discussing when a short follow-up omits the case identifier.

[Company and supply-chain context](../../HARBOUR.md) · [Module 2 business situation](../../reference/harbour-learning-journey.md#module-2)

## The user thinks they are having one conversation

The account manager writes: “Check order O-17.” The assistant replies with the order quantities. The manager then asks: “Who should review it?” To the person, this is one continuous exchange. To the application, it is a sequence of requests, stored messages, data lookups and generated responses.

If the program sends only “Who should review it?”, the meaning of “it” may be missing. The application must supply relevant earlier information or keep a state record containing the current order. This is why a conversation interface needs more than a textbox connected to generation.

## History, state and memory

**History** is a record of earlier turns. **State** is the information the application retains to continue its work. It can include history, a selected order ID, whether a lookup completed and whether an action is awaiting approval. “Memory” is often used for all of these, so ask what is actually stored and where.

Suppose the saved messages say “Inspect order O-17” and “Who should review it?” The first message gives the second its meaning. The application can separately store H-17 as the case currently open. The order and case have different identifiers because they are different records. If the adviser switches to another case, updating the selected case does not erase the messages. The application has to decide which information the next answer should rely on.

A list of messages is a simple history representation. A database record is more suitable for durable work across sessions. A summary can compress older turns, but it is another generated representation that can omit a qualification. None of these operations changes the model's weights by itself.

State also needs a scope. One user's history should not accidentally become another user's context. A variable shared by every session is therefore a different design from a per-session record, even if both make a demonstration appear to remember.

## Answering from a record

When asked the current order status, the assistant should consult an appropriate record. Asking the model to guess from its training does not make sense for a particular current order. The model can help interpret the request and formulate a response; a tool can obtain the operational value.

A **tool** is an application-defined capability, such as `lookup_order`. The application describes the tool's name, purpose and required input. The model may generate a **tool call**, a request to use that capability with particular arguments. The application then receives that request, validates it, checks permissions and performs the operation if permitted.

Imagine a receptionist taking a request to retrieve a customer file. Understanding the request does not itself establish entitlement to see the file. Likewise, a model generating a tool name does not authorise the action.

## The complete loop

The application sends the conversation and tool descriptions. The model requests `lookup_order` with `order_id` equal to `O-17`. The application checks that the tool exists and that the current user may access that order, calls the relevant service, and returns the result in the protocol expected by the model API. The next model response can refer to that result.

The matching request identifier matters. It connects a tool result to the call that requested it. Without it, several simultaneous requests could have their results confused. Tool calling is therefore a structured protocol around generation, not a model silently operating your computer.

The same interaction pattern can serve an order lookup or a delivery investigation, but each task needs explicit access rules and action boundaries. See the [official function-calling explanation](https://developers.openai.com/api/docs/guides/function-calling) for the application/model boundary; exact API formats depend on the interface in use.

## Reads and writes have different consequences

Reading an order can disclose information. Changing an order changes the business record. Sending a customer a credit promise can create an expectation even if finance has not issued a credit. Design these as different capabilities.

An assistant may observe, recommend, draft, authorise or execute, with a different permitted scope for each act. A broad tool called `handle_order` conceals these distinctions. Narrow tools make the boundary easier to inspect and test.

Calling a read-only tool twice may waste time. Calling a credit-creation tool twice may issue duplicate credits. Repeated operations need an explicit policy, which Module 8 develops further.

## How a user interface calls the program

A **callback** is a function registered for another component to call when an event occurs. Submitting a message is an event. A UI library supplies the message and history to the callback; the callback returns values for the UI to show.

**Streaming** sends output in pieces. The program can display partial text while generation continues. It needs to distinguish a piece of new text from the full answer so far. A partial stream can end in an error; displaying a prefix does not prove that a complete response was delivered.

A **generator** is a Python function that can yield a value, pause and continue. The next lesson shows one without a network connection. Streaming describes delivery; a generator is one programming mechanism for handling it.

## When conversation is useful

Chat can help with variable language and follow-up questions. A form may be better when every request needs an order ID, reason code and two quantities. A hybrid can use a form for required facts and conversation for clarifications.

The interface should follow the task. A friendly conversation that repeatedly fails to collect required evidence can be worse than a short form.

**Check:** Explain why retaining the order ID in a session is different from training a model, and why a correct tool request still needs an application permission check. A strong answer identifies separately the information needed to understand the request and the authority needed to execute it.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Conversation state and rules structure the situations the service can recognise. The research chapter explains [programmes and exceptions](../../reference/research/03-decisions.md#programmes-and-exceptions).

## Practical activity: Keep an order selection separate from the words used in a follow-up.

History is the saved sequence of turns. State is the information the application retains to continue its task. A role labels who supplied a message.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

```python
from ai_orgdesign.workspace import project_root, live_mode
ROOT = project_root()
RUN_LIVE = live_mode()
if RUN_LIVE:
    from ai_orgdesign.provider import Gateway
    gateway = Gateway(max_requests=12, max_output_tokens=1000)
print("Live mode:", RUN_LIVE)
```

### Predict and follow the values

Which case identifier should be retained across the follow-up?

```python
history = [{"role":"user","content":"Inspect order O-17"}]
state = {"case_id":"H-17"}
history.append({"role":"user","content":"Who should review it?"})
print(history)
print(state)
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    answer = gateway.generate("Who should review it?", messages=history, instructions="Discuss the fictional delivery investigation. Ask for missing information; do not infer verified receipt.")
    print(answer.text)
    print(gateway.ledger())
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** H-17 identifies the investigation case; O-17 is its order. Neither storing a message nor selecting a case trains the model.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Conversation history is the record of earlier turns. Application state can also record the case currently selected. Each new request depends on the information the application makes available.

## What this means for the business process

Show the active case to the adviser and ask for clarification when the earlier conversation and the selected case point to different orders. A default can support routine work, but the service needs an exception path when that default no longer fits.

For the research behind this design choice, read [Programmes and exceptions](../../reference/research/03-decisions.md#programmes-and-exceptions).

## Next lesson

Once the application knows which case is in view, the next lesson shows how it can look up that case through a checked operation. [Lesson 2.2: Follow a conversation through a validated tool](02-code-workshop.md).
