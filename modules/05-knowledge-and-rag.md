# Module 5: Organisational knowledge and RAG

[Previous module](04-evaluation-and-code-generation.md) · [Guide index](../README.md) · [Next module](06-data-baselines-and-adaptation.md)

## What you should be able to do

Explain embeddings, chunks and retrieval; trace basic and enhanced RAG implementations; distinguish retrieval quality from answer quality; and design a knowledge assistant that preserves source authority and competing interpretations.

**Course walkthrough:** [day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/day1.ipynb), [day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/day2.ipynb), [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/day3.ipynb), [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/day4.ipynb), [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/day5.ipynb), [basic ingestion](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/implementation/ingest.py), [basic answering](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/implementation/answer.py), [enhanced ingestion](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/pro_implementation/ingest.py), [enhanced answering](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/pro_implementation/answer.py), [evaluation](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/evaluation/eval.py), and [app](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/app.py).

## 1. Concepts: retrieving evidence at inference time

**Retrieval-augmented generation (RAG)** retrieves relevant material and supplies it as context for generation. It changes the evidence available at inference time without changing model weights. It is a useful architecture for changing organisational knowledge, but does not guarantee that the right evidence is found or faithfully used.

An **embedding** represents text numerically so a similarity function can compare it with other text. Similarity can capture related meaning, but is not a measure of truth, authority or permission. Two contradictory policies can be semantically close.

A **chunk** is a retrieval unit: an excerpt plus metadata. Small chunks can isolate a fact but lose qualifications. Large chunks retain context but may dilute matches and occupy more prompt space. Overlap reduces boundary loss while increasing duplication and storage. Heading-aware or section-aware splitting can preserve relationships that fixed character boundaries miss.

