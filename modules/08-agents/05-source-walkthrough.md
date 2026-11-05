# Lesson 8.5: Trace the capstone across models, services and stored work

[Module route](README.md) · [Next: complete the operating design](06-design-lab.md)

## Begin where the application begins

The source [DealAgentFramework](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/deal_agent_framework.py) opens a vector collection, loads stored opportunities and leaves the planner uninitialised until needed. `run` initialises it, calls `plan`, appends a returned opportunity and writes memory. That stored memory records surfaced opportunities; it is not a complete ledger of every source ever examined.

Follow one description through [the fixed planner](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/planning_agent.py), scanner, estimator and messenger. The scanner proposes candidate deals. The estimator compares an observed advertised price with a predicted price. The planner applies a threshold and selects an alert. The messenger performs an external notification. These are different claims and side effects.

## Read the ensemble's executable expression

[EnsembleAgent](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/ensemble_agent.py) normalises the description and obtains frontier, specialist and neural predictions. Its inspected expression is `0.8 × frontier + 0.1 × specialist + 0.1 × neural`. A comment describing regression does not mean those weights are fitted at that point.

For predictions 100, 80 and 120 in that order, the combination is 100. Agreement in the aggregate does not show that the components are independently correct. If all three rely on a misleading description, their errors can align. Evaluate the ensemble against the best individual component, including cost and missing-component behaviour.

## A familiar method call can cross a remote boundary

The specialist uses a deployed service whose [setup](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/pricer_service2.py) loads a quantized base and pinned adapter. The method invocation goes across a service boundary. Deployment configuration specifies dependencies, credentials, hardware, timeout and cache. Those concerns are absent from an ordinary in-process subtraction function.

A cold service may load before answering. Keeping capacity warm can improve responsiveness while adding operating cost. An architecture diagram should identify that service and its ownership rather than suggesting every box is a cheap local function.

## Compare the autonomous planner

The [autonomous version](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/autonomous_planning_agent.py) exposes operations to model-selected routing. Its tool descriptions define what may be proposed; its handler maps names to functions. A model-supplied estimated value should not automatically become the trusted basis for a notification. A stronger arrangement refers to a stored estimate and checks its threshold at execution.

The fixed route is easier to inspect when the required sequence is stable. The autonomous route can adapt where evidence gathering genuinely varies. Choose based on that difference, not because one architecture has a more ambitious name.

## Persistence and presentation add failure boundaries

Writing opportunities to a JSON file is a simple teaching memory mechanism. Concurrent writers can overwrite each other; a crash during writing can leave incomplete data. A temporary file and atomic replacement can improve a single-writer pattern, while a transactional store may be appropriate for multiple workers.

The source [interface](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/price_is_right.py) uses worker threads and queues to keep the display responsive. A progress log and a final result serve different contracts. If the worker raises without publishing a terminal outcome, a consumer can wait indefinitely. Lesson 8.7 develops that mechanism.

## A complete source-reading record

For one run, mark candidate identity, retrieved examples, component predictions, selected threshold, attempted notification, acknowledged response and stored opportunity. Identify where the record is missing. The original demonstration is not a production completion ledger.

**Worked diagnosis:** The source log says notification ran, but the user received nothing. Inspect the messenger's HTTP response and any delivery acknowledgement before resending. A function returning normally does not establish delivery, and a blind retry can duplicate a message whose first acknowledgement was lost.

## Read the organisational connection

A service trace reveals contributions whose receipt and acceptance conditions should be explicit. The research chapter explains [dependency management](../../reference/research/02-coordination.md#identify-what-depends-on-what).
