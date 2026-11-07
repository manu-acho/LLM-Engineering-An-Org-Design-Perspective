# Lesson 9.6: Design the front door and the promise behind it

[Download the matching notebook](/downloads/09-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../10-agent-orchestration/README.md)

## Business context: Harbour

Describe the service honestly to a customer without implying that an agent can approve a remedy.

[Company and supply-chain context](../../HARBOUR.md) · [Module 9 business situation](../../reference/harbour-learning-journey.md#module-9)

## The interface creates expectations

**Fictional case.** Harbour's website assistant says “I'll handle your complaint.” Visitors reasonably expect more than a transcript. Internally, the assistant can only collect an order ID, retrieve status and draft a case. The mismatch is organisational: the wording promises a service that the receiving arrangement does not yet supply.

Harbour defines a narrower promise: “I can collect the relevant details, show recorded status and prepare your enquiry for the service team.” The interface reports whether submission was accepted and gives a reference. A failed lookup or submission does not end with a success sentence.

## Separate the automation boundary from ownership

| Contribution | Assistant/app responsibility | Human or service ownership |
|---|---|---|
| Interpret the enquiry | Identify proposed category and missing fields | Intake owner reviews unresolved categories |
| Read evidence | Query permitted records and retain source identity | Source owner maintains record meaning |
| Prepare a case | Produce referenced draft | Case owner remains responsible for customer progress |
| Submit | Use approved route with request identity | Receiving team accepts or rejects work |
| Follow up | Show acknowledged status | Service owner manages overdue cases |

The assistant can support several contributions without becoming an accountable organisational actor. Naming it “case manager” does not allocate a human mandate or create receiving capacity.

## Choose a coordination arrangement

Ordinary enquiries need predictable transfer. Harbour standardises minimum fields and acceptance status. Disputed evidence needs reciprocal adjustment. Those cases enter a specialist conversation while one named case owner retains the customer relationship.

This connects Thompson's interdependence with the mechanisms discussed in the [organisation design review](../../reference/research/01-organisation-design.md). Standardisation helps routine flow; mutual adjustment becomes valuable when participants must revise their contributions together.

## Work through an operating day

On Monday the assistant prepares 80 cases. Fifty meet minimum evidence requirements and are accepted. Twenty need clarification and ten fail because the order system is unavailable. The dashboard should not report 80 resolved enquiries. It should show 50 accepted submissions, 20 awaiting customer information and ten pending service recovery.

The intake owner reviews the clarification queue. The operator investigates the outage. The receiving team owns the accepted contribution, while overall customer ownership remains explicit. Each outcome has a next action and role.

If the assistant increases accepted intake beyond receiving capacity, Harbour limits scope or changes staffing and allocation. It does not interpret every growing queue as an invitation to automate more judgement.

## Examine possibilities for different people

For a customer with an order reference, the assistant may enable out-of-hours submission. For a customer without one, the same mandatory field may block legitimate access. A documented alternative route preserves the service purpose. For intake staff, a referenced draft may enable preparation only if they can correct it and reach a responsible specialist.

These are actor-specific possibilities to investigate, drawing on the [technology and organisation review](../../reference/research/06-technology-in-practice.md). Availability of a chat window is not evidence that these possibilities are realised.

**Worked decision:** Harbour should initially measure accepted submission, clarification burden, customer effort and progress after handoff. Conversation volume is a usage measure. The service promise determines which outcomes matter.

## Read the organisational connection

The intake promise depends on what the receiving activity can actually accept and perform. The research chapter explains [the worked handoff design](../../reference/research/02-coordination.md#a-worked-handoff-design).

## Practical activity: Make the public promise match the permitted contribution.





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

Should this interface promise an approved remedy?

```python
promise = {"can_collect":True,"can_prepare":True,"can_authorise":False}
assert not promise["can_authorise"]
print("The service prepares an investigation for an accountable team.")
```

No. It can state the actual contribution and who owns the next step.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    answer = gateway.generate("Draft a short customer-facing explanation for a service that gathers evidence for an investigator but cannot authorise remedies. Avoid claiming the complaint is resolved.")
    print(answer.text)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: Should this interface promise an approved remedy?

**Worked answer.** No. It can state the actual contribution and who owns the next step.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
