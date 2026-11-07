# Harbour through the course: from delivery problem to organisational design

[Meet Harbour](../HARBOUR.md) · [Curriculum](../CURRICULUM.md) · [Workbook](../WORKBOOK.md) · [Case records](case-data-guide.md)

Read the company introduction before Module 1. The situations below revisit the same supply-chain business from different angles. They describe design questions and proposed arrangements, not successive claims that Harbour has adopted each capability. Keep a design record as the course progresses.

## Three connected parts

Part 1 examines the evidence, tasks and technical options. Part 2 examines dependencies, accepted handoffs and bounded agent execution. Part 3 examines implementation, capacity, ownership and controlled change. Goods, information and money remain connected throughout. A technical demonstration never substitutes for evidence about the whole customer service.

## Module 1

### Foundations: evidence, language models and work

Harbour supplies packaging that business customers need for their own dispatch work. In H-17, the order and shipment entries each show twelve boxes, while the customer reports ten. Customer service needs an investigation brief that helps operations examine the discrepancy without assigning a cause prematurely.

**Design record.** Draw goods, information and remedy-decision paths for H-17. Identify an evidence owner, a case owner and a decision owner; explain why they differ.

**Worked direction.** Customer service records the report; warehouse and transport contacts examine their evidence; an investigator coordinates the unresolved case. A manager considers a remedy and finance handles an authorised account change. These proposed responsibilities need acceptance and time, not merely names on a diagram.

[Open Module 1](../modules/01-standalone-foundations/README.md)

## Module 2

### Conversations, tools and action boundaries

A Harbour adviser may discuss several customer deliveries in one session. A follow-up such as “who should review it?” must retain the selected case and the adviser’s actual access scope. A coherent answer about the wrong order can send work to the wrong team or disclose another region’s information.

**Design record.** Specify what a continuing conversation remembers, which lookups it permits and how a proposed action becomes an accepted next step.

**Worked direction.** Keep case selection in explicit state and derive access from the signed-in identity. Permit source reads and drafts separately from decisions. Retain an accepted recipient and return incomplete contributions rather than treating every chat response as completed work.

[Open Module 2](../modules/02-conversation/README.md)

## Module 3

### Open models and inference

Harbour is considering how to obtain model capability for internal investigation notes. Hosting locally may change where data is processed, but it also creates responsibility for model files, updates and support. A separate meeting-note illustration examines whether a suggestion can be mistaken for an accepted commitment; it is not additional delivery evidence.

**Design record.** Compare a local model and a provider service for Harbour’s preparation task, including data access, technical support and fallback.

**Worked direction.** Local execution can give direct control over model files and processing location, but someone must maintain the environment and investigate bad outputs. A provider reduces some hosting work while adding service and data-handling dependencies. Neither supplies record authority or business approval.

[Open Module 3](../modules/03-open-models/README.md)

## Module 4

### Evaluation and business value

Harbour wants to know whether assisted preparation improves investigation work. A wrong route may create another handoff; an unsupported “delivery complete” conclusion may delay a valid complaint. Faster drafting matters only in relation to checking, clarification, waiting and the customer-facing outcome.

**Design record.** Write a comparison of manual preparation, direct record lookup and assisted preparation, with quality, effort and elapsed-service measures.

**Worked direction.** Use the same eligible case population and record preparation, checking, rework and waiting. Record unsupported claims and unresolved cases separately. A saved preparation minute is not automatically a saved cost or a shorter resolution; investigate who can use the released capacity.

[Open Module 4](../modules/04-evaluation/README.md)

## Module 5

### Organisational knowledge and retrieval

Harbour’s investigator needs the policy relevant to the disputed delivery. An old rule or another region’s rule can sound convincing while being unsuitable. Finance also needs to know which policy governed an account correction. Finding text is therefore part of maintaining a dependable evidence and decision process.

**Design record.** Design a policy source register showing owner, region, effective version, correction route and response to conflicting passages.

**Worked direction.** A source owner maintains approved policy; access checks establish scope; retrieval selects within that scope. The investigator can inspect source identity and refer a conflict. Finance’s need for a valid correction basis cannot be satisfied by a high similarity score alone.

[Open Module 5](../modules/05-rag/README.md)

## Module 6

### Data, categories and baselines

Harbour routes delivery discrepancies to investigation and invoice questions to finance. These categories allocate work, so disagreements about labels can become disagreements about responsibility. Historical examples may preserve an old arrangement even when the file is tidy and the classifier trains successfully.

**Design record.** Write a routing agreement between customer service, operations and finance, including ambiguous and mixed cases.

