# Organisation design research: a reading guide

## Why look beyond the technology?

A useful AI system has to fit into work. Someone supplies the information, interprets an answer, decides what to do and handles the exceptions. Literature from organisation design research helps explain these connections.

The six reviews below approach the problem from different directions. They examine how work is divided, how people coordinate, how decisions are shaped, how systems fit their setting, how routines develop and how technical features become useful in practice. Each topic offers questions you can apply to an AI proposal.

The reviews are the sources used for this guide's organisational discussions. The applications to Harbour are interpretations of those ideas, not findings from a real AI deployment. The reviews draw on different levels of source access, and not every original article has been independently checked for this guide. Consult an original study before relying on a detailed claim about its findings.

## Six topics and what they add

### 1. Organisation design: dividing work creates a need to reconnect it

[Stream 1 review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_01_Organisation_Design_Detailed_Review.md)

The review connects Thompson's interdependence, Galbraith's information-processing view and Mintzberg's coordination mechanisms with configurational accounts of design. An isolated feature has no self-contained organisational meaning. Its significance depends on tasks, information, authority, incentives, other mechanisms and context.

**Transfer:** A summarisation feature should be assessed as part of who gathers evidence, who interprets it and who can act. An agent architecture's technical decomposition does not establish an effective division of organisational work. Modules 1, 3, 4 and 8 use this argument.

### 2. Coordination: identify the dependency before choosing the mechanism

[Stream 2 review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_02_Coordination_Theory_Detailed_Review.md)

Malone and Crowston supply dependency management as the starting point. Okhuysen and Bechky distinguish mechanisms from accountability, predictability and common understanding. Carlile's knowledge-boundary perspective explains why a common representation may leave differences in meaning or interests unresolved. Relational and practice perspectives add expertise, communication and ongoing repair.

**Transfer:** A shared AI summary can make a handoff visible without resolving what “complete” means to sales and operations. A semantic search result can find relevant words without settling conflicting claims. Modules 2, 3, 5 and 8 make these distinctions concrete.

### 3. Decision theory: follow the premises and discretion

[Stream 3 review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_03_Decision_Theory_Detailed_Review.md)

The review builds from Simon's bounded rationality and decision premises, programmes in March and Simon, authority and its acceptance, and distinctions among information, calculation, recommendation, decision, authorisation and execution. Formal permissions and actual influence are different. Automation can move judgement to categories, thresholds, model labels or exception rules.

**Transfer:** A human approval button does not show that the human controls the decisive assumptions. Training labels and evaluation metrics are premises too. Modules 2, 4, 6, 7 and 8 examine where those choices originate and who can change them. Public-administration evidence on discretion relocation is used as a sensitising lens, not direct evidence about private-sector AI.

### 4. Enterprise systems: generic capability, local fit and implementation

[Stream 4 review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_04_Enterprise_Systems_Implementation_Transformation_Detailed_Review.md)

The synthesis connects integration and package logic with fit/misfit, tailoring and implementation over time. Strong and Volkoff's misfit domains direct attention to functionality, data, usability, roles, control and culture. Markus and Tanis offer a lifecycle lens. These are useful ways to examine the problem, not a claim that an LLM application and an ERP package are identical.

**Transfer:** A successful prototype can still impose unsuitable categories or a review workload the client cannot sustain. Options include changing the process, configuration, extension, bounded workaround or rejecting the use case. Modules 3, 4, 6 and 8 use this lens. No unverified cloud-ERP or SAP product rules are imported.

### 5. Organisational routines: the workflow file is not the work

[Stream 5 review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_05_Organisational_Routines_Detailed_Review.md)

Feldman and Pentland distinguish participants' abstract understandings of recurrent work, the ostensive aspect, from situated performances, the performative aspect. Artefacts such as forms, procedures and software are analytically distinct from both. Pentland and Feldman's design argument and D'Adderio's artefact work help explain why software is consequential without fully determining action.

**Transfer:** An AI-generated procedure, system log or prompt template cannot establish a whole organisational routine. Training on past behaviour may freeze a particular representation of practice while excluding unrecorded repair work. Modules 1, 3, 5, 7 and 8 examine these issues.

### 6. Technology, materiality and organisation: how a possibility becomes consequential

[Stream 6 review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_06_Technology_Materiality_Organisation_Detailed_Review.md)

Orlikowski's duality and practice accounts explain how technologies are shaped through action and enter the conditions of later work. Materiality directs attention to the digital arrangements that make a difference: required fields, representations, access controls, processing logic and durable records. Hutchby, Markus and Silver, and Leonardi contribute to a relational account of affordances and constraints. An affordance is a possibility for a particular actor to act through an arrangement under particular conditions. It is not simply another name for a feature. Volkoff and Strong and Strong et al. address actualisation, the process through which such possibilities are realised over time.

