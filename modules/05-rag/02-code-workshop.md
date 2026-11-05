# Lesson 5.2: Retrieve current permitted evidence

[Download the matching notebook](/downloads/05-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Follow filtering and lexical ranking into the returned evidence.





The exercise code below runs from a prepared course checkout. In the matching notebook, the setup cell already supplies ROOT and RUN_LIVE. If following the code here, run this setup first:

```python
from ai_orgdesign.workspace import project_root, live_mode
ROOT = project_root()
RUN_LIVE = live_mode()
if RUN_LIVE:
    from ai_orgdesign.provider import Gateway
    gateway = Gateway(max_requests=12, max_output_tokens=1000)
print("Live mode:", RUN_LIVE)
```

### Predict and follow the values

Which tenant should every result belong to?

```python
from ai_orgdesign.case_data import POLICIES
from ai_orgdesign.labs.m05 import retrieve
hits = retrieve("delivery quantity", tenant="north", documents=POLICIES)
print([(hit["id"], hit["score"]) for hit in hits])
assert all(hit["active"] and hit["tenant"] == "north" for hit in hits)
```

north. Filtering after a global shortlist could discard forbidden hits without recovering the best permitted evidence.

### Complete the exercise

Write the prediction before consulting the worked answer: Which tenant should every result belong to?

**Worked answer.** north. Filtering after a global shortlist could discard forbidden hits without recovering the best permitted evidence.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

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
