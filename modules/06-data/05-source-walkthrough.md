# Lesson 6.5: Follow an example from raw record to evaluated prediction

[Module route](README.md) · [Next: decide what the labels should represent](06-design-lab.md)

## What you'll learn and why it matters

Follow one record from its raw fields through preparation, prediction and evaluation. Learn where the expected answer belongs and how a preparation rule can change the task.

Start with the fields of one raw example. The programme turns those fields into input for a fitted predictor and then compares the prediction with an expected value. Follow those steps separately. Inspect where the expected answer is used so it does not silently become part of the input.

[Open the companion workshop notebook](../../notebooks/06-data.ipynb).

## Source preparation is part of the model

In [Week 6 day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day1.ipynb), product records are selected, cleaned, inspected, deduplicated and split. Price range and minimum text length define the population. A model evaluated there has not automatically been assessed for sparse records or prices outside that range.

Exact duplicate removal is useful but does not remove every near-identical product family. If variants cross train and test, performance may overstate ability on genuinely new products. Preserve source identifiers and group related records when that matches the intended generalisation question.

[Day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day2.ipynb) uses model-assisted rewriting and batch jobs. A JSONL line is one request record. A remote batch job can finish after submission and out of order. Join results by stable request ID; do not assume the first output belongs to the first input. Keep failed and missing outputs visible.

## Move beyond a constant baseline

The source [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day3.ipynb) compares simpler predictors before neural and model-based methods. The following independent classifier uses words as features. It needs `scikit-learn`, but performs no downloads or remote calls.

```python
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_text = [
    "credit refund approval", "finance credit adjustment",
    "warehouse delivery recount", "shipment quantity check",
]
training_labels = ["finance", "finance", "operations", "operations"]
pipeline = make_pipeline(CountVectorizer(), MultinomialNB())
pipeline.fit(training_text, training_labels)
predictions = pipeline.predict(["credit approval", "warehouse recount"])
assert predictions.tolist() == ["finance", "operations"]
```

`CountVectorizer.fit` learns a vocabulary and maps each description into word-count columns. `MultinomialNB` learns category-related word statistics, using smoothing to avoid treating every unseen word/category combination as impossible. The pipeline ensures that future text goes through the same feature mapping before prediction.

Unlike the majority baseline, this predictor uses the description. It still does not understand business authority. “Do not issue a credit; recount first” can contain many finance-associated words while requiring an operations first action. Put that case in evaluation rather than interpreting two successful assertions as broad quality evidence.

## Follow the neural loop in the original notebook

In [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day4.ipynb), identify feature tensors, targets, model output, loss, gradient clearing, backward differentiation and optimizer step. Clearing gradients matters because many libraries accumulate them. Forgetting to clear when accumulation was not intended changes the update.

Training mode and evaluation mode can produce different behaviour. Evaluation without gradients reduces bookkeeping but does not make the evaluation independent: independence comes from the data and experiment design. Record preprocessing and target transformations, especially any logarithmic price representation, before interpreting error units.

The [evaluator](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/pricer/evaluator.py) accepts a predictor and inspects predictions case by case. In the source workflow, malformed numeric answers can become a default zero. An improved experiment should separately record invalid output, valid predicted zero and task error. Otherwise parsing failures become misleading numerical estimates.

## Keep the full record

For each case, retain source ID, split, available description, preprocessing revision, expected target, prediction, validity and error. Across the experiment, retain the selected population and excluded records. That makes it possible to distinguish a model failure from a changed dataset or parser.

**Practice with feedback:** A new model improves average price error, but all missing outputs were dropped. Restore those cases with explicit invalid status, compare coverage and then compare error among valid predictions. A better average on fewer usable cases may be an unsuitable service improvement.

## Read the organisational connection

A stored record captures selected events rather than every interpretation or repair activity. The research chapter explains [the limits of recorded evidence](../../reference/research/05-routines.md#what-logs-can-show).

## What to remember

Preparation determines what a predictor sees. The original neural loop fits parameters and the evaluation compares predictions with reference values. Keep those roles distinct in the experiment record.

## What this means for the business process

Version the preparation and label rules alongside the predictor. If a route is disputed, let the receiving team inspect how the example was prepared and what the reference was intended to represent.

For the research behind this design choice, read [Decision premises](../../reference/research/03-decisions.md#decision-premises).

## Next lesson

Next define that allocation rule clearly enough for two people to label the same difficult request consistently. [Lesson 6.6: Redesign a routing task before learning its labels](06-design-lab.md).
