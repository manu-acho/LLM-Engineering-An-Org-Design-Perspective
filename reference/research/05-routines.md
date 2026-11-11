# Research chapter 5: AI in the work people actually repeat

[Research reading guide](../literature-guide.md) · [Previous: implementation](04-implementation.md) · [Next: technology in practice](06-technology-in-practice.md)

Read [Meet Harbour](../../HARBOUR.md) for the shared fictional company. In this chapter, its delivery-investigation work illustrates the difference between a process diagram and the repeated, sometimes informal work of handling exceptions. The case is an application of the research concepts, not evidence for the original studies.

## The workflow diagram leaves something out

**Fictional teaching case.** Harbour's process diagram shows five steps: receive complaint, collect evidence, draft response, review, close. Staff describe several additional activities. They call familiar warehouse colleagues, check whether the customer is waiting on a second shipment, and sometimes keep a case open after the system records closure.

These activities might be useful adjustments, inconsistencies or failures. The diagram cannot settle the interpretation. It describes an arrangement; studying recurrent work requires evidence of what people understand and do across cases.

Organisational-routines research explains why this distinction matters. The chapter begins with recurrence and capability, then opens the relationship among understandings, performances and artefacts. It returns to the AI workflow to examine variation, learning and evidence.

## A routine is a pattern of interdependent action

