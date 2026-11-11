# Lesson 5.2: Retrieve current permitted evidence

[Download the matching notebook](/downloads/05-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

An old policy can contain exactly the right search words and still be the wrong policy to use. Filtering removes candidates that fail rules such as access or date. Ranking orders the candidates that remain by relevance. In the lab, track one excluded document and one returned document; the best match among eligible records may differ from the best match before filtering.

Filter for permitted region and current policy before using textual similarity to select passages.

[Company and supply-chain context](../../HARBOUR.md) · [Module 5 business situation](../../reference/harbour-learning-journey.md#module-5)

## Practical activity: Follow filtering and lexical ranking into the returned evidence.


### Predict and follow the values

Which tenant should every result belong to?

```python
from ai_orgdesign.case_data import POLICIES
from ai_orgdesign.labs.m05 import retrieve
hits = retrieve("delivery quantity", tenant="north", documents=POLICIES)
print([(hit["id"], hit["score"]) for hit in hits])
assert all(hit["active"] and hit["tenant"] == "north" for hit in hits)
```

### Complete the exercise

**Worked answer.** north. Filtering after a global shortlist could discard forbidden hits without recovering the best permitted evidence.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

### Programming practice

Write permitted(records, tenant) to select only active records in that tenant.

Start with the placeholder in the notebook, then compare with this worked solution. The contrasting checks are part of understanding the contract.

```python
def permitted(records, tenant):
    return [row for row in records if row["tenant"] == tenant and row["active"]]

rows=[{"tenant":"north","active":True},{"tenant":"south","active":True},{"tenant":"north","active":False}]
assert len(permitted(rows,"north")) == 1
assert permitted(rows,"missing") == []
```


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
