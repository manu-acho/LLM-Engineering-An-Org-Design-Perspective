# Lesson 14.6: Read a completed AI integration proposal

[Module route](README.md) · [Next: evaluate the service over time](07-service-evaluation.md)

## The proposal in one paragraph

**Entirely fictional worked dossier.** Harbour proposes a referenced drafting service for non-urgent delivery disputes. It will gather permitted order and current policy records, identify missing evidence and prepare a proposal for an accountable reviewer. It will retain case ownership, record acceptance of handoffs and expose recovery work. It will not grant remedies automatically during the pilot.

This completed example applies the seven-step plan in Lesson 14.4. Its figures, policies and results are teaching assumptions, not client evidence.

## 1. Present process and selected population

Harbour handles 1,000 enquiries a month. Four hundred contain sufficiently long free-text descriptions to make assisted drafting plausible. Routine status questions remain direct lookups. Urgent cases and disputed policy interpretations remain outside the initial scope.

Preparation currently averages 12 minutes, review three and expected rework two. Elapsed resolution averages two days because records and acceptance sometimes wait. The proposal therefore distinguishes effort saving from responsiveness.

## 2. Alternatives and reason for the selected pattern

The first alternative is improved intake plus direct lookup. The second adds a fixed retrieval-and-draft route. The third uses a bounded agent to select follow-up evidence. Harbour initially chooses the second: both order and policy are mandatory, so fixed application orchestration makes that dependency clear. Agent selection remains an evaluated extension for cases whose evidence needs genuinely vary.

MCP is used only if several authorised applications need the same maintained capabilities. A direct adapter remains adequate for a single application. The pilot is not required to demonstrate every framework studied.

## 3. Technical path and artefacts

```text
Intake and identity → case-scoped reads → versioned evidence
→ referenced draft → review of proposal revision
→ approved submission → receiving acceptance → outcome record
```

The retained artefacts are case ID, source versions, prompt/configuration revision, draft, missing information, review decision, action ID, receipt and acceptance state. Conversation text supports the task but is not the only business record. External submission uses an agreed duplicate/reconciliation contract.

## 4. Work and decision allocation

| Role | Contribution and authority |
|---|---|
| Intake/case owner | Establish scope, obtain clarification, retain customer progress |
| Source owners | Correct order evidence and publish current policy |
| Reviewer | Accept, reject or revise the identified proposal within mandate |
| Execution owner | Enforce permitted operation and preserve action identity |
| Receiving team | Accept usable work or return an explicit reason |
| Operator | Recover failed services and surface uncertain work |
| Process/policy owner | Change categories, thresholds and the wider arrangement |

If the same person holds several roles, the record still distinguishes their decisions. A platform administrator's technical access does not automatically confer policy authority.

## 5. Capacity and economics

Assume actual use reaches 70% of 400 eligible cases: 280. Preparation falls to six minutes, review rises to four and expected rework falls to one. Total effort changes from 17 to 11 minutes, saving six per assisted case or 28 hours monthly.

At £30 an hour, capacity value is £840. Monthly operation and maintenance are £350, leaving £490 before implementation cost. With an illustrative £6,000 initial cost, simple payback would exceed twelve months if that capacity value were actually realised and stable. Service-quality benefits are evaluated separately. If use is only 35%, the ongoing difference falls to £70 under the same assumptions.

## 6. Evaluation and decision gates

Use frozen development and held-out cases containing normal work, missing evidence, conflicting sources, stale proposals, scope denial and service failure. Compare improved intake alone with intake plus drafting. Report supported claims, invalid outputs, review corrections, accepted handoffs, effort by role, waiting and customer outcomes.

An unsupported external commitment stops the affected action route for investigation. A source outage creates pending work with an owner. Pilot expansion requires maintained quality and useful outcomes, not merely a high count of tool calls.

## 7. Stabilisation and revision

During stabilisation, owners inspect pending and rejected cases daily. Repeated category disagreement goes to policy review. After the arrangement is used recurrently, inquiry follows off-system repair and whether different actors can meaningfully correct a proposal. Model, source or category changes trigger relevant reevaluation and a rollback decision.

## A worked outcome and next decision

Suppose the pilot achieves the effort figures but elapsed resolution stays at two days. Interviews and case traces show warehouse evidence remains the main wait. Harbour retains drafting for the measured capacity benefit, improves the evidence contribution and does not claim faster resolution. It postpones autonomy expansion until a specific permitted operation addresses that dependency.

**Practice:** Change one assumption, such as adoption, review effort or eligible volume, and recalculate the case. Then state which organisational arrangement would need to change to make the improved figure plausible. Arithmetic and design must support each other.

**Research foundation:** The [six-stream literature guide](../../reference/literature-guide.md) supplies the dependency, decision-premise, fit, routine and actualisation lenses used throughout this dossier.