**Worked direction.** Finance receives the defined invoice/tax issues; operations investigates recorded-versus-reported delivery differences. Missing information stays visible. The teams agree how to accept, return or jointly examine mixed cases rather than forcing every message into a misleading single label.

[Open Module 6](../modules/06-data/README.md)

## Module 7

### Model adaptation and specialisation

Harbour is exploring whether adapting a model improves the narrow task of distinguishing finance and delivery messages. Changing model parameters can reproduce useful patterns, but it can also preserve obsolete classifications. Current policy and case evidence still need their own owners and update routes.

**Design record.** Prepare a model-change record with category owners, training-data boundaries, evaluation and a return-to-baseline plan.

**Worked direction.** Operations and finance agree the categories; a technical owner records model and adapter versions; evaluation uses separate examples. Keep policy retrieval and decision rights outside the learned weights. A perfect four-message score would not justify broader deployment.

[Open Module 7](../modules/07-specialisation/README.md)

## Module 8

### An AI service within an operating model

Harbour now has several possible technical contributions: retrieving records, preparing a draft and proposing a recipient. A customer still needs someone to own the unresolved delivery. The operating-model question is how people and services accept, challenge and complete these contributions together.

**Design record.** Produce an operating model with named contribution owners, acceptance conditions, decision rights and exception routes.

**Worked direction.** An operations case owner coordinates investigation; functional specialists own their evidence; authorised review precedes a remedy. Technical support owns execution defects. A case is not commercially resolved merely because a draft was produced or a simulated decision was recorded.

[Open Module 8](../modules/08-agents/README.md)

## Module 9

### Agent loops and bounded autonomy

An investigator may need several lookups before understanding a complaint. An agent loop could choose which permitted lookup to request next, but repeated requests can consume time and cost while leaving the original delivery unresolved. The company must define both capability and stopping conditions.

**Design record.** Write an agent mandate with allowed reads, limits, evidence requirements and an accountable recipient at termination.

**Worked direction.** Allow selected case and policy reads, reject unknown capabilities and stop within the declared budget. Return evidence and unresolved questions to the investigator. Do not grant credit, payment or replacement authority because the model requests it.

[Open Module 9](../modules/09-agent-loops/README.md)

## Module 10

### Orchestration and accepted handoffs

Harbour can separate preparation into an evidence contribution and a policy contribution. The investigator then needs a combined account that preserves both. Sending two fluent outputs to another component does not establish that they refer to the same case or are usable for the next task.

**Design record.** Define one handoff contract, its acceptance owner and the route for wrong-case, missing-source or conflicting contributions.

**Worked direction.** The receiver checks case identity and permitted sources before relying on the result. Contradictory accounts remain explicit. Integration work needs an owner and time; creating another specialist does not remove that work.

[Open Module 10](../modules/10-agent-orchestration/README.md)

## Module 11

### Teams and task dependencies

Warehouse and policy questions may sometimes proceed independently, while a conclusion depends on both. A finance adjustment may require a manager’s decision first. Harbour needs to understand these task dependencies before expecting a team of agents to make investigations faster.

**Design record.** Draw the investigation dependency map and identify which contributions can proceed concurrently and which must wait.

**Worked direction.** Independent source reads may overlap, but a remedy still depends on accepted evidence and authorised review. A disputed count may require discussion rather than another parallel call. Include reviewer and specialist capacity when comparing arrangements.

[Open Module 11](../modules/11-agent-teams/README.md)

## Module 12

### Durable state and human review

A Harbour case can wait for a recount, carrier information or a reviewer who is unavailable. During that wait, the case or policy may change. Resuming yesterday’s proposed decision against today’s record would confuse durable storage with current authority.

**Design record.** Specify a paused case’s owner, awaited contribution, expiry or review conditions and safe resumption checks.

**Worked direction.** Save the contribution and its source/version identity. Keep an owner for waiting work, revisit stale facts and revalidate policy before committing. A stored model draft can be reused where suitable; a changed business situation may need a new investigation.

[Open Module 12](../modules/12-stateful-agents/README.md)

## Module 13

### Frameworks and interoperable contributions

Harbour may use different frameworks to execute a preparation task. Changing the framework should not silently change what “reported quantity”, “unverified receipt” or “accepted contribution” means. Those meanings connect the technical interface with operations and finance responsibilities.

**Design record.** Write a framework-independent contract and a migration check for facts, source meaning, failures and responsibilities.

**Worked direction.** Compare case identity, supplied quantities and receipt status, then inspect errors and usage separately. Operations retains ownership of investigation and finance retains its decision boundary. Changing a runtime does not establish equivalent business behaviour by itself.

