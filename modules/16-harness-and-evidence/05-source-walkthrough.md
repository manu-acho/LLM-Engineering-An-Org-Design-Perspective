# Lesson 16.5: Trace instruction identity, time and assumed cost

[Download the matching notebook](/downloads/16-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Inspect an incomplete response without accepting it as an answer.





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

Should a response marked incomplete count as a completed answer?

```python
import httpx
from openai import OpenAI
from ai_orgdesign.provider import Gateway,ModelRunError
body={"id":"offline-response","object":"response","created_at":1,"model":"offline-test","status":"incomplete","output":[],"usage":{"input_tokens":5,"output_tokens":5,"total_tokens":10}}
transport=httpx.MockTransport(lambda request:httpx.Response(200,json=body))
client=OpenAI(api_key="offline-fixture",base_url="https://course.invalid/v1",http_client=httpx.Client(transport=transport))
fixture=Gateway(client=client,model="offline-test",max_requests=1)
try:
    fixture.generate("fixture")
except ModelRunError as error:
    print("Expected incomplete-response failure:",error)
print(fixture.ledger())
```

No. Its usage may still exist and should not be discarded. This cell uses an offline transport, not a paid service.

### Complete the exercise

Write the prediction before consulting the worked answer: Should a response marked incomplete count as a completed answer?

**Worked answer.** No. Its usage may still exist and should not be discarded. This cell uses an offline transport, not a paid service.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
