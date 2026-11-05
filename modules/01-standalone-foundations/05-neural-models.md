# Lesson 1.5: From the tiny model to a neural LLM

[Download the lesson notebook](/downloads/05-neural-models.ipynb) · [Notebook setup and study workflow](../../STUDY-WORKSPACE.md)

[Previous lesson](04-evidence-pipeline.md) · [Module route](README.md) · [Next: business design](06-business-design.md)

## What carries across?

The tiny model introduced representation, training, conditional probability, token selection and stopping. These ideas also help explain neural language models. The implementation differs substantially. A modern neural LLM does not normally keep only a table of adjacent word counts.

A **parameter** is a numerical value adjusted during learning. Neural models contain arrays of parameters used in numerical operations. A token identifier selects a learned numerical representation, often called an **embedding**. Its entries are not a list of human-written definitions. Training adjusts representations and other parameters to improve an objective across examples.

## Scores and probabilities

At a generation step, the model produces scores over possible next tokens. These scores are often called **logits**. `softmax` converts a vector of scores into probabilities that sum to one. Mathematically these are positive for finite scores; floating-point computation can round extremely small values to zero. `exp(x)` means raising the constant e, approximately 2.718, to the power x. For scores 1, 0 and minus 1 at temperature one:

```text
exp(1) ≈ 2.718
exp(0) = 1
exp(-1) ≈ 0.368
total ≈ 4.086
probabilities ≈ 0.6652, 0.2447, 0.0900
```

The lab prints this calculation under `neural_score_illustration`. The scores are supplied by hand; no neural network produced them. The numerical operation is real, while the upstream neural computation is being explained conceptually.

To avoid overflow for large scores, the implementation subtracts the largest score before exponentiation. This shifts every score by the same amount and preserves the relative probabilities. It allows the check with scores 1000, 999 and 998 to run without trying to represent `exp(1000)`.

## Learning from prediction error

A common language-model training objective rewards assigning higher probability to an observed next token. The **loss** is a numerical measure used to evaluate the current prediction during learning. For a target with probability `p`, a negative-log-probability loss is `-log(p)`. A target assigned probability 0.5 has a loss of about 0.693; at 0.25, about 1.386. Lower loss under that objective means more probability was assigned to the target.

**Gradient-based optimisation** adjusts selected parameters using information about how the loss changes with them. This is different from the pilot's counting procedure. Later training modules will implement that process directly; this pilot does not claim to train a neural LLM.

Predictive loss is not business truth or organisational value. A training example can contain an inaccurate claim. A model can improve its predictive objective while preserving a misleading category. Evaluation must therefore connect the model's task to the intended use and evidence.

## Attention and context

The **transformer** architecture uses attention mechanisms to combine information from different sequence positions. In plain language, the computation forms context-sensitive representations rather than consulting only the preceding word. The original Transformer paper studied sequence-transduction tasks; it should not be described as a direct evaluation of today's instruction-following assistants. [Vaswani et al. (2017)](https://arxiv.org/abs/1706.03762)

Many text-generation LLMs generate autoregressively: they produce a token conditioned on available context, append it and continue. Modern systems vary in architecture and additional training. Instructions, conversation history and retrieved evidence must still be assembled by the application within the model's input and output limits.

The **context window** concerns the sequence capacity available for a computation under the model's rules. Longer context makes more material available; it does not guarantee that every qualification is used correctly. Missing evidence cannot be recovered from a claim that the interface remembers the case.

## Why fluent errors remain possible

A likely continuation is not an independently verified statement. A neural model may produce a familiar explanation for a delivery discrepancy without a source supporting that cause. Providing evidence can improve the available basis, but its use and the resulting claims still require assessment.

Sampling, greedy selection and temperature affect token choice. They cannot themselves check shipment truth. Additional training for instruction following or preferences can alter behaviour, but should not be described as a guarantee of factual correctness.

## Explain it back

Why is the word-count lab a legitimate learning example, and what would be misleading to claim about it?

**Worked response:** it actually estimates a small language model and performs inference, making probability and decoding inspectable. It would be misleading to claim that it has neural embeddings, attention, broad language competence, reliable reasoning about deliveries or the capabilities of a production LLM.

The [technology chapter](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps) connects this discipline to organisational claims: demonstrate the operation that was tested, then identify the further evidence needed for a broader conclusion.
