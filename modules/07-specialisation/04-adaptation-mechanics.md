# Lesson 7.4: Understand an adapter, a training batch and a loss

[Download the matching notebook](/downloads/07-04-adaptation-mechanics.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: train and reload a tiny adapter](05-source-walkthrough.md)

## Business context: Harbour

A training batch is a group of examples used together for one training step. Loss is a number that measures how poorly predictions fit the expected answers under a chosen rule. Trace one prediction for an expected answer: the lesson's rule penalises it more when the model gives that answer a lower probability. Then see which values an adapter is allowed to change.

Compare training and held-out behaviour without treating a tiny text split as enterprise evidence.

[Company and supply-chain context](../../HARBOUR.md) · [Module 7 business situation](../../reference/harbour-learning-journey.md#module-7)

## Two smaller tables change a larger transformation

LoRA represents an update through two smaller matrices. A matrix is a rectangular table of numbers with defined multiplication rules. Suppose a layer's existing transformation is a two-by-two identity matrix: it preserves a two-value input. Add a rank-one update formed from a column `[1, 2]` and a row `[0.5, -0.5]`. Their product is `[[0.5, -0.5], [1, -1]]`.

For input `[2, 0]`, the original output is `[2, 0]`. The update contributes `[1, 2]`. With scale one, the new output becomes `[3, 2]`. The restriction to a product of smaller tables limits possible updates while reducing trainable entries for sufficiently large layers. It does not make the base model unnecessary.

Rank, scaling and target layers are separate choices. Increasing rank changes update capacity and resource use. Changing the target layers changes where adaptation can act. The proper comparison is held-out task behaviour at an acceptable cost, not rank alone.

## What exactly gets graded?

A causal language model predicts a next token from an earlier prefix. During supervised adaptation, an example may contain prompt IDs followed by completion IDs. Labels at prompt positions can use an ignore marker such as `-100`, while completion labels retain token IDs.

For input `[1, 2, 3, 4]` and labels `[-100, -100, 3, 4]`, the usual causal model loss shifts predictions and labels internally. The score after reading tokens 1 and 2 is assessed against target 3. The next prediction is assessed against 4. The prompt is visible even though its positions are not graded as completion targets.

An attention mask does something different: it identifies real versus padded input positions. A completion mask identifies supervision positions. A causal mask prevents use of future positions. Keeping these distinct prevents a well-formed batch from quietly training the wrong objective.

## From probability to loss

If the model assigns the correct next token probability 0.5, negative log probability is approximately 0.693. At probability 0.1 it is about 2.303. Lower loss rewards more probability on the target. This does not grade the legitimacy of a business category or the truth of a training label. A consistent but bad label can be learned successfully.

## Where quantization enters

QLoRA uses a quantized frozen base with trainable adaptation. The original method's NF4 representation, double quantization and memory-management choices address resource constraints. Stored precision, computation precision and adapter precision need not be identical. Quantization does not mean all operations become four-bit arithmetic.

The next lesson deliberately uses a tiny non-quantized model so ordinary local hardware can expose training and reload mechanics. It does not claim to benchmark QLoRA. Quantized transformer adaptation would require additional model-specific configuration, hardware checks and evaluation; it is not executed by the linear lab.

**Worked check:** A trained adapter file is small. Can it serve independently? Usually it needs the compatible base, tokenizer or defined token mapping, configuration, input contract and output interpretation. Its size is a property of what was saved, not a complete account of the running system's resource needs.

**Technical foundation:** [LoRA paper](https://arxiv.org/abs/2106.09685), [QLoRA paper](https://arxiv.org/abs/2305.14314) and the source walkthrough below.

## Read the organisational connection

An adapter changes a technical arrangement; consequences for work require a further account. The research chapter explains [materiality in digital systems](../../reference/research/06-technology-in-practice.md#materiality-in-digital-systems).

## Practical activity: Calculate which prediction positions contribute to a masked loss.


### Predict and follow the values

How many positions contribute under this mask?

```python
import math
probabilities = [0.5,0.25,0.8]
mask = [0,0,1]
loss = sum(-math.log(p)*use for p,use in zip(probabilities,mask)) / sum(mask)
print("Answer-only loss:", loss)
assert abs(loss + math.log(0.8)) < 1e-12
```

### Complete the exercise

**Worked answer.** One. A loss mask selects grading positions; it is different from the attention mask controlling which positions participate in relevant model operations.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

### Programming practice

Write masked_mean(values, mask) that averages only selected values. Reject an empty selection.

Start with the placeholder in the notebook, then compare with this worked solution. The contrasting checks are part of understanding the contract.

```python
def masked_mean(values, mask):
    if not sum(mask):
        raise ValueError("No selected positions")
    return sum(value*selected for value,selected in zip(values,mask))/sum(mask)

assert masked_mean([10.,2.],[0,1]) == 2.
assert masked_mean([10.,2.],[1,1]) == 6.
```

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
