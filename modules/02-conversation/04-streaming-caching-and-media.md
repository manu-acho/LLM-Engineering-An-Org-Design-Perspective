# Lesson 2.4: What changes when a conversation streams or uses media?

[Download the matching notebook](/downloads/02-04-streaming-caching-and-media.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: the complete tool exchange](05-source-walkthrough.md)

## A conversation has several kinds of state

A user sees one continuous exchange. The application may hold a displayed transcript, a shorter model context, a selected customer record and an unfinished tool request. These objects need not contain the same information. Naming them separately helps explain why an earlier order number appears on screen while the next model call does not receive it.

Suppose a callback receives the new question and a history list. It constructs request messages, obtains a response and returns an updated display. A **callback** is a function registered to run after an event. The interface calls it later. Passing `chat` registers the function; passing `chat(...)` executes it immediately and supplies its result instead.

## Deltas and prefixes solve different display problems

A streaming service may produce pieces such as `"Order"`, `" O-17"` and `" is disputed"`. These are **deltas**, additions to the answer. A display expecting complete current text needs `"Order"`, then `"Order O-17"`, then `"Order O-17 is disputed"`.

```python
def accumulate(deltas):
    text = ""
    for delta in deltas:
        text += delta
        yield text

assert list(accumulate(["Order", " O-17"])) == ["Order", "Order O-17"]
```

The generator preserves `text` between iterations. If an interface appends these prefixes instead of replacing its display, it produces duplicated language. The bug is a contract mismatch. It is not evidence that the model repeated itself.

Measure **time to first visible text** separately from **time to complete answer**. Streaming can improve the former without improving the latter. Do not enable a “send to customer” action merely because a plausible prefix is visible.

## Caching is reuse of computation

Repeated requests sometimes share a long instruction or evidence prefix. A provider may reuse eligible previously processed input. This is prompt caching. It differs from an application cache that returns a previously saved answer without calling a model, and from conversation memory that supplies past information.

In an application answer cache, the key must include the information that can change correctness: question, relevant source version, permitted scope and important settings. A cached policy answer for one user must not disclose material to another. An unchanged question can require a changed answer after policy revision.

Provider caching rules vary. Inspect actual usage when testing an integration. A cached input computation, a saved answer and stored conversation history have different freshness and billing implications.

## Media creates another transformation chain

A media application may combine text generation with image or speech generation. A chain that first generates text and then renders it as speech differs from a model that processes audio directly. Inspect which representation and source identity survive each transformation.

For a spoken order enquiry, transcription may turn `O-17` into `017`. The lookup can be correct for its input while referring to the wrong record. An image of a destination can be attractive without improving ticket-price accuracy. Make media optional where it does not contribute to the task.

**Worked diagnosis:** An assistant answers quickly, displays the same sentence twice and speaks an outdated policy. Investigate three separate mechanisms: prefix/delta handling, cache invalidation and text-to-speech input. One “better prompt” is unlikely to repair all three.

## Read the organisational connection

Streaming and media interfaces change what becomes visible and when it can be examined. The research chapter explains [materiality in digital systems](../../reference/research/06-technology-in-practice.md#materiality-in-digital-systems).

## Practical activity: Assemble a streamed answer from deltas and inspect its completion.

A delta is the new part of an output. A generator yields successive pieces while retaining its place. A completed stream includes a final response status; an interrupted one leaves partial text.



The exercise code below runs from a prepared course checkout. In the matching notebook, the setup cell already supplies ROOT and RUN_LIVE. If following the code here, run this setup first:

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

What is the complete string after all three deltas?

```python
pieces = ["Evidence ","awaits ","review."]
answer = ""
for piece in pieces:
    answer += piece
    print(answer)
assert answer == "Evidence awaits review."
```

Each piece contains only newly arrived text; joining them reconstructs the full answer. A partial prefix is not a completed response.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    parts = []
    for delta in gateway.stream("Explain the difference between an order and verified receipt in two sentences."):
        parts.append(delta)
        print(delta, end="")
    print("\nCompletion record:", gateway.ledger())
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: What is the complete string after all three deltas?

**Worked answer.** Each piece contains only newly arrived text; joining them reconstructs the full answer. A partial prefix is not a completed response.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

### Programming practice

Write join_deltas(parts) to reconstruct a streamed answer.

Start with the placeholder in the notebook, then compare with this worked solution. The contrasting checks are part of understanding the contract.

```python
def join_deltas(parts):
    answer = ""
    for part in parts:
        answer += part
    return answer

assert join_deltas(["one ","two"]) == "one two"
assert join_deltas([]) == ""
```

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
