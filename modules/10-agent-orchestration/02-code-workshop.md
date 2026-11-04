# Lesson 10.2: Gather evidence without confusing checks and permission

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## A coordinator with two required inputs

This original teaching example models the dependency behind a research manager. It uses Python's standard library and fake evidence functions. It calls no models, sends no messages and uses no external accounts.

```python
import asyncio

async def order_evidence(case):
    await asyncio.sleep(0)
    return {"source": "order-17", "reported_difference": 2}

async def policy_evidence(case):
    await asyncio.sleep(0)
    return {"source": "policy-v3", "requires_review": True}

async def prepare_case(case, fetch_order, fetch_policy):
    results = await asyncio.gather(
        fetch_order(case), fetch_policy(case), return_exceptions=True
    )
    failures = [type(item).__name__ for item in results if isinstance(item, Exception)]
    if failures:
        return {"status": "incomplete", "failures": failures}
    order, policy = results
    return {
        "status": "draft",
        "case_id": case["id"],
        "sources": [order["source"], policy["source"]],
        "reported_difference": order["reported_difference"],
        "requires_review": policy["requires_review"],
    }

def authorise_handoff(draft, approval):
    if draft["status"] != "draft":
        raise ValueError("Evidence collection is incomplete")
    if not approval or approval["case_id"] != draft["case_id"]:
        raise PermissionError("No matching approval")
    if approval["decision"] != "approve":
        raise PermissionError("Review did not approve this handoff")
    return {"status": "ready_for_execution", "case_id": draft["case_id"]}

case = {"id": "C-17"}
draft = asyncio.run(prepare_case(case, order_evidence, policy_evidence))
print(draft["status"], draft["sources"])
try:
    authorise_handoff(draft, None)
except PermissionError as error:
    print(type(error).__name__)
```

Expected output:

```text
draft ['order-17', 'policy-v3']
PermissionError
```

## How to read the asynchronous part

Calling an `async def` function creates a coroutine object representing work that can be awaited. It does not by itself run the complete function. `asyncio.run` creates an event loop, runs the top-level coroutine to completion and closes that loop. A notebook with an existing event loop normally uses `await` instead.

The two calls inside `gather` are submitted together. `await asyncio.sleep(0)` yields control in this fake; it imitates a point at which real network work would wait. It does not measure real service speed. `gather` returns results in input order, so `order, policy = results` still matches the two supplied operations.

`return_exceptions=True` returns ordinary operation exceptions as items rather than immediately propagating them. The list comprehension identifies those failures before unpacking results as evidence dictionaries. This is an explicit **all-required-inputs policy**: either source failure prevents a draft.

That choice is not universally correct. A system could return a partial draft clearly marked with unavailable evidence. The important point is to choose deliberately. Silently omitting the failed policy branch would make incomplete evidence look like a normal answer.

## A separate boundary for action

A valid draft is still not an approval. `authorise_handoff` checks both the case identity and the review decision. It returns readiness, not an execution receipt. Nothing has been handed off by this code.

The approval dictionary is a simplified teaching input. A real application must obtain it through an authenticated review process, bind it to the precise proposal version, verify the reviewer's authority and detect changes since approval. Matching `case_id` alone would allow an old approval to be reused for a changed draft. Module 12 develops that version problem.

Likewise, checking that source fields exist does not prove their content. The two fake functions always return the same values. In a real system, source status, scope and meaning still need assessment.

## Read the original orchestration

The course's [orchestration notebook](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/2_openai/2_lab2.ipynb) compares code-controlled parallel drafting with specialist agents exposed through `as_tool` and a handoff. Its examples include sending email. In this guide, read those paths as code rather than assuming that the final send is necessary for learning the pattern.

In [ResearchManager](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/2_openai/deep_research/research_manager.py), `run` plans searches, performs them, writes a report and then sends email. Its `perform_searches` uses `asyncio.gather(*tasks)`. The star expands the list of coroutines into separate arguments. Unlike our example, that call does not set `return_exceptions=True`. The difference matters when a search fails.

`yield` in the manager's asynchronous generator produces progress updates as work proceeds. “Searches complete” is a status message about that stage. The report's claims still depend on the quality of search results, source selection and synthesis. [Planner](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/2_openai/deep_research/planner_agent.py) and [writer](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/2_openai/deep_research/writer_agent.py) definitions show which output structures the manager expects.

## Alternatives worth comparing

A sequential implementation is easier to debug and may suit services with tight rate limits. Parallel reads can reduce waiting when dependencies allow them. A durable job queue is more suitable when work must outlive the web request, recover after a process crash or wait for an approver.

A model-selected manager can adapt its choice of specialists, but it makes the dependency path less fixed. If both evidence sources are mandatory on every case, ordinary Python can enforce that requirement directly. Use model judgement where the task needs interpretation, not to rediscover an invariant rule each time.

**Try it:** Replace `policy_evidence` with an async function that raises `TimeoutError`. Predict the returned status and whether authorisation can proceed. Then explain why returning a model's reassurance would not supply the missing policy evidence.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.
