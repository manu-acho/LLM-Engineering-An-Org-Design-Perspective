# Lesson 1.3: A better brief does not automatically produce a better decision

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## The case

**Fictional teaching case.** Harbour's account managers spend time collecting delivery complaints, shipment records and policy extracts for operations. A founder proposes an AI brief: put the relevant material in one place, summarise it and recommend the next check. The demonstration is persuasive. The team hopes to halve handling time.

Before estimating the benefit, follow the work. The account manager hears the customer's account. The warehouse sees a shipment record. Finance controls credits. Operations reconciles contradictory evidence. Each role knows something different, and none necessarily owns the whole response.

The operating problem is therefore partly information preparation and partly the integration of specialised work. The literature helps us keep those problems visible.

## Dividing work and bringing it back together

The [organisation design review](../../reference/literature-guide.md) begins with **differentiation**, dividing work into tasks, roles and units, and **integration**, reconnecting those contributions. Specialisation makes expertise possible. It also creates dependencies.

Thompson distinguishes different ways in which tasks depend on each other. Stream 1 explains these as forms of **interdependence**. A brief passed from account management to operations is a sequential dependency: one task needs the output of another. A disputed delivery can create a reciprocal dependency: the warehouse and account manager must respond to each other, perhaps more than once, before either can finish.

This is a transfer of theory to the fictional case. It does not establish how a particular organisation coordinates. Its practical value is to distinguish two designs. A fixed report may help a straightforward handoff. An unresolved discrepancy may need a conversation between specialists rather than a longer report.

## Information processing includes attention and action

Galbraith asks how organisations handle the information they need to do their work. When people cannot predict what a task will require, they need more information while carrying it out. An organisation can make some tasks more predictable, or improve how people gather, share and interpret information. This is the **information-processing view** of organisation design.

The AI brief potentially increases processing capacity: it gathers material and makes selected points easier to see. It can also reduce apparent uncertainty by omitting qualifications. Those effects look similar if you judge only readability. A concise brief saying “two boxes missing” may be easier to read than “customer reports a two-box difference; shipment completeness is disputed,” but it carries a stronger and less defensible claim.

Assess what the brief makes visible, what it removes and who can correct it. More text and fewer words are both means, not outcomes. The decisive question is whether the relevant actor can understand the situation and act appropriately.

## A representation is not the routine

Stream 5's routines review distinguishes an **artefact**, such as a procedure or software output, from participants' understandings and actual performances. Feldman and Pentland give names to two sides of a routine. The **ostensive aspect** is the understanding people use to describe and guide the work. The **performative aspect** is what particular people do on particular occasions. The formal procedure is a separate artefact: it may influence both, but it is not a complete account of either.

An AI brief is an artefact. A manager's statement that “operations always verifies shortages” is an account of how the work should or usually does proceed. Observing several cases may reveal that account managers sometimes resolve small complaints directly because operations is unavailable. These are different kinds of evidence.

The teaching consequence is simple: do not build exclusively from the formal process description and then claim to have automated the routine. Investigate actual handoffs, exception handling and the informal repair work that makes the formal path usable.

## Make the benefit hypothesis testable

“Halve handling time” needs a defined beginning, end and quality condition. Are we measuring preparation time, elapsed time to a customer answer or time spent across all teams? Does a shorter account-manager task produce extra operations work?

Compare representative cases handled with and without the brief. Record evidence completeness, unsupported claims, clarification requests, time spent by each role and elapsed resolution time. Investigate cases where performance worsens. A generated page count or user satisfaction rating cannot answer the whole question.

There is no claim here that the proposed system will improve those measures. The measures make the proposal assessable.

## Who can act through the brief?

Stream 6 adds an actor-specific question to the information-processing analysis. A **feature** is an inspectable arrangement, such as source labels in a brief. An **affordance** is a possibility for a particular actor to do something through that arrangement under relevant conditions. These are different claims.

For an operations specialist who can open the source records, the brief may enable comparison of customer and warehouse accounts. For an account manager without warehouse access, the same labels may offer little ability to check the discrepancy. A readable brief can exist while meaningful verification remains unavailable.

The material representation matters: removing “customer reports” changes the claim; truncating the evidence can remove an exception. The code's transformation has a precise effect. Whether the resulting brief helps the recipient coordinate work depends on access, interpretation, responsibility and a route to act.

Extend the discussion below by asking who can correct a wrong brief and what happens after correction. Observe actual corrections and downstream responses before claiming the possibility has been realised. This is an application of [Stream 6](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_06_Technology_Materiality_Organisation_Detailed_Review.md), not evidence of a Harbour outcome.

## Apply the idea: where would you start?

Suppose preparation takes 15 minutes, operations waits one day for a warehouse clarification, and finance rejects one in five submissions for missing evidence. What would you investigate before buying a summarisation tool?

**Worked explanation:** The preparation task might be worth improving, but the day-long wait and missing-evidence pattern may dominate. The next questions are which evidence is absent, why it is absent and who can supply it. A mandatory structured field, a different handoff or access to a source record may help more than another paragraph of generated prose. AI may still assist with free-text interpretation once the evidence path is repaired.

**Rival explanation:** If a pilot improves, the gain might come from clearer submission requirements introduced alongside the model. Compare or document that change rather than attributing the entire outcome to generation.

## Try it

Prepare a one-page design brief stating the dependency, the proposed information transformation, its evidence owner, a correction route and an outcome measure. Add a sentence identifying what remains unknown about actual practice.

**Research basis:** [Stream 1](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_01_Organisation_Design_Detailed_Review.md), particularly division/integration and information processing; [Stream 5](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_05_Organisational_Routines_Detailed_Review.md), particularly artefacts, understandings and performances. These links identify the review syntheses used here. They do not imply a new verification of every original study.
