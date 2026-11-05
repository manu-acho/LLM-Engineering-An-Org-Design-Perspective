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
