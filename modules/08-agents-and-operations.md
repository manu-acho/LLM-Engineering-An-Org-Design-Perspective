# Module 8: Agents, coordination and operations

[Previous module](07-fine-tuning-and-qlora.md) · [Guide index](../README.md)

## What you should be able to do

Trace the capstone's scanner, estimators, planner, notifications and UI; distinguish deterministic orchestration from model-selected sequencing; understand service loading and durable state; and design an accountable workflow with bounded authority.

**Course walkthrough:** [day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/day1.ipynb), [day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/day2.ipynb), [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/day3.ipynb), [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/day4.ipynb), [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/day5.ipynb), [framework](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/deal_agent_framework.py), [UI](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/price_is_right.py), [fixed planner](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/planning_agent.py), [autonomous planner](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/autonomous_planning_agent.py), [ensemble](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/ensemble_agent.py), and [remote model service](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/pricer_service2.py).

## 1. Concepts: autonomy is a design variable

An agent system combines observations, state, model decisions and executable actions. Inspect what actually chooses the next step. A collection of classes called “agents” may still follow a completely predetermined workflow.

The local capstone has both forms. `PlanningAgent` implements a fixed sequence in Python. `AutonomousPlanningAgent` exposes tools and lets the model request their sequence. The default framework instantiates `PlanningAgent`, so the final local application does not automatically use the autonomous planner merely because that class exists.

More autonomy can accommodate variable tasks, but introduces additional paths to evaluate and supervise. For a stable business process, an explicit workflow can provide the required flexibility with fewer failure modes.

**Durable state** records what happened across runs. It differs from a model's current context and from learned parameters. **Idempotency** means that retrying an operation with the same identity does not repeat its business effect. This matters when actions send messages or change records.

Deployment also changes the problem. A model that works in a notebook must be loaded, served, monitored and updated under real latency, availability and cost constraints. Code packaging is only one part of that operating system.

## 2. What the code does

### Day 1: make a specialised model available remotely

The Modal service specifies an image, libraries, secrets, a GPU, timeout and a persistent model cache. Decorators register class lifecycle and remotely callable methods. `setup` loads the base model/tokenizer and attaches the pinned adapter once per container rather than per prediction.

`SpecialistAgent` finds the named deployed class, creates a handle, and calls `self.pricer.price.remote(description)`. This looks like a method call but crosses a service boundary. Network failure, remote exceptions and cold-start delay belong in the design.

`MIN_CONTAINERS = 0` permits scale-down in the shown configuration; the first request may need model loading. Keeping capacity warm trades ongoing resource use for responsiveness. Treat exact platform settings as snapshot code and verify against the service version before deployment.

### Day 2: retrieve analogues and combine predictions

`FrontierAgent.find_similars` embeds a product description and retrieves five similar products with known prices. `messages_for` inserts them as examples before requesting an estimate. This is RAG applied to prediction rather than policy question answering.

`EnsembleAgent.price` first normalises the description, then obtains specialist, frontier and neural-network predictions. The inspected combination is **hard-coded**: `0.8 × frontier + 0.1 × specialist + 0.1 × neural_network`. Its docstring describes learned regression weights, but the implementation does not fit them there. Read executable expressions when comments and code diverge.

An ensemble is useful when its components contribute complementary signal. Three correlated estimators can share the same error. Measure improvement over the best single estimator before accepting the extra cost and failure dependencies. The current calls are sequential; parallelising independent estimators could reduce latency but requires timeouts, concurrency control and a missing-result policy.

### Day 3: scan and notify

`ScrapedDeal.fetch` reads RSS entries and their pages. It extracts descriptions and truncates fields. HTML selectors and public page formats are external dependencies; a missing element should become an extraction failure rather than a fabricated deal.

`ScannerAgent` excludes already-recorded URLs, asks a model to select described deals with clear prices, and parses structured records. Schema compliance does not prove the extracted price was the actual price rather than an advertised discount. Retain source evidence and validate numeric constraints.

`MessagingAgent.alert` formats a notification deterministically. `notify` instead asks a model to write the message before sending it. `push` posts to an external notification API; the shown implementation does not check the returned HTTP status. A log saying the method ran is not proof of delivery.

### Day 4: compare the two planners

The fixed planner scans, estimates up to five deals, sorts by estimated saving and sends an alert if the best exceeds its threshold. That threshold is explicit executable policy.

The autonomous planner supplies tools for scanning, estimating and notifying. It repeatedly calls the model until the model stops requesting tools. `handle_tool_call` maps names to functions and expands parsed arguments with `**arguments`.

This alternative needs an explicit step/time/cost limit. It also accepts an estimated value as a notification argument supplied by the model, rather than requiring a trusted estimate record ID. A stronger design would look up the stored estimate, compute the threshold in code and enforce the notification policy at the execution boundary.

The instance guard `self.opportunity` prevents a second notification within one planner run after success, but is not durable duplicate protection across crashes or concurrent runs. The method can also return “Notification sent ok” when it ignored a repeated request, making its status less informative than it appears.

### Day 5: persist results and display ongoing work

