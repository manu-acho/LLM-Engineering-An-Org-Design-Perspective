# Workbook: understand the mechanism, apply the idea

[Guide index](README.md) · [Start here](START-HERE.md)

Reading an explanation is one step. Trying to explain a result, change an example or choose between two designs reveals what you understand and what needs another look.

Use this workbook alongside the modules. Work with the fictional Harbour case or an invented situation of your own. You can complete the exercises on paper. Running code is optional unless you choose to investigate an implementation in more depth.

## A useful rhythm for each module

1. **Explain:** describe one idea in ordinary language, with an example.
2. **Trace:** follow one input through the code. Predict the output before reading the explanation or running it.
3. **Compare:** consider a simpler design or a different way to organise the work. When would it be preferable?
4. **Apply:** identify who would use the output, what they could do with it and what might still go wrong.
5. **Check:** separate what the example demonstrates from what would require evidence in real work.

Keep the first attempt. Revising an explanation after noticing a mistake is useful evidence of learning.

## An example of a learning record

In Module 1, the small program subtracts ten reported boxes from twelve ordered boxes. It returns two. That calculation does not prove that the warehouse lost two boxes or that a credit should be issued.

A useful record might say: “The program calculates a reported difference and puts it in a draft brief. I can reuse the separation between preparing evidence and generating text. Before using this at work, I would check the records and agree who can resolve a disagreement.”

Notice the three parts: what the code does, which pattern is reusable, and what the organisation still needs to decide.

## Your module record

Use these prompts for a short note rather than trying to write a perfect report.

| Prompt | What to record |
|---|---|
| The idea | Explain one mechanism without copying the lesson's definition |
| The code | Follow inputs, important steps, outputs and possible failures |
| A reusable pattern | Name the pattern and give a small example of where it helps |
| An alternative | Compare a simpler or differently organised approach |
| The work | Identify the problem, the people involved and the information they need |
| The responsibility | State who can recommend, approve, act and handle exceptions |
| The evidence | Record what is known, what is assumed and what would need testing |
| The next decision | Explain whether to proceed, revise, investigate further or stop |

## From an available feature to a useful result

A feature can exist without being useful to everyone. A link to policy may help a reviewer who has access and time to read it. It may do little for someone who cannot open the source or challenge the recommendation.

For the mechanism in each module, ask:

- Who is trying to do what?
- What could the feature help that person do, and under which conditions?
- What might it make harder for someone else?
- What would people actually need to do to make it useful?
- What evidence would show a benefit, and what else might explain that result?

[Lesson 8.4](modules/08-agents/04-technology-in-practice.md) works through these questions in detail. The [literature guide](reference/literature-guide.md) explains the research concepts behind them.

## Practice through Part I

| Module | Try this | What to explain afterwards |
|---|---|---|
| 1 | Trace one source through a brief; test truncation | Explain where missing information first disappears |
| 2 | Draw a lookup and proposal tool sequence | Distinguish model request, permission and execution receipt |
| 3 | Inspect token/model interfaces; design meeting-note evidence links | Explain why probabilities do not establish factual confidence |
| 4 | Compare a reference and optimised algorithm | Correctness outcomes precede the timing result |
| 5 | Label evidence for eight questions before retrieval | Diagnose a failure to a specific stage |
| 6 | Specify labels, splits, baselines and error consequences | Explain why one evaluation is fit for the intended decision |
| 7 | Inspect prompt/completion examples and loss labels | Identify target leakage and train/serve mismatches |
| 8 | Simulate retry, crash and exception scenarios | Show how state and authority prevent duplicate effects |

## Practice through Part II

Use the same module record for the six agent-engineering modules. No external model call is required to investigate the small examples.

| Module | Try this | What to explain afterwards |
|---|---|---|
| 9 | Trace one allowed lookup, a denied lookup and a budget-exhausted loop | A proposed action, executed tool and verified business conclusion differ |
| 10 | Fail one required evidence branch | A coordinator needs a policy for partial results and separate authorisation |
| 11 | Reorder a task and remove an evidence field | Data-contract checks do not establish factual support or reviewer independence |
| 12 | Resume with an old proposal approval | Stored state, matching authority and durable effects require distinct controls |
| 13 | Claim the same task with two workers | A conditional update and a common status meaning solve different problems |
| 14 | Call an undiscovered operation without permission | Discovery does not replace enforcement at execution |

For a complete application, use the [integration plan](modules/14-agent-integration/04-integration-plan.md). Define a bounded problem, compare an alternative, allocate responsibility and state what evidence would justify expanding the system's scope.

## Recurring Harbour Services case

Keep a case notebook with these evolving artifacts:

