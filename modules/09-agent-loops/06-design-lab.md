# Lesson 9.6: Design the front door and the promise behind it

[Module route](README.md) · [Next module](../10-agent-orchestration/README.md)

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

This connects Thompson's interdependence with the mechanisms discussed in the [organisation design review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_01_Organisation_Design_Detailed_Review.md). Standardisation helps routine flow; mutual adjustment becomes valuable when participants must revise their contributions together.

## Work through an operating day

On Monday the assistant prepares 80 cases. Fifty meet minimum evidence requirements and are accepted. Twenty need clarification and ten fail because the order system is unavailable. The dashboard should not report 80 resolved enquiries. It should show 50 accepted submissions, 20 awaiting customer information and ten pending service recovery.

The intake owner reviews the clarification queue. The operator investigates the outage. The receiving team owns the accepted contribution, while overall customer ownership remains explicit. Each outcome has a next action and role.

If the assistant increases accepted intake beyond receiving capacity, Harbour limits scope or changes staffing and allocation. It does not interpret every growing queue as an invitation to automate more judgement.

## Examine possibilities for different people

For a customer with an order reference, the assistant may enable out-of-hours submission. For a customer without one, the same mandatory field may block legitimate access. A documented alternative route preserves the service purpose. For intake staff, a referenced draft may enable preparation only if they can correct it and reach a responsible specialist.

These are actor-specific possibilities to investigate, drawing on the [technology and organisation review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_06_Technology_Materiality_Organisation_Detailed_Review.md). Availability of a chat window is not evidence that these possibilities are realised.

**Worked decision:** Harbour should initially measure accepted submission, clarification burden, customer effort and progress after handoff. Conversation volume is a usage measure. The service promise determines which outcomes matter.
