# Lesson 1.4: Prepare evidence and construct a request

[Download the lesson notebook](/downloads/04-evidence-pipeline.ipynb) · [Notebook setup and study workflow](../../STUDY-WORKSPACE.md)

[Previous lesson](03-learning-and-generation.md) · [Module route](README.md) · [Next: neural models](05-neural-models.md)

## Business context: Harbour

A brief crosses from customer-facing intake to investigation. Its usefulness depends on carrying the source and uncertainty with each claim.

[Company and supply-chain context](../../HARBOUR.md) · [Module 1 business situation](../../reference/harbour-learning-journey.md#module-1)

## Follow one case through ordinary code

Run:

```sh
python3 foundations_lab.py brief
```

The embedded case supplies a case identifier, a unit and three source-labelled quantities. No website is fetched and no model is called. The program creates a structured investigation brief. The distinction is useful: evidence preparation can be examined separately from generation.

## The input contract

The **input contract** states what a function accepts and how it handles unacceptable inputs. `build_brief` requires a dictionary, a nonempty case identifier, the unit `boxes`, and three records named `order`, `shipment` and `customer_report`. Each record needs a nonnegative whole quantity and a distinct, nonempty source identifier.

These are deliberately narrow teaching rules. The function rejects kilograms, fractional quantities and missing values. A real service might support them, but would need explicit conversions and appropriate meanings. Silently treating packs as boxes would be a semantic error even if the program performed arithmetic correctly.

Validation checks structure and specified constraints. It cannot show that a shipment record is accurate or that a customer account is truthful. A well-formed input can still contain a mistaken fact.

## Preserve status while changing representation

The function loops over three pairs: a record name and its status. Order and shipment quantities receive `recorded`; the customer quantity receives `reported`. The labels describe their provenance, not a ranking of who must be believed.

For each record, the function builds a new dictionary with `kind`, `quantity`, `unit`, `status` and `source_id`. `facts.append(...)` adds it to the output list. The input is not modified. Keeping preparation free of input mutation makes repeated inspection less surprising: examining a case does not silently change it.

The resulting facts preserve twelve, twelve and ten. The program does not average them, replace the customer report with the shipment quantity or select a cause. The disagreement remains visible.

## Make the calculation's basis explicit

The comparison subtracts the customer-reported quantity from the order quantity. Its value is two. Its `basis` lists `order-17` and `customer-17`. The shipment source is retained among the facts, but it is not an operand in this subtraction.

That distinction helps an investigator reconstruct the result. A calculation can cite sources that do not actually support its inputs, so source identifiers should follow the operation rather than be attached decoratively after the answer is produced.

The status is `difference_to_investigate`. It is not `confirmed_shortage`. The unresolved fields are `actual_received_quantity` and `cause_of_difference`. If a future interface removes these qualifications, the display has changed the organisational claim even though the arithmetic remains correct.

The comparison can also be negative. If the customer reports fourteen boxes, twelve minus fourteen is minus two. That signals a discrepancy in the opposite direction; the code does not clamp it to zero or invent an explanation. The unit remains boxes throughout.

## Constructing messages is not running inference

Run:

```sh
python3 foundations_lab.py request
```

`make_request` returns a list of two dictionaries. The first supplies task instructions under a `system` role. The second supplies the prepared brief under a `user` role. The **role** is part of this illustrative message organisation; it does not make a statement true or enforce a business permission.

`json.dumps` converts the brief into JSON text. **Serialisation** is the conversion of structured values into a transportable representation. `json.loads` performs the reverse operation. Serialisation preserves selected values in a defined format; it does not verify their meaning.

The instructions ask a future model to preserve sources and uncertainty, avoid inventing a cause and avoid authorising action. This is task framing. It is not a security boundary or proof of compliance. The example sends no HTTP request, names no provider or model and returns no generated answer.

## Where a real model would connect

A provider adapter could accept the prepared messages, send an authenticated request, check transport and response status, extract output and return a result for further checking. A local model adapter could perform the inference on suitable hardware. Either path adds dependencies, failure modes and operating decisions.

The surrounding application would need timeouts, explicit failures, handling of incomplete results and checks appropriate to the task. It should not treat every successful HTTP response as a valid brief. The ability to send a request and the ability to support a business claim are different tests.

No external adapter is required to complete this module. The numerical model provides actual local inference; the evidence pipeline provides a complete local transformation. Later planned modules add modern model integrations as separately testable components.

## Compare the alternatives

A deterministic template could display the facts and unresolved questions with no generation. A language model might help compress a long narrative or express a brief for a recipient. A specialist conversation may be needed when the terms or interests themselves are disputed.

Choosing among these depends on the contribution required. If the problem is subtracting two quantities, a model adds little. If the problem is a long, varied narrative, drafting may help. If “received” has different meanings across parties, fluent wording cannot settle the disagreement. The [coordination chapter](../../reference/research/02-coordination.md#shared-data-and-shared-meaning) explains this last boundary.

## Trace exercise

Which output changes if `customer_report.quantity` becomes eleven, and which claim should remain unresolved?

**Worked response:** the customer fact becomes eleven and the comparison becomes one. Its source identifier remains `customer-17`, assuming that identifier refers to the revised teaching record. The actual received quantity and cause remain unresolved. In a production version, record revision identity would also need to distinguish the old and new evidence rather than overwrite their history.

## Try the live model

The [live-model guide](../../reference/live-model-guide.md) prepares the API configuration. The matching notebook adds a real request and records the returned model, status, usage and duration. Inspect every factual claim. In a development run, the model inferred shipped quantity from an order record; the source did not establish that inference. The [worked experiment record](../../reference/worked-model-experiments.md) explains this observed failure and the later corrections.
