# Lesson 5.5: Follow filtering, vectorisation and ranking

[Download the matching notebook](/downloads/05-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m05.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

retrieve first selects records with the requested tenant and active status. Only those records enter TfidfVectorizer.fit_transform. TF-IDF gives words weights based on their frequency within and across the selected documents; it creates sparse numerical vectors, not neural embeddings. The query uses the fitted vocabulary through transform. Cosine similarity compares vector direction, and ranking uses score followed by document ID to break ties reproducibly. Positive-score results retain document identity and version. grounded_context formats that evidence for a later answer stage, but performs no generation.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Ask whether filtering after a global top-two search can lose the best permitted result. Then remove all permitted documents and decide what the service should show.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m05 import retrieve
assert retrieve("unmatchedzzzz") == []
assert retrieve("delivery", tenant="unknown") == []
print("No permitted evidence is a visible outcome.")
```

**Interpretation.** A global top-two may contain only forbidden or obsolete records. Removing them afterward cannot recover the permitted records that never entered the shortlist. An empty permitted corpus returns an empty list in this lab. The interface should report that evidence was not available and route the question appropriately, rather than invent an answer.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

Searching delivery evidence in north returns the active P-2 policy. It excludes the retired P-1 and the south P-3 before fitting or ranking. A query whose words do not occur in the permitted vocabulary returns no hits. Returning no evidence is different from answering that no policy exists.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. Keyword search is easy to inspect but can miss paraphrases. Dense embeddings may recover semantic matches but require their own model, index lifecycle and evaluation. Hybrid retrieval combines signals. None reconciles conflicting authority automatically. Chunking and reranking should respond to observed failures, not an assumed need for a more elaborate stack.

The [research connection](../../reference/research/02-coordination.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
