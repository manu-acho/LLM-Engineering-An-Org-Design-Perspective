# Lesson 8.3: Designing an operating organisation around the workflow

[Download the matching notebook](/downloads/08-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md) · [Curriculum index](../../README.md)

## Business context: Harbour

Assign case ownership across customer service, warehouse, transport coordination and finance.

[Company and supply-chain context](../../HARBOUR.md) · [Module 8 business situation](../../reference/harbour-learning-journey.md#module-8)

## The capstone decision

**Fictional case.** Harbour is ready to pilot an assistant that reads a complaint, gathers order and policy evidence, proposes a route and prepares a handoff. The design team has eight attractive component names and a diagram showing their connections. The operations director asks: “Who owns a case when one of these steps fails?”

That question turns an architecture diagram into an organisation design problem. The workflow must allocate work, attention, authority and repair, including work created by its own failures.

## Start with dependencies

Research chapter 2's dependency lens asks what one activity needs from another. Intake supplies an identifiable request. Evidence gathering supplies reliable records. A reviewer needs a supported proposal. The execution service needs an authorisation it can validate. The receiving team needs a handoff it accepts as usable.

Some relations are sequential. Others become reciprocal when evidence conflicts and teams must revise their understanding. A message queue can manage transfer and waiting; it cannot settle what finance and operations consider adequate evidence.

Describe the dependency before choosing the mechanism. A status field, escalation meeting, validation rule and specialist conversation solve different parts of the problem.

## Fit concerns the whole arrangement

Research chapter 1's configurational view asks whether division of work, information, roles and authority fit together. A reviewer with formal approval rights but no source access cannot perform the intended review. A queue owner without capacity becomes a bottleneck. An assistant that increases proposal volume without improving quality can intensify those dependencies.

Technical component boundaries need not match organisational boundaries. One service may support several roles; one human task may require several services. Do not infer an effective organisation chart from the number of agents.

An ensemble likewise concerns prediction, not consensus among accountable stakeholders. Combining three numerical estimates does not replace a decision about whose judgement is legitimate.

## Distinguish design, configuration and performance

The linked reviews distinguish what a design describes, what an organisation configures, and what people actually do. These are called **represented design**, **implemented configuration** and **enacted practice**. For our pilot, a prompt describes intended behaviour. Enabled tools and access rules describe deployed capability. Observation and traces reveal particular performances. Repeated inquiry can reveal patterns and outcomes.

A workflow file proves what was encoded. It does not show whether employees use it, work around it or repair it off-system. Conversely, a workaround does not prove the encoded rules had no effect. It may be a response to a very consequential constraint.

Research chapter 5's artefact perspective avoids both extremes. Software can block, route and record while still leaving interpretation, communication and adaptation in the wider routine.

## Implementation continues after launch

Research chapter 4's lifecycle lens treats go-live as one point in a longer process. The team learns during stabilisation, discovers misfit and adjusts use. Define how that learning reaches design owners.

A proposed operating arrangement might include an intake owner, a source/policy owner, a reviewer role, an execution owner, a service operator and a process owner who reviews end-to-end performance. In a small firm, one person may hold several roles. Keep the responsibilities distinct so changes and failures have an owner.

Research chapter 3 adds a question about discretion: who can revise the categories and thresholds that guide the workflow? An escalation route that permits only individual exceptions, with no route to challenge a repeatedly bad rule, leaves important design authority unaddressed.

## Actualisation joins the components to the work

The workflow's tools and states are material arrangements with identifiable technical effects. To claim that they help work move between teams, name who does what and under which conditions. Someone must be available to receive the case. They need usable evidence, suitable authority and a way to recover when something fails.

**Actualisation** concerns the actions through which a possibility becomes consequential over time. Installing the planner, training staff once or observing one completed case does not establish that process. Follow repeated cases, including repairs and off-system coordination, and investigate which outcomes emerge for different roles.

A record can help someone trace an event without ensuring that anyone explains it, takes responsibility or corrects a problem. The receipt simulator demonstrates a local acknowledgement pattern; its code cannot establish that an organisational owner investigates a disputed handoff or can enforce a correction.

The [capstone lesson](04-technology-in-practice.md) develops this distinction through an evidence-panel case and compares feature, affordance, constraint, actualisation and outcome. Its framework adapts [Research chapter 6](../../reference/research/06-technology-in-practice.md) without treating its theoretical perspectives as interchangeable.

## Apply the idea: respond to three breakdowns

Consider three events: the policy service is unavailable; a reviewer rejects a proposal because the category is wrong; and the receiving team says a recorded handoff never reached its working queue. What should happen next in each case, and who should own the unresolved work?

**Worked response:** The first needs a bounded service failure and an owner for pending work, not an invented policy. The second needs correction of the case plus investigation of the label rule if recurrent. The third requires reconciliation between execution receipt and actual receiving workflow. A log line saying “sent” cannot settle it.

What would you measure to judge the whole workflow? Include correct end-to-end completion, waiting, clarification loops, reviewer effort, duplicate actions, abandoned cases and successful recovery. Investigate whose work changed. A decline in account-manager effort may coexist with increased specialist burden.

**Rival explanation:** Apparent adoption failure could reflect an unsuitable interface, a justified control concern, inadequate capacity or distrust created by earlier errors. Treat these as competing explanations requiring evidence rather than labelling employees resistant.

## Build a pilot plan

Create a pilot operating design containing the dependency map, permitted action table, state transitions, evidence requirements, exception/repair owners and evaluation plan. Show how staff can contest a result and how a revised policy reaches the application. State which parts were simulated and which, if any, were tested in real work.

The result is a practical brief for an AI pilot. Its value is the connection between mechanism and organisational judgement: what the system does, what work remains and what evidence would justify expanding its scope.

**Research basis:** The [research foundation](../../reference/literature-guide.md), especially dependency management, configurational fit, decision premises, implementation over time and the artefact/practice distinction. These concepts guide the fictional design; the curriculum claims no empirical AI implementation outcomes.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Workflow, roles, evidence, capacity and incentives need to be considered together. The research chapter explains [fit among design choices](../../reference/research/01-organisation-design.md#fit-is-a-relationship-among-choices).

## Practical activity: Include the receiving team's work in the operating model.





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

What is the total illustrative work here?

```python
responsibilities = [{"stage":"draft","minutes":3,"owner":"application support"},{"stage":"investigation","minutes":12,"owner":"operations"},{"stage":"exception","minutes":8,"owner":"manager"}]
print("Illustrative work minutes:",sum(row["minutes"] for row in responsibilities))
```

Twenty-three minutes. This does not include waiting and is not measured operating evidence.

### Complete the exercise

Write the prediction before consulting the worked answer: What is the total illustrative work here?

**Worked answer.** Twenty-three minutes. This does not include waiting and is not measured operating evidence.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour now has several possible technical contributions: retrieving records, preparing a draft and proposing a recipient. A customer still needs someone to own the unresolved delivery. The operating-model question is how people and services accept, challenge and complete these contributions together.

**Task:** Produce an operating model with named contribution owners, acceptance conditions, decision rights and exception routes.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

An operations case owner coordinates investigation; functional specialists own their evidence; authorised review precedes a remedy. Technical support owns execution defects. A case is not commercially resolved merely because a draft was produced or a simulated decision was recorded.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.

## Follow an authorised remedy into the remaining work

In this separate fictional follow-through, investigation supports a proposed replacement. An authorised manager approves that proposal. No stock availability, shipment or financial event follows automatically from that approval. The table describes work Harbour would still need to organise; it is not a set of integrations implemented by the notebook.

| Step | Accountable contribution | Evidence or decision needed | What remains open |
|---|---|---|---|
| Remedy authorisation | Authorised manager selects an appropriate remedy | Current case evidence and applicable policy | Availability, feasible delivery and any account adjustment |
| Replacement feasibility | Warehouse/planning contact confirms a suitable item and available quantity | Stock identity, unit, availability and competing commitments | A delivery commitment to the customer |
| Delivery arrangement | Operations and transport coordination arrange the accepted plan | Feasible dispatch/carrier timing and customer needs | Physical fulfilment and evidence of receipt |
| Account treatment | Finance determines and processes any authorised adjustment required by the selected remedy | Approved instruction and relevant invoice/account records | Confirmation that the recorded account reflects the decision |
| Customer communication and follow-up | Customer service communicates the accepted plan; the case owner follows unresolved work | Confirmed commitments and actual completion evidence | Any delivery, account or customer issue not yet completed |

A replacement does not automatically imply a refund or credit. The commercial treatment depends on the remedy and policy. Avoid issuing an adjustment merely because the earlier route label says `finance`.

**Independent application.** Suppose replacement stock is unavailable after approval. What should the customer be told, who coordinates the next decision and which state must not be presented as complete?

**Worked direction.** Customer service should communicate the uncertainty and the next confirmed update, rather than promise an unconfirmed dispatch. The case owner coordinates warehouse/planning information and any revised authorised remedy. Approval remains a recorded decision; delivery and any account work remain unfinished. A closed API request must not be labelled “customer resolved”. Carry this trace into the [final workbook](../../WORKBOOK.md#final-harbour-organisation-design-review).

## Research extension: examine the wider arrangement

[Governance and accountability](../../reference/research/08-governance-and-accountability.md#put-decisions-near-knowledge-while-examining-the-costs). Compare the location of relevant knowledge with the right to decide. An agent summary changes communication but does not remove the cost of transferring meaning.
