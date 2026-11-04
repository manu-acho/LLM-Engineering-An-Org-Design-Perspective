# Lesson 8.7: Make failures terminal, visible and recoverable

[Module route](README.md) · [Next module](../09-agent-loops/README.md)

## A progress message is not a final result

A web interface starts work in a background thread so it can remain responsive. The worker sends progress events through a queue. If it fails before sending a final event, the interface can wait forever. The failure has happened, but the user-facing state never reaches a conclusion.

A queue transfers events between parts of a program. It does not automatically define which event ends the request. Establish a contract: each job produces a terminal success or error event, and the consumer also has its own waiting policy.

```python
from queue import Queue, Empty
from threading import Thread

def worker(job_id, operation, events):
    try:
        events.put({"job": job_id, "kind": "progress", "text": "Started"})
        result = operation()
        events.put({"job": job_id, "kind": "success", "result": result})
    except Exception as error:
        events.put({"job": job_id, "kind": "error", "error": type(error).__name__})

events = Queue()
thread = Thread(target=worker, args=("J-17", lambda: 12-10, events))
thread.start()
terminal = None
while terminal is None:
    try:
        event = events.get(timeout=2)
    except Empty:
        raise TimeoutError("No event arrived within the waiting policy")
    if event["kind"] in {"success", "error"}:
        terminal = event
thread.join(timeout=2)
assert terminal["result"] == 2
```

The timeout bounds one wait for an event. It does not cancel the worker. A real application also needs a total deadline, cancellation cooperation and a way to reconcile a result arriving after the user stops waiting. The queue here is in memory and disappears with the process. Durable work needs a persistent job record.

## The crash gap is a business problem too

Imagine a handoff service submits a case, then crashes before saving the acknowledgement. On restart the local record says unsent, while the receiving system may already hold the case. A local duplicate guard cannot settle this uncertainty.

A stable action ID lets the receiving service recognise repeated attempts, if it supports that contract. A transactional outbox records the intended external work alongside a local state change, so a dispatcher can retry it. An outbox alone does not force the external system to perform an action exactly once. Combine it with idempotent operations or reconciliation of uncertain outcomes.

## Distinguish three recovery choices

Retry repeats an operation believed safe to repeat. Resume continues from an identified stored state. Reconcile investigates what actually happened before deciding whether to retry or correct it. A network timeout after submission often calls for reconciliation rather than an immediate fresh action.

Assign an owner to uncertain work. The operator can inspect service health; the case owner determines what the customer still needs. The receiving team may be needed to confirm whether the handoff entered its working queue. A log available only to engineers is not a complete operating recovery process.

**Worked exercise:** Replace the operation with a function raising `ValueError`. The terminal event should be `error`, so the interface can stop waiting and show an appropriate status. Then imagine the whole process is forcibly stopped: no in-memory error event can be relied on. A restarted service needs a durable job record and a stale-work policy. The distinction is between a caught function error and failure of the process that would report it.
