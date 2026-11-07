# Lesson 9.3: Design the work before delegating the next step

[Download the matching notebook](/downloads/09-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Business context: Harbour

Assign responsibility when a tool fails or an agent stops without sufficient evidence.

[Company and supply-chain context](../../HARBOUR.md) · [Module 9 business situation](../../reference/harbour-learning-journey.md#module-9)

## The assistant starts acting like the front door

**Fictional case.** Harbour puts its new investigating assistant on the customer-service portal. It can ask follow-up questions, collect contact details and record unresolved issues. Managers hope the service team will receive clearer cases. After a month, staff report that customers believe a recorded complaint is already being investigated.

The application has acquired a place in the workflow, whether or not anyone called it a new role. What it asks, records and promises shapes the work that arrives next. A polished conversation can create an expectation that nobody has agreed to fulfil.

## Decision premises enter before a recommendation

Simon's decision-premise perspective, developed in the [decision-theory review](../../reference/research/03-decisions.md), asks which facts, categories and alternatives shape a later choice. The portal decides which questions to ask and which tools to call. It may classify a report as a shortage rather than a damaged delivery, shaping the evidence that the next team sees.

The explicit registry in the workshop helps identify one boundary: the application can look up an order but cannot issue a credit. That boundary is necessary but incomplete. The wording of the final draft can still imply that compensation is coming. A system can shape a commitment without possessing an execution tool.

Define separate permissions to collect a report, ask for evidence, recommend an action and make a commitment. Check the customer-facing wording against those distinctions. “Your concern has been recorded” must not silently become “we have accepted responsibility”.

## A handoff needs a receiving arrangement

The [coordination review](../../reference/research/02-coordination.md) starts with dependencies. Customer intake supplies something another activity needs. Who receives the issue? In what form? By when? What happens if the warehouse record conflicts with the customer's account?

Adding an uncertainty log is not enough. Someone needs to read it, distinguish urgent cases, request missing evidence and communicate a next step. Otherwise the assistant has moved work into a quieter queue rather than resolved a coordination problem.

Okhuysen and Bechky's distinctions help separate the mechanism from what it supports. A case number can help make responsibility visible. A response-time commitment can support predictability. A shared case summary may support common understanding. None of these conditions follows automatically from the existence of a chatbot.

## Representation is not accepted authority

The course's digital twin makes an especially useful example. A model receives information about a person and speaks in a configured style. In an organisation, the same pattern could create a procurement assistant described as “our purchasing manager”.

The name and voice do not confer that manager's authority. A supplier may nevertheless interpret an answer as a commitment. Agree how the assistant identifies its role, which claims it can make, and which requests must reach a person. This is a design of representation and responsibility as well as a prompt-writing task.

The lesson is not that assistants should be impersonal or unhelpful. It is that the interface should make its practical role understandable. A customer needs to know whether they are obtaining information, submitting evidence, receiving a recommendation or securing an authorised decision.

## A checklist can hide the work that matters

The [routines review](../../reference/research/05-routines.md) separates artefacts from people's understandings and actual performances. A checklist is an artefact. An employee may understand “investigate” to include a call to the warehouse supervisor. The system may mark the item complete after retrieving a database row.

Compare those meanings before measuring completion rates. If staff repair the assistant's cases through calls and spreadsheets, include that effort in the assessment. A cleaner portal can coexist with more difficult work for the receiving team.

## Who can use the new information?

The [technology-and-organisation review](../../reference/research/06-technology-in-practice.md) adds an actor-specific question. The brief may enable an operations specialist to compare records if they have source access, time and a correction route. The same brief may only enable a customer-service adviser to notice that a specialist is needed.

These are different possibilities, or **affordances**, of the same output. The code establishes that a lookup result was returned. Evidence of actual work is needed to establish that a particular person could use it, did use it and produced a useful result.

## Apply the idea

Suppose the portal's completion rate is 90%, but unresolved issues wait three days and staff often contact customers again for information already mentioned in the chat. Would you expand the agent's tools or investigate the receiving process first?

A useful response traces one case from the conversation to accepted ownership. Perhaps the conversation is sound but the export loses the transcript reference. Perhaps the receiving team lacks capacity. Perhaps the completion label counts “draft produced” as “case resolved”. Each explanation points to a different intervention.

A simpler alternative may be a structured intake form plus a supported summarisation step. The agent loop earns its place when adapting questions improves evidence collection enough to justify the extra variability.

**Try it:** Write a service promise for the assistant in three sentences. State what it can do, what a recorded case means and who owns the next step. Then identify one code check, one operating arrangement and one outcome measure needed to support that promise.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Delegation needs an account of what work is allocated and how it rejoins the wider service. The research chapter explains [division and integration](../../reference/research/01-organisation-design.md#division-creates-a-need-for-integration).

## Practical activity: Keep application permission checks independent of planner instructions.





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

Does a model saying the request is authorised change the tenant check?

```python
from ai_orgdesign.agent_loop import execute
try:
    execute("lookup_case",{"case_id":"H-18"},"north")
except PermissionError:
    print("Cross-scope read denied")
else:
    raise AssertionError("The scope boundary failed")
```

No. Trusted identity and application policy determine scope.

### Complete the exercise

Write the prediction before consulting the worked answer: Does a model saying the request is authorised change the tenant check?

**Worked answer.** No. Trusted identity and application policy determine scope.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

### Programming practice

Write allowed(name) for an explicit read-only tool allowlist.

Start with the placeholder in the notebook, then compare with this worked solution. The contrasting checks are part of understanding the contract.

```python
def allowed(name):
    return name in {"lookup_case","search_policy"}

assert allowed("lookup_case") is True
assert allowed("approve_payment") is False
```

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

An investigator may need several lookups before understanding a complaint. An agent loop could choose which permitted lookup to request next, but repeated requests can consume time and cost while leaving the original delivery unresolved. The company must define both capability and stopping conditions.

**Task:** Write an agent mandate with allowed reads, limits, evidence requirements and an accountable recipient at termination.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Allow selected case and policy reads, reject unknown capabilities and stop within the declared budget. Return evidence and unresolved questions to the investigator. Do not grant credit, payment or replacement authority because the model requests it.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
