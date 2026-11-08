# Research chapter 4: Making AI fit the organisation

[Research reading guide](../literature-guide.md) · [Previous: decisions](03-decisions.md) · [Next: routines](05-routines.md)

Read [Meet Harbour](../../HARBOUR.md) for the shared fictional company. In this chapter, its delivery-investigation work illustrates the comparison needed to assess an assisted service alongside changes in the surrounding work. The case is an application of the research concepts, not evidence for the original studies.

## A successful demonstration can still be a poor fit

**Fictional teaching case.** Harbour tests an AI complaint assistant on carefully prepared examples. It reads the records, produces a useful brief and proposes a next step. In the pilot, some advisers cannot access the shipment record. The mandatory form cannot express an uncertain quantity. A reviewer receives work outside their expertise. None of these problems appeared in the demonstration.

The application can possess a capability while the operating arrangement fits poorly. Enterprise-systems research helps explain this gap because it studies how generic software designs meet particular organisations. Its concepts can inform AI integration without assuming that a language-model application and an enterprise resource planning system are identical.

This chapter follows that encounter from generic assumptions through misfit, adaptation, implementation and outcomes. The cited enterprise-system studies support concepts and bounded findings in their own settings. The Harbour applications are teaching interpretations.

## Generic software carries assumptions

A packaged system must serve more than one organisation. It therefore contains general choices about recognised objects, data, roles, sequences and controls. Strong and Volkoff (2010) examine how such generic requirements meet local requirements through a three-year qualitative enterprise-system study. Their publisher abstract identifies six misfit domains and distinguishes deficiencies from impositions. [Strong and Volkoff (2010)](#strong-and-volkoff-2010)

An AI application also embodies assumptions, even when the model can generate flexible language. A form defines valid inputs. A tool defines an available action. A prompt expresses priorities. A review path assumes someone can supply judgement at a particular moment. Flexibility in wording does not remove those arrangements.

**Integration** connects data or processes that were previously separate. **Standardisation** reduces variation through common categories or procedures. The two can support one another but are distinct. Sharing complaint data connects activities; requiring every team to use one complaint taxonomy standardises representation. Either change may have benefits and costs. Volkoff, Strong and Elmes (2005) distinguish process and data integration, directing attention to the different relationships joined by a system. [Volkoff et al. (2005)](#volkoff-strong-and-elmes-2005)

In AI engineering, a common interface may simplify service access while hiding differences in source timeliness or meaning. The relevant inquiry is what has been connected, which variation has been removed and whose work changes as a result. An integration count cannot answer those questions.

## Six kinds of misfit

A **misfit** is a mismatch between the system and an organisational requirement. A **deficiency** concerns something needed but missing; an **imposition** concerns something the system requires that is unwanted or unsuitable. Strong and Volkoff's distinctions direct attention beyond missing functionality. [Strong and Volkoff (2010)](#strong-and-volkoff-2010)

The following AI examples are adaptations of those concepts, not findings from the original study.

| Domain | Fictional AI example | Question for investigation |
|---|---|---|
| Functionality | The assistant cannot retain two conflicting accounts | Is this capability required for the intended cases? |
| Data | Intake requires a confirmed quantity before a recount exists | Can uncertainty be recorded without inventing a value? |
| Usability | Checking the draft requires repeatedly changing screens | What effort does a complete review actually take? |
| Role | A reviewer is assigned work requiring another team's expertise | Who can perform and accept this contribution? |
| Control | The interface allows a proposal to change after approval | Which checks bind permission to the approved action? |
| Organisational culture | Staff perceive contesting the assistant as unwelcome | What evidence shows how challenge is treated in practice? |

The last row cannot be diagnosed from a screen alone. Interviews, observation and organisational context are needed. Nor should every unfamiliar feature be labelled a misfit. The comparison requires an identified requirement and evidence that the arrangement fails to meet it or imposes an unsuitable demand.

Strong and Volkoff distinguish fit as coverage from fit as enablement. In plain language, offering the required function is not the same as enabling people to accomplish their work through it. A source panel can exist while the reviewer lacks access to the underlying documents. The chapter uses the distinction through the review and publisher abstract, without importing detailed original case claims.

## Responses to misfit

Misfit does not determine one correct response. An organisation might change the process, configure the application, add an extension, use another service, limit the scope or reject the use case. Brehm, Heinzl and Markus (2001) develop a spectrum of tailoring choices for ERP systems. Their contribution here is to avoid treating every adaptation as the same operation. [Brehm et al. (2001)](#brehm-heinzl-and-markus-2001)

For the fictional assistant, selecting a supported review threshold is configuration. Adding a source-comparison panel is an extension. Rewriting core workflow behaviour changes a different part of the system. The precise terminology and maintenance consequences depend on the application. The ERP taxonomy is a useful starting vocabulary, not a verified rule about a current AI product.

Every proposed response also has an organisational side. Allowing an unknown quantity helps honest intake, but creates cases needing clarification. A new specialist role requires staffing and knowledge. A local workaround may keep service running while making records incomplete. An assessment should follow the work created by the adaptation rather than treating technical completion as the end.

## Implementation extends beyond launch

Markus and Tanis (2000) organise the enterprise-system experience into chartering, project, shakedown, and onward-and-upward phases. [Markus and Tanis (2000)](#markus-and-tanis-2000)

**Chartering** concerns why to invest, what scope to pursue and under what conditions. For the AI service, the first question is whether difficult free-text complaints are the right population. **Project work** selects and constructs the arrangement: evidence sources, roles, prompts, integrations, checks and training. **Shakedown** concerns transition and stabilisation, when missing knowledge and unexpected cases become visible. **Onward and upward** concerns continued maintenance, development and benefit realisation.

These are lenses for inquiry rather than a guarantee of a tidy sequence. Learning may force a return to scope or design choices. A model or source-policy change can reopen questions that appeared settled. A service needs continuing ownership for these changes, even if its initial implementation was small.

Boudreau and Robey (2005), in an interpretive government-agency case, show that users can avoid and later reinvent use through improvised learning. The bounded lesson is that installed technology does not determine use. It is not a prediction that Harbour's staff will follow the same trajectory. [Boudreau and Robey (2005)](#boudreau-and-robey-2005)

## Capability, configuration, practice and outcome

Four kinds of evidence answer different questions. A capability description says what the system offers. Configuration records show selected rules and integrations. Repeated accounts and observations show how people work with, around or outside those arrangements. Outcome evidence concerns consequences over a specified period and at a specified level.

For example, a successful test can show that a known proposal version is required by an execution check. It cannot establish that staff recurrently use the intended proposal path. A log can show submitted cases and review events. It may omit telephone clarification. A shorter review time can be real while warehouse work increases. This evidence sequence adapts the reviews' framework; it is not a single established causal model.

## Benefits need a population and a comparison

Shang and Seddon (2002) distinguish operational, managerial, strategic, IT-infrastructure and organisational benefit dimensions. The framework classifies potential benefits; its evidence base does not establish that every enterprise system produces them. For AI integration, the useful transfer is to specify the claimed benefit rather than use “transformation” as an undefined result. [Shang and Seddon (2002)](#shang-and-seddon-2002)

An operational claim might concern time per eligible case. A managerial claim might concern visibility of unresolved work. An organisational claim might concern a sustained change in how teams share responsibility. These require different observations. A working demonstration supplies none of them by itself.

The comparison also matters. If intake requirements and reviewer training improve alongside the assistant, the total change cannot be attributed entirely to generation. A comparator with the same improved intake, or careful documentation of the combined intervention, makes the interpretation more credible. Selection matters too: staff may use the system mainly on easy cases.

## Implementation as learning across boundaries

Requirements are not always settled facts waiting to be translated into code. People may understand the existing work differently, know different parts of the package and discover consequences only when they try a new arrangement. Robey, Ross and Boudreau (2002) examine enterprise-system implementation through organisational learning and knowledge barriers. Their work explains why implementation can involve conflict and revision rather than a straightforward transfer of agreed requirements. [Robey et al. (2002)](#robey-ross-and-boudreau-2002)

An AI pilot can expose several such boundaries. Advisers know the language customers use. Investigators know what makes evidence usable. Developers know which inputs a tool accepts. A policy owner knows why an exception exists. Agreement that the assistant should “resolve routine cases” can conceal different understandings of both resolve and routine.

**Fictional implementation exercise.** Harbour follows a disputed complaint together, from intake to customer response. The adviser explains why a quantity is uncertain. The investigator demonstrates the source comparison. The developer shows how the current form rejects an unknown quantity. The policy owner identifies which uncertainty can remain open at each stage. The exercise makes the requirement concrete enough to compare several responses.

Learning here is more than teaching staff to use the chosen interface. It can change the interface, task boundary, evidence requirement or role allocation. It can also reveal that the proposed scope is unsuitable. Treating every disagreement as resistance would miss the knowledge that the disagreement supplies.

## Choosing where to adapt

An adaptation has a location and a continuing cost. Changing intake requirements places work on the people collecting information. Configuring a supported option creates a setting that someone must understand and maintain. An extension creates code and interfaces that must remain compatible. A manual workaround can preserve service while distributing knowledge and records outside the main application. Brehm and colleagues' spectrum of tailoring choices provides a foundation for examining these differences. [Brehm et al. (2001)](#brehm-heinzl-and-markus-2001)

A useful decision records the requirement, the affected roles, the chosen response, its dependencies and the reason alternatives were rejected. For an AI service, it should also identify which source, model, prompt or tool changes would require retesting. This is an implementation design practice developed from the chapter's concepts, not a product-specific prescription.

The decision need not always favour the most technically sophisticated response. If routine requests can be answered by a direct record lookup, a deterministic interface may provide a clearer fit. If descriptions vary widely but the output must preserve evidence, a drafting capability may help. If the central difficulty is conflicting interests, neither implementation removes the need for an organisational resolution mechanism.

## Whose benefit, and at which point in time?

The same service can have different consequences for different roles. An adviser may save preparation time while an investigator receives more marginal cases. A manager may gain visibility while staff spend additional time classifying records. The benefit categories identified by Shang and Seddon help keep these consequences separate. They are not independent promises that a deployment will fulfil. [Shang and Seddon (2002)](#shang-and-seddon-2002)

Time also changes the assessment. Early support effort can be high during stabilisation; later changes can expose new requirements or remove earlier gains. Markus and Tanis's lifecycle lens therefore complements the question of whose benefit is being measured. An initial adoption count cannot establish sustained use, and sustained use cannot by itself establish that the service is preferable to its alternatives. [Markus and Tanis (2000)](#markus-and-tanis-2000)

## A worked implementation choice

Harbour limits the proposed pilot to long, non-urgent complaints with accessible source records. It retains a direct route for urgent or disputed cases. Staff can record unknown quantities; an intake owner obtains missing evidence. A reviewer can return the draft and request a specialist discussion. The service owner maintains the source and prompt versions and reviews failures.

The pilot compares structured intake and direct lookup with structured intake plus the draft. It records preparation, review, clarification and elapsed resolution, together with unsupported claims and work transferred to other roles. These are proposed measures, not reported results.

Suppose checking takes longer than expected because sources open in separate systems. Buying a larger model does not directly address that usability problem. Possible responses include changing the evidence interface, limiting scope to accessible sources, or retaining manual handling. The choice should be tested against the actual requirement.

## Study pause: choose an adaptation

An assistant requires a verified customer quantity before allowing submission. Staff often have only an estimate. Compare changing the process with changing the software.

**Worked response:** Requiring verification before intake could improve downstream certainty but delay cases and shift work to advisers. Allowing an explicitly unverified estimate could preserve early intake but require a later verification state and owner. Neither option is free. The decision depends on service timing, evidence needs and who can perform verification.

## Continue with the course

Apply these concepts to [the pilot's worked business design](../../modules/01-standalone-foundations/06-business-design.md) and [the exercises](../../modules/01-standalone-foundations/07-assessment.md). The [standalone curriculum](../../CURRICULUM.md) identifies how later planned modules will develop the technical and organisational questions together.

## AI research extension: what a measured productivity result can establish

Brynjolfsson, Li and Raymond (2025) study the introduction of a generative-AI assistant in customer support. The published study covers 5,172 agents and reports an average increase of about 15% in issues resolved per hour, with substantial differences across workers. Less experienced and lower-skilled workers benefited more on the principal productivity measure. This is evidence from a particular work setting, not a general forecast for every AI service. [Brynjolfsson et al. (2025)](../bibliography.md#brynjolfsson-et-al-2025)

**Productivity** relates an output to an input, such as resolved cases per labour hour. Its meaning depends on how output, labour and case quality are defined. A higher rate of drafts per hour is a different outcome from a higher rate of durable resolutions.

**Harbour application.** The study offers a reason to investigate differences by experience and task. It does not justify placing 15% in a Harbour business case as an expected return. Packaging discrepancies involve warehouse evidence, transport dependencies and finance actions that may differ from the studied service.

An implementation evaluation should record which cases enter the comparison, when access changes, what other practices change and whether assistance is actually used. **Selection bias** occurs when compared groups differ in ways relevant to the result. If experienced staff receive the difficult cases after an AI rollout, a simple average can misrepresent both their contribution and the tool's effect.

A useful evaluation therefore combines operational measures with evidence about the work. It might compare evidence-preparation time, total resolution time, remedy errors and investigation effort, while tracking case mix and experience. A short pilot can establish whether a defined arrangement is usable under tested conditions. Claims about durable benefits need a longer and broader comparison.

**Study exercise.** Write two conclusions from a pilot in which briefs become faster but unresolved complaints rise. A weak conclusion says that AI improved productivity. A stronger conclusion specifies the faster activity, reports the adverse service measure and investigates whether missing handoffs, changed case mix or another condition explains the divergence. Connect the investigation to [process architecture](09-process-architecture.md).

## References

The [project bibliography](../bibliography.md) brings together the chapter references and additional AI research, with source-access notes.

### Strong and Volkoff (2010)

Strong, D. M., and Volkoff, O. (2010). Understanding organization-enterprise system fit: A path to theorizing the information technology artifact. *MIS Quarterly, 34*(4), 731–756. [Journal record](https://aisel.aisnet.org/misq/vol34/iss4/8/).

### Brehm, Heinzl and Markus (2001)

Brehm, L., Heinzl, A., and Markus, M. L. (2001). Tailoring ERP systems: A spectrum of choices and their implications. *Proceedings of the 34th Annual Hawaii International Conference on System Sciences*. [Publication](https://doi.org/10.1109/HICSS.2001.927130).

### Markus and Tanis (2000)

Markus, M. L., and Tanis, C. (2000). The enterprise systems experience: From adoption to success. In R. W. Zmud (Ed.), *Framing the Domains of IT Management: Projecting the Future Through the Past* (pp. 173–207). Pinnaflex Educational Resources.

### Boudreau and Robey (2005)

Boudreau, M.-C., and Robey, D. (2005). Enacting integrated information technology: A human agency perspective. *Organization Science, 16*(1), 3–18. [Publication](https://doi.org/10.1287/orsc.1040.0103).

### Shang and Seddon (2002)

Shang, S., and Seddon, P. B. (2002). Assessing and managing the benefits of enterprise systems: The business manager's perspective. *Information Systems Journal, 12*(4), 271–299. [Publication](https://doi.org/10.1046/j.1365-2575.2002.00132.x).

### Volkoff, Strong and Elmes (2005)

Volkoff, O., Strong, D. M., and Elmes, M. B. (2005). Understanding enterprise systems-enabled integration. *European Journal of Information Systems, 14*(2), 110–120. [Publication](https://doi.org/10.1057/palgrave.ejis.3000528).

### Robey, Ross and Boudreau (2002)

Robey, D., Ross, J. W., and Boudreau, M.-C. (2002). Learning to implement enterprise systems: An exploratory study of the dialectics of change. *Journal of Management Information Systems, 19*(1), 17–46. [Publication](https://doi.org/10.1080/07421222.2002.11045713).
