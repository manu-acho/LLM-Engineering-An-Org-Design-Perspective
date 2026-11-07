# Lesson 4.4: Calculate what a quality score leaves out

[Download the matching notebook](/downloads/04-04-measures-and-uncertainty.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: evaluate the generated program](05-source-walkthrough.md)

## Business context: Harbour

Interpret precision and recall using the cases that should have been found, rather than a reassuring overall percentage.

[Company and supply-chain context](../../HARBOUR.md) · [Module 4 business situation](../../reference/harbour-learning-journey.md#module-4)

## A decision rule creates different errors

Suppose an assistant flags cases requiring specialist review. In ten fictional cases, seven truly need review. It flags eight: six correctly and two unnecessarily. It misses one true review case. The remaining case correctly proceeds without review.

| Actual situation | Flagged | Not flagged |
|---|---|---|
| Review required | 6 true positives | 1 false negative |
| Review unnecessary | 2 false positives | 1 true negative |

**Precision** asks how many flagged cases were correctly flagged: `6 / 8 = 75%`. **Recall** asks how many cases needing review were found: `6 / 7`, approximately 85.7%. **Accuracy** asks how many decisions matched overall: `(6 + 1) / 10 = 70%`.

Each denominator answers a different question. Reviewers care about the usefulness of incoming flags. A process owner concerned about missed controls cares about recall. Neither number alone expresses the cost of errors.

## Add consequences without hiding the assumptions

If unnecessary review costs five minutes and a missed review creates an illustrative expected loss of £100, convert effort consistently before combining quantities. At £30 an hour, two unnecessary reviews cost £5 in capacity. The missed review contributes £100 under the assumed loss estimate. These values are fictional and must be elicited or estimated for a real service.

A rule that flags everything has 100% recall here, but generates three unnecessary reviews. A rule that flags nothing uses no review capacity and misses all seven. The task is to choose an acceptable operating trade-off, not maximise a metric in isolation.

## Check how the sample was selected

Ten cases are enough to understand arithmetic. They are weak evidence of operating performance. If they came from last week's most troublesome complaints, their category frequencies may not represent ordinary work. If the same cases guided prompt revisions, they are development cases.

Keep a held-out set and report the underlying counts. One additional miss changes results substantially in a small sample. A larger sample reduces some sampling uncertainty, but does not repair missing case types or unreliable reference labels. Repeated outputs on one case measure variability for that case, not coverage of the population.

## Make evaluation labels inspectable

```python
def counts(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("Each case needs a prediction")
    if any(type(x) is not bool for x in actual + predicted):
        raise ValueError("Use explicit Boolean labels")
    return {
        "tp": sum(a and p for a, p in zip(actual, predicted)),
        "fp": sum(not a and p for a, p in zip(actual, predicted)),
        "fn": sum(a and not p for a, p in zip(actual, predicted)),
        "tn": sum(not a and not p for a, p in zip(actual, predicted)),
    }
```

The length check prevents `zip` from silently ignoring unmatched cases. Explicit Boolean labels prevent an error string from being interpreted as a positive label merely because non-empty strings are truthy in Python. Invalid outputs should have their own status before metric calculation.

## Compare systems on the same cases

If one system fails where another succeeds, inspect those paired cases. An average score can hide that one is better on routine work and worse on consequential exceptions. Keep the prompt, source revision, population, abstention rule and reviewer criteria in the experiment record.

**Worked check:** A supplier reports “95% accuracy” after excluding malformed answers. Ask how many answers were excluded and what happens to those cases operationally. Correctness among parseable outputs and coverage across all cases must both be reported. A system does not remove work by returning an unusable answer that disappears from the spreadsheet.

## Read the organisational connection

An aggregate score can conceal differences in case difficulty and work shifted to other roles. The research chapter explains [benefit evidence](../../reference/research/04-implementation.md#benefits-need-a-population-and-a-comparison).

## Practical activity: Calculate precision and recall with explicit counts.





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

What is recall for this example?

```python
true_positive, false_positive, false_negative = 3, 1, 2
precision = true_positive / (true_positive + false_positive)
recall = true_positive / (true_positive + false_negative)
print({"precision":precision,"recall":recall})
```

Three out of five actual positive cases were found, so recall is 0.6. Precision asks a different denominator question.

### Complete the exercise

Write the prediction before consulting the worked answer: What is recall for this example?

**Worked answer.** Three out of five actual positive cases were found, so recall is 0.6. Precision asks a different denominator question.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