`DealAgentFramework` lazily initializes the fixed planner, loads prior opportunities from JSON, runs the planner and appends a returned opportunity to disk. This memory tracks surfaced opportunities, not every URL ever scanned. That distinction affects repeat processing.

The UI starts work in a thread and sends logs/results through queues. A generator polls those queues and yields interface updates. If the worker raises before posting a result, the consumer can keep waiting. A robust implementation would send a terminal success/error event in all cases and use cancellation/timeouts.

The JSON memory file is suitable for a single-user demonstration. Concurrent writers, interrupted writes and durable deduplication call for a more appropriate transactional store. Console-style agent logs are useful debugging output, but a business audit trail additionally needs record IDs, authorised actor, input/source versions, decision, action and outcome.

## 3. Learn the coordination pattern

**Teaching example: dependency-free, dry-run workflow with no external effects:**

```python
def propose_escalations(requests, classify, seen_ids):
    proposals = []
    for request in requests:
        if request["id"] in seen_ids:
            continue
        label = classify(request["text"])
        if label == "exception":
            proposals.append({
                "request_id": request["id"],
                "action": "propose_specialist_review",
                "status": "awaiting_owner_review",
            })
    return proposals

def simple_classifier(text):
    return "exception" if "exception" in text.lower() else "routine"

proposals = propose_escalations(
    [{"id": "R-1", "text": "Exception needs review"}],
    simple_classifier,
    seen_ids=set(),
)
```

The workflow fixes the sequence; classification supplies a bounded judgement; the result is a proposal. It deliberately does not mark an action complete or send a message. Completion state should follow an acknowledged business effect, not the mere creation of a draft.

For a real worker, represent lifecycle states explicitly, for example `received → evidence_ready → proposed → approved → executed`, with `failed` and `cancelled` transitions. Each transition should record who or what authorised it. A queue delivers work; a state store records what is true about that work.

Patterns include **composition of specialised services**, **lazy initialization**, **strategy replacement**, **remote procedure calls**, **durable state**, **producer/consumer queues**, **bounded loops**, and **idempotent action handling**. Python's [task and cancellation documentation](https://docs.python.org/3/library/asyncio-task.html) offers another concurrency model; async tasks are an alternative to threads for suitable I/O libraries, not a guarantee of faster CPU computation.

## 4. Alternatives and operating decisions

| Design | Best reason to choose it | Main evaluation burden |
|---|---|---|
| Fixed Python pipeline | Sequence and policy are stable | Each stage and its failure paths |
| Explicit state machine | Pauses, approvals, retries and resumability matter | Valid transitions and durable recovery |
| Model-selected tool loop | Next steps genuinely depend on varied language/context | Action selection, termination and policy enforcement |
| Multi-estimator ensemble | Complementary predictions improve measured outcomes | Added cost, correlation and partial failures |
| Single capable model | A simpler baseline meets the objective | Coverage and reliability on the actual task |

Ask whether added agents correspond to useful separations of capability, authority or evidence. More named agents alone do not produce organisational robustness. Shared bad inputs can still propagate through every component.

## 5. Business application and organisation design

For Harbour, use a workflow that reads a request, gathers permitted policy/status evidence, drafts a classification and handoff, and routes exceptions to an accountable owner. Keep commitments, record changes and outbound communication behind explicit authority rules.

Start by investigating the work and its dependencies. Agree who may observe, recommend, authorise and execute. Connect the approved systems, then test the workflow under realistic operating conditions. This is a proposed delivery approach, not a claim about a real implementation.

Oversight must be practical. Specify who monitors unresolved work, how overrides are recorded, what triggers rollback and who can change the action policy. “Human in the loop” only helps when that person has time, evidence and authority to intervene.

Measure end-to-end correct completion, time to resolution, handoff quality, duplicate actions, intervention rate, abandoned work and recovery time. Also examine whether the system shifts hidden review work to another team. A locally faster assistant can worsen the process if downstream specialists receive more incomplete requests.

## 6. Experiment, diagnose and reflect

**Exercise:** Design Harbour's workflow as five states and an exception route. Simulate a missing record, contradictory policies, a repeated request ID, a failed notification and a crash after execution but before acknowledgement. Explain how the system knows whether retrying would repeat an effect.

Compare a fixed workflow with a model-selected planner on the same synthetic cases. Score correct outcomes, unnecessary calls, policy violations and recovery effort. Give the autonomous version a step limit and permit only dry-run proposal tools during evaluation.

**Common failures:** mistaking the autonomous class for the default planner; treating hard-coded ensemble weights as learned; trusting a parsed estimate as authoritative; repeating side effects after retry; logging success before checking delivery; UI polling with no terminal error event.

**Check your understanding:** Where is authority enforced? What does memory actually contain? Which failures can be retried safely? When would a state machine be preferable to an autonomous loop?

**Answer cues:** at action execution with trusted identity/state and policy; only the records actually persisted; retry safety depends on idempotency and acknowledgement; use explicit states for stable processes requiring approvals and recovery.

**Decision note:** Produce an operating design with sources, roles, state transitions, action permissions, recovery paths, evaluation gates and an owner for post-launch change.
