# Lesson 14.4: Build an AI integration plan around the work

[Download the matching notebook](/downloads/14-04-integration-plan.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Business application](03-business-and-organisation.md) · [Part II route](../../AGENT-ENGINEERING.md)

## Begin with a service problem

**Fictional case.** Harbour wants faster, more reliable resolution of delivery disputes. Staff collect records from several systems, clarify missing evidence and negotiate who should act. Preparation takes time, but waiting for an accepted response is often the larger delay.

A proposal says “deploy a team of agents”. That is an architectural idea, not yet an account of how service improves. This final exercise turns the concepts and code into an operating proposal that can be investigated, compared and revised.

## 1. Describe the work before adding AI

Choose a bounded request type. Identify who receives it, what information each role needs, where decisions occur and which exceptions require judgement. Follow a case through to an outcome the receiving parties recognise.

For Harbour, distinguish customer report, shipment record, reported difference, verified shortage, authorised credit and customer resolution. Those labels represent different claims. Record where the existing process already relies on informal calls or repair work.

Use the dependency question from coordination theory: what does each activity need from another to proceed? The answer may reveal a missing source, unclear responsibility or an unavailable specialist before any model is considered.

## 2. State the proposed contribution precisely

A bounded first proposal is: “Gather permitted order and policy evidence, identify missing information and prepare a referenced draft for an accountable reviewer.” It promises neither automatic credit decisions nor resolution of every disagreement.

Define which steps are deterministic and which require language interpretation. A program can enforce required fields and perform arithmetic. A model may help interpret a complaint or suggest useful clarification questions. A person may need to resolve conflicting claims or decide whether an exception is legitimate.

Compare a simpler alternative: improve the intake form and source access, then use a fixed lookup-and-draft workflow. The agent design needs a reason for its extra flexibility.

## 3. Choose technical patterns from dependencies

| Need | Candidate pattern | Question that still needs an answer |
|---|---|---|
| Adapt the next evidence request | Bounded tool loop | Which actions are permitted, and when does it stop? |
| Gather independent records | Parallel reads | What happens if a required source fails? |
| Obtain specialist advice | Specialist exposed as a tool | Who integrates and owns the result? |
| Continue in a specialist service | Handoff | Has the receiving service accepted the case? |
| Wait for review | State and checkpoint | Which proposal version is being reviewed? |
| Share work between runtimes | Common task contract | Do status fields have the same meaning? |
| Reuse business capabilities | Direct adapter or MCP service | Who enforces scope and owns capability semantics? |

This is a decision table, not a requirement to use every pattern. One application may need only a few. Framework choice follows the needed capabilities and the team's ability to operate them.

## 4. Allocate responsibility at the boundaries

Specify the source owner, reviewer, policy owner, execution owner, service operator and end-to-end process owner. Describe what each can see and change.

For Harbour, the source owner can correct a misleading delivery record. The reviewer can reject an unsupported proposal. The policy owner can resolve a recurring category dispute. The operator can recover a failed process. These are distinct forms of intervention.

Name an owner for waiting and failed cases. A tool error or an exhausted step budget should produce a visible case state and a route to action. Returning an error string to a screen does not assign responsibility.

## 5. Plan evidence at different levels

Inspect the represented design: prompts, tool contracts, task dependencies and graph transitions. Test the configured permissions and version checks. Establish that reviewer roles, capacity and procedures are in place.

Then observe repeated use. Can staff inspect the sources? Do corrections reach the next team? What work happens outside the application? These observations connect available features to actualisation, the actions through which possibilities become consequential.

Finally compare outcomes: supported resolutions, elapsed time, waiting, rework, unsupported commitments and effort by role. Include difficult cases and cases where the system worsens the work. A trace of successful tool calls is not an outcome measure by itself.

## 6. Make the pilot informative

Begin with a defined population and a comparison. For example, compare a referenced read-only draft with the current process for similar disputed-delivery cases. Record concurrent changes such as better intake requirements or added staffing.

Set quality conditions and a stopping rule before expanding scope. An illustrative condition is that every recommendation retains source references and unresolved conflicts. An illustrative stop condition is an unsupported customer commitment. These are proposed design choices, not empirically validated thresholds.

Investigate rival explanations. Faster handling might come from easier cases, better source access or a temporary increase in capacity rather than model orchestration. Document the combined intervention where effects cannot be separated.

## 7. Define how the arrangement changes

State who reviews overrides, source changes, repeated failures and new request categories. Decide when prompts, schemas, tools or task rules need a new version and who approves that version.

Retain enough information to reconstruct an important decision without collecting unnecessary personal data. Ensure a rollback route and a way to identify unresolved work during recovery. A model update may change behaviour even when the surrounding workflow is unchanged.

Implementation continues through these adjustments. Treat staff feedback as evidence about the design, while checking which proposed changes preserve important controls.

## A worked pilot decision

Suppose the pilot halves draft preparation time, but total resolution time is unchanged because finance still waits for warehouse evidence. The supported conclusion is a local preparation improvement, with an unresolved dependency limiting the broader benefit.

A reasonable next step is to improve the evidence path and receiving arrangement before granting more autonomy. Additional tools may help once the missing capability is identified. An agent that takes more steps cannot resolve absent authority or unavailable evidence by persistence alone.

The plan should therefore connect a specific mechanism to a specific change in work and an appropriate evidence test. That connection is the purpose of studying AI engineering and organisation design together.

**Try it:** Prepare a two-page pilot plan using these seven steps. Include one simpler alternative, one technical failure, one organisational breakdown and the role responsible for each response. Identify which claims you can support now and which remain hypotheses.

**Research basis:** [Organisation design](../../reference/research/01-organisation-design.md), [coordination](../../reference/research/02-coordination.md), [decision theory](../../reference/research/03-decisions.md), [enterprise-system implementation](../../reference/research/04-implementation.md), [routines](../../reference/research/05-routines.md) and [technology in practice](../../reference/research/06-technology-in-practice.md). These reviews inform the questions; the fictional plan is not a reported deployment outcome.

## Read the organisational connection

Integration planning should connect task scope, information, roles, rights and capacity. The research chapter explains [fit among design choices](../../reference/research/01-organisation-design.md#fit-is-a-relationship-among-choices).
