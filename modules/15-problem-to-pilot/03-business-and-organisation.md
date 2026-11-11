# Lesson 15.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/15-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## Business context: Harbour

Follow one case with the people who actually do the work. The team's description of “handling a discrepancy” may include chasing evidence or negotiating a promise that never appears in the form. Discovery is the work of learning those steps and constraints before committing to a design. Decide what is in scope and who can challenge that choice.

Separate preferences, observed work and policy obligations when defining requirements.

[Company and supply-chain context](../../HARBOUR.md) · [Module 15 business situation](../../reference/harbour-learning-journey.md#module-15)

## The first design decision is what work to support

A fictional discovery exercise at Harbour finds two possible causes of slow resolution. Investigators spend time locating records, but some cases also wait because no team accepts ownership when order and shipment records disagree. These are different problems. Faster drafting may reduce search effort while leaving responsibility unresolved.

Galbraith's information-processing view helps distinguish reducing information requirements from increasing information-processing capacity. A standard intake form can reduce repeated clarification; better retrieval can increase access to evidence. Neither necessarily resolves competing interpretations or decision rights. The [organisation design chapter](../../reference/research/01-organisation-design.md) explains the argument and its limits, with the bibliographic references to Galbraith (1973, 1977).

## Conduct a discovery conversation around one case

Follow a case from its arrival to its current outcome. Record who first noticed it, which information was missing, what each person did and why it moved to another person. Distinguish formal instructions from an account of what actually happened. A diagram can represent the intended route while interviews and observations reveal necessary workarounds.

An investigator might explain that the shipment system records dispatch, not receipt. That distinction changes the evidence requirement: agreement between order and dispatch cannot establish actual delivery. A manager might say that only a regional lead can approve a remedy. That changes the authority route. These findings should enter acceptance examples and the design, not remain informal background knowledge.

The exercise is illustrative. It does not report interviews conducted at a real distributor. In an actual pilot, retain evidence for each requirement and record unresolved disagreements. A stakeholder's preference, an observed practice and a binding policy are different bases for a design choice.

## Define a scope that remains contestable

The initial service prepares quantity-discrepancy briefs for one region. It neither adjudicates damaged-goods claims nor closes cases. Operations owns the case; source-system owners correct records; the authorised manager decides any remedy. A learner should be able to explain why each boundary follows from the work rather than from the convenience of a model interface.

The design should be challenged. A rival explanation is that poor source access, rather than drafting, creates most delay. Another is that unclear ownership causes repeated handoffs. Compare an improved record view and an explicit intake owner with the proposed assistant. A credible pilot can conclude that the simpler intervention is preferable.

## Worked business decision

Harbour authorises a limited comparison of manual preparation, a deterministic record view and an assisted brief. The same inclusion rules apply to each route. The comparison records preparation effort, missing evidence, review effort, unsupported conclusions and elapsed resolution time. Excluded cases and their handling remain visible.

This decision does not claim an expected percentage saving. It creates a way to learn whether the contribution helps under the stated conditions. The [implementation chapter](../../reference/research/04-implementation.md) develops fit, adjustment and rival explanations. It also explains why installing software and observing benefit are separate evidential steps.

## Practical activity: Compare an AI proposal with a simpler organisational intervention.


### Predict and follow the values

Which alternative directly addresses unclear initial responsibility?

```python
alternatives=[{"name":"record view","changes":"source access"},{"name":"intake owner","changes":"responsibility"},{"name":"drafting assistant","changes":"preparation"}]
print(alternatives)
```

### Complete the exercise

**Worked answer.** intake owner addresses that mechanism. A model upgrade may leave it unchanged.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour’s discovery exercise distinguishes two potential causes of delay: locating evidence and obtaining accepted cross-team ownership. A coding project could improve the first while leaving the second untouched. The pilot therefore starts with an operational question and a comparator, not an assumption that agents are required.

**Task:** Write a pilot charter naming the eligible work, alternatives, participating roles, measures and stop conditions.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Compare manual preparation, direct lookup and assisted preparation under matched inclusion rules. Give cross-team ownership problems their own design response. A restricted generated function can help implement a rule; it cannot decide which organisational rule is appropriate.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.

## Research extension: examine the wider arrangement

[Process architecture](../../reference/research/09-process-architecture.md#worked-design-extend-the-boundary-of-success). Define the pilot boundary before selecting measures. Evidence readiness, remedy authorisation and completed resolution are distinct outcomes.
