# Lesson 10.5: Configure an agent, run it and inspect its result

[Module route](README.md) · [Next: compare organising arrangements](06-design-lab.md)

## Read the source's research manager

In [ResearchManager](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/2_openai/deep_research/research_manager.py), `run` creates a trace, asks a planner for searches, awaits concurrent searches, asks a writer for a report and passes that report to an email agent. `yield` produces progress information at successive stages.

`plan_searches` reads `result.final_output`, expecting the planner's structured output. `perform_searches` builds coroutine operations and awaits `asyncio.gather`. Results retain input ordering even if search completion times differ. The inspected function does not use `return_exceptions=True`; an exception can propagate rather than become a partial result.

The final email stage is an external effect. The original workflow is not executed in this lesson. A report written successfully and an email accepted by its provider are separate outcomes.

## A complete small SDK integration

The following new example needs `openai-agents`, `pydantic`, `OPENAI_API_KEY` and an accessible `OPENAI_MODEL`. It performs paid model requests if run. The only local tool reads synthetic data. It was not executed against a model during authoring.

```python
import asyncio
import os
from pydantic import BaseModel
from agents import Agent, Runner, function_tool, trace

@function_tool
def lookup_order(order_id: str) -> dict:
    """Read synthetic recorded quantities for order O-17."""
    if order_id != "O-17":
        raise ValueError("Unknown synthetic order")
    return {"source_id": "order-17:v1", "ordered": 12, "reported_received": 10}

class CaseDraft(BaseModel):
    reported_difference: int
    source_ids: list[str]
    unresolved: list[str]

async def main():
    investigator = Agent(
        name="Evidence investigator",
        model=os.environ["OPENAI_MODEL"],
        instructions=(
            "Read the synthetic order. Report the customer's quantity difference. "
            "Do not claim the shortage is verified or approve a remedy."
        ),
        tools=[lookup_order], output_type=CaseDraft,
    )
    with trace("Synthetic disputed delivery"):
        result = await Runner.run(
            investigator, "Investigate O-17", max_turns=4
        )
    draft = result.final_output
    if draft.reported_difference != 2 or draft.source_ids != ["order-17:v1"]:
        raise ValueError("Draft does not match this synthetic source contract")
    return draft

if __name__ == "__main__":
    print(asyncio.run(main()).model_dump())
```

`@function_tool` exposes a function through the SDK's tool machinery. Creating `Agent` defines its configuration. `Runner.run` executes the loop. `output_type` requests an inspectable result structure. The final deterministic check compares two fields with our known synthetic record. It does not establish all claims or prove that a tool was actually consulted; inspect the run items or trace when tool-use evidence matters.

In a notebook with a running event loop, use `await main()` rather than `asyncio.run`. A turn limit does not guarantee a draft: exceeding it is a failure outcome that the application must handle visibly.

## Add a specialist without confusing the control pattern

In the source [orchestration lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/2_openai/2_lab2.ipynb), a specialist can be exposed through `as_tool`. The coordinator calls it and receives a contribution. A handoff instead changes the active agent for the conversation branch. Neither creates accepted organisational ownership by itself.

When both order and policy evidence are always required, ordinary application code can enforce that dependency before invoking a writer. When choosing the next specialist requires interpretation, model routing can be tested against the fixed alternative. Keep evaluation cases and available evidence consistent.

## Interpret the resulting run

Read the structured output alongside tool events and sources. If the model returns correct arithmetic but claims verification elsewhere, the draft still needs correction. If the tool fails and the model returns a plausible answer, the application should expose the missing evidence rather than treat final-output existence as completion.

**Worked extension:** Add a policy specialist returning policy version and required review status. Require both records in application code before drafting. Then deliberately fail policy lookup. The appropriate terminal state is incomplete evidence, not a generated substitute policy.

**Documentation:** [OpenAI Agents SDK overview](https://developers.openai.com/api/docs/guides/agents/sdk). The pinned course supplies the source orchestration discussed here; the new small example is an independently authored integration.
