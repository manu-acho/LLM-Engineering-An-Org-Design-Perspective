# Lesson 11.5: Find missing prerequisites and task cycles

[Download the matching notebook](/downloads/11-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

A cycle occurs if task A waits for B and B waits for A. Neither can begin. First check that all named prerequisites exist and can be completed in some order. Then compare independent calls in a live run and see whether their work overlaps in time. Being allowed to overlap and actually overlapping are different claims.

Compare observed parallel execution time with the human work still waiting afterwards.

[Company and supply-chain context](../../HARBOUR.md) · [Module 11 business situation](../../reference/harbour-learning-journey.md#module-11)

## Practical activity: Run genuinely overlapping specialist calls and inspect elapsed work.

 An asynchronous operation can suspend while compatible work proceeds. The notebook uses await to obtain its result; this is different from a business acceptance acknowledgement.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

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

Can the coordinator run before both required specialists finish?

```python
import time
print("The live cell runs the two independent specialists concurrently, then coordinates their outputs.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import team
    started=time.perf_counter()
    result = await team(gateway,parallel=True)
    print(result)
    print("Observed elapsed seconds:",time.perf_counter()-started)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. Parallel preparation does not remove the dependency on both results.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
