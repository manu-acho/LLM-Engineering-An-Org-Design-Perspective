# Lesson 15.1: From a business problem to a pilot

[Download the matching notebook](/downloads/15-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## Business context: Harbour

Turn the customer-service problem into a bounded pilot question with affected roles and excluded cases.

[Company and supply-chain context](../../HARBOUR.md) · [Module 15 business situation](../../reference/harbour-learning-journey.md#module-15)

## Start with the work that is failing

Harbour's customer operations team spends time finding order, shipment and customer records before deciding what to investigate. The initial complaint is that cases take too long. That statement does not yet identify the cause. Missing records, unclear ownership, batching, repeated data entry and waiting for a manager could each contribute. An AI assistant affects some of these mechanisms and may leave others unchanged.

A **problem statement** identifies the affected work, the observed difficulty and the outcome sought. A useful formulation is: prepare a traceable discrepancy brief so an investigator can begin with the relevant records, while retaining unresolved facts and the existing remedy authority. It names a contribution without assuming that the system should decide the remedy.

A **requirement** states a behaviour or condition the service must satisfy. “Use an agent” is a design choice. “A north-region user cannot obtain a south-region case” is an access requirement. “A brief preserves which quantity was reported rather than verified” is an evidence requirement. Separating the two makes alternative designs possible.

## Make success concrete before writing the implementation

An **acceptance example** supplies a particular input, expected result and reason. It translates a general requirement into something that can be checked. The local lab includes a discrepancy, a forbidden scope and a missing source. These examples are deliberately small enough to inspect by hand. They are not a representative evaluation population.

Requirements also need negative examples. If the expected result is only a polished brief, a system can appear successful while inventing a source or failing to deny access. Negative cases state what the service must refuse, preserve or leave unresolved. Acceptance examples should record the agreed response to ambiguity, not silently turn ambiguity into a convenient label.

A **baseline** is the alternative against which a proposed contribution is compared. It may be the existing manual process, an improved form or a small deterministic script. The lab's rule-based route is a baseline that already handles scope and missing evidence without a model. A model must justify what it adds: interpreting variable language, finding relevant passages or preparing a readable draft. It should not receive credit for arithmetic or access checks already supplied by ordinary code.

## Build a vertical slice

A **vertical slice** connects one input to one usable output through all essential layers. For Harbour this means taking a fictional case, checking scope, preparing evidence and showing an investigation result. It is preferable to building an attractive interface whose backend decisions remain unspecified. The slice exposes assumptions at the boundaries early.

Choose a narrow population, such as uncomplicated quantity discrepancies with the three required records. State exclusions, such as damaged goods, mixed units and uncertain customer identity. Exclusions define where the pilot must stop or refer; they are not permission to discard difficult cases from the outcome assessment. Track their frequency and handling effort.

## Use a coding agent as an implementation contributor

A coding agent can propose code, tests and documentation. Its output still needs inspection. Give it a bounded task, the relevant interfaces, acceptance examples and constraints. Ask for the smallest change that satisfies the examples, then inspect the diff and run checks. A prompt that asks for an “enterprise-grade platform” without explicit requirements delegates too many consequential design choices.

A practical work order might be: implement route for the three supplied cases; preserve input data; reject missing scope; add a negative test; report which checks ran. Do not give the coding agent production credentials merely to make a local example work. Generated tests can share the same mistaken interpretation as generated code, so at least some expected outcomes should be reasoned independently.

The supplied implementation is already written and can be studied without purchasing or installing a coding agent. The optional exercise is to propose a small change and compare its behaviour with the acceptance cases. The learning objective is responsible specification and review, not proficiency with one commercial coding interface.

## Practical activity: Turn an observed delay into a bounded problem statement.





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

Does the problem statement require an autonomous remedy decision?

```python
problem={"work":"delivery investigation","difficulty":"records are scattered","proposed_contribution":"traceable brief","excluded":"automatic remedy"}
print(problem)
```

No. It specifies a bounded contribution and an exclusion.

### Complete the exercise

Write the prediction before consulting the worked answer: Does the problem statement require an autonomous remedy decision?

**Worked answer.** No. It specifies a bounded contribution and an exclusion.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
