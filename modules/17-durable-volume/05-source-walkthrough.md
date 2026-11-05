# Lesson 17.5: Inspect ownership, waiting and completion

[Download the matching notebook](/downloads/17-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Reclaim a lease while refusing the former owner's completion.





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

May attempt-3 reclaim this completed job?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.business import CaseStore
with TemporaryDirectory() as directory:
    store=CaseStore(Path(directory)/"jobs.db");store.enqueue("one")
    assert store.claim("one","attempt-1",0)
    assert not store.claim("one","attempt-2",5)
    assert store.claim("one","attempt-2",11)
    store.finish("one","attempt-2",12)
    assert not store.claim("one","attempt-3",30)
print("Completed jobs are not reclaimed")
```

No. Expiration allows recovery of running work, not repetition of completed work.

### Complete the exercise

Write the prediction before consulting the worked answer: May attempt-3 reclaim this completed job?

**Worked answer.** No. Expiration allows recovery of running work, not repetition of completed work.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
