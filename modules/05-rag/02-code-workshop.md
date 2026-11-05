# Lesson 5.2: Retrieve current permitted evidence

[Download the matching notebook](/downloads/05-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

A policy assistant needs the current permitted evidence, not simply a plausible paragraph. At Harbour an older policy, another region's policy and a current policy can share many words, making relevance alone an inadequate selection rule.

The implementation lives in `src/ai_orgdesign/labs/m05.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

retrieve first selects records with the requested tenant and active status. Only those records enter TfidfVectorizer.fit_transform. TF-IDF gives words weights based on their frequency within and across the selected documents; it creates sparse numerical vectors, not neural embeddings. The query uses the fitted vocabulary through transform. Cosine similarity compares vector direction, and ranking uses score followed by document ID to break ties reproducibly. Positive-score results retain document identity and version. grounded_context formats that evidence for a later answer stage, but performs no generation.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m05 import retrieve, grounded_context
hits = retrieve("delivery evidence")
assert [hit["id"] for hit in hits] == ["P-2"]
print(grounded_context(hits))
```

Searching delivery evidence in north returns the active P-2 policy. It excludes the retired P-1 and the south P-3 before fitting or ranking. A query whose words do not occur in the permitted vocabulary returns no hits. Returning no evidence is different from answering that no policy exists.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Ask whether filtering after a global top-two search can lose the best permitted result. Then remove all permitted documents and decide what the service should show.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** A global top-two may contain only forbidden or obsolete records. Removing them afterward cannot recover the permitted records that never entered the shortlist. An empty permitted corpus returns an empty list in this lab. The interface should report that evidence was not available and route the question appropriately, rather than invent an answer.

## Consider the alternative

Keyword search is easy to inspect but can miss paraphrases. Dense embeddings may recover semantic matches but require their own model, index lifecycle and evaluation. Hybrid retrieval combines signals. None reconciles conflicting authority automatically. Chunking and reranking should respond to observed failures, not an assumed need for a more elaborate stack.

The [organisation design reading](../../reference/research/02-coordination.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
