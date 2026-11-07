# Lesson 6.1: How examples become a prediction system

[Download the matching notebook](/downloads/06-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Business context: Harbour

Explain the work assigned by a routing label before representing it as training data.

[Company and supply-chain context](../../HARBOUR.md) · [Module 6 business situation](../../reference/harbour-learning-journey.md#module-6)

## The task must be defined before the model

Harbour has thousands of old requests. A manager asks whether AI can learn which team should receive a new one. Before choosing a model, ask what the old assignment means. Was it the appropriate team, the first team contacted, the team available that day or the team that eventually repaired the problem?

A dataset can contain a clear column called `assigned_team` while leaving that question unresolved. Technical training can succeed at reproducing the column without solving the intended organisational problem.

## Examples, features and targets

An **example** is one case used for learning or evaluation. Its **input features** are the information available for prediction. Its **target**, often called a label, is what the model is supposed to predict.

For routing, the request description is an input and the desired team is a categorical target. This is **classification**, selecting a category. Predicting an estimated price is **regression**, predicting a numerical quantity. The difference matters: a price error of £10 and a request assigned to the wrong team require different ways of measuring error.

Features must be available at the moment of use. A “final resolution note” may predict the right team very well precisely because it was written after the work was completed. Supplying it during evaluation of initial routing would test a task the operational system cannot perform.

## Learning a relationship rather than writing every rule

In ordinary rule programming, a person specifies a mapping: if a description contains an exact marker, choose a team. In **supervised learning**, a training procedure uses input/target pairs to adjust a model's parameters.

For numerical prediction, a simple model may learn that certain features tend to accompany higher values. For classification, it may learn patterns that distinguish categories. “Learn” means adjusting a numerical mapping under a specified objective. It does not mean the system has acquired an independent understanding of whether a category is legitimate.

A **baseline** can be extremely simple: predict the most frequent team or the average observed price. It establishes what happens without sophisticated modelling. If a complex system cannot improve on a suitable baseline, complexity has not yet been justified.

## Training, validation and test

Training data is used to fit parameters. Validation data is used to choose settings, representations or models. Test data is reserved for assessment after those choices are made. These are roles in an experimental design, not just names for three files.

If you repeatedly inspect test performance and revise the system to improve it, that set has become part of development. A later independent holdout or new period may be needed for a credible final estimate.

Random splitting is not always appropriate. Closely related requests from the same customer or one repeated incident can appear on both sides. Grouping related records or splitting by time may better reflect use. The right split follows the question: predicting similar cases now and generalising to new clients are different assessments.

## Leakage and distribution shift

**Leakage** is the use of information that would not legitimately be available for the prediction being evaluated. Target values left in a description, near-duplicate cases across splits and preprocessing fitted using test information are common examples.

**Distribution shift** occurs when operational cases differ from development cases. A model trained on detailed, well-documented complaints may struggle on short messages. Balancing categories can help a learning problem but can also change the apparent frequency of errors relative to real work. State what population the score represents.

## What a loss and an update do

A **loss** is a numerical expression of the training error. For a numerical target, one option squares the difference between prediction and target; large errors then receive a larger penalty. Other tasks need other losses.

In neural-network training, the program computes predictions, calculates loss, determines how selected parameters contribute to that loss and updates them. A **gradient** expresses how the loss would change with a small parameter change. An **optimizer** uses that information to choose an update. You do not need to calculate gradients manually to follow the sequence.

An **epoch** is a pass through the training examples. A **batch** is a group processed for an update or part of one. More epochs can improve training fit while worsening performance on new cases. Good training performance alone is not sufficient.

## Adaptation has alternatives

If the system lacks current policy, retrieval or a database tool may help more than training. If format is inconsistent, improve the output contract. If the category definitions are disputed, clarify them and collect labels before fitting a model. Fine-tuning is one intervention among these.

**Check:** Explain why a model can predict historical team assignments accurately and still route tomorrow's requests badly. Include ambiguity in labels, unavailable features, changing work and the difference between imitation and an appropriate operating rule.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A label supplies a category through which subsequent cases become recognisable. The research chapter explains [decision premises](../../reference/research/03-decisions.md#decision-premises).

## Practical activity: Separate a message, its historical label and the meaning of that label.





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

Are first_team and final_owner necessarily the same target?

```python
rows = [{"text":"invoice and missing shipment","first_team":"finance","final_owner":"operations"}]
print(rows[0])
assert rows[0]["first_team"] != rows[0]["final_owner"]
```

No. Their operational meanings must be decided before fitting a predictor.

### Complete the exercise

Write the prediction before consulting the worked answer: Are first_team and final_owner necessarily the same target?

**Worked answer.** No. Their operational meanings must be decided before fitting a predictor.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
