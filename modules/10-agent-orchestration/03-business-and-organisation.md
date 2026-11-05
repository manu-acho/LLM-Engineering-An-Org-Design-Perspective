# Lesson 10.3: A software handoff is not accepted ownership

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## The manager agent reports success

**Fictional case.** Harbour's coordinator retrieves evidence and asks a finance specialist to recommend a response. The application records a handoff. Customer service assumes finance now owns the case. Finance regards the specialist as an advisory tool and expects customer service to continue. The customer hears nothing.

Both teams can be acting consistently with their own understanding. The problem is the meaning attached to the transition. A runtime handoff changed the active model configuration. It did not necessarily create an accepted obligation in a human service.

## Begin with the dependency

The [coordination review](../../reference/research/02-coordination.md) encourages us to specify what a receiving activity needs. Finance may need an identified order, an evidence comparison, a policy reference and a record of the customer's request. A free-form summary may omit a required condition even when it is easy to read.

Define the handoff as a contract about information and responsibility. State who submits, who accepts, what counts as usable evidence, when a response is due and where rejected cases go. “Sent to finance” and “accepted by finance” need different statuses if acceptance matters.

This makes an engineering decision visible. Does the main assistant call finance as a helper and retain the case, or transfer an ongoing conversation to a specialist service? The organisational answer should shape the runtime choice rather than being inferred from it afterwards.

## A manager name does not confer management authority

In the [decision-theory review](../../reference/research/03-decisions.md), decision premises and authority are different from merely producing a recommendation. A manager agent can select sources, frame alternatives and choose which specialist output to emphasise. Those are influential choices. It still cannot confer legitimate approval on itself by returning a field called `approved`.

The workshop separates evidence collection from authorisation. In a real organisation, the authorisation rule also has an owner. Who can change the permitted category, the threshold or the list of approvers? Repeated exceptions should reach someone able to revise a bad rule, not only individual reviewers asked to work around it.

Consider a model-based checker that declares an email professional. That may help communication quality. It does not establish that the organisation should make the proposed commitment, contact that recipient or use those records. Quality checks must be connected to the decisions they actually support.

## Parallelism redistributes work and waiting

The [organisation-design review](../../reference/research/01-organisation-design.md) asks whether task division and integration fit together. Running evidence searches in parallel can reduce elapsed collection time. It can also produce more drafts than reviewers can inspect, shifting the bottleneck downstream.

Measure role-specific work as well as service speed. A coordinator that returns in seconds may create several minutes of reconciliation for finance. Duplicate requests can make a receiving team do the same investigation twice. More components are useful only where their contributions and integration costs justify them.

A simpler design might gather two records in code and ask one model to draft a clearly bounded brief. It may be preferable to a manager that decides whether required checks deserve to be performed on each run.

## Design for a missing or disputed result

The [enterprise-systems review](../../reference/research/04-implementation.md) broadens fit beyond feature availability. A technically successful handoff can fit local roles poorly. For example, the assigned reviewer may lack warehouse access, or the proposed response deadline may be impossible for the night shift.

Build the exception path alongside the normal one. If policy retrieval fails, who owns the waiting case? If reviewers disagree, who can resolve the category? If an approval expires, who requests a new review? These arrangements are part of implementation, not cleanup work after a demo.

## Follow use beyond the trace

The [technology-and-organisation review](../../reference/research/06-technology-in-practice.md) distinguishes a possible action from its actualisation. A trace showing a finance specialist was called establishes a software event. To investigate whether the new handoff works, follow accepted cases, rejections, informal clarifications and delayed responses over time.

A reviewer may technically have a challenge button but no time or evidence to use it. The possibility of meaningful review depends on that person's working conditions. Counting approvals without investigating those conditions leaves several explanations open.

## Apply the idea

Harbour reports a 40% reduction in preparation time, but finance rejects a quarter of submissions and customer response time is unchanged. Would you add a better manager model, change the required evidence, redesign acceptance or reduce the scope of the service?

A defensible answer first identifies why cases are rejected and whether the comparison involved similar cases. An apparent model failure might be a missing source reference. An apparent adoption failure might be a legitimate refusal to accept unsupported work. The intervention follows the diagnosis.

**Try it:** Draw five statuses: evidence pending, draft ready, submitted, accepted and resolved. For each transition, name the responsible role, required evidence and confirmation record. Mark where the coordinator remains accountable for following up, even if another agent has produced an answer.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Routing makes assignment visible without establishing accepted ownership. The research chapter explains [mechanisms and conditions](../../reference/research/02-coordination.md#mechanisms-and-conditions).
