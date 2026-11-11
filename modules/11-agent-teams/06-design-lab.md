# Lesson 11.6: Divide work where specialisation earns its integration cost

[Module route](README.md) · [Next module](../12-stateful-agents/README.md)

A separate agent may help if one task needs different evidence or a different skill. It also creates another result to check and combine. Compare a single worker with the smaller independent parts of a divided workflow. Identify which division helps enough to pay for the extra handoffs in this case.

## Test whether four contributors are needed

**Fictional case.** Harbour proposes a researcher, policy analyst, drafter and reviewer agent for every enquiry. Some cases require a single status lookup; others require evidence interpretation and specialist judgement. Uniformly assigning four agents may add reports and delay without adding useful competence.

The team writes a contribution table. The researcher locates permitted evidence. The policy analyst applies current scope and identifies unresolved interpretation. The drafter prepares language. The reviewer tests specified claims against evidence. If the reviewer sees only the draft, it cannot independently check a source that the draft misrepresents.

## Use modularity as a contingent design choice

Modularity divides a system into parts with limited interactions. A clear interface can make components easier to replace. But tightly interdependent work can create repeated cross-boundary clarification. More modules can therefore increase integration work.

The [organisation design review](../../reference/research/01-organisation-design.md) distinguishes technical decomposition from organisational division. A software boundary is useful here when it creates a real difference in evidence, capability, checking or maintenance. Merely naming the same model four times does not establish those differences.

## Compare two complete arrangements

| Element | Four-stage crew | Bounded investigator plus independent check |
|---|---|---|
| Evidence collection | Separate researcher | Investigator uses permitted tools |
| Policy | Separate analysis task | Fixed required policy read with specialist escalation |
| Draft | Dedicated drafter | Investigator returns structured draft |
| Check | Reviewer consumes task context | Deterministic checks plus source-capable reviewer |
| Integration burden | Several task interfaces | Fewer interfaces, with explicit exceptional route |

Harbour pilots the second arrangement for routine cases and retains specialist collaboration for disputed interpretations. This is not a universal preference for fewer agents. It matches the selected population's dependency pattern.

## Calculate the review trade-off

Suppose four stages each add two minutes of service time, excluding waiting, while the smaller arrangement adds four minutes and a two-minute check. The potential difference is two minutes per case. If the four-stage route prevents more consequential errors, that extra effort may be justified. If all reviewers rely on the same incomplete summary, the extra time may buy little additional evidence.

Compare corrections against original sources, not agreement between generated opinions. Correlated errors can create apparent consensus. Independent checking requires a different evidential opportunity, not necessarily a different model brand.

## Fit the human work around the software contributions

The investigator's output goes to a case owner who can obtain missing evidence. The policy owner adjudicates recurring disputes. The reviewer can reject a claim without being penalised for slowing throughput. A process owner monitors whether the combination improves accepted work.

The configuration includes incentives and capacity. If every rejection creates a performance penalty for the reviewer, formal rejection rights may not translate into meaningful challenge. Shared goals and mutual respect across specialists affect coordination alongside schemas and task context.

## Learn from one revision cycle

After the first pilot week, reviewers repeatedly identify missing receipt conditions. Harbour changes evidence collection, not just the final wording. In the next week, source-complete cases improve while a new regional category remains problematic. That category goes to policy review rather than being patched into an agent's backstory.

**Worked decision:** Retain a separate specialist only when its contribution can be stated, evaluated and integrated. If removing an agent loses only another restatement, redesign the division. If it loses access to necessary expertise or an independent checking opportunity, preserve that contribution and improve its interface.

**Research basis:** [Coordination](../../reference/research/02-coordination.md) and [decision theory](../../reference/research/03-decisions.md) complement the division/integration argument.

## Read the organisational connection

Compare the benefit of specialisation with handoffs, reconciliation and maintenance. The research chapter explains [decomposition and integration](../../reference/research/01-organisation-design.md#when-more-agents-create-more-integration-work).

The research chapter also explains [how specialist processes connect](../../reference/research/09-process-architecture.md#process-architecture-connects-the-processes).