Pentland and Hærem (2015) characterise routines through repetitive, recognisable patterns of interdependent action involving multiple actors. A written procedure, a single repeated individual act and one completed workflow are not sufficient evidence of such a pattern. [Pentland and Hærem (2015)](#pentland-and-h-rem-2015)

A routine can be recognisable across several complaint investigations even when the order of clarifications differs. What makes them instances of that routine requires investigation of the pattern and how participants recognise it, not merely whether a process name appears in a system.

An **organisational capability** is an ability to accomplish a kind of work, such as investigating delivery discrepancies reliably. The capabilities perspective on routines asks how organisations preserve and reproduce that ability. The **practice perspective** examines the situated actions through which people perform, sustain and change recurring patterns. Parmigiani and Howard-Grenville (2011) distinguish these perspectives in their review. The two address related questions, but they should not be collapsed: a documented capability does not establish an enacted pattern or reliable organisational capability. [Parmigiani and Howard-Grenville (2011)](#parmigiani-and-howard-grenville-2011)

## Understandings and performances

Feldman and Pentland (2003) distinguish **ostensive** and **performative** aspects of routines. The ostensive aspect concerns the abstract understanding participants use to guide, describe and account for the work. The performative aspect concerns particular actions by particular people in particular circumstances. Their argument describes a **recursive relationship** in which each aspect can shape the other over time. A general understanding guides a particular performance. What happens during that performance can then reinforce or change the understanding used on later occasions. [Feldman and Pentland (2003)](#feldman-and-pentland-2003)

At Harbour, “a complaint is complete only when the customer has an answer” is one account of the work. A particular adviser checking a second shipment before responding is an action in a particular performance. Several participants may hold different understandings of completion. One manager's interview cannot establish a single shared understanding.

An **artefact** is an object associated with the work, such as a form, prompt, rule, interface, diagram, record or official procedure. It can influence participants' understandings and actions, but it should not be substituted for either routine aspect. Pentland and Feldman (2005, 2008) distinguish artefacts from the routines in which they participate. [Pentland and Feldman (2005)](#pentland-and-feldman-2005) · [Pentland and Feldman (2008)](#pentland-and-feldman-2008)

For an AI application, a prompt template is an artefact; a generated brief is another. Neither is an organisational routine. A model may reproduce the wording of a standard response without reproducing the work through which staff established that the response was suitable.

## Designing an artefact and designing a pattern

Pentland and Feldman (2008) address the danger of designing artefacts while expecting coordinated patterns of action to follow automatically. It does not imply that artefacts are unimportant or that formal design is futile. [Pentland and Feldman (2008)](#pentland-and-feldman-2008)

The distinction changes implementation questions. A new evidence form can require a field. Staff still need a way to obtain the evidence, interpret uncertainty and deal with missing information. If completion is compulsory before evidence exists, the form may redirect work into guessing or an unofficial channel. Whether it does so requires observation.

D'Adderio (2008, 2011) gives artefacts a consequential place in routine dynamics without treating them as fully determining action. Her work examines relationships between formal arrangements and performances, including how arrangements are reframed. The teaching application is to inspect the exact operation: what does the software require, enable, prevent, record or connect? [D'Adderio (2008 and 2011)](#d-adderio-2008-and-2011)

A permission can block an action inside the system. A required status can make some sequence unavoidable there. These are real technical effects. They do not establish the complete organisation of the work, which may also involve preparation, conversation, timing and activity elsewhere.

## Variation is a question, not a verdict

Suppose one adviser asks the customer to recount before contacting the warehouse, while another first checks shipment evidence. Both performances differ from the diagram. The variation might reflect case conditions, expertise, time pressure or inconsistent training. Calling every deviation non-compliance would decide the explanation before investigating it.

**Agency** here concerns participants' capacity to act and influence how work is performed. **Organisational context** includes the relationships, expectations and conditions in which they act. Howard-Grenville (2005) examines how these help explain both flexibility and persistence in a particular manufacturing setting. The study helps explain why stable routines can contain varied performances. This is not evidence that every workaround is helpful or legitimate. [Howard-Grenville (2005)](#howard-grenville-2005)

A useful inquiry distinguishes authorised exceptions, local adaptations, workarounds and errors. It asks who can vary the work, whose adaptations become accepted and which changes remain invisible. A process that appears uniform in event logs may contain substantial variation in off-system activity.

## Repeated action and learning

**Routine dynamics** concerns how participants sustain or change recurring patterns through their understandings, actions and use of artefacts, both as they repeat the work and when they formally redesign it. Feldman (2000) examines how participants respond to outcomes of earlier performances. A participant encounters a consequence, adjusts the next performance and may help retain a new pattern. The explanation does not reduce learning to accumulating records. It concerns how differences are noticed, interpreted and retained in work, rather than claiming that one feedback button establishes learning. [Feldman (2000)](#feldman-2000)

**AI application:** collecting corrections can supply useful material for revising a prompt, training data or procedure. The organisation still needs to interpret those corrections. A correction might address a factual error, an inappropriate category or a legitimate disagreement about the response. Training on every accepted edit without examining its basis can preserve a temporary workaround as a general rule.

A feedback arrangement should therefore connect corrections to case evidence, responsible interpretation and a versioned change. It should also examine what later performances do with the change. Updating a file establishes an artefact revision, not a routine improvement.

## Connected routines and hidden work

An investigation does not stand alone. Intake, warehouse checking, credit handling and customer communication connect through records and requests. A local improvement can change work elsewhere: a faster draft can increase review arrivals; a stricter review can increase clarification requests; closing cases quickly can leave customer follow-up outside the recorded path.

A **routine ecology** consists of related routines whose performances affect one another. For Harbour, faster complaint preparation can send more cases into the investigation routine, changing what investigators must handle and when. The concept shifts attention from one recurring sequence to the relationships among several. Sele and Grand (2016) examine routine interactions in a research-laboratory setting. The concept directs attention to how one recurring pattern enters the conditions of another. It does not claim that a workflow graph reveals the complete ecology or that every connected activity forms one routine. [Sele and Grand (2016)](#sele-and-grand-2016)

In practical terms, inspect the artefacts around the assistant as well as the assistant itself. An evidence spreadsheet, message channel and personal notebook may be part of how work remains possible. Removing one during an automation project without understanding its contribution can leave a dependency unsupported.

## Capability, memory and the danger of freezing one account

Nelson and Winter (1982) place routines at the centre of an evolutionary account of the firm. Routines help explain how organisations preserve capabilities and reproduce ways of acting without solving every problem anew. This perspective makes continuity intelligible. The later practice perspective opens the routine to examine how that continuity is produced through particular actions. [Nelson and Winter (1982)](#nelson-and-winter-1982) · [Parmigiani and Howard-Grenville (2011)](#parmigiani-and-howard-grenville-2011)

The distinction between a record and a routine matters when Harbour trains an AI tool from past cases. A training example might record that finance closed a complaint. The recurring work that made closure possible may have included an adviser calling the warehouse, an investigator checking a split shipment and finance waiting for confirmation before issuing a credit. Each source, such as the case record or written procedure, shows only some of those activities.

Suppose Harbour uses the team that closed each case as the label the model learns to predict. A complaint investigated by the warehouse and closed by finance then receives the label “finance”. If the purpose is to choose who should act **next**, that label teaches the model the wrong target for this case. A model can predict the closing team correctly and send a new complaint past the investigation it still needs. Preparing training examples therefore involves deciding which part of the routine the prediction should support.

A sound preparation exercise therefore asks which part of the recurrent work is being learned. Is the target a next step, an eventual outcome, a category supplied for reporting or an expert judgement? Who produced the record, and what had already happened before it was recorded? These questions connect routine theory to the selection of examples and labels.

## Systems of artefacts and the retention of change

Cacciatori (2012) examines a developing bidding routine through systems of artefacts. The study shows why the relations among artefacts deserve attention: forms, models and other representations can support different contributions, carry different interests and help stabilise a working arrangement. Its engineering-design case does not establish how an AI deployment will develop. It offers a way to examine the combination rather than credit one artefact with the whole pattern. [Cacciatori (2012)](#cacciatori-2012)

For Harbour, the relevant combination might include the intake form, the generated brief, source records, a review checklist and the exception queue. Changing the prompt while leaving the other artefacts inconsistent can create a new mismatch. A brief may begin distinguishing reported and verified quantities while a downstream form still accepts only one number. The conceptual improvement in the brief has not yet become a coherent working arrangement.

Repeated variation becomes organisationally consequential when something retains it. A useful correction may enter a local explanation, a form, a rule or a changed expectation about who should act. Retention does not require every performance to become identical, and it is not necessarily an improvement. An expedient workaround can become durable too. Feldman's account of **endogenous change**, which arises through the routine's own performance and participants' responses to it, and D'Adderio's analysis of artefacts make the content and consequences of that retention important questions. [Feldman (2000)](#feldman-2000) · [D'Adderio (2008 and 2011)](#d-adderio-2008-and-2011)

An AI feedback process should therefore follow a correction beyond its collection. Someone must interpret what problem the correction addresses, decide whether it should apply elsewhere, alter the relevant arrangement and examine later performances. A count of edits measures recorded editing activity. Evidence of learning requires a stronger account of what changed and how it entered subsequent work.

## What logs can show

Event logs can reveal recorded sequences, recurrence and timing. They cannot by themselves show all interpretations, conversations, manual checks or reasons for variation. A participant account can explain a case while omitting other activities or presenting the work selectively. Repeated observation can reveal actions but has limits of coverage. The distinction between an artefact, a participant account and recurrent performance determines what each source can establish.

A credible study combines sources appropriate to its question. To investigate whether an AI brief changes complaint handling, it might compare recorded case paths, observe selected performances and gather participant explanations of specific decisions. The aim is not to reconstruct every detail but to avoid treating one source as an answer to a different question.

## A worked inquiry at Harbour

Harbour proposes observing a sample of cases before and during a limited pilot. The inquiry records the initial brief, later corrections, source checks, communications and what different actors count as completion. It includes difficult and returned cases rather than only successful demonstrations.

One possible finding would be that staff use the draft but recreate evidence in a separate spreadsheet. That observation would establish additional work in the observed cases. Explaining it would require checking whether the spreadsheet offers missing comparison, supports trust, duplicates a control or survives mainly from habit. These are rival explanations, not interchangeable conclusions.

If a redesigned evidence panel later reduces spreadsheet work, the claim should identify the cases, period and observed changes. It should not jump from a feature release to organisation-wide transformation.

## Study pause: classify the evidence

There is a new prompt, an interview saying “we always verify”, and 200 logged approvals. What can each establish?

**Worked response:** The prompt shows a represented instruction. The interview supplies a participant's account of the work. The logs show recorded approval events. None alone establishes that all relevant evidence was checked, what occurred outside the system or a complete shared understanding of the routine.

## Continue with the course

Apply these concepts to [Harbour's worked business design](../../modules/01-foundations/06-design-lab.md). The [companion curriculum](../../README.md) connects these questions to agent workflows and business integration.

## AI research extension: visible compliance and changed ways of knowing

A **regime of knowing** is an established arrangement for deciding what counts as relevant knowledge and how claims become credible in work. The term directs attention to expertise, accepted evidence and practical authority, rather than information volume alone.

Pachidi et al. (2021) examine the introduction of an algorithmic technology in a telecommunications organisation. Their study follows **symbolic actions**, actions that express or display a position toward a technology, and changes in an established regime of knowing. Displaying support or recording compliance can matter to how a change develops, alongside how the technology is actually used. The study examines how apparent conformity and advocacy enter the wider sequence of change. A single organisational study does not establish a universal adoption pattern. [Pachidi et al. (2021)](../bibliography.md#pachidi-et-al-2021)

The study raises a question about routine work. When staff use an AI category in a record, does it also shape how they understand the case and decide what to do? Completing a required field is one observable action. The evidence people trust and the steps they take to resolve a dispute may follow a different pattern. Over time, a category first used for reporting could become part of how staff judge complaints.

At Harbour, investigators could copy the assistant’s category into a mandatory field and still call a transport specialist before acting. The entry shows that the category was recorded. The call might supply expertise the assistant lacks, help staff check unreliable categories, or continue out of habit even when the category helps. Following similar cases over time could show when staff rely on the category, when they challenge it and what they learn from the call.

The evidence must connect performances over time. Compare the recorded category, the explanation given in case meetings, actual remedy choices and revisions to the classification scheme. Observe contested cases as well as ordinary ones. A dashboard counting completed categories cannot show whether the category guides the decision.

**Study exercise.** Identify two rival explanations for a rise in recorded use after training. One is increased confidence in the assistant; another is compliance with a reporting requirement. A worked inquiry would look for changed evidence use, corrections, unrecorded checking and participants' explanations. It would avoid equating either the official record or a single interview with the entire routine. [Governance](08-governance-and-accountability.md) then asks who can revise the requirement when the observed pattern undermines useful work.

## References

The [project bibliography](../bibliography.md) brings together the chapter references and additional AI research, with source-access notes.

### Pentland and Hærem (2015)

Pentland, B. T., and Hærem, T. (2015). Organizational routines as patterns of action: Implications for organizational behavior. *Annual Review of Organizational Psychology and Organizational Behavior, 2*, 465–487. [Publication](https://doi.org/10.1146/annurev-orgpsych-032414-111412).

### Parmigiani and Howard-Grenville (2011)

Parmigiani, A., and Howard-Grenville, J. (2011). Routines revisited: Exploring the capabilities and practice perspectives. *Academy of Management Annals, 5*(1), 413–453. [Publication](https://doi.org/10.1080/19416520.2011.589143).

### Feldman and Pentland (2003)

Feldman, M. S., and Pentland, B. T. (2003). Reconceptualizing organizational routines as a source of flexibility and change. *Administrative Science Quarterly, 48*(1), 94–118. [Publication](https://doi.org/10.2307/3556620) · [Author-hosted article](https://socialecology.uci.edu/sites/socialecology.uci.edu/files/users/feldmanm/Feldman_and_Pentland_2003.pdf).

### Pentland and Feldman (2008)

Pentland, B. T., and Feldman, M. S. (2008). Designing routines: On the folly of designing artifacts, while hoping for patterns of action. *Information and Organization, 18*(4), 235–250. [Publication](https://doi.org/10.1016/j.infoandorg.2008.08.001).

### Pentland and Feldman (2005)

Pentland, B. T., and Feldman, M. S. (2005). Organizational routines as a unit of analysis. *Industrial and Corporate Change, 14*(5), 793–815. [Publication](https://doi.org/10.1093/icc/dth070).

### Feldman (2000)

Feldman, M. S. (2000). Organizational routines as a source of continuous change. *Organization Science, 11*(6), 611–629. [Publication](https://doi.org/10.1287/orsc.11.6.611.12529).

### Sele and Grand (2016)

Sele, K., and Grand, S. (2016). Unpacking the dynamics of ecologies of routines: Mediators and their generative effects in routine interactions. *Organization Science, 27*(3), 722–738. [Publication](https://doi.org/10.1287/orsc.2015.1031).

### D'Adderio (2008 and 2011)

D'Adderio, L. (2008). The performativity of routines: Theorising the influence of artefacts and distributed agencies on routines dynamics. *Research Policy, 37*(5), 769–789. [Publication](https://doi.org/10.1016/j.respol.2007.12.012). D'Adderio, L. (2011). Artifacts at the centre of routines: Performing the material turn in routines theory. *Journal of Institutional Economics, 7*(2), 197–230. [Publication](https://doi.org/10.1017/S174413741000024X).

### Howard-Grenville (2005)

Howard-Grenville, J. A. (2005). The persistence of flexible organizational routines: The role of agency and organizational context. *Organization Science, 16*(6), 618–636. [Publication](https://doi.org/10.1287/orsc.1050.0150).

### Nelson and Winter (1982)

Nelson, R. R., and Winter, S. G. (1982). *An Evolutionary Theory of Economic Change*. Harvard University Press.

### Cacciatori (2012)

Cacciatori, E. (2012). Resolving conflict in problem-solving: Systems of artefacts in the development of new routines. *Journal of Management Studies, 49*(8), 1559–1585. [Publication](https://doi.org/10.1111/j.1467-6486.2012.01065.x).
