# Lesson 1.7: Exercises, failure cases and worked answers

[Previous lesson](06-business-design.md) · [Module route](README.md) · [Workbook](../../WORKBOOK.md)

## 1. Follow a learned change

**Exercise:** The original training set contains two `the → order` pairs, one `the → record` pair and one `the → evidence` pair. Add two sentences ending in `record`. Calculate the probabilities after `the` at temperature one.

**Worked answer:** there are six observations: order two, record three, evidence one. The probabilities are 2/6, 3/6 and 1/6. Greedy generation selects record. The change came from training data, not a new inference prompt or a verified business fact.

## 2. Explain a length-limited result

**Exercise:** Run `generate(train(TRAINING_TEXT), max_tokens=2)` in an interactive Python session after importing the lab. Explain its result.

```python
import foundations_lab as lab
result = lab.generate(lab.train(lab.TRAINING_TEXT), max_tokens=2)
print(result)
```

**Worked answer:** the result is `{'text': 'check the', 'stop_reason': 'length_limit'}`. The program reached its token bound before selecting `<END>`. Treating that result as complete would hide the stop condition.

## 3. Preserve uncertainty

**Exercise:** Replace the customer quantity with `None`. What should happen, and why is zero an unsuitable fallback?

**Worked answer:** `build_brief` raises `ValueError`. The input contract needs a known nonnegative whole quantity. Zero would assert that the customer reported receiving none, which the missing value does not establish. A future intake design could support explicit unknown quantities, but would need a separate representation and verification path.

## 4. Change a source without changing its meaning

**Exercise:** The shipment record becomes eleven while the customer report remains ten. Does the comparison in the current lab become one?

**Worked answer:** no. The comparison is defined as order quantity minus customer-reported quantity, so it remains two. The shipment fact becomes eleven and introduces a different discrepancy. A separate shipment-versus-report comparison could be added with its own basis. Quietly changing the calculation's operands would alter the contract.

## 5. Identify the unsupported claim

**Exercise:** A draft says, “The warehouse miscounted two boxes; issue a credit.” Identify the steps beyond the evidence.

**Worked answer:** it treats the reported discrepancy as a confirmed shortage, attributes a warehouse cause and proposes a business response without the required investigation or authority. A supported brief preserves the conflicting quantities and asks what evidence is needed next. Neither the tiny model nor the brief builder verifies the cause.

## 6. Recalculate the business case

**Exercise:** Keep 210 monthly uses, but assume preparation saves four minutes and review takes three. At £30 an hour and £180 monthly running cost, what is the scenario difference?

**Worked answer:** net effort reduction is one minute per use, or 210 minutes: 3.5 hours. Its capacity value is £105. Subtracting £180 gives minus £75 before implementation costs. This scenario does not show cash losses or savings by itself; it identifies assumptions under which the proposed capacity benefit would not cover that running-cost estimate.

## 7. Complete a design that can be challenged

**Exercise:** Prepare a short proposal containing the evidence, unresolved questions, technical contribution, recipient, correction route, action boundary and evaluation comparison. Include an alternative to using generation.

**Worked answer:** [the workbook's completed first design](../../WORKBOOK.md#a-completed-first-design) provides one defensible arrangement. Another can be justified if it preserves evidence, identifies accepted ownership and states the basis for its expected contribution. A proposal that merely names a human approver is incomplete without source access, capacity and a route to challenge premises.

## What the automated checks establish

Run `python3 -m unittest -v test_foundations.py` beside the lab file. The checks examine learned frequencies, changed training data, unknown contexts, stopping conditions, temperature, numerical stability, evidence status, validation, input preservation and execution from another working directory.

They do not establish model truthfulness, a secure external integration or business improvement. The distinction between a configured operation and an organisational consequence is developed in [the research evidence path](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).

The pilot is complete when the learner can explain the outputs and the design, including what each cannot establish. The next standalone modules are identified as planned in [the curriculum](../../CURRICULUM.md).
