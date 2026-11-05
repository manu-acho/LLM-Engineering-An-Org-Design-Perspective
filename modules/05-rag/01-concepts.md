# Lesson 5.1: How an assistant finds organisational knowledge

[Download the matching notebook](/downloads/05-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## The policy is not automatically inside the model

Harbour's assistant is asked: “Who can authorise a credit when delivery is disputed?” The answer may depend on current policy, the order's region, value and exception category. A language model's general training does not establish the current internal rule.

One solution is to retrieve relevant records and provide them to the model before it answers. This is **retrieval-augmented generation**, usually abbreviated RAG. Retrieval supplies candidate evidence; generation uses that evidence to formulate an answer. It is not another name for training the model on the documents.

## Begin with ordinary search

Suppose a small folder contains three policies. A keyword search can find documents containing “credit”. This approach is easy to inspect but may miss a policy that calls the same action a “commercial adjustment”. It may also retrieve an irrelevant discussion of credit cards.

Search therefore needs a representation of the question, a way of comparing it with records and a rule for selecting candidates. Different approaches solve those problems differently. Exact search is useful for IDs and precise phrases. Semantic search can help with paraphrases. Neither alone establishes which policy is authoritative.

## Embeddings: comparing numerical representations

An **embedding** is a numerical representation of an item such as a sentence. A model maps text to a vector, an ordered list of numbers. A similarity method compares the vectors to identify texts that may be related.

Imagine placing documents on a map where related topics tend to be nearby. Real embeddings have many dimensions, not just the two on a printed map. The analogy helps explain proximity; it does not mean that every numerical direction has a simple label or that nearby texts agree.

“Finance approves credits” and “Finance must not approve this category” may be semantically related. Search can retrieve both. Similarity concerns relation in the representation, not truth, current validity, agreement or access rights.

The same compatible embedding method should be used for indexed material and queries. Two vectors of the same length from unrelated models need not occupy a comparable representation space.

## Why documents are split into chunks

A **chunk** is a unit selected for retrieval, usually text plus descriptive information. A ten-page policy may contain several topics. Retrieving only the relevant section saves space and can focus the answer.

Splitting can also remove meaning. A sentence approving credits may depend on an exception stated in the next paragraph. **Overlap** repeats some text across neighbouring chunks to reduce boundary loss, but increases duplication. Section-aware splitting can preserve headings and qualifications more naturally than a fixed number of characters.

There is no universally correct chunk size. Evaluate whether the needed evidence and its conditions remain together on representative questions.

## Metadata carries context about evidence

**Metadata** is information about a record: source ID, owner, effective date, version, business scope or access category. The text alone may not say which policy supersedes another. Metadata and explicit policy rules help the application handle that distinction.

A **vector store** retains embeddings and associated records. It can perform a similarity query, retrieve records by ID and apply supported filters. The store is not an organisational authority by itself. A filter should reflect trusted access policy rather than a user's or model's claimed entitlement. See [Chroma's query documentation](https://docs.trychroma.com/docs/querying-collections/query-and-get) for the technical interface.

## Two pipelines rather than one

The ingestion pipeline loads sources, extracts text, creates chunks, generates embeddings and builds an index. The answering pipeline prepares a query, retrieves candidates, selects evidence, constructs a prompt and generates an answer with source references.

**Ingestion** need not run every time someone asks a question. It should respond appropriately to source updates. An old index can faithfully retrieve a policy that is no longer current; the error is a freshness/design problem even if similarity search worked perfectly.

Some systems **rewrite** a follow-up question to make its referents explicit. Others **rerank** retrieved candidates by examining their relevance more closely. These add stages with their own benefits, errors, latency and costs. Keep a simpler search baseline to discover whether each stage helps.

## Evidence support and an answer are separate objects

A retrieved document may be relevant while failing to support the specific answer. A citation can point to a real file and still be misleading. Check whether the claim follows from the cited passage, including conditions and scope.

Separate retrieval evaluation from answer evaluation. First ask whether the needed evidence was available and retrieved. Then ask whether generation represented it faithfully and handled absence or conflict appropriately.

**Check:** A system cites an old policy that exactly matches the question. Which parts might be working, and which part could still be wrong? A strong answer identifies successful matching alongside failed version selection, and avoids attributing every wrong answer to generation.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Finding passages does not settle what different groups understand them to mean. The research chapter explains [shared data and shared meaning](../../reference/research/02-coordination.md#shared-data-and-shared-meaning).
