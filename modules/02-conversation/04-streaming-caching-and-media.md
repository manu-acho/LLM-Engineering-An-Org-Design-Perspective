# Lesson 2.4: What changes when a conversation streams or uses media?

[Module route](README.md) · [Next: the complete tool exchange](05-source-walkthrough.md)

## What you'll learn and why it matters

Distinguish a growing display, stored conversation information and media passed to the model. Learn why an adviser needs to know whether what appears on screen is provisional or complete.

A browser can show “Checking” and then append “ case H-17”, or it can receive the whole phrase again and replace the display. Streaming delivers output in parts. Appending a piece that already includes the earlier text would display it twice. The same separation matters when a photo is added: what the user sees is one part of the system; what the application has received, stored and sent to the model must be checked separately.

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

Provider caching rules vary. The original [week 2 day 1 notebook](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day1.ipynb) explores interfaces and caching. Treat its billing observations as historical results, not guaranteed prices. Inspect actual usage when testing a current integration.

## Media creates another transformation chain

The source [day 5 project](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week2/day5.ipynb) combines conversation with generated images and speech. A chain of text generation followed by speech generation is different from one model understanding audio directly. In both cases, ask which representations cross the boundary.

For a spoken order enquiry, transcription may turn `O-17` into `017`. The lookup can be correct for its input while referring to the wrong record. An image of a destination can be attractive without improving ticket-price accuracy. Make media optional where it does not contribute to the task.

**Worked diagnosis:** An assistant answers quickly, displays the same sentence twice and speaks an outdated policy. Investigate three separate mechanisms: prefix/delta handling, cache invalidation and text-to-speech input. One “better prompt” is unlikely to repair all three.

## Read the organisational connection

Streaming and media interfaces change what becomes visible and when it can be examined. The research chapter explains [materiality in digital systems](../../reference/research/06-technology-in-practice.md#materiality-in-digital-systems).

## What to remember

The application can append a new fragment or replace the display with the full text so far. Stored information, reused computation and visible output are distinct.

## What this means for the business process

Mark streamed text as a draft until the application has a final outcome. If a delivery photo matters, show whether it reached the step that checks evidence. What the interface lets an adviser see shapes what they can reasonably do next.

For the research behind this design choice, read [Feature, affordance and constraint](../../reference/research/06-technology-in-practice.md#feature-affordance-and-constraint).

## Next lesson

Next use the original tool call and interface callback to trace a result all the way back to the right request and display. [Lesson 2.5: Trace a complete tool call and interface callback](05-source-walkthrough.md).
