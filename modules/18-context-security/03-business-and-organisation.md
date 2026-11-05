# Lesson 18.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/18-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

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
