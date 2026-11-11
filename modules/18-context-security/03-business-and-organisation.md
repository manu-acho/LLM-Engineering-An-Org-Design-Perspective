# Lesson 18.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/18-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## What you'll learn and why it matters

Allocate rights to change shared definitions and policies. This helps Harbour keep teams aligned when the meaning of a field changes.

## Business context: Harbour

If all teams use a field named “delivery date”, they still need to agree whether it is the promised, recorded or confirmed date. Shared context gives the system common material to work from. Decide who can change that definition, how changes are communicated and what happens to decisions already in progress.

Assign ownership of definitions and corrections across operations, finance and technology.

[Company and supply-chain context](../../HARBOUR.md) · [Module 18 business situation](../../reference/harbour-learning-journey.md#module-18)

## A shared definition can distribute authority

Harbour creates a context service so several assistants can use the same policy definitions. This makes maintenance easier, but also makes a central choice consequential. Which document counts as current? Who can correct it? Which region's exceptions remain visible? These are organisational decisions carried by the technical arrangement.

The [decision-making chapter](../../reference/research/03-decisions.md) explains how categories and programmes structure what situations an organisation recognises and how it responds. Applying that reasoning here is a research-informed interpretation: the context layer influences the premises available to a service, but its existence does not establish how staff actually interpret or use them.

## Do not confuse uniformity with agreement

A common field name can hide different meanings. Shipment quantity may mean dispatched quantity to the warehouse and expected receipt to a customer team. Joining the data without retaining this distinction creates apparent agreement. A glossary of enterprise terms needs an owner, examples and a route for disputed definitions.

The technical glossary in this course explains software concepts. A real organisation also needs its own business vocabulary. Case identifiers, source versions and status labels should state their meaning in the specific service. Shared syntax is useful, but it does not remove differences in expertise, interests or interpretation.

## Establish decision rights for context changes

A source owner can correct a factual record. A policy owner can decide which rule applies. A service owner can decide whether a changed source requires reevaluation of a model configuration or reopened cases. Keeping these acts distinct avoids giving a context editor unintended authority over remedies.

A change record should identify the old and new definitions, effective scope, reason, reviewer and affected services. The local policy version check detects a mismatch but does not decide whether a case should retain its earlier policy. That transition rule belongs to the relevant organisational authority.

## Examine who is enabled and constrained

A central context service may help an investigator locate evidence while constraining a regional specialist whose legitimate exception is not represented. The [technology-in-practice chapter](../../reference/research/06-technology-in-practice.md) explains why possibilities and constraints are relational to actors and goals. It is too broad to say that a feature empowers the organisation without identifying who can do what under which conditions.

A contestation route should therefore accompany the shared definition. Staff need a way to flag an unsuitable category or obsolete source without being forced to pretend the case fits. Contestation is not automatic permission to bypass policy; it is a governed route for examining a mismatch.

## Worked control design

Harbour keeps a source registry with owner, version, scope and review date. The application filters context by trusted scope, preserves source identities and checks policy version again when a decision commits. A record owner receives correction requests; the policy owner resolves disputed applicability; operations manages affected cases.

The design is tested against wrong-region reads and stale decisions. Further review would examine deployment credentials, logging access, backup copies and administrative paths. Those remain separate from the narrow local test result. Security and organisation design meet in explicit authority, correction and accountability arrangements rather than in a claim that adding a gateway makes the service governed.

## Practical activity: Name decision rights for source and policy changes.


### Predict and follow the values

Who decides policy applicability in this proposal?

```python
owners={"factual correction":"record owner","policy applicability":"policy owner","affected cases":"operations"}
print(owners)
```

### Complete the exercise

**Worked answer.** policy owner. A context editor should not acquire that right accidentally.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour’s regional records, current policy and finance definitions can be shared selectively to support investigation. A customer message can also contain misleading instructions. Treating every available string as equally authoritative could leak evidence or change the meaning of a commercial decision.

**Task:** Create an evidence-authority map separating customer reports, operational records, policy and authenticated permissions.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

A customer report can establish what was reported without setting system rules. A policy needs an approved version and owner. Regional scope comes from trusted application identity. Finance and operations should agree the meaning of shared fields and correct them through owned routes.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.

## Research extension: examine the wider arrangement

[Governance and accountability](../../reference/research/08-governance-and-accountability.md#four-terms-that-answer-different-questions). Separate access permission, authority to act and an obligation to explain. A logged identity does not establish all three.

[Infrastructure and standards](../../reference/research/07-infrastructure-and-standards.md#classification-changes-what-an-organisation-can-see). Context categories can change who sees evidence. Examine exclusions, ambiguous categories and the route for correcting a classification.

## What to remember

A common field name can carry different interpretations. An editor's ability to prepare context does not grant authority to change a policy.

## What this means for the business process

Name an owner for a field's definition and for policy approval. Communicate revisions to dependent teams and say what happens to cases already in review.

For the research behind this design choice, read [Standards make comparison possible and require continuing work](../../reference/research/07-infrastructure-and-standards.md#standards-make-comparison-possible-and-require-continuing-work).

## Next lesson

Next turn those responsibilities into testable conditions on what can enter a request and what can support a decision. [Lesson 18.4: Make the operating contract inspectable](04-operating-contract.md).
