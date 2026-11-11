# Lesson 17.5: Inspect ownership, waiting and completion

[Download the matching notebook](/downloads/17-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Follow a case first claimed by one worker and then reclaimed by another after the lease expires. Identify the evidence that lets the second worker finish and makes the first worker's later result unacceptable. The case number has not changed, but permission to complete that attempt has.

Trace queue recovery and retry identity rather than assuming an external action occurs exactly once.

[Company and supply-chain context](../../HARBOUR.md) · [Module 17 business situation](../../reference/harbour-learning-journey.md#module-17)

## Practical activity: Reclaim a lease while refusing the former owner's completion.


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

### Complete the exercise

**Worked answer.** No. Expiration allows recovery of running work, not repetition of completed work.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
