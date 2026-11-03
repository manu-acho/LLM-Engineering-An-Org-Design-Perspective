# Module 6: Data, baselines and adaptation

[Previous module](05-knowledge-and-rag.md) · [Guide index](../README.md) · [Next module](07-fine-tuning-and-qlora.md)

## What you should be able to do

Trace raw records through curation, batching and evaluation; compare simple predictors with neural and language models; explain leakage and validation; and decide whether model adaptation is justified.

**Course walkthrough:** [day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day1.ipynb), [day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day2.ipynb), [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day3.ipynb), [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day4.ipynb), [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/day5.ipynb), [parser](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/pricer/parser.py), [Item model](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/pricer/items.py), [batch helper](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/pricer/batch.py), and [evaluator](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week6/pricer/evaluator.py).

## 1. Concepts: the dataset defines the problem you actually solve

The capstone estimates product prices from descriptions. This is a supervised prediction task: each example pairs input features with a target. Performance depends on how records were collected, cleaned, selected and divided: not just the model architecture.

**Training data** fits parameters. **Validation data** guides design choices. **Test data** estimates performance after those choices are fixed. Repeatedly choosing models based on the same test results makes that test part of development. Preserve a later holdout or new evaluation period for a more credible final estimate.

**Leakage** occurs when information unavailable at prediction time influences training or evaluation. Examples include a target price left in a description, related duplicates split between train and test, preprocessing fitted using test data, or human labels created with access to the outcome being predicted. Use a pipeline that fits learned transforms on training data only. [Scikit-learn pitfalls guidance](https://scikit-learn.org/stable/common_pitfalls.html).

**Distribution shift** means that the examples encountered in use differ from those used to develop the system. Weighted sampling may make a teaching dataset more balanced while moving it away from real operational frequency. The evaluation distribution should represent the decision you intend to support.

## 2. What the code does

### Day 1: parse, deduplicate, sample and split

The notebook loads product metadata and inspects price and text-length distributions. `parser.parse` filters price range and minimum detail, cleans descriptive fields and creates a validated `Item`. `scrub` removes selected metadata and code-like identifiers, truncating the result.

Selection rules create a particular population. A predictor trained only on sufficiently detailed descriptions in a bounded price range has not been evaluated for sparse descriptions or prices outside that range.

The notebook shuffles, removes exact duplicate titles and full descriptions, and uses weighted random sampling to alter category and price representation. Exact deduplication does not remove every near-duplicate product family. Deduplication by title can also merge distinct variants.

The compact expression involving `seen.add(...)` uses a side effect inside a list comprehension. Understand it, but prefer an explicit loop when readability matters. The later train/validation/test slices rely on the preceding shuffle and selection process.

Inspect units: `get_weight` converts units to **pounds**, although some notebook plot labels refer to ounces. This matters if you interpret regression coefficients or compare inputs from another system. Put units in field names or metadata.

### Day 2: normalise descriptions with batch processing

The model rewrites product text into a consistent format. Each batch JSONL row includes a `custom_id`, endpoint, method and request body. Upload and submission produce remote IDs. Later, polling checks status, downloads results and applies summaries to items by ID.

This is an asynchronous **job lifecycle** even though the Python helper uses ordinary synchronous methods. Work completes elsewhere between submission and retrieval. It is different from Python `async def`.

Joining by `custom_id` matters because result order need not match request order. The current helper interprets IDs as positions in the item list. Stable record IDs plus an explicit lookup map are safer when records can be reordered. Track errors and missing results instead of assuming every response has a successful body.

`Batch.save` persists job state using pickle; load only trusted pickle files. The class-level batch registry can also retain entries across repeated notebook runs. Resetting the kernel or explicitly clearing the registry prevents accidental duplicate submissions.

### Day 3: establish baselines and fit simpler models

The notebook compares a random guess, a constant based on training prices, a regression over weight/text length, a word-count linear model, and a random forest. The common callable interface is `predictor(item) -> number or parseable text`, allowing the same evaluator to compare them.

`CountVectorizer.fit_transform` learns a vocabulary from training descriptions and returns a sparse document-feature matrix. At prediction time, `transform` uses that same vocabulary. A model trained against those columns must be served with the matching vectorizer.

Linear regression learns coefficients for features. Random forests combine fitted decision trees. Neither needs a generative dialogue interface. Traditional models remain legitimate candidates when the task is constrained and labels are available.

### Day 4: understand an explicit training loop

The neural example hashes text into features, converts the sparse matrix to dense tensors, and applies a stack of linear layers and ReLU activations. `unsqueeze(1)` changes target shape from `[batch]` to `[batch, 1]`, matching the model output.

The core loop is:

```python
# Course pattern; requires configured model, tensors and optimizer.
optimizer.zero_grad()
outputs = model(batch_X)
loss = loss_function(outputs, batch_y)
loss.backward()
optimizer.step()
```

Clear accumulated gradients; predict; compare with targets; differentiate loss; update parameters. Evaluation uses `model.eval()` and `torch.no_grad()` without updating weights. The printed training loss in the inspected loop is the final batch's loss, not the epoch average. Dense conversion can also consume substantial memory. [PyTorch optimisation explanation](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html).

The same day compares human estimates and prompted LLMs. Human performance is a baseline with its own expertise and effort assumptions, not an automatic gold standard.

### Day 5: understand the managed fine-tuning workflow

Examples become JSONL records with user input and the desired assistant answer. Files are uploaded, a job is created, status/events are inspected, and the resulting model ID is used for inference. Capture the returned job ID directly rather than selecting “the latest job”, which may belong to another experiment.

The local notebook warns that its demonstrated provider/model fine-tuning path is no longer suitable for new users. Treat this as historical workflow instruction, not verified current account access. The transferable concepts are dataset contracts, job lifecycle, model versioning and held-out evaluation. Module 7 develops the locally controllable adaptation route.

## 3. Learn the evaluation pattern

**Teaching example: dependency-free metrics with strict failure handling:**

```python
import math

def regression_errors(truths, predictions):
    if not truths or len(truths) != len(predictions):
        raise ValueError("Expected equal, non-empty sequences")
    pairs = [(float(y), float(p)) for y, p in zip(truths, predictions)]
    if not all(math.isfinite(y) and math.isfinite(p) for y, p in pairs):
        raise ValueError("Values must be finite")
    errors = [p - y for y, p in pairs]
    return {
        "mae": sum(abs(e) for e in errors) / len(errors),
        "rmse": math.sqrt(sum(e * e for e in errors) / len(errors)),
    }

scores = regression_errors([100, 200, 300], [110, 180, 330])
```

Mean absolute error (MAE) is an average absolute deviation in target units. RMSE weights large errors more heavily. R² compares squared error with a mean-target baseline; it is not “percentage accuracy” and can be negative. Choose a metric that reflects the operational loss rather than whichever looks most impressive. [Scikit-learn metric reference](https://scikit-learn.org/stable/modules/model_evaluation.html).

The course evaluator parses model text with a regular expression, turning unparseable text into zero. That mixes a formatting failure with a real zero prediction. Keep parse failures separate and report their rate. It uses a thread pool to overlap independent predictions, useful for I/O-bound API work; concurrency can also increase rate-limit failures.

Its cumulative error confidence band uses an approximate normal formula. Correlated records, skewed errors and an unrepresentative sample can undermine its interpretation. A narrow band does not establish that deployment conditions match the sample.

## 4. Alternatives and business judgement

| Observed problem | Candidate approach | Why |
|---|---|---|
| The answer is in changing records | Retrieval or a database tool | Update evidence rather than weights |
| Output format is inconsistent | Better prompting, validation or constrained output | Cheaper intervention before training |
| Narrow numeric prediction | Regression or boosted/tree model | Efficient and directly aligned with the target |
| Stable task behaviour remains weak despite good context | Fine-tuning experiment | Adapt repeated behaviour using suitable examples |
| Labels are unreliable or conceptually disputed | Clarify definitions and annotation first | Training amplifies the existing label problem |

For Harbour, a plausible task is classifying incoming requests into service categories. Unlike retail price prediction, this is classification and needs different metrics: precision/recall by class, misrouting consequences and escalation behaviour. Transfer the experimental method, not the capstone's metric mechanically.

Historic routing labels may encode workarounds and disputed ownership. A model that reproduces them accurately can perpetuate a flawed operating model. Have process owners and frontline staff distinguish legitimate categories, exceptions and accidental habits before turning history into a training target.

## 5. Experiment, diagnose and reflect

**Exercise:** Define a synthetic request classification task with three categories and an “uncertain” outcome. Write annotation rules and ten deliberately ambiguous examples. Ask how two reviewers would resolve disagreements. Then choose a majority-class baseline and a simple rule baseline before considering an LLM.

For the price task, compute error for a mean baseline, a median baseline and one candidate on the same frozen examples. The mean minimises squared error for a constant predictor; the median minimises absolute error. State why your chosen loss matches the decision.

**Common failures:** labels leaking into input; train/test duplicates; weight-unit mismatch; output parsing errors disguised as predictions; unmatched batch IDs; repeated test-set optimisation; interpreting last-batch loss as an epoch trend.

**Check your understanding:** What does a baseline tell you? Why does a more balanced dataset not automatically give a realistic estimate? Why might good model accuracy preserve a bad workflow? What is the cheapest plausible intervention before fine-tuning?

**Answer cues:** whether added complexity improves on simpler options; operational frequencies may differ; labels embody existing arrangements; repair task definition, evidence, prompts and validation first.

**Decision note:** State the target, input availability, label definition, split strategy, baseline, error costs and criteria for proceeding to adaptation.
