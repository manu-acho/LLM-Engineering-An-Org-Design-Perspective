# Lesson 19.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/19-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## Operation needs an owner after release

A project team can produce a working service while leaving responsibility after release unclear. Harbour therefore names who handles an unavailable source, an incorrect brief, a pending decision, a database restore and a disputed customer outcome. One person can hold several roles in a small pilot, but the responsibilities should still be visible.

The [implementation chapter](../../reference/research/04-implementation.md) distinguishes installation from organisational adjustment and benefit. Deployment changes the technical availability of the service; recurrent use may reveal new coordination work and misfit. Go-live is therefore a point in the inquiry, not the outcome measure.

## Prepare a handover that supports action

A useful handover includes the service purpose and exclusions, a dependency map, configuration and release identities, recovery steps, known limits, open issues and escalation contacts. It should let another operator answer a concrete incident question without reconstructing the development chat.

For the local teaching application, an operator can start the server, inspect health, authenticate a scoped read and run the tests. The database lives under outputs and is not a managed backup. A future hosted version needs a persistent store and a tested restore procedure before it can promise continuity. The absence of these facilities is a scope limit, not a hidden operational assumption.

## Work an incident from symptom to recovery

Assume the application responds but all policy lookups fail. A process-level health check may remain green while the service is not ready for its intended task. The operator should stop unsupported work, preserve pending cases and tell the case owner what is unavailable. Retrying every request without a limit can worsen the dependency failure.

Next identify the relevant version, affected interval and cases. Restore the dependency or select a known working configuration. Then reconcile work that may have completed without an acknowledgement. A restart can repair availability while leaving duplicate or incomplete business actions unresolved.

## Avoid transferring invisible work

An automated service can shift troubleshooting to users, record owners or an understaffed support team. Include that effort in the operating design and benefit comparison. A low engineering maintenance estimate is incomplete if investigators spend substantial time interpreting ambiguous failures.

Conversely, some initial support work can build a shared understanding that improves later use. Routine dynamics suggests examining repeated performances and retained adjustments rather than assuming either permanent burden or inevitable learning. The [routines chapter](../../reference/research/05-routines.md) explains the theoretical basis and evidence needed for such interpretations.

## Worked release decision

Harbour permits a local learning release with fictional data and a fixed principal mapping. A public customer-facing release requires additional evidence about identity, hosting, persistence, recovery, security and service capacity. The release record separates completed local tests from these unexecuted conditions.

The decision also specifies retirement. When a source or model becomes unsupported, the owner must decide whether to replace, narrow or withdraw the contribution. Preserve required case records and provide an alternative route for pending work. Continuing ownership includes the possibility of stopping a service whose contribution no longer justifies its operating burden.