**Transfer:** An evidence panel can make passages available without making a reviewer able to challenge a recommendation. Source interpretation, time, authority and a correction route can all affect the possibility of meaningful review. A required evidence field can support downstream checking while obstructing intake when the source is unavailable. The business lessons examine these relations. [Lesson 8.4](../modules/08-agents/04-technology-in-practice.md) develops a full worked application across the curriculum.

The review also examines sociomateriality, which treats social and material relations as constitutively entangled in practice. It does not present this as interchangeable with critical-realist affordance analysis or Leonardi's imbrication account. Those positions differ over how actors and technical arrangements can be separated analytically. The guide examines actors, arrangements and goals separately without claiming to settle that debate or to have observed sociomaterial practice merely by inspecting code.

**Evidence boundary:** The six-layer chain below brings together ideas from Reviews 4 to 6. It is not a single established model attributable to one author. The electronic-health-record setting of Strong et al. is not evidence that an AI approval workflow produces the same process or outcome. Detailed primary-source claims remain subject to the review's evidence limits.

## The evidence ladder used throughout the curriculum

| Object | An AI example | Appropriate evidence | What it cannot establish alone |
|---|---|---|---|
| Represented design | Prompt, schema, workflow diagram | Inspect the artifact and its version | Whether it was deployed or followed |
| Configured technology | Enabled tools, access rules, thresholds | Inspect selected settings, rules and integrations | Whether the wider operating arrangement is in place |
| Implemented arrangement | A deployed assistant plus reviewer roles, procedures and training | Deployment and operating evidence | Successful use or benefit merely because go-live occurred |
| Perceived possibility or constraint | What a reviewer believes they can inspect or contest, given their goals | Situated accounts, elicitation and observation | That the possibility is used or the belief is universally shared |
| Enacted practice | Requests recurrently handled across people and tools | Repeated observation and detailed traces, including off-system work | The whole practice from a single event or log alone |
| Realised outcome | Consequences for particular roles and the process over a specified period | Comparative/longitudinal outcome evidence connected to the process | Universal causation or automatic transfer to another organisation |

This ladder adapts the synthesis in the literature reviews. Participants' understandings, including ostensive accounts of routines, remain relevant to the perceived/situated levels; the concepts should not be equated. Actualisation is a process linking arrangements, actors and consequences, not a synonym for installing software or merely reporting that it was used. A study can stop at an earlier layer if its claims also stop there.

## Questions to take into the modules

| Module | Question to explore | What to examine |
|---|---|---|
| 1 | Who can use the brief to act, rather than merely read it? | Source labels, correction route and recipient role |
| 2 | For whom does tool access enable action, and which approval conditions remain absent? | Permission checks, evidence access and review capacity |
| 3 | When does editable meeting text become a usable, contestable record? | Confirmation state and links to speech evidence |
| 4 | What process connects a configured feature to a measured outcome? | Layered evaluation and rival explanations |
| 5 | Which actor can retrieve, interpret and resolve evidence conflicts? | Retrieval filters, version metadata and policy owner |
| 6 | When do mandatory labels help downstream work and constrain valid intake? | Missing/uncertain categories and adjudication |
| 7 | How do changed categories and goals alter the value of a specialised model? | Overrides, taxonomy ownership and revision process |
| 8 | How do roles, tools and recovery arrangements work together over time? | State/receipt design and actualisation inquiry |

These questions supplement the existing explanations, code workshops and cases. They do not replace technical behaviour with an abstract assertion that everything is contextual.

## Connect a research idea to a concrete mechanism

Use a concept when it helps explain something specific. Truncation changes which facts remain visible. A dispatch table limits the actions an application can take. Training labels preserve selected categories. A queue distributes waiting and attention. An execution log records an event, but it cannot make someone take responsibility for a problem.

Start with one of those mechanisms. Ask what the research concept helps you notice, which alternative explanation remains possible and what evidence would distinguish them. That is more useful than attaching a theorist's name to a recommendation without changing the inquiry.

## Carry the literature into agent engineering

[Part II](../AGENT-ENGINEERING.md) uses the same six perspectives to examine loops, specialist teams, stateful review and shared capabilities. Division of work creates integration needs. Tool and category choices shape decision premises. Review interrupts create queues that need capacity and ownership. A common protocol does not make different teams agree on completion.

The [final integration plan](../modules/14-agent-integration/04-integration-plan.md) connects these ideas to a proposed business pilot. It separates the represented design, configured capabilities, actual work and outcomes rather than treating a working agent demonstration as evidence of organisational benefit.
