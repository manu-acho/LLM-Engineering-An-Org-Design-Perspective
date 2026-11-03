# Lesson 5.2: Search, filter and return the evidence

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## Build a search you can inspect

We will use keyword overlap rather than embeddings. This makes the retrieval procedure visible without installing libraries. The limitations are part of the lesson, not a claim that this is a complete RAG service.

```python
records = [
    {"id": "P-1", "scope": "service", "current": True,
     "text": "Finance reviews disputed delivery credits"},
    {"id": "P-0", "scope": "service", "current": False,
     "text": "Account managers approve delivery credits"},
    {"id": "H-1", "scope": "restricted", "current": True,
     "text": "Staff credit eligibility depends on employment terms"},
]

def retrieve(question, records, permitted_scopes, k=2):
    terms = set(question.lower().split())
    candidates = []
    for record in records:
        if record["scope"] not in permitted_scopes or not record["current"]:
            continue
        words = set(record["text"].lower().split())
        score = len(terms & words)
        if score > 0:
            candidates.append((score, record))
    candidates.sort(key=lambda pair: pair[0], reverse=True)
    return [record for score, record in candidates[:k]]

evidence = retrieve("Who reviews delivery credits", records, {"service"})
```

## Separate policy filtering from ranking

Each dictionary has text and metadata. In a real organisation, `current` should follow a version/effective-date policy; here it is a supplied teaching flag. Likewise, `permitted_scopes` is supplied locally so the example is readable. An operational application must derive permissions from trusted identity and authorisation.

The loop first excludes records outside scope or marked non-current. `continue` skips the rest of that loop iteration. Filtering before evidence reaches the model matters: you cannot disclose a restricted passage to the model and assume that a later prompt will undo the disclosure.

`lower()` removes case differences; `split()` makes whitespace-delimited pieces; `set()` keeps unique pieces. `terms & words` calculates the set intersection, the terms present in both. `len` counts them. It is a simple relevance score.

The procedure appends a tuple containing score and record. `sort` orders the list in place. The `key` argument supplies a function telling Python which value to compare. `lambda pair: pair[0]` is a short unnamed function that selects the tuple's score. `reverse=True` puts larger scores first. The final comprehension returns records without the scores, limited by `k`.

Our query retrieves P-1. P-0 is excluded as non-current, even though it matches several terms. H-1 is excluded by scope. The result demonstrates a rule-based retrieval boundary, not the correctness of the policy flags themselves.

## Build context without losing identity

```python
def make_context(evidence):
    if not evidence:
        return "No permitted current evidence was found."
    return "\n\n".join(f"[{r['id']}] {r['text']}" for r in evidence)

context = make_context(evidence)
```

`join` combines the prepared strings with blank lines. Including the source ID keeps a route back to the record. A generation adapter can receive this context plus the question. Its answer should not exceed what these records support.

Returning the evidence separately is often preferable to returning only an answer string. A UI can then show exact passages, and an evaluator can inspect what the model actually received.

## Connect to the original implementations

Week 5 begins with dictionary-based retrieval, then introduces chunking, embeddings and Chroma. In [implementation/ingest.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/implementation/ingest.py), documents acquire metadata, are split and indexed. In [implementation/answer.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/implementation/answer.py), the question retrieves documents that are joined into context, and the function returns answer plus documents.

The enhanced implementation rewrites queries, searches both forms, merges results and reranks them. Each transformation needs inspection. A rewrite can change intent. Merging by text can confuse versions. A reranker returning an ID list needs checks for missing, duplicate or out-of-range IDs.

The source evaluation helper measures keyword hits and ranking positions. Those are useful diagnostics, but keywords can appear in a passage that contradicts the intended answer. The compact [engineering chapter](../05-knowledge-and-rag.md) explains the exact limitations of its metrics and judge prompt.

## Alternatives and practice

Exact lexical search handles order numbers and named codes well. Embeddings help with paraphrases. Hybrid retrieval combines approaches; a reranker can refine candidate order. More stages are worthwhile only when they solve observed failures.

Try “Who handles commercial adjustments?” in our toy search. It may return no useful result because the terms do not overlap. That is a representation limitation, not proof that no policy exists. Then mark P-0 current as well and inspect what the program does. It can retrieve conflicting records; it cannot resolve policy authority without an explicit rule.

**What the example shows:** An empty result should become a bounded statement about the search, not a declaration that the organisation has no policy. Conflicting evidence should trigger a version/scope check or a visible uncertainty, not arbitrary selection of the most convenient sentence.
