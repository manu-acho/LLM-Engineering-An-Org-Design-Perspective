# Lesson 16.5: Trace instruction identity, time and assumed cost

[Download the matching notebook](/downloads/16-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

The model may stop before returning a complete brief. Follow the run's status as well as the words it produced. Identify which version of the instruction ran, which time was measured and which price would have to be assumed to estimate cost. Partial text is not an accepted brief.

Trace an instruction version and distinguish measured usage from assumed prices.

[Company and supply-chain context](../../HARBOUR.md) · [Module 16 business situation](../../reference/harbour-learning-journey.md#module-16)

## Practical activity: Inspect an incomplete response without accepting it as an answer.


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

### Complete the exercise

**Worked answer.** No. Its usage may still exist and should not be discarded. This cell uses an offline transport, not a paid service.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
