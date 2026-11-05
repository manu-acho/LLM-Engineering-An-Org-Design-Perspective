# Module 1 lab and the wider code route

[Start here](START-HERE.md) · [Module route](modules/01-standalone-foundations/README.md)

## Notebook route

Use the [study workspace guide](STUDY-WORKSPACE.md) for the prepared environment and seven lesson notebooks. They import the complete lab below rather than maintain separate copies. The notebooks need Jupyter packages; the two Python files can also run alone using the standard library.

## If the course checkout is already present

No download is needed. Open the matching notebook, or run `uv run python examples/01-foundations/foundations_lab.py model` from the project root. The four commands below use two files: three select different operations in foundations_lab.py, and one runs test_foundations.py. The four training sentences are values inside the program, not separate files.

For later modules, follow their own code workshops and notebooks under notebooks. Shared implementations are under src/ai_orgdesign/labs. The [verification guide](reference/verification.md) records their scope.

## Alternative: download the two Module 1 files

Download [the complete lab](/downloads/foundations_lab.py) and [its checks](/downloads/test_foundations.py) into the same folder. The program contains the four training sentences and fictional case. It neither reads confidential files nor contacts a model or external service.

From that folder on macOS or Linux:

```sh
python3 foundations_lab.py model
python3 foundations_lab.py brief
python3 foundations_lab.py request
python3 -m unittest -v test_foundations.py
```

On Windows, use `py -3` instead of `python3`. The code uses Python's standard library and is written for Python 3.10 or later. The recorded runtime check used Python 3.14.4 on macOS. No Windows execution or external provider behaviour is claimed by that check.

## Expected model result

The `model` command prints these values, with the probabilities represented as JSON numbers:

```json
{
  "after_the": {"evidence": 0.25, "order": 0.5, "record": 0.25},
  "greedy": {"stop_reason": "end_token", "text": "check the order"},
  "neural_score_illustration": [0.6652409557748218, 0.24472847105479764, 0.09003057317038046],
  "tokens": ["check", "the", "order"]
}
```

Spacing is formatted for display and does not affect JSON values. The last digits of floating-point calculations can vary across environments. Compare probabilities to a suitable numerical tolerance; the three probabilities after `the` have the stated frequency interpretation.

The `neural_score_illustration` field applies softmax to three supplied scores. It does not claim that the program runs a neural network. The actual trained model is the adjacent-token count model.

## Expected brief

The `brief` command returns case `D-17`. Its facts preserve the order quantity twelve, shipment quantity twelve and customer-reported quantity ten. The first two have status `recorded`, the third `reported`. Each retains its own source identifier.

Its comparison contains:

```json
{
  "basis": ["order-17", "customer-17"],
  "order_minus_customer_report": 2,
  "status": "difference_to_investigate",
  "unit": "boxes"
}
```

The unresolved fields remain `actual_received_quantity` and `cause_of_difference`. The permitted output is `investigation_brief_only`. The program has calculated a difference, not confirmed a shortage or authorised a response.

## Expected request

The `request` command prints two messages. The system message specifies the preparation task and its limits. The user message contains the brief encoded as JSON text. No generated answer follows, because no model request is sent. Quotation marks within the encoded JSON are escaped; that is normal serialisation, not a changed quantity.

## Checks and their scope

The supplied test file runs 13 checks. They examine learned frequencies, effects of changing training data, unknown contexts, empty training, stop conditions, temperature, numerical stability, source status, input preservation, missing and unsuitable values, duplicate identifiers, request serialisation and execution from another directory.

An `OK` result supports these behaviours under the tested conditions. It does not demonstrate the accuracy of an external model, the completeness of business controls or organisational benefit. Those are different claims requiring appropriate evidence.

## Common failures

| Symptom | Likely cause | Next check |
|---|---|---|
| Command not found | Python is absent or the launcher differs | Run the version command in Start here |
| Cannot open the file | Wrong working folder or filename | Confirm the files were saved with `.py`, not `.py.txt` |
| Import error for `foundations_lab` | Tests and lab are in different folders | Place the two downloads together |
| `ValueError` after an input edit | The explicit input contract was violated | Read the exception and compare unit, quantity and source fields |
| Different greedy result after editing training | Learned counts changed | Recalculate the conditional distribution |
| No model-generated brief | The request example only constructs messages | Review the boundary described in Lesson 1.4 |

## Read the full implementation

The downloaded lab is the complete source, not a fragment. It is organised into tokenisation, counting, probability conversion, generation, evidence preparation, message construction and command-line execution. Lessons 1.2 to 1.5 explain those patterns and their alternatives. The test file provides executable examples of valid and invalid use.
