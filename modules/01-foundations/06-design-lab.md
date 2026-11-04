# Lesson 1.6: Choose how information and work should be connected

[Module route](README.md) · [Next module](../02-conversation/README.md)

## Three plausible designs

**Fictional worked case.** Harbour receives 800 delivery enquiries a month. Staff spend 12 minutes assembling records for each enquiry. Some are straightforward status checks; others contain conflicting evidence. The managing director asks for “an AI summary for every case”. Before accepting that scope, compare three arrangements.

| Arrangement | Work performed | Where judgement remains |
|---|---|---|
| Structured intake and direct lookup | Required order ID, standard fields, displayed source records | Staff interpret unusual language and conflicts |
| Referenced AI brief | Model drafts a summary from permitted records | Reviewer checks material claims and chooses next action |
| Specialist case conversation | Relevant people clarify discrepancies together | Participants negotiate meaning and accepted responsibility |

The options can coexist. A standard lookup may suit ordinary enquiries, a draft may help long free-text complaints, and a reciprocal conversation may remain necessary for disputed facts.

## Diagnose the dependency before selecting the tool

Thompson distinguishes pooled, sequential and reciprocal interdependence in the [organisation design review](../../reference/literature-guide.md). Shared use of a policy service creates a pooled dependence on its availability. Passing a prepared case to operations is sequential. Repeatedly revising an account with the warehouse is reciprocal. A summary helps transfer information; it does not automatically provide the mutual adjustment required by the third situation.

Mintzberg's coordination mechanisms sharpen the alternatives. Standardisation can define the minimum evidence for routine work. Direct supervision can settle responsibility in a particular exception. Mutual adjustment lets specialists work through an uncertain case. These are broad organising mechanisms, not three features that one chatbot must contain.

Galbraith offers another design choice: reduce information-processing demand or increase capacity. Clear intake requirements reduce repeated clarification. A referenced brief increases capacity to handle information already gathered. If enquiry quality is poor, combining both may be more coherent than making the summary longer.

## Work through the economics

Suppose 300 monthly cases contain long descriptions and are eligible for the draft. Actual use reaches 70%, or 210 cases. Preparation falls from 12 to 7 minutes, but checking the draft takes two additional minutes. Net saving is three minutes per used case: 630 minutes, or 10.5 hours a month.

At an illustrative labour cost of £30 per hour, the capacity value is £315. If monthly inference, maintenance and support total £180, the difference is £135 before implementation cost. This is a scenario calculation. It does not mean £135 appears in the bank: staff may use the time for additional work, shorter queues or better service.

If review takes five additional minutes, the net time saving disappears. If staff use the system only on easy cases already taking five minutes, the original comparison is wrong. Investigate actual eligible cases and effort rather than multiplying a demonstration's saving by the whole organisation's volume.

## Make the configuration coherent

The chosen pilot targets long, non-urgent complaints. An intake owner ensures the order ID is available. A policy owner maintains current sources. The reviewer can open the passages and correct a misleading claim. Operations accepts or rejects the handoff against an agreed minimum-evidence standard. A process owner checks whether unresolved cases move faster across the whole service.

This connects roles, information, controls and capacity. Giving the reviewer responsibility without source access would make the configuration inconsistent. Rewarding account managers solely for fast submission could encourage incomplete drafts. Incentives belong in the design alongside the prompt.

## A complete first decision

Harbour selects a four-week referenced-brief pilot for the 300-case population, with a structured-intake comparator. It records preparation, review, clarification and elapsed resolution time, plus unsupported claims. Staff retain the right to use a specialist conversation for reciprocal exceptions. The organisation will expand only if quality is maintained and useful capacity or service improvement is observed.

**Try the decision yourself:** Suppose preparation improves but warehouse waiting does not. Should Harbour grant the assistant more autonomy? A reasoned answer first investigates the missing dependency. More autonomy is justified only if the assistant can perform a specific permitted contribution that addresses it. A faster summary alone does not establish that case.

**Research basis:** The [organisation design](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_01_Organisation_Design_Detailed_Review.md) and [coordination](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_02_Coordination_Theory_Detailed_Review.md) reviews inform this application. The figures and decision are teaching assumptions.
