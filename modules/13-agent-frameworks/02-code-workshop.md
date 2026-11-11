# Lesson 13.2: Run the same task in Python and LangGraph

[Download the matching notebook](/downloads/13-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

In one version ordinary Python code controls the sequence. In the other, LangGraph runs steps connected in a graph. Identify where the same case enters and where the result leaves each version. Keep the purpose and expected facts fixed so differences in the two runs can be interpreted.

Run the model-backed graph path and inspect its contribution.

[Company and supply-chain context](../../HARBOUR.md) · [Module 13 business situation](../../reference/harbour-learning-journey.md#module-13)

## Practical activity: Run a model-backed contribution inside LangGraph.


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

Does the first deterministic node call a language model?

```python
from ai_orgdesign.labs.m13 import graph
local=graph().invoke({"case_id":"H-17","tenant":"north"})
print("Deterministic graph first:",local)
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.frameworks import langgraph_run
    result=langgraph_run(gateway)
    print(result["brief"])
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. The live cell adds an actual model-backed investigation node.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
