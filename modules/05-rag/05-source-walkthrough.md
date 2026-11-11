# Lesson 5.5: Build and trace a complete retrieval-and-answering path

[Module route](README.md) · [Next: design knowledge ownership](06-design-lab.md)

Follow a small set of documents into storage, through search and into the supplied context. Embeddings are lists of numbers that allow text to be compared; the local example makes the representation visible. Finding a passage supplies material for a response, while the source and its limits still need to travel with it.

[Open the companion workshop notebook](../../notebooks/05-rag.ipynb).

## Follow the original ingestion path

Open the course's [ingestion implementation](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/implementation/ingest.py). `fetch_documents` iterates through folders, loads Markdown and adds a `doc_type` field. The folder structure therefore becomes metadata used to interpret sources.

`create_chunks` splits those documents using a 500-character target and 200-character overlap in this implementation. These are characters, not tokens. `create_embeddings` uses the configured embedding service and persists records in Chroma. Its teaching rebuild deletes an existing collection. A maintained service should instead consider versioned builds and an intentional switch between indexes, so readers do not see a partially rebuilt knowledge base.

The [answer implementation](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/implementation/answer.py) combines prior user messages with the current question for retrieval, joins returned passages into context, constructs model messages and returns both answer and documents. Returning documents keeps evidence available to the interface and evaluator.

## A real vector-store lab without external models

This independent lab needs `chromadb`. It uses explicit invented vectors to expose storage and retrieval. There is no embedding service, model download or network request. The vectors illustrate the interface rather than semantic quality. The temporary index is deleted when the block exits.

```python
from tempfile import TemporaryDirectory
import chromadb
from chromadb.config import Settings

def prepare_answer(question, collection, embed, generate):
    found = collection.query(
        query_embeddings=[embed(question)], n_results=2,
        where={"current": True}, include=["documents", "metadatas"],
    )
    evidence = [
        {"id": source_id, "text": text, "metadata": metadata}
        for source_id, text, metadata in zip(
            found["ids"][0], found["documents"][0], found["metadatas"][0]
        )
    ]
    messages = [
        {"role": "system", "content": "Use supplied evidence; preserve exceptions."},
        {"role": "user", "content": question + "\n" + "\n".join(
            f"[{r['id']}] {r['text']}" for r in evidence
        )},
    ]
    return {"answer": generate(messages), "evidence": evidence}

with TemporaryDirectory() as directory:
    client = chromadb.PersistentClient(path=directory, settings=Settings(anonymized_telemetry=False))
    collection = client.create_collection("policies", embedding_function=None)
    collection.add(
        ids=["P-3", "P-4", "P-old"],
        documents=[
            "Finance reviews disputed credits.",
            "Operations supplies delivery evidence.",
            "Account managers approve all credits.",
        ],
        metadatas=[{"current": True}, {"current": True}, {"current": False}],
        embeddings=[[1.0, 0.0], [0.8, 0.2], [1.0, 0.0]],
    )
    result = prepare_answer(
        "Who handles a disputed credit?", collection,
        embed=lambda question: [1.0, 0.0],
        generate=lambda messages: "DRAFT: inspect P-3 and P-4 together.",
    )
    assert {r["id"] for r in result["evidence"]} == {"P-3", "P-4"}
    print(result["answer"])
```

The constant embedding and fake answer are deliberate dependencies. This lab tests an actual vector-store query, metadata exclusion, evidence assembly and generation boundary. It does not test learned retrieval or language synthesis. Replace `embed` with a compatible query embedding function and `generate` with the adapter from Lesson 1.5 to create an external integration. Rebuild document vectors with that same embedding representation first. Matching dimensionality alone is insufficient.

## Inspect every intermediate artefact

To connect an embedding service, keep document and question embedding under the same explicit contract. This optional adapter requires a configured OpenAI client and compatible embedding model, and makes an external request when called. It was not executed against a provider during authoring. It follows the embedding interface used in the original course.

```python
def embed_texts(client, model, texts):
    response = client.embeddings.create(model=model, input=texts)
    rows = sorted(response.data, key=lambda item: item.index)
    if [row.index for row in rows] != list(range(len(texts))):
        raise ValueError("Embedding results do not match the submitted inputs")
    return [row.embedding for row in rows]
```

Use the returned document vectors during index construction. For a query, supply a single question and use its first returned vector. Store the embedding model/revision with the index, then reject an incompatible query configuration rather than silently comparing unrelated coordinate systems. Replacing only the question's invented vector in the lab would not produce meaningful semantic search.

Retain original source, chunk boundaries, metadata, embedding identity, candidate IDs, final selected evidence, messages and output. For a failed answer, ask where the necessary passage disappeared. A correct source can be lost in extraction, chunking, retrieval, reranking or prompt assembly.

The course's [enhanced answer path](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week5/pro_implementation/answer.py) rewrites the query, retrieves twice, merges by text, reranks IDs and keeps a final subset. Inspect `rerank`: an integer list still needs checks for duplicate, omitted and out-of-range IDs. An ID of zero in code subtracting one can accidentally select the last Python list item.

Its retry decorator specifies waiting behaviour without an explicit stopping policy. Waiting longer and stopping eventually are different controls. Define both for a maintained service.

## Interpret an experiment

Prepare questions requiring a rule, an exception, two documents, an obsolete version and an answer outside the corpus. Label needed evidence first. Compare lexical search, vector retrieval and reranking on those same questions. Retain wrong and empty results. A higher ranking score is useful only if it improves the evidence and answers needed for the application.

**Worked diagnosis:** The answer cites P-3 accurately but misses a policy exception absent from the returned evidence. Changing the answer prompt may help abstention, but cannot supply that missing passage. Investigate chunking and retrieval, then repeat the frozen evaluation.

**Technical reference:** [Chroma query and get](https://docs.trychroma.com/docs/querying-collections/query-and-get). The course source and this independent lab use different embedding arrangements.

## Read the organisational connection

A retrieved contribution needs source identity, uncertainty and acceptance conditions. The research chapter explains [the worked handoff design](../../reference/research/02-coordination.md#a-worked-handoff-design).
