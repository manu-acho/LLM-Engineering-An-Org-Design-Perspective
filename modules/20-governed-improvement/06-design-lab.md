# Lesson 20.6: Complete a defensible service decision

[Download the matching notebook](/downloads/20-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Research chapter](../../reference/research/05-routines.md)

## Business context: Harbour

The final decision brings together three questions: did the program perform the agreed task, can Harbour operate it when things go wrong, and does it help the customer get a better resolution? Use a difficult case to test each claim. Record what the available evidence supports and what still needs checking before a wider release.

Defend the end-to-end Harbour design, including supply-chain dependencies, finance boundaries, failure handling and evidence still needed.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## Prepare the decision record

The fictional Harbour case is an opportunity to connect an executable pattern with the organisation around it. The technical walkthrough supplies the mechanism. This exercise asks what contribution should be accepted, by whom and under which conditions.

Write a one-page decision record with a stated population and exclusions, the proposed contribution, authoritative sources, the people or services involved, acceptance conditions, refusal conditions, recovery and a comparison against an alternative. Keep unsupported assumptions visible. Do not fill a missing business rule by quietly turning a convenient software default into policy.

## Work the difficult case first

Suppose an improver repeatedly tests candidates against the same held-out cases. Explain why those cases eventually stop functioning as an independent test, even if their filenames never change.

Before running a variation, predict the result and its business implication. An exception is not necessarily a defect: denying a forbidden read or rejecting a stale approval can be the intended behaviour. Explain which distinction matters in this case.

**Worked reasoning.** Selection decisions convey information about the test set. Repeated optimisation against its scores can overfit the selection process without directly displaying labels. Keep separate development and final confirmation sets, restrict evaluation access, record the number of selection rounds and use a new representative comparison when scope changes. Human approval should examine the experiment design as well as the displayed score.

## Separate the technical claim from the service claim

The illustrative candidate is blocked without approval and passes the stated gate with approval. A candidate with more unsafe decisions is blocked even if its accuracy improves. Different dataset identities raise an error because the comparison is not the declared experiment. Promotion does not establish statistical significance or guarantee future performance.

The code checks support that local claim under the supplied fictional inputs. A service-level claim needs a defined comparison population, an observation period, a reference process and evidence about the surrounding work. Record failed and referred cases as well as successful ones. Omitting them can change both the denominator and the apparent benefit.

## Worked choice among alternatives

A fixed, periodically reviewed configuration may be safer and cheaper than automatic proposal generation. An improver can suggest changes without holding promotion authority. Versioning and rollback preserve a recovery route, but cannot undo every external consequence already caused by a released version.

A defensible decision can retain the simpler alternative, narrow the contribution, request more evidence or authorise a bounded pilot. It need not select the most technically elaborate arrangement. The reason should connect observed difficulties with an intervention that can plausibly address them.

## Check the completed explanation

A strong response defines unfamiliar terms, names the relevant owner rather than a vague human-in-the-loop, explains what the code establishes and identifies at least one rival explanation for a favourable result. It should also state what new evidence could change the decision. The linked research chapter supplies the theoretical argument and scholarly references; the case here is an application, not a finding from that literature.

## An offline illustration before the measured capstone

The offline `run()` illustration is in `src/ai_orgdesign/capstone.py`. The practical extension below uses `run_live()` with actual generated drafts and calculated evaluation results. It retrieves permitted current policy, accepts a source-labelled contribution, opens the authenticated application, records a simulated return-for-evidence decision, retries the same command and applies the declared improvement gate. The contribution and manager action are scripted. The evaluation figures are illustrative. No model decides the remedy.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from ai_orgdesign.capstone import run

with TemporaryDirectory() as folder:
    result = run(Path(folder) / "capstone.db")
    assert result["decision"]["status"] == "returned"
    assert result["replay_equal"]
    print(result)
```

Read the boundary field in the result before interpreting it. The integrated local example checks that its supplied components connect under the stated conditions. It does not show a real employee accepting a handoff, a live model supporting a claim, a payment happening or a released configuration improving an organisation.

**Worked final proposal.** Harbour can use the service to prepare evidence-linked material while investigators retain unresolved facts and managers retain remedy authority. Record owners handle corrections; operations owns the case; the engineering owner handles execution defects. Test with a bounded population and compare manual preparation, a simpler record view and the assisted route. Include evidence completeness, review effort, unsupported conclusions, waiting, reopening and customer outcomes. Expansion depends on those observations, not the mere fact that this capstone ran.

**Extension.** Propose one change to the retrieval corpus or acceptance contract. State its expected benefit and a negative case it could worsen. Run the relevant local checks, retain the baseline and describe a confirmation study. A defensible answer may choose not to release the change.

## Practical activity: Join actual model drafting, HTTP review, retries and measured evaluation.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

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

Does this capstone demonstrate cloud operation or real organisational benefit?

```python
print("The live capstone uses fictional evidence, a simulated reviewer and actual model responses.")
print("The reviewer returns the case for further evidence; no payment capability exists.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from ai_orgdesign.capstone import run_live
    with TemporaryDirectory() as directory:
        result=run_live(gateway,Path(directory)/"capstone.db",action="return")
        print(result)
        assert result["replay_equal"]
        assert result["promotion"]["promote"] is False
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. It verifies an integrated local learning path. The service proposal must identify the additional operating and outcome evidence needed.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Bring the whole business back into view

Use the [final Harbour organisation design review](../../WORKBOOK.md#final-harbour-organisation-design-review) to defend the service beyond its API outputs. Explain the customer need, goods and information flows, finance decision boundary, cross-functional dependencies, capacity, source correction and incident ownership. Compare the proposed arrangement with a simpler alternative and identify a condition under which it should be withdrawn.

A completed capstone run establishes selected local execution behaviour. It does not demonstrate a physical delivery, an account adjustment, customer benefit or adoption of the proposed responsibilities. Retain those distinctions in the final recommendation.

## Defend the proposal using the earlier operational records

Bring three separate teaching artefacts into the proposal: the SC-U1 compatible-quantity check from [Lesson 1.4](../01-standalone-foundations/04-evidence-pipeline.md#check-what-a-quantity-counts-before-subtracting), the SC-M1–SC-M4 comparison from [Lesson 4.4](../04-evaluation/04-measures-and-uncertainty.md#compare-drafting-effort-with-timely-investigation-resolution), and the receiving-team capacity calculation from [Lesson 17.3](../17-durable-volume/03-business-and-organisation.md#calculate-capacity-for-the-receiving-team). They are separate fictional exercises, not new observations or hidden inputs for the live H-17 capstone.

**Worked synthesis.** Refuse to calculate a discrepancy when units or item identity conflict. The constructed service comparison halves preparation effort from sixteen to eight minutes while timely investigation resolution stays at two of four cases. At thirty arrivals and twenty reviews per hour, the simplified review workload still exceeds capacity by ten cases. These observations support investigating evidence compatibility and receiving-team work alongside generation; they do not establish that more agents or more reviewers are necessarily the answer.

Connect that argument to the [remedy follow-through](../08-agents/03-business-and-organisation.md#follow-an-authorised-remedy-into-the-remaining-work). Describe what an accepted draft, a review decision, physical fulfilment and an account adjustment each establish. A candidate with a better model score may still be unsuitable if it creates unmanageable review work or a promise unsupported by stock and transport information.
