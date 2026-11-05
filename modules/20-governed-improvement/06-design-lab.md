# Lesson 20.6: Complete a defensible service decision

[Download the matching notebook](/downloads/20-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Research chapter](../../reference/research/05-routines.md)

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

## Run the cumulative service slice

The capstone implementation is `src/ai_orgdesign/capstone.py`. It retrieves permitted current policy, accepts a source-labelled contribution, opens the authenticated application, records a simulated return-for-evidence decision, retries the same command and applies the declared improvement gate. The contribution and manager action are scripted. The evaluation figures are illustrative. No model decides the remedy.

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
