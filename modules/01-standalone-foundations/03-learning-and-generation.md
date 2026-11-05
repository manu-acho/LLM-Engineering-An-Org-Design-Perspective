# Lesson 1.3: Train a tiny language model

[Previous lesson](02-python-first-steps.md) · [Module route](README.md) · [Next: evidence preparation](04-evidence-pipeline.md)

## A model small enough to inspect

The lab learns from four sentences:

```text
check the order
check the record
check the order
check the evidence
```

A **token** is one unit in a model's representation of text. The example tokenizer lowercases text and extracts words, numbers and selected punctuation. `Check the order` becomes the list `["check", "the", "order"]`. Modern model tokenizers often use word fragments or other units. This example's word boundaries are a deliberate simplification, not a rule about every LLM.

A **bigram model** predicts the next token using only the previous token. “Bi” refers to the pair. It is a statistical language model, but it has no neural network and no understanding of Harbour's delivery records. N-gram modelling provides a transparent introduction to conditional probability and generation. [Jurafsky and Martin, chapter 3](https://web.stanford.edu/~jurafsky/slp3/3.pdf)

## What training does

`train` adds two boundary markers to each sentence. `<START>` marks its beginning and `<END>` its end. For the first sentence, the sequence is:

```text
<START> → check → the → order → <END>
```

`zip(sequence, sequence[1:])` pairs each item with the following item. `sequence[1:]` means the sequence from position one onward. The loop increments the count for each observed pair. `Counter` stores the counts; `defaultdict` creates a counter when a previous token is first encountered.

After training, `the` has been followed by `order` twice, `record` once and `evidence` once. The model stores these observed frequencies. Adding a training sentence changes the counts. Generating a continuation without changing the training data does not.

## Conditional probability

**Conditional probability** expresses a probability given some available condition. Here the condition is the previous token. At temperature one, the estimated probability of an observed following token is its pair count divided by all following-token counts for that previous token:

```text
P(order | the) = 2 / 4 = 0.50
P(record | the) = 1 / 4 = 0.25
P(evidence | the) = 1 / 4 = 0.25
```

The vertical bar means “given”. The probabilities sum to one. They describe continuations in the learned representation, not the chance that an order record is true.

The implementation takes logarithms of the positive counts and uses `softmax` to obtain the distribution. At temperature one, exponentiating those log-counts recovers their relative frequencies. This formulation also lets the lesson inspect how temperature changes sharpness. `log` is the natural logarithm, the inverse of the exponential function `exp`. In this calculation, applying `exp` to `log(count)` recovers the count before normalisation.

## Select, append and repeat

**Decoding** is the procedure for selecting output tokens from a model's probabilities. The example uses **greedy decoding**, selecting the highest-probability next token. Equal probabilities are resolved alphabetically so the result is reproducible. From `<START>`, the output is:

```text
check the order
```

The selection line uses `min` with a key `(-probability, token)`. The minus sign puts the highest probability first when searching for the smallest key. The token text breaks a tie alphabetically. A `lambda` is a small function written in place to compute that key.

After `order`, the next token is `<END>`, so generation stops. A hard token bound provides a second stopping condition. With a bound of two, the result is `check the`, and the stop reason is `length_limit`. A stopped response is not necessarily a completed response.

An alternative is **sampling**, drawing a token according to the distribution. It can produce different continuations from the same trained model. This lab uses greedy decoding to make the first trace easy to reproduce. It does not claim that every deployed model uses greedy decoding.

## Temperature changes selection conditions

**Temperature** rescales scores before conversion to probabilities. A positive value below one sharpens relative preferences; a value above one flattens them. For the counts after `the`, temperature 0.5 gives probabilities proportional to 4, 1 and 1. Temperature 2 gives probabilities proportional to the square roots of 2, 1 and 1.

Temperature does not introduce evidence or check truth. In this greedy implementation, the highest-ranked token remains the same for these positive temperatures. The distribution changes even though the selected result does not. A more varied sampled response would not be evidence of improved judgement.

The lab requires a finite positive temperature and rejects zero. Its default greedy decoder is a separate selection rule. Provider interfaces can define temperature differently; no provider interface is being called here.

## Failure and alternatives

The model cannot predict from an unobserved previous token such as `refund`. It raises an explicit error. A model with smoothing could assign probability to unseen combinations; a backoff model could use a less specific context. These are alternatives that solve particular sparsity problems. Neither turns four sentences into a general assistant.

A longer-context n-gram model uses more previous tokens but requires more observed combinations. A neural model instead learns distributed numerical representations that can generalise beyond an exact pair table. Lesson 1.5 explains that distinction without pretending the tiny example contains a transformer.

## Try a training change

Add four copies of `check the evidence` to the training list. Predict the new probability of `evidence` after `the`.

**Worked response:** the counts become five for `evidence`, two for `order` and one for `record`, totalling eight. At temperature one, the probability of `evidence` is 5/8, or 0.625. Greedy generation now selects that continuation. A change in training examples has changed the model; it has not verified anything about the delivery case.

The [organisational data discussion](../../reference/research/03-decisions.md#facts-values-and-the-alternatives-that-disappear) explains why the selection and interpretation of examples matter beyond numerical accuracy.
