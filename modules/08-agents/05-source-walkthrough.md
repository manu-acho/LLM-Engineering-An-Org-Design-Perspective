# Lesson 8.5: Trace the decision transaction and command identity

[Download the matching notebook](/downloads/08-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Reject a different decision based on a stale case version.



A `try` block attempts an operation. A matching `except` handles the stated failure. An `else` after the handler runs only when no exception occurred; here it can expose an expected refusal that failed to happen.

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

Should the second manager silently overwrite the first decision?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.business import CaseStore
with TemporaryDirectory() as directory:
    store=CaseStore(Path(directory)/"case.db");store.seed()
    store.decide("H-17","north","a","manager",1,"return","first")
    try:
        store.decide("H-17","north","b","manager",1,"approve","second")
    except ValueError as error:
        print("Expected conflict:",error)
    else:
        raise AssertionError("A stale decision must fail")
```

No. The second action must use a current, permitted state and a fresh review.

### Complete the exercise

Write the prediction before consulting the worked answer: Should the second manager silently overwrite the first decision?

**Worked answer.** No. The second action must use a current, permitted state and a fresh review.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
