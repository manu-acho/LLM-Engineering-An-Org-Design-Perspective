# Lesson 6.2: Build and inspect a baseline before training

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

A simple starting rule can send every request to the most common team in the examples. This is a baseline, a reference result for judging whether more complicated methods help. Count the training labels, make one prediction for the held-out examples, then compare the prediction with what those examples actually say.

[Open the companion workshop notebook](../../notebooks/06-data.ipynb).

## A baseline with no model library

We will learn the most frequent team in a tiny training set and use that one team for every prediction. This is intentionally unhelpful for interpreting descriptions. It gives us a transparent starting point.

```python
training = [
    {"text": "Shipment quantity query", "team": "operations"},
    {"text": "Delivery confirmation", "team": "operations"},
    {"text": "Credit authorisation", "team": "finance"},
]
validation = [
    {"text": "Warehouse check", "team": "operations"},
    {"text": "Disputed financial adjustment", "team": "finance"},
]

def fit_majority(examples):
    if not examples:
        raise ValueError("Training examples are required")
    counts = {}
    for example in examples:
        team = example["team"]
        counts[team] = counts.get(team, 0) + 1
    return max(sorted(counts), key=lambda team: counts[team])

def evaluate_constant(chosen_team, examples):
    if not examples:
        raise ValueError("Evaluation examples are required")
    outcomes = []
    for example in examples:
        outcomes.append({
            "expected": example["team"],
            "predicted": chosen_team,
            "correct": chosen_team == example["team"],
        })
    accuracy = sum(row["correct"] for row in outcomes) / len(outcomes)
    return accuracy, outcomes

chosen_team = fit_majority(training)
accuracy, outcomes = evaluate_constant(chosen_team, validation)
```

## What was fitted?

`counts` begins as an empty dictionary. Each training example contributes one count under its team name. `.get(team, 0)` returns zero when that team has not appeared before. The dictionary becomes `operations: 2` and `finance: 1`.

`max` selects the team with the greatest count. Sorting the names first gives a predictable tie behaviour: the first name in sorted order wins if counts are equal. That is a convention for this teaching example, not a defensible business tie policy by itself.

The fitted “model” is simply the chosen string `operations`. Prediction ignores the description. It can still score reasonably if most cases belong to that team. This is why a baseline helps prevent you from mistaking a superficially good aggregate score for intelligent discrimination.

## What did evaluation calculate?

For each validation example, the program stores expected team, prediction and whether they match. Python treats `True` as 1 and `False` as 0 in this sum. Dividing the number of matches by the number of cases gives **accuracy**, the fraction of correct classifications.

The example produces 0.5, or 50%. The operations case is correct and the finance case is wrong. With only two cases, this is an arithmetic demonstration, not a credible performance estimate.

Retaining `outcomes` matters. If finance errors are more consequential, the aggregate hides an important failure pattern. A real classification evaluation can examine each category and distinguish missed cases from inappropriate assignments. Those criteria should follow the operational consequences.

## Connect to the original price task

In [week6/day3.ipynb](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day3.ipynb), the constant baseline predicts a training-set average price. More sophisticated examples use features such as text length or word counts. `fit` learns relationships from training data; `predict` uses the fitted object on new inputs.

`CountVectorizer` converts descriptions into columns representing words. `fit_transform` learns the vocabulary and creates training features. `transform` applies that same vocabulary later. Changing the vocabulary without refitting the predictor changes what the columns mean. Save the preprocessing and predictor as a compatible pair.

The neural example converts features to tensors. Its core operations clear gradients, calculate predictions and loss, run backward differentiation and update parameters. Evaluation mode and no-gradient execution then assess new data without parameter updates. The compact chapter explains the actual source functions in more detail.

## Batch jobs are another lifecycle

Week 6 also rewrites many descriptions using remote batch jobs. The code writes one JSON request per line, submits a job, waits for remote completion, fetches results and joins them back using identifiers. This is not the same as a neural training batch, even though the word is shared.

Results may finish out of order. Stable IDs preserve the relationship between an input and its output. A missing result needs an error status, not a silently empty description. Persisting job state can let work resume, but repeated submissions need deliberate duplicate handling.

## Alternatives and practice

Compare the majority baseline with a hand-written rule that routes explicit “credit” requests to finance. Fix the validation examples before comparing. If you repeatedly change rules based on these examples, treat them as development cases and obtain another set for final assessment.

**What the example shows:** The rule may improve these two examples while failing on “Do not issue a credit; check delivery first.” A keyword feature and an appropriate classification are different objects. Retain difficult cases and examine whether the label represents first action, eventual owner or decision authority.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A baseline creates a comparison before investment in a more complex model. The research chapter explains [benefit evidence](../../reference/research/04-implementation.md#benefits-need-a-population-and-a-comparison).
