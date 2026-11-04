# Lesson 8.3: Designing an operating organisation around the workflow

[Previous lesson](02-code-workshop.md) · [Module route](README.md) · [Curriculum index](../../README.md)

## The capstone decision

**Fictional case.** Harbour is ready to pilot an assistant that reads a complaint, gathers order and policy evidence, proposes a route and prepares a handoff. The design team has eight attractive component names and a diagram showing their connections. The operations director asks: “Who owns a case when one of these steps fails?”

That question turns an architecture diagram into an organisation design problem. The workflow must allocate work, attention, authority and repair, including work created by its own failures.

## Start with dependencies

Stream 2's dependency lens asks what one activity needs from another. Intake supplies an identifiable request. Evidence gathering supplies reliable records. A reviewer needs a supported proposal. The execution service needs an authorisation it can validate. The receiving team needs a handoff it accepts as usable.

Some relations are sequential. Others become reciprocal when evidence conflicts and teams must revise their understanding. A message queue can manage transfer and waiting; it cannot settle what finance and operations consider adequate evidence.

Describe the dependency before choosing the mechanism. A status field, escalation meeting, validation rule and specialist conversation solve different parts of the problem.

## Fit concerns the whole arrangement

Stream 1's configurational view asks whether division of work, information, roles and authority fit together. A reviewer with formal approval rights but no source access cannot perform the intended review. A queue owner without capacity becomes a bottleneck. An assistant that increases proposal volume without improving quality can intensify those dependencies.

Technical component boundaries need not match organisational boundaries. One service may support several roles; one human task may require several services. Do not infer an effective organisation chart from the number of agents.

An ensemble likewise concerns prediction, not consensus among accountable stakeholders. Combining three numerical estimates does not replace a decision about whose judgement is legitimate.

## Distinguish design, configuration and performance

The linked reviews distinguish what a design describes, what an organisation configures, and what people actually do. These are called **represented design**, **implemented configuration** and **enacted practice**. For our pilot, a prompt describes intended behaviour. Enabled tools and access rules describe deployed capability. Observation and traces reveal particular performances. Repeated inquiry can reveal patterns and outcomes.

A workflow file proves what was encoded. It does not show whether employees use it, work around it or repair it off-system. Conversely, a workaround does not prove the encoded rules had no effect. It may be a response to a very consequential constraint.

Stream 5's artefact perspective avoids both extremes. Software can block, route and record while still leaving interpretation, communication and adaptation in the wider routine.

## Implementation continues after launch

Stream 4's lifecycle lens treats go-live as one point in a longer process. The team learns during stabilisation, discovers misfit and adjusts use. Define how that learning reaches design owners.

A proposed operating arrangement might include an intake owner, a source/policy owner, a reviewer role, an execution owner, a service operator and a process owner who reviews end-to-end performance. In a small firm, one person may hold several roles. Keep the responsibilities distinct so changes and failures have an owner.

Stream 3 adds a question about discretion: who can revise the categories and thresholds that guide the workflow? An escalation route that permits only individual exceptions, with no route to challenge a repeatedly bad rule, leaves important design authority unaddressed.

## Actualisation joins the components to the work

The workflow's tools and states are material arrangements with identifiable technical effects. To claim that they help work move between teams, name who does what and under which conditions. Someone must be available to receive the case. They need usable evidence, suitable authority and a way to recover when something fails.

**Actualisation** concerns the actions through which a possibility becomes consequential over time. Installing the planner, training staff once or observing one completed case does not establish that process. Follow repeated cases, including repairs and off-system coordination, and investigate which outcomes emerge for different roles.

A record can help someone trace an event without ensuring that anyone explains it, takes responsibility or corrects a problem. The receipt simulator demonstrates a local acknowledgement pattern; its code cannot establish that an organisational owner investigates a disputed handoff or can enforce a correction.

The [capstone lesson](04-technology-in-practice.md) develops this distinction through an evidence-panel case and compares feature, affordance, constraint, actualisation and outcome. Its framework adapts [Stream 6](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_06_Technology_Materiality_Organisation_Detailed_Review.md) without treating its theoretical perspectives as interchangeable.

## Apply the idea: respond to three breakdowns

Consider three events: the policy service is unavailable; a reviewer rejects a proposal because the category is wrong; and the receiving team says a recorded handoff never reached its working queue. What should happen next in each case, and who should own the unresolved work?

**Worked response:** The first needs a bounded service failure and an owner for pending work, not an invented policy. The second needs correction of the case plus investigation of the label rule if recurrent. The third requires reconciliation between execution receipt and actual receiving workflow. A log line saying “sent” cannot settle it.

What would you measure to judge the whole workflow? Include correct end-to-end completion, waiting, clarification loops, reviewer effort, duplicate actions, abandoned cases and successful recovery. Investigate whose work changed. A decline in account-manager effort may coexist with increased specialist burden.

**Rival explanation:** Apparent adoption failure could reflect an unsuitable interface, a justified control concern, inadequate capacity or distrust created by earlier errors. Treat these as competing explanations requiring evidence rather than labelling employees resistant.

## Build a pilot plan

Create a pilot operating design containing the dependency map, permitted action table, state transitions, evidence requirements, exception/repair owners and evaluation plan. Show how staff can contest a result and how a revised policy reaches the application. State which parts were simulated and which, if any, were tested in real work.

The result is a practical brief for an AI pilot. Its value is the connection between mechanism and organisational judgement: what the system does, what work remains and what evidence would justify expanding its scope.

**Research basis:** The [six-stream foundation](../../reference/literature-guide.md), especially dependency management, configurational fit, decision premises, implementation over time and the artefact/practice distinction. These concepts guide the fictional design; the curriculum claims no empirical AI implementation outcomes.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.
