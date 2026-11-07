# Lesson 2.3: Who decides when the assistant can act?

[Download the matching notebook](/downloads/02-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Business context: Harbour

Drafting an explanation and authorising a replacement or credit belong to different business decisions.

[Company and supply-chain context](../../HARBOUR.md) · [Module 2 business situation](../../reference/harbour-learning-journey.md#module-2)

## The proposal

**Fictional case.** Harbour's assistant can retrieve quantities and draft a response. The founder now proposes “one-click resolution”: the assistant recommends a credit and finance clicks approve. Management calls this human control.

Suppose the assistant also selects which records finance sees, assigns the complaint category and calculates an eligibility score. The approver retains the final button, but the system has already shaped what they see and consider. To understand who controls the decision, look at those earlier choices too.

## Who sets the starting points for a decision?

People cannot inspect every fact or compare every possible action before deciding. Simon calls these limits **bounded rationality**. Organisations help by setting goals, deciding which information matters and defining options and rules. These starting points are **decision premises**. Research chapter 3 explains why they matter: whoever sets them can shape many later decisions.

In our case, “short delivery”, “verified shortage” and “goodwill credit” are different categories. A classification can determine which evidence is requested and which response is considered legitimate. Even a screen default can influence which alternatives receive attention.

An AI recommendation is therefore partly a presentation of premises. Ask who selected its input fields, examples, thresholds and evaluation criteria. The visible approver may not be the actor with the greatest influence over those choices.

## Separate the acts

Consider a five-step chain. The application retrieves two quantities. It calculates a difference. The assistant recommends a credit. An authorised manager approves it. The finance system issues it.

Retrieval provides information. Subtraction performs calculation. Recommendation proposes an option. Authorisation grants permission. Execution changes the business state. Depending on the organisational arrangement, a decision may occur when the option is selected or when a commitment is made. Do not collapse the entire chain into “the AI decided”.

The distinction also improves accountability. If the quantities were wrong, investigate the records. If the eligibility rule was unsuitable, investigate the premise. If an approved credit was issued twice, investigate execution and recovery. A single blame category called “AI error” hides the work needed to repair the system.

## Permission and practical authority

The review distinguishes formal rights from actual influence and discusses authority as a relationship involving acceptance. A technical permission can show what a role is allowed to do in a system. It cannot establish whether that person has the information, expertise, time or organisational standing to challenge a recommendation.

The executive lesson is to design a review task, not just an approval control. What evidence should the reviewer inspect? What disagreement can they record? Where does a disputed case go? Who can change a bad rule discovered repeatedly?

This transfer is interpretive. We are not claiming that every AI system removes reviewer discretion. We are asking where the room to exercise judgement, called **discretion**, could move, and what evidence would reveal that change.

## Coordination depends on more than a shared answer

Research chapter 2, drawing on Okhuysen and Bechky, separates a mechanism from the conditions it may support: accountability, predictability and common understanding. The assistant's shared case summary is a mechanism. It may clarify responsibility or next steps. Finance and account management may still understand “customer resolved” differently.

If account management wants to preserve the relationship and finance wants stronger proof before credit, a perfectly readable summary does not remove the conflict. Carlile's knowledge-boundary lens suggests that the problem may involve different meanings and interests, requiring translation and negotiation. Generating a compromise sentence is not the same as reaching an authorised agreement.

## Tool access is a condition, not a complete review capability

The dispatcher in Lesson 2.2 can establish whether an order ID is in a permitted set. That is an inspectable code check. It does not establish that the reviewer understands the order, has time to investigate it or can change a flawed recommendation.

Research chapter 6 uses **affordance** for something a particular person could do with a system under particular conditions. The same approval screen may enable a trained reviewer to challenge a credit while functioning as a routine confirmation step for someone with no source access. Actual use needs investigation rather than inference from the button.

A constraint can also serve different goals. Requiring approval blocks rapid execution but may enable an appropriate review boundary. Whether it produces useful control or an unattended queue depends on the working arrangement. Do not equate fewer clicks with better authority design.

Now suppose one reviewer lacks source access and another has only seconds per case. Which changes to the system, staffing or authority would make review workable? [Research chapter 6](../../reference/research/06-technology-in-practice.md) supports this diagnostic; it does not prove any particular review outcome.

## Apply the idea

How would you redesign the one-click proposal? Specify the evidence an approver sees, the actions allowed before approval, who handles exceptions and how a disputed category can be changed.

**A defensible design:** The assistant can read permitted records and draft a recommendation with evidence references. A deterministic check verifies required fields. Finance reviews the evidence and selects an outcome, including “insufficient information”. A separate execution tool accepts a valid approval record. Disputed eligibility rules go to the policy owner rather than being repeatedly improvised by individual reviewers.

**A plausible alternative:** For a low-value, narrow category, the organisation could authorise automatic execution under explicit criteria and limits. That is a different allocation of authority. It should be approved, tested and monitored as such, rather than disguised as a human-controlled system.

Assess correct resolution, review effort, disagreement handling and duplicate effects. If approvals are nearly automatic, investigate whether the recommendations are excellent, the task is simple or review has become ceremonial. The approval rate alone cannot distinguish these explanations.

**Try it:** Create an action/authority table with separate rows for information, calculation, recommendation, authorisation and execution.

**Research basis:** [Research chapter 3](../../reference/research/03-decisions.md), particularly premises, authority and discretion; [Research chapter 2](../../reference/research/02-coordination.md), particularly conditions and knowledge boundaries. See [transfer limits](../../reference/literature-guide.md).

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A technical entitlement does not by itself establish an organisational mandate. The research chapter explains [permission and authority](../../reference/research/03-decisions.md#permission-and-authority).

## Practical activity: Distinguish a read, a proposed remedy and permission to decide.





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

Which role in this fictional arrangement holds the decide right?

```python
rights = {"investigator":{"read","draft"},"manager":{"read","draft","decide"}}
assert "decide" not in rights["investigator"]
assert "decide" in rights["manager"]
print(rights)
```

The manager holds the stated right. A model writing manager in its output does not acquire that role.

### Complete the exercise

Write the prediction before consulting the worked answer: Which role in this fictional arrangement holds the decide right?

**Worked answer.** The manager holds the stated right. A model writing manager in its output does not acquire that role.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

A Harbour adviser may discuss several customer deliveries in one session. A follow-up such as “who should review it?” must retain the selected case and the adviser’s actual access scope. A coherent answer about the wrong order can send work to the wrong team or disclose another region’s information.

**Task:** Specify what a continuing conversation remembers, which lookups it permits and how a proposed action becomes an accepted next step.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Keep case selection in explicit state and derive access from the signed-in identity. Permit source reads and drafts separately from decisions. Retain an accepted recipient and return incomplete contributions rather than treating every chat response as completed work.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
