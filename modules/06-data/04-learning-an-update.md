# Lesson 6.4: Calculate a training update and a task error

[Module route](README.md) · [Next: follow the data and baseline code](05-source-walkthrough.md)

## Fit a rule instead of specifying it completely

Consider a deliberately tiny numerical task: predict `y` from `x` using `prediction = weight × x`. The training examples are `(1, 2)` and `(2, 4)`. Start with weight zero. Predictions are zero and zero, so squared errors are four and sixteen. Mean squared error is ten.

The derivative of mean squared error with respect to this weight is the average of `2 × x × (prediction - target)`. At weight zero it is minus ten. That negative gradient says increasing the weight locally reduces the loss. A learning rate of 0.1 moves the weight to one. Predictions become one and two; mean squared error falls to 2.5.

```python
examples = [(1.0, 2.0), (2.0, 4.0)]
weight = 0.0
learning_rate = 0.1
history = []
for step in range(4):
    loss = sum((weight*x-y)**2 for x, y in examples) / len(examples)
    gradient = sum(2*x*(weight*x-y) for x, y in examples) / len(examples)
    history.append((weight, loss))
    weight -= learning_rate * gradient
assert history[0] == (0.0, 10.0)
assert history[1] == (1.0, 2.5)
assert abs(weight - 1.875) < 1e-12
```

This is **gradient descent** in a one-parameter model. The training procedure changes the mapping using examples. The code's derivative was calculated for this particular loss; general neural libraries calculate derivatives through a computational graph using automatic differentiation.

## Why settings change learning

A much larger learning rate can overshoot. A small one can improve slowly. Repeating the data gives more update opportunities but does not establish generalisation. This tiny linear task is well behaved; real model loss surfaces and datasets are more complex.

A batch supplies several examples for an update. Gradient accumulation combines contributions across smaller batches before updating, often to manage memory. An epoch describes a pass through the data. These are separate controls. Doubling epochs does not mean doubling the model's useful knowledge.

## Measure the task the model will perform

For price regression, mean absolute error averages the absolute distance between predicted and actual prices. Root mean squared error takes the square root of mean squared error and penalises large errors more strongly. Both are in the target's units after the relevant transformation; MSE itself is in squared units.

For categorical routing, a £10 error has no direct meaning. Use category-level errors, precision and recall, abstentions and the consequences of misrouting. If finance is rare, a majority classifier can have high accuracy while missing finance entirely.

## Separate preprocessing from prediction

A word-vector vocabulary fitted on training descriptions maps words to columns. The predictor learns relationships involving those columns. At evaluation, use the same mapping. Rebuilding the vocabulary from test cases can leak information or change column meaning. Save the preprocessing with the fitted model.

**Worked check:** A training loss falls while held-out routing gets worse. That is a reason to examine overfitting, split design, label quality and distribution differences. It is not a reason to report the training curve as operational accuracy. The loss is the objective used for updating; the business decision needs evidence on cases it will actually encounter.
