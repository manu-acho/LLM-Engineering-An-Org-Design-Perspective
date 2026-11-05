# Lesson 4.3: Metrics are part of the design of work

[Download the matching notebook](/downloads/04-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Two teams, two successes

**Fictional case.** Harbour pilots an assistant. Account management reports faster drafting. Operations reports more incomplete handoffs. Finance reports unchanged resolution time. Each statement can be true.

Evaluation needs a unit of analysis: an individual task, a whole request, a team or an end-to-end process. A local measure should not silently become a claim about the whole organisation.

## Metrics select attention

Research chapter 3's decision-premise lens explains why a metric is more than a reporting device. A target such as “close the ticket within one hour” selects what deserves attention and what appears satisfactory. If closure can occur before the customer receives a workable answer, the metric can reward a narrow interpretation of completion.

An AI model evaluated on drafting speed will be selected differently from one evaluated on supported commitments and successful handoffs. The evaluator is helping define the task. Ask who can contest that definition and whose costs are missing.

This does not imply that quantitative metrics are useless. It implies that a measure must be connected to a stated purpose, with known exclusions and consequences.

## Does the proposed system fit the rest of the work?

Research chapter 1 examines how the parts of an organisation fit together. This **configurational** view asks whether tasks, roles, information and authority support one another. It gives us a reason to examine more than the new feature. Faster drafting can help if evidence is reliable, reviewers have appropriate capacity and downstream teams can act. The same feature can increase congestion if it produces submissions faster than specialists can inspect them.

Research chapter 4 extends the point to implementation. A system can fit functionality but impose an unsuitable role or control. Strong and Volkoff's misfit domains, explained in that chapter, provide questions about functionality, data, usability, roles, controls and culture. They are a diagnostic lens, not an automatic scorecard that establishes causation.

For the pilot, investigate whether operations receives better evidence, merely more text or a different burden of interpreting uncertain claims. A model upgrade cannot by itself resolve a disputed definition of a complete handoff.

## An evaluation that follows the dependency

Trace one request from receipt to accepted resolution. Record preparation time, review time, clarification loops, waiting and outcome quality. Keep failure cases. Compare cases of similar difficulty and note other changes introduced during the pilot.

The organisational theory does not prescribe one experimental design for every client. It helps identify what the design must explain. If the intervention changes both submission requirements and generation, distinguish their contribution where possible or state that the result concerns the combined package.

Add qualitative investigation when a metric shifts unexpectedly. A lower override rate can mean better recommendations, less reviewer attention or reduced ability to challenge. Interviews and observed review sessions can help distinguish those accounts; the number alone cannot.

## Locate the missing step between feature and result

Research chapter 6 distinguishes an arrangement's existence, an actor's possibility to act through it, the process of realising that possibility and an outcome. A live evidence panel does not establish meaningful review; meaningful review does not by itself establish fewer incorrect credits.

Build the evaluation in layers. Inspect what is configured, establish which roles and procedures are operating, ask how participants perceive the arrangement, observe repeated use, then assess relevant outcomes. These are evidence needs, not a guaranteed linear causal chain. The six-layer framework brings together ideas from several reviews. It is a teaching synthesis, not a model created by one author.

Apply this to the pilot metrics: increased panel use could mean useful checking, confusion requiring repeated openings or extra evidence work. Follow cases and investigate differences rather than assigning one interpretation to the click count.

Add a question to the evaluation plan: who should be able to do what with this system, and what conditions would make that possible? [Research chapter 6](../../reference/research/06-technology-in-practice.md) supplies the conceptual distinction; case evidence must establish the actual process and consequences.

## Apply the idea

Suppose drafting time fell from ten to three minutes, incomplete handoffs rose from 10% to 25%, and customer resolution time stayed at two days. Would you call the pilot a success? What would you need to know before expanding it?

**Worked response:** The evidence supports a local drafting improvement and a deterioration in one handoff-quality measure. It does not support improved end-to-end service. Check whether the cases were comparable and what counted as incomplete, then investigate why more incomplete submissions occurred. The business decision could be to revise input collection and review design before expanding access.

**Rival explanation:** Perhaps the pilot deliberately handled harder cases. Then the raw comparison could be misleading. Compare easy cases with easy cases and difficult ones with similarly difficult cases. This gives a fairer basis for judgement than declaring success or failure from the overall averages.

A project team can use this analysis to agree how the system will be evaluated. Agree the decision, outcomes, quality gates and evidence before the demonstration creates expectations.

**Try it:** Write a one-page evaluation plan with a primary end-to-end outcome, two quality gates, measures of effort for each role, and a way to investigate contradictory results.

**Research basis:** [Research chapter 1](../../reference/research/01-organisation-design.md) on fit and interdependent design; [Research chapter 3](../../reference/research/03-decisions.md) on attention and premises; [Research chapter 4](../../reference/research/04-implementation.md) on fit and outcomes. These chapters develop the research concepts used in the teaching case.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

The metric selects properties to reward and can redirect attention. The research chapter explains [decision premises](../../reference/research/03-decisions.md#decision-premises).

## Practical activity: Locate the work transferred by a faster draft.





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

Which route has the lower total in this invented example?

```python
manual = {"preparation_minutes":12,"review_minutes":3}
assisted = {"preparation_minutes":4,"review_minutes":12}
print("Manual total:", sum(manual.values()))
print("Assisted total:", sum(assisted.values()))
```

manual totals fifteen minutes; assisted totals sixteen. Faster drafting alone does not establish a service improvement.

### Complete the exercise

Write the prediction before consulting the worked answer: Which route has the lower total in this invented example?

**Worked answer.** manual totals fifteen minutes; assisted totals sixteen. Faster drafting alone does not establish a service improvement.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
