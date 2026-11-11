# Lesson 5.4: Calculate similarity and inspect what ranking means

[Module route](README.md) · [Next: build the retrieval pipeline](05-source-walkthrough.md)

A long policy might put an exception in the paragraph after a general rule. A chunk is a piece of text prepared for search. If the two paragraphs are split, the search might find the rule and miss the exception. Compare what the system ranks with what the adviser actually needs, then count how many required pieces made it into the returned list.

## Why turn text into numbers?

Keyword search compares visible words. An embedding model maps text into vectors so related expressions can have useful numerical relationships even when their words differ. The embedding is learned; a two-dimensional illustration cannot reproduce that learning. It can make the comparison operation understandable.

Imagine a query vector `[1, 1]`, a policy vector `[2, 2]` and an unrelated record `[1, -1]`. **Cosine similarity** compares their directions. The dot product of query and policy is four. Their lengths are the square roots of two and eight. Dividing four by the product of those lengths gives one. The unrelated record has dot product zero with the query, so its cosine is zero.

```python
from math import sqrt

def cosine(left, right):
    if len(left) != len(right):
        raise ValueError("Dimensions differ")
    denominator = sqrt(sum(x*x for x in left)) * sqrt(sum(x*x for x in right))
    if denominator == 0:
        raise ValueError("A zero vector has no direction")
    return sum(x*y for x, y in zip(left, right)) / denominator

assert abs(cosine([1, 1], [2, 2]) - 1) < 1e-12
assert cosine([1, 1], [1, -1]) == 0
```

Direction is not truth or source authority. An obsolete credit policy and a current credit policy can be very similar. Their difference may concern precisely the threshold the user needs. Metadata and authority rules therefore remain necessary alongside ranking.

## Chunk boundaries alter the object being compared

Suppose a policy says “Account managers may approve routine credits. Disputed deliveries require finance review.” Splitting after the first sentence can produce a highly relevant but incomplete passage. Overlap can retain the second sentence, but it also duplicates text. Larger chunks can preserve conditions while consuming more context.

Compare two chunking configurations on the same labelled questions. Do not assume that one size is universally best. Measure whether the complete supporting passage is available, not merely whether the word “credit” appears.

## Calculate retrieval measures

For a fictional question, two passages are labelled necessary: P-3 contains the rule and P-4 the exception. The system returns `[P-9, P-3, P-8]`. Precision at three is `1/3`, because one of three returned passages is relevant. Recall at three is `1/2`, because one of two required passages was found. Reciprocal rank is `1/2`, because the first relevant passage is second.

If the system returns P-3 first but still omits P-4, reciprocal rank becomes one while recall remains one-half. Improving rank has not repaired missing evidence. The denominator and relevance labels matter.

An answer can be factually consistent with P-3 and still omit the exception. Evaluate retrieval and the generated answer separately: correct passages, faithful claims, sufficient qualifications, appropriate abstention and useful source links.

## Introduce extra stages only against an observed failure

A query rewrite may resolve “Who handles it?” using earlier context. Retaining the original query offers a fallback when the rewrite changes intent. A reranker compares retrieved candidates more closely, but cannot rank a passage that was never retrieved. Hybrid search can combine exact-code matching with semantic matching.

**Worked exercise:** An embedding search fails on order `O-1704`, but a database lookup finds it. That is a reason to route exact identifiers to a suitable exact-match operation, not a reason to train embeddings until they approximate database identity. The better architecture can combine mechanisms rather than demand that one search method solve every task.

## Read the organisational connection

Similarity measures compare representations without resolving differences in meaning or interest. The research chapter explains [knowledge boundaries](../../reference/research/02-coordination.md#shared-data-and-shared-meaning).