[Open Module 13](../modules/13-agent-frameworks/README.md)

## Module 14

### MCP and business capabilities

Harbour wants tools that different assistants can discover and use consistently. A case lookup and policy search could be exposed through MCP, but discovering a tool does not grant a regional user new access or authorise a financial action.

**Design record.** Document one capability’s owner, allowed inputs, scope, output meaning, failure contract and support route.

**Worked direction.** Expose a bounded read with server-side scope and source identity. An unavailable result should remain unavailable rather than becoming invented evidence. The local teaching MCP connection does not establish remote authentication or a production finance integration.

[Open Module 14](../modules/14-agent-integration/README.md)

## Module 15

### From a business problem to a pilot

Harbour’s discovery exercise distinguishes two potential causes of delay: locating evidence and obtaining accepted cross-team ownership. A coding project could improve the first while leaving the second untouched. The pilot therefore starts with an operational question and a comparator, not an assumption that agents are required.

**Design record.** Write a pilot charter naming the eligible work, alternatives, participating roles, measures and stop conditions.

**Worked direction.** Compare manual preparation, direct lookup and assisted preparation under matched inclusion rules. Give cross-team ownership problems their own design response. A restricted generated function can help implement a rule; it cannot decide which organisational rule is appropriate.

[Open Module 15](../modules/15-problem-to-pilot/README.md)

## Module 16

### Agent harnesses and operational evidence

When an investigation draft is wrong, Harbour needs to know which evidence and instructions produced it. Operations needs enough information to correct the work; technical support needs enough to diagnose execution. Keeping every customer detail in unrestricted logs would create another problem.

**Design record.** Design an incident record linking execution identity, affected cases, business owner, technical owner and correction status.

**Worked direction.** Retain permitted source and configuration identities, status and relevant usage, with access and retention rules. Technical repair restores execution; the case owner still checks whether customers received an unsuitable answer or whether work needs to be repeated.

[Open Module 16](../modules/16-harness-and-evidence/README.md)

## Module 17

### Durable case handling at volume

Harbour may receive several complaints while investigators and warehouse contacts are already busy. Faster concurrent preparation can increase the queue waiting for acceptance. A worker that finishes late must also be prevented from overwriting work another worker has legitimately taken over.

**Design record.** Create a capacity and recovery plan with preparation rate, human review limits, queue owner and response to overdue cases.

**Worked direction.** Limit concurrent work and observe receiving-team capacity. Distinguish a queued technical job from ownership of the commercial case. Expired workers must not commit stale results; any external physical or financial action would need its own reconciliation.

[Open Module 17](../modules/17-durable-volume/README.md)

## Module 18

### Enterprise context, security and controls

Harbour’s regional records, current policy and finance definitions can be shared selectively to support investigation. A customer message can also contain misleading instructions. Treating every available string as equally authoritative could leak evidence or change the meaning of a commercial decision.

**Design record.** Create an evidence-authority map separating customer reports, operational records, policy and authenticated permissions.

**Worked direction.** A customer report can establish what was reported without setting system rules. A policy needs an approved version and owner. Regional scope comes from trusted application identity. Finance and operations should agree the meaning of shared fields and correct them through owned routes.

[Open Module 18](../modules/18-context-security/README.md)

## Module 19

### Deployment and continuing service ownership

An investigation service used beyond one developer needs support, access management, change windows and a way to handle outages. Harbour’s business customers still need a response when the model or application is unavailable. Finance must not lose its review boundary because an endpoint is reachable.

**Design record.** Write a service acceptance record covering users, owner, support hours, access, rollback, fallback and unresolved deployment requirements.

**Worked direction.** Keep a usable manual investigation route and a named business owner alongside technical support. Local HTTP checks demonstrate selected contracts; hosting, real identity integration, backup restoration and load capacity need separate evidence before a live business release.

[Open Module 19](../modules/19-deployment-ownership/README.md)

## Module 20

### Governed improvement and integration capstone

Harbour’s final decision concerns a proposed business arrangement as well as a software configuration. A candidate can match more route references while consuming more resources or increasing review work. The company must weigh those trade-offs and retain the option to simplify, defer or withdraw the capability.

**Design record.** Produce a final business and organisation design proposal joining customer outcome, goods and information flows, finance authority, service ownership and measured technical evidence.

**Worked direction.** Limit assistance to justified contributions; retain functional source owners and accountable investigation. Explain accepted handoffs, capacity, remedy authority and correction. State what actual checks establish, compare with simpler arrangements, and define conditions for expansion, revision or withdrawal.

[Open Module 20](../modules/20-governed-improvement/README.md)