A **vector store** stores embeddings and associated records. Similarity search returns candidates; a reranker can reorder them against the question. The query and stored documents must use compatible embedding representations. Equal vector dimensions alone are not enough to make two embedding models interchangeable. Chroma distinguishes similarity `query` from record-oriented `get`. [Official query documentation](https://docs.trychroma.com/docs/querying-collections/query-and-get).

RAG has two flows:

```text
Ingestion: source → parse → chunk → embed → index
Answering: question → retrieve → select evidence → generate → show sources
```

The first can run on a schedule or source change. The second runs per question. Do not re-ingest everything just because a user asks another question.

## 2. What the code does

### Day 1: establish a simple retrieval baseline

The notebook reads employee and product files into a dictionary. It normalises a user message into lowercase words and returns documents whose keys appear in that message. This demonstrates retrieval without a vector database.

It is also intentionally limited. Using an employee's final name as a key can collide. A multiword product key may not match individual tokens. A reliable extension would use stable IDs and aliases rather than assume a filename-derived word uniquely identifies a record.

### Days 2–3 and `implementation/`: build a persistent index

`fetch_documents()` loads Markdown files and adds a `doc_type` metadata value. `create_chunks()` splits documents. The day 2 notebook uses 1,000-character chunks with 200-character overlap; the packaged basic implementation uses 500 and 200. Read the actual version you run rather than treating one parameter as a universal recommendation.

`create_embeddings()` builds a persisted Chroma collection. Existing collections are deleted in this teaching rebuild. In a service, versioned indexes and a controlled switch can avoid destructive rebuilds and inconsistent queries.

`answer_question` combines the current question with previous user turns for retrieval, retrieves documents, joins their text, constructs messages and invokes the model. It returns `(answer, docs)`, preserving evidence for the UI. The UI then renders both conversation and source context.

Concatenating all prior user questions can introduce stale topics. It is a baseline history strategy, not semantic conversation understanding. Also check retriever configuration for your installed version: explicitly configure `search_kwargs={"k": ...}` when creating a retriever rather than assuming every `invoke` keyword changes its search behaviour.

### Day 5 and `pro_implementation/`: add stages selectively

The enhanced ingestion asks a model to create chunks containing a headline, summary and original text. Pydantic classes define the expected shape. A multiprocessing pool processes documents concurrently; `imap_unordered` yields whichever result finishes next. Exponential retry delays address some transient errors, but the shown decorator lacks an explicit stop condition. A production pipeline needs bounded attempts and a failure record.

Generated headlines can improve matching, but generated summaries may distort a source. A field called `original_text` is not proof of exact copying: verify it against the source or store exact source spans directly. Preserve original documents independently.

The enhanced query flow is:

1. `rewrite_query` makes a short, context-rich search query.
2. `fetch_context_unranked` searches for both the original and rewritten query.
3. `merge_chunks` merges results by text equality.
4. `rerank` asks for a structured ordering of candidate IDs.
5. `fetch_context` keeps the first `FINAL_K` results.
6. `make_rag_messages` includes source-labelled extracts before answer generation.

Keeping the original query alongside the rewritten query can reduce losses when the rewrite is wrong. Still validate reranker IDs: correct JSON types do not prevent duplicates, omitted IDs or out-of-range values. Stable chunk IDs offer better deduplication than comparing whole strings.

### Day 4: inspect what evaluation actually measures

`evaluation/test.py` loads JSONL cases with a question, keywords, reference answer and category. `calculate_mrr` computes reciprocal rank for the first retrieved chunk containing a keyword; `evaluate_retrieval` averages that over keywords. Coverage counts how many expected keywords appear.

The nDCG helper assigns binary relevance by keyword occurrence and calculates the ideal ordering from the retrieved set itself. This evaluates ranking within retrieved candidates, not recall over every relevant document in the corpus. A high score can coexist with missing critical evidence.

The answer judge scores accuracy, completeness and relevance against a reference. Although descriptions mention retrieved context, the inspected `judge_messages` do not actually include those documents. Do not interpret the resulting scores as a direct grounding audit. Add evidence comparison explicitly if that is your evaluation objective.

## 3. Learn the patterns and a simple alternative

**Teaching example: dependency-free keyword retrieval with explicit evidence:**

```python
def retrieve(question, records, k=2):
    terms = set(question.lower().split())
    scored = []
    for record in records:
        overlap = len(terms & set(record["text"].lower().split()))
        if overlap:
            scored.append((overlap, record))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [record for _, record in scored[:k]]

records = [
    {"id": "policy-v2", "text": "Operations owns routine requests"},
    {"id": "exception-v1", "text": "Specialists review requests involving exceptions"},
]
evidence = retrieve("Who owns routine requests", records)
```

This baseline is deliberately weak: punctuation, inflections and synonyms are untreated. Its value is transparency. If a vector-based implementation cannot outperform a basic search baseline on your questions, investigate before adding further stages.

Recognise **extract–transform–load**, **metadata propagation**, **schema validation**, **two-stage retrieval**, **query rewriting**, **deduplication**, and **returning evidence alongside an answer**.

| Choice | Alternative | Decision criterion |
|---|---|---|
| Dense similarity | Keyword/BM25 or hybrid search | Exact identifiers and uncommon names may need lexical matching |
| Fixed-size chunks | Section/heading-aware chunks | Qualifications and policy structure must stay together |
| LLM chunk summaries | Exact spans with deterministic metadata | Fidelity is more important than semantic enrichment |
| LLM reranker | Cross-encoder or no reranker | Measure quality gain against latency and complexity |
| One shared index | Tenant/scope-separated indexes or enforced filters | Access boundaries must hold before context reaches the model |
| Concatenated history | Contextual query rewrite with original-query fallback | Follow-up resolution matters without dragging in stale topics |

Metadata filters can restrict records, but filtering syntax alone is not an authorisation system. The application must derive permitted scope from trusted identity and policy, then enforce it on every retrieval. [Chroma metadata filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering).

## 4. Business application and organisation research

For Harbour, store the approved policy, the process owner's commentary and interview evidence as different source types. Include effective date, version, scope and owner. A policy tells you what should happen; an interview gives a situated account of practice. Neither should silently overwrite the other.

An answer to “Who handles exceptions?” could report the formal rule, a documented deviation and an unresolved ownership dispute. This is often more useful than one confident synthesis. Separate missing evidence from evidence of absence.

In research, retrieval can support locating passages and comparing interpretations. Theme generation does not establish construct validity or a causal explanation. Keep an audit trail from source passage to interpretation, and use human review to examine disconfirming cases.

Assess retrieval recall on labelled evidence sets, citation correctness, unsupported claims, appropriate abstention, freshness, access-boundary failures and review effort. Add questions that cross documents, refer to an earlier policy, contain an ambiguous name or should not be answerable at all.

## 5. Experiment, diagnose and reflect

**Exercise:** Create six synthetic records: two policies with different dates, two interview excerpts, one exception log and one irrelevant document. Define eight questions and label the needed evidence before building retrieval. Include a follow-up pronoun and a question outside the corpus.

Compare keyword search, a simple vector setup if available, and rewritten-query retrieval. Change only one stage per comparison. For a wrong answer, identify whether the cause is missing source, extraction, retrieval, context selection or generation.

**Common failures:** changing embeddings without re-indexing; conflicting metadata versions; no access filter; a rewritten query that changes intent; a plausible answer with decorative rather than supporting citations. A visually pleasing t-SNE cluster plot is not evidence that answers are accurate.

**Check your understanding:** Why is relevance different from authority? What does the inspected nDCG calculation omit? Why retain the original query? Can a schema establish that a source quote is exact?

**Answer cues:** matching meaning says nothing about who may define policy; missing corpus evidence can be invisible to the metric; rewriting can lose intent; exactness requires comparison to source content.

**Decision note:** Specify source authority, access scope, version rules, an abstention policy and a diagnostic evaluation set.
