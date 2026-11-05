# Lesson 4.5: Trace error categories and the chosen loss rule

[Download the matching notebook](/downloads/04-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Measure actual generated routes rather than inventing a score.

A reference label is an agreed target used for scoring. A split reserves different cases for different experiment stages; publicly visible teaching cases are not evidence of enterprise generalisation.



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

Should confirmation reference labels be included in a model's input?

```python
from ai_orgdesign.case_data import DEVELOPMENT_IDS, CONFIRMATION_IDS
assert not set(DEVELOPMENT_IDS) & set(CONFIRMATION_IDS)
print("Development IDs:", DEVELOPMENT_IDS)
print("Confirmation IDs:", CONFIRMATION_IDS)
```

No. The evaluator uses reference labels after generation; the model receives case evidence and policy.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import evaluate
    report = evaluate(gateway, ["H-17","H-19","H-20"])
    print(report)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: Should confirmation reference labels be included in a model's input?

**Worked answer.** No. The evaluator uses reference labels after generation; the model receives case evidence and policy.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