1. Process evidence brief with sources, uncertainty and interview questions.
2. Assistant authority table: observe / recommend / draft / execute.
3. Deployment comparison and evidence-linked meeting note design.
4. Correctness-first experiment report.
5. Knowledge-source registry and labelled retrieval cases.
6. Task definition, annotation guide and baseline evaluation.
7. Adaptation experiment and artifact manifest.
8. Workflow states, operating responsibilities and recovery plan.

## Authority table template

| Capability | Input/source | Allowed actor/scope | AI authority | Approval/exception owner | Evidence of completion |
|---|---|---|---|---|---|
| Read request status | Approved request system | To define | Observe | To define | Source record/version |
| Draft a handoff | Permitted request and policy | To define | Draft | To define | Draft with source IDs |
| Change assignment | Authoritative workflow system | To define | To decide explicitly | To define | Acknowledged transition ID |

## Experiment report template

**Decision this experiment informs:**

**Task, population and exclusions:**

**Baseline and candidate:**

**Frozen input cases / split version:**

**Correctness and business outcome criteria:**

**Error categories and consequences:**

**Configuration:** Provider/model or artifact revision, prompt, preprocessing, retrieval settings and runtime as relevant.

**Results:** Per-case outcomes, invalid outputs, aggregate metrics, variation, latency/cost and human review effort.

**Limitations:** Sample coverage, label disagreement, known missing sources and differences from operating conditions.

**Interpretation and next decision:**

## Questions to take back to work

- Which aspects of work are formally specified, and which depend on situated judgement?
- Does the proposed system reduce coordination effort or move it to another role?
- Which sources are treated as authoritative, and whose experience becomes less visible?
- How can a worker contest a model's classification or recommendation?
- What changes to roles or workflow would be needed even if no AI were introduced?
- What evidence would distinguish a technical improvement from a useful organisational outcome?

## Model and data manifest template

| Field | Value to record |
|---|---|
| Task and label specification | Version and accountable owner |
| Source/data revision | Stable identifier, collection conditions and exclusions |
| Split construction | Train/validation/test names, grouping and time boundaries |
| Model/tokenizer/adapter | Exact compatible IDs and revisions |
| Input contract | Prompt/template, token budget and preprocessing |
| Output contract | Schema, parser and invalid-output policy |
| Evaluation | Cases, baseline, metrics, observed results and reviewer |
| Operating controls | Access scope, action authority, rollback and monitoring owner |

## Check your understanding

You can explain the mechanism, trace the code without guessing, implement a small variation, justify an alternative and make a bounded business decision from evidence. Completing a notebook or obtaining a fluent answer alone is not enough.

## Build a cumulative application record

Each module's completed design case demonstrates an output before asking for a new application. Read that worked example, then prepare the corresponding record below. Keep assumptions explicit and use fictional data when practising.

The cases vary volume, adoption, effort and cost assumptions to investigate different decisions. They are scenarios rather than one empirical financial history. When combining them into a single proposal, choose one consistent set of assumptions and recalculate the results.

| Module | Technical record | Organisational decision record |
|---|---|---|
| 1 | Request, response and evidence transformation trace | Compare intake, referenced drafting and specialist conversation |
| 2 | Tool schema, checked arguments, call IDs and result round trip | Allocate recommendation, approval and execution; calculate review capacity |
| 3 | Model/template/input/output shape and meeting-note claim trace | Define draft, confirmation, correction and accepted commitment |
| 4 | Frozen cases, confusion counts, failure coverage and timing boundaries | Compare total effort, quality and end-to-end outcomes |
| 5 | Source-to-chunk-to-retrieval-to-answer evidence record | Complete a source registry and conflict-resolution route |
| 6 | Feature representation, fitted predictor and held-out outcomes | Define what a routing label means and who adjudicates it |
| 7 | Masked batch, update history, adapter/base manifest and reload check | Compare specialisation with simpler methods and govern category revision |
| 8 | Service/persistence/queue boundaries and uncertain action state | Complete roles, capacity, recovery and pilot scope |
| 9 | Plan, executed observations, budgets and terminal outcome | Define an honest service promise and accepted intake |
| 10 | Structured contribution, SDK run and trace interpretation | Specify specialist contributions and receiving ownership |
| 11 | Configuration, predecessor context, crew result and acceptance evidence | Justify specialisation against integration cost |
| 12 | State/reducer/checkpoint/interrupt and versioned review | Design waiting, discretion, capacity and recovery work |
| 13 | Common contract, actual invocation differences and stale-result checks | Agree shared meanings, maintenance and acceptance responsibilities |
| 14 | MCP discovery/call/resource path and backend record | Complete a comparative pilot dossier with costs and evidence gates |

Finish by comparing the [completed integration dossier](modules/14-agent-integration/06-design-lab.md) with your record. If a proposed business outcome cannot be connected to a mechanism, role, action and evidence, identify the missing part rather than filling it with an optimistic assertion.
