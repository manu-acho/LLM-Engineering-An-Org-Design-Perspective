# Lesson 18.1: Enterprise context, security and controls

[Download the matching notebook](/downloads/18-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## Shared context needs accountable sources

An enterprise context layer supplies definitions, policy, identifiers and operational evidence used by several applications. It can reduce repeated integration work. It can also distribute an obsolete definition widely. Reuse makes source ownership more important because a correction or failure can affect several services at once.

Harbour's context response contains a scoped case and active policy records. A source identifier and version allow an investigator to ask which text informed a recommendation. The response does not merge policy and customer statements into one undifferentiated truth. The knowledge service should make disagreements visible and identify who can resolve them.

## Authentication, authorisation and evidence are different checks

**Authentication** establishes an identity according to a mechanism such as a signed session or validated token. **Authorisation** determines whether that identity may perform a particular operation on a resource. **Evidence validation** examines whether inputs satisfy the operation's requirements. Passing one check does not imply passing the others.

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
