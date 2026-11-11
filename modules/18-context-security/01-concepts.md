# Lesson 18.1: Enterprise context, security and controls

[Download the matching notebook](/downloads/18-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## What you'll learn and why it matters

Distinguish identity, permission and evidence checks. Use those checks to decide which material can reach a model and which text should be treated as a customer's account.

## Business context: Harbour

Knowing who made a request is authentication. Deciding whether that person may see this case is authorisation. Determining whether a statement in the case is supported requires evidence. Follow a request from a different region and a message that contains an instruction addressed to the assistant. Neither text nor identity alone should bypass the access check.

Identify the source and authority behind context supplied to the assistant.

[Company and supply-chain context](../../HARBOUR.md) · [Module 18 business situation](../../reference/harbour-learning-journey.md#module-18)

## Shared context needs accountable sources

An enterprise context layer supplies definitions, policy, identifiers and operational evidence used by several applications. It can reduce repeated integration work. It can also distribute an obsolete definition widely. Reuse makes source ownership more important because a correction or failure can affect several services at once.

Harbour's context response contains a scoped case and active policy records. A source identifier and version allow an investigator to ask which text informed a recommendation. The response does not merge policy and customer statements into one undifferentiated truth. The knowledge service should make disagreements visible and identify who can resolve them.

## Authentication, authorisation and evidence are different checks

**Authentication** establishes an identity according to a mechanism such as a signed session or validated token. **Authorisation** determines whether that identity may perform a particular operation on a resource. **Evidence validation** examines whether inputs satisfy the operation's requirements. Passing one check does not imply passing the others.

Suppose an adviser signs in and requests H-17. Signing in gives the application a basis for knowing who is asking. The case's region determines whether that adviser may read it. Even an adviser with access may lack proof of delivery. That is an evidence problem, which the access check cannot settle.

A manager can be authenticated and still lack access to another region's case. A permitted read can return a stale policy. A current policy can still leave the facts unresolved. The local functions take trusted tenant and role arguments to expose these boundaries; the HTTP application later resolves those arguments from a server-controlled principal mapping.

## Treat external text as data

A customer report may contain text that resembles an instruction to the model. Retrieved documents, email and tool results can carry similar material. **Prompt injection** attempts to redirect model behaviour through such content. The important trust question is where the text came from and whether it is allowed to govern the operation.

Instructions to ignore malicious text can be useful, but are not an enforcement boundary. Deterministic access checks, narrow tools, argument validation, least privilege and approval rules should still apply if a model misinterprets a report. The course does not implement a universal injection detector or claim that a keyword filter would be one.

A **threat model** identifies assets, actors, trust boundaries, plausible attacks and consequences. Start with concrete assets: case records, source policies, credentials and remedy authority. Consider an unauthorised read, fabricated evidence, a malicious tool argument and a repeated decision. Describe the check that should block each attempt and the record needed to investigate a failure.

## Check freshness where it matters

Policy versioning identifies which rule was used. A long-running case can encounter a policy change between preparation and approval. The decision store therefore requires a submitted policy version matching the current case requirement. It rejects stale submissions rather than pretending that an old review is automatically valid.

A real policy lifecycle also needs effective dates, transition rules and an owner who can decide which version governs an existing case. A single integer comparison does not supply that governance. Distinguish technical detection of a changed version from the organisational decision about what the change means.

## Reduce access before relying on detection

Least privilege means granting only the capabilities needed for the task. A read-only investigation contribution does not need a general SQL console, arbitrary shell access or a payment credential. Restricting the available capability limits the consequence of mistaken model output.

Negative tests should include wrong tenant, wrong role, stale version, missing source and invalid arguments. They establish selected boundaries under stated conditions. A broader service assessment would also cover credential lifecycle, dependency vulnerabilities, deployment configuration, logging, backup access and insider misuse. These concerns should be assigned to owners and tested as real scope expands, rather than compressed into a claim that the system is secure.

## Practical activity: Assemble context after applying scope and freshness conditions.


### Predict and follow the values

Does being textually relevant make P-old current?

```python
from ai_orgdesign.case_data import POLICIES
context=[p for p in POLICIES if p["tenant"]=="north" and p["active"]]
print([p["id"] for p in context])
assert "P-old" not in [p["id"] for p in context]
```

### Complete the exercise

**Worked answer.** No. Its retired status excludes it from current context.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Authentication establishes identity. Authorisation decides access to a particular operation or record. Evidence and currency require their own checks.

## What this means for the business process

Apply scope and freshness before assembling context. Keep customer text in the role of evidence, and derive authority from the service's trusted rules, so material in a record cannot give itself permission.

For the research behind this design choice, read [Permission and authority](../../reference/research/03-decisions.md#permission-and-authority).

## Next lesson

The next workshop follows one permitted request and one cross-region denial to the point where context would be assembled. [Lesson 18.2: Assemble context inside an access boundary](02-code-workshop.md).
