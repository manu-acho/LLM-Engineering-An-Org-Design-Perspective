# Lesson 4.5: Trace error categories and the chosen loss rule

[Download the matching notebook](/downloads/04-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Trace a generated route into its error category and loss calculation. Learn to keep the expected route separate from the information the model receives.

## Business context: Harbour

A generated route is the queue the model actually proposes for a case. An expected route is the reference choice the exercise uses to score it. First inspect one pair and name the error, if any. Then see how the chosen loss rule changes the result when an expensive mistake replaces a minor one. Live output must come from the run rather than a guessed answer.

Keep evaluation references out of model inputs and inspect actual generated routes against their defined meanings.

[Company and supply-chain context](../../HARBOUR.md) · [Module 4 business situation](../../reference/harbour-learning-journey.md#module-4)

## Practical activity: Measure actual generated routes rather than inventing a score.

A reference label is an agreed target used for scoring. A split reserves different cases for different experiment stages; publicly visible teaching cases are not evidence of enterprise generalisation.


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

Should confirmation reference labels be included in a model's input?

```python
from ai_orgdesign.case_data import DEVELOPMENT_IDS, CONFIRMATION_IDS
assert not set(DEVELOPMENT_IDS) & set(CONFIRMATION_IDS)
print("Development IDs:", DEVELOPMENT_IDS)
print("Confirmation IDs:", CONFIRMATION_IDS)
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

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

**Worked answer.** No. The evaluator uses reference labels after generation; the model receives case evidence and policy.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

The model receives case evidence and policy. The evaluator later compares the proposed route with the reference label and applies the declared penalties.

## What this means for the business process

Keep evaluation labels out of model input and let the process owner review disputed reference labels. Otherwise an apparent failure or gain can reflect a contested routing policy rather than the model's performance.

For the research behind this design choice, read [Decision premises](../../reference/research/03-decisions.md#decision-premises).

## Next lesson

The next lesson takes the evaluation beyond routing scores to examine total resolution and alternative explanations. [Lesson 4.6: Decide whether a measured improvement changes the organisation](06-design-lab.md).
