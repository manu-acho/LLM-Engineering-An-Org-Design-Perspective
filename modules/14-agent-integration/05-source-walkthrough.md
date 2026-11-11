# Lesson 14.5: Run the actual MCP client and server exchange

[Download the matching notebook](/downloads/14-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

The client asks the server what tools it offers, then requests a particular operation. Follow what was discovered and what was actually called; they are separate events. A model selecting a discovered tool does not bypass the server's checks on the request.

Follow a model’s proposed tool use through the actual MCP connection and observations.

[Company and supply-chain context](../../HARBOUR.md) · [Module 14 business situation](../../reference/harbour-learning-journey.md#module-14)

## Practical activity: Let a model use tools discovered through a real MCP exchange.

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

Is the model connected directly to a general database console?

```python
print("The live cell starts the local stdio server, discovers tools and returns their observations to the model.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.labs.m14 import model_exchange
    result=await model_exchange(gateway)
    print(result["text"])
    print(result["trace"])
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. It receives the advertised narrow read capabilities.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
