# Lesson 2.1: How a conversation becomes a controlled interaction

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## The user thinks they are having one conversation

The account manager writes: “Check order O-17.” The assistant replies with the order quantities. The manager then asks: “Who should review it?” To the person, this is one continuous exchange. To the application, it is a sequence of requests, stored messages, data lookups and generated responses.

If the program sends only “Who should review it?”, the meaning of “it” may be missing. The application must supply relevant earlier information or keep a state record containing the current order. This is why a conversation interface needs more than a textbox connected to generation.

## History, state and memory

**History** is a record of earlier turns. **State** is the information the application retains to continue its work. It can include history, a selected order ID, whether a lookup completed and whether an action is awaiting approval. “Memory” is often used for all of these, so ask what is actually stored and where.

A list of messages is a simple history representation. A database record is more suitable for durable work across sessions. A summary can compress older turns, but it is another generated representation that can omit a qualification. None of these operations changes the model's weights by itself.

State also needs a scope. One user's history should not accidentally become another user's context. A variable shared by every session is therefore a different design from a per-session record, even if both make a demonstration appear to remember.

## Answering from a record

When asked the current order status, the assistant should consult an appropriate record. Asking the model to guess from its training does not make sense for a particular current order. The model can help interpret the request and formulate a response; a tool can obtain the operational value.

A **tool** is an application-defined capability, such as `lookup_order`. The application describes the tool's name, purpose and required input. The model may generate a **tool call**, a request to use that capability with particular arguments. The application then receives that request, validates it, checks permissions and performs the operation if permitted.

Imagine a receptionist taking a request to retrieve a customer file. Understanding the request does not itself establish entitlement to see the file. Likewise, a model generating a tool name does not authorise the action.

## The complete loop

The application sends the conversation and tool descriptions. The model requests `lookup_order` with `order_id` equal to `O-17`. The application checks that the tool exists and that the current user may access that order, calls the relevant service, and returns the result in the protocol expected by the model API. The next model response can refer to that result.

The matching request identifier matters. It connects a tool result to the call that requested it. Without it, several simultaneous requests could have their results confused. Tool calling is therefore a structured protocol around generation, not a model silently operating your computer.

The original course uses this loop for airline prices. The business pattern transfers to order status, but the access rules and consequences must be designed for the new context. See the [official function-calling explanation](https://developers.openai.com/api/docs/guides/function-calling) for the application/model boundary; exact API formats depend on the interface in use.

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
