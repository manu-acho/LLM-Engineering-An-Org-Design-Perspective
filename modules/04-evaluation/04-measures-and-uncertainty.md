# Lesson 4.4: Calculate what a quality score leaves out

[Download the matching notebook](/downloads/04-04-measures-and-uncertainty.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: evaluate the generated program](05-source-walkthrough.md)

## Business context: Harbour

A rule that sends every uncertain case to a specialist catches more risky complaints and creates more unnecessary reviews. One kind of error misses a case that needs review; the other sends a case that did not need it. Follow the counts first. The loss rule then attaches explicit consequences to those counts so readers can question what the comparison values.

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


### Predict and follow the values

What is recall for this example?

```python
true_positive, false_positive, false_negative = 3, 1, 2
precision = true_positive / (true_positive + false_positive)
recall = true_positive / (true_positive + false_negative)
print({"precision":precision,"recall":recall})
```

### Complete the exercise

**Worked answer.** Three out of five actual positive cases were found, so recall is 0.6. Precision asks a different denominator question.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Compare drafting effort with timely investigation resolution

Consider four separate fictional investigation cases SC-M1–SC-M4 under two designed scenarios, A and B. Each case has been open for ten business hours at the observation point. The agreed exercise target is resolution within four business hours of opening; all four cases have passed that deadline. `resolved_hours` records the elapsed time to confirmed investigation resolution, or `None` if still open. This is a supplied scenario fact, not a model prediction, a delivery punctuality measure or proof of how Harbour performs.

Scenario B halves preparation time. Does it also improve the proportion resolved within target? `service_summary` uses all four eligible cases as the denominator, keeps open cases visible and separates preparation minutes from elapsed business hours. `<=` includes a resolution at exactly four hours. The function illustrates a declared measure; it is not a general business-calendar or event-validation library. In the counting expressions, `for row in rows` visits each case, and `sum` counts a true condition as one and a false condition as zero. The worked variation uses `dict(row)` to copy each record before changing it, preserving the original scenario.

```python
scenario_a = [
    {"id": "SC-M1", "prep_minutes": 4, "resolved_hours": 3},
    {"id": "SC-M2", "prep_minutes": 4, "resolved_hours": 5},
    {"id": "SC-M3", "prep_minutes": 4, "resolved_hours": None},
    {"id": "SC-M4", "prep_minutes": 4, "resolved_hours": 4},
]
scenario_b = [
    {"id": "SC-M1", "prep_minutes": 2, "resolved_hours": 3},
    {"id": "SC-M2", "prep_minutes": 2, "resolved_hours": 7},
    {"id": "SC-M3", "prep_minutes": 2, "resolved_hours": None},
    {"id": "SC-M4", "prep_minutes": 2, "resolved_hours": 4},
]

def service_summary(rows, target_hours=4):
    if not rows:
        raise ValueError("An eligible population is needed")
    timely = sum(row["resolved_hours"] is not None and row["resolved_hours"] <= target_hours for row in rows)
    open_cases = sum(row["resolved_hours"] is None for row in rows)
    return {
        "eligible": len(rows),
        "timely": timely,
        "timely_share": timely / len(rows),
        "open_overdue": open_cases,
        "preparation_minutes": sum(row["prep_minutes"] for row in rows),
    }

a = service_summary(scenario_a)
b = service_summary(scenario_b)
assert a["timely_share"] == b["timely_share"] == 0.5
assert a["preparation_minutes"] == 16 and b["preparation_minutes"] == 8
assert b["open_overdue"] == 1
print("Scenario A:", a, "Scenario B:", b)

```

### Independent application

In a copy of scenario B, set SC-M3’s resolution to six hours. Predict timely share, open overdue cases and whether this establishes an improvement in the four-hour measure. Identify what the case owner should investigate rather than attributing all waiting to the model.

### Worked comparison

The open case is now resolved, so open overdue falls from one to zero. Timely share stays at 50% because six hours exceeds the four-hour target. Both observations matter. Preparation is eight minutes in B versus sixteen in A, but this constructed comparison does not establish a causal benefit from AI. Investigate evidence waiting, warehouse/carrier responses, review capacity and accepted ownership.

The measure concerns investigation resolution. It is different from a delivery arriving on time or the customer receiving an agreed replacement. Carry the population, time boundary, numerator, denominator and open-case count forward with the result.

```python
changed_b = [dict(row) for row in scenario_b]
changed_b[2]["resolved_hours"] = 6
changed = service_summary(changed_b)
assert changed["timely_share"] == 0.5
assert changed["open_overdue"] == 0
assert scenario_b[2]["resolved_hours"] is None
print(changed)

```
