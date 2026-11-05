# Research chapter 3: Decisions, judgement and authority with AI

[Research reading guide](../literature-guide.md) · [Previous: coordination](02-coordination.md) · [Next: implementation](04-implementation.md)

## The final click is only one part of the decision

**Fictional teaching case.** Harbour's assistant proposes a customer credit. A manager clicks approve. The company describes the arrangement as human control. Yet the assistant selected the evidence, classified the case, excluded some alternatives and drafted the recommendation before the manager opened the screen.

The manager may still exercise meaningful judgement. The button alone cannot establish that. The inquiry must follow how the problem was framed, which options became visible and who could revise the assumptions. Decision theory supplies a vocabulary for doing so.

The discussion begins with limits on attention and calculation, then follows the premises and programmes that make choice manageable. Authority and discretion complicate the picture. The chapter ends with a worked design in which recommendation, authorisation and execution remain distinguishable.

## Bounded rationality

**Bounded rationality** concerns choice under limits of information and computational capacity. Simon (1955) challenges models that require a decision-maker to know and evaluate everything relevant. His behavioural approach examines simpler procedures compatible with actual limits. The resulting design question concerns the procedures that make choice possible under those limits. [Simon (1955)](#simon-1955)

This is more useful than saying that people make mistakes. It changes the design question: how does the organisation make a problem manageable? A service team cannot reconsider every policy, source and possible action from first principles for every complaint. Categories, procedures, expertise and information channels help narrow the task.

AI can alter those limits by preparing information or suggesting alternatives. It can also introduce new limits: a selected set of retrieved passages, a compressed account or an apparently complete answer may narrow what receives attention. The sensible question is which parts of the decision environment have changed, not whether human limits have disappeared.

**Satisficing** means searching for an acceptable option rather than demonstrating that it is the best of all possible options. In a fictional service case, a team may seek a response that meets evidence, fairness and timing requirements. Those requirements must be defensible. An easy-to-meet threshold does not become appropriate merely because it makes search shorter. A satisfactory response is defined by the criteria used in the search, so those criteria belong in the analysis.

## Decision premises

A **decision premise** is part of the basis that guides a choice: a fact, goal, category, value, expectation or rule. Simon's organisational account explains how influence can operate through these premises without a senior actor deciding every individual case. [Simon (1997)](#simon-1997)

At Harbour, “customer reports ten boxes” is a factual input with a source and qualification. “Preserve customer trust” is a goal. “Approve only after confirming the discrepancy” is a rule. “Small shortage” is a classification whose boundaries someone selected. These do different work in the decision.

An AI pipeline distributes premises through technical operations. Retrieval selects passages. Training labels supply categories. A prompt defines an acceptable answer. A metric rewards some properties over others. A tool schema determines the actions that can be requested. These observations are applications of premise reasoning to AI engineering, not claims that Simon studied current model systems.

The resulting questions are practical. Who maintains the category? Who can correct the source? Can the reviewer see an excluded alternative? Which assumptions survive into the final record? A correct calculation does not validate the premises it uses.

## Programmes and exceptions

A **programme**, in March and Simon's account, is a structured response to a recognised situation. Programmes reduce repeated search by supplying procedures or expected actions. [March and Simon (1993)](#march-and-simon-1993)

In a simple service rule, a recognised low-value case with complete evidence enters a standard review path. The amount comparison is a calculation. The rule connecting conditions to a path is a programmed response. The human's interpretation of conflicting evidence may remain less programmed.

A recurring problem is failure to recognise an exception. If the system requires every case to fit one existing label, unfamiliar cases can become ordinary cases by force of classification. An “unknown” or “needs clarification” option may preserve useful uncertainty, but it also creates work that needs an owner and a response arrangement.

## Permission and authority

**Permission** is what the system technically allows an identity to do. **Authority** concerns an organisational relationship or right to decide. They should not be treated as interchangeable.

Simon examines authority through acceptance of another actor's decision as a premise for action. Aghion and Tirole (1997), working in a different theoretical tradition, distinguish **formal authority**, the right to decide, from **real authority**, effective control over a decision. These theories are not equivalent. Their common practical warning is that a formal allocation does not establish how influence works. [Simon (1997)](#simon-1997) · [Aghion and Tirole (1997)](#aghion-and-tirole-1997)

A reviewer can possess a technical approval right while relying almost entirely on the specialist who frames the options. Conversely, an expert may influence the result without holding the approval permission. These are possibilities to investigate. They should not be assumed from job titles or logs.

For an AI tool, valid credentials establish neither the legitimacy of the business action nor the authority to take it in every case. The service needs explicit conditions governing the operation, and the organisation needs an account of who can establish and contest those conditions. This is an organisational interpretation, not legal advice about any particular mandate.

## Where discretion moves

**Discretion** is the recognised room to interpret a situation or choose among alternatives. Automation can narrow discretion at the transaction while moving choices to those who design categories, thresholds, evidence rules and exception routes.

Bovens and Zouridis (2002) examine shifts from street-level to system-level bureaucracy in public administration. Their account supports asking where judgement is located as systems take over processing. Its constitutional setting cannot simply be transferred to a private business. The AI examples here use the narrower idea of **discretion relocation** as an analytical lens. [Bovens and Zouridis (2002)](#bovens-and-zouridis-2002)

At Harbour, a credit recommendation may become automatic while discretion remains in the definition of a valid shortage. If a model was trained on prior approvals, the labels may preserve historical judgements. Moving the reviewer to the end of the process does not necessarily give that reviewer control over those earlier choices.

Joseph and Gaba (2020) connect structure, information processing and decision-making through aggregation and constraint perspectives. The first asks how contributions are combined; the second asks how available behaviour and choice are restricted. Together, the perspectives connect information provision with the narrowing of alternatives. They offer complementary questions for an AI service rather than a ready-made score of decision quality. [Joseph and Gaba (2020)](#joseph-and-gaba-2020)

## Distinct acts in one workflow

| Act | Fictional example | What it does not establish |
|---|---|---|
| Information provision | Show the customer's report | That the report is correct |
| Calculation | Subtract ten from twelve | Why the difference occurred |
| Recommendation | Propose a credit | Permission to issue it |
| Decision | Select the response | That execution succeeded |
| Authorisation | Permit the specified credit | That all relevant alternatives were considered |
| Execution | Create the credit transaction | That the customer problem is resolved |
| Recording | Store the action and actor identifier | Answerability or decision quality on its own |

These are working distinctions for analysing the service. They can overlap in practice, so the point is to identify each operation rather than force every event into an exclusive category.

## A worked review arrangement

Harbour proposes that the assistant prepare options, their evidence and unresolved claims. The reviewer can inspect sources, request clarification, reject the proposal or choose a permitted response. Approval refers to a specific proposal version. If quantities change, that approval cannot silently authorise a different proposal. The execution service separately checks the permitted operation and records its result.

This design makes some forms of control inspectable. It does not prove meaningful review. A reviewer who lacks time, knowledge or practical permission to disagree may still routinely confirm the recommendation. Conversely, frequent overrides may indicate healthy challenge, poor drafts or inconsistent policy. The interpretation needs case evidence.

Useful inquiry follows several cases from source selection through review to execution, including rejected proposals. It records what reviewers inspected, what they changed, which alternatives were absent and how disputed premises were revised. Recorded clicks alone answer a narrower question.

## Facts, values and the alternatives that disappear

A **factual premise** concerns what is treated as the state of the world. A **value premise** concerns what is preferred or regarded as acceptable. The distinction helps unpack a recommendation, although the two can be intertwined in a category or rule. In Simon's account, organisational influence can operate through both kinds of premise. [Simon (1997)](#simon-1997)

For Harbour, an order quantity is a factual input. Giving priority to urgent customer needs is a value choice. The rule defining an urgent case connects observations with a judgement about priority. A model that predicts urgency from historical labels does not remove that judgement; it learns a representation of selected earlier classifications. A technically accurate prediction can reproduce a category that the organisation ought to reconsider.

Alternatives also deserve inspection. An assistant may offer “credit” and “reject” while omitting “request a recount” or “confirm a second shipment”. The final reviewer can choose between the displayed options and still lack a relevant alternative. Restoring meaningful judgement may therefore require changing the menu, evidence or task framing rather than adding another approval gate. This is an AI design interpretation of decision-premise reasoning.

Exception handling provides a test of the arrangement. Can an actor identify a case that does not fit the available programme? Can the case remain unresolved without being misclassified? Can the reason for the exception reach someone who can revise the programme? These questions distinguish discretion within a rule from the capacity to change the rule itself.

## Decisions also communicate responsibility and legitimacy

Decisions can do more than select an operational response. Brunsson (1990) examines decisions as ways of allocating responsibility and producing legitimacy. A formal decision can show that an organisation has considered an issue or followed a recognised procedure, without transparently determining subsequent action. This does not make the decision meaningless; it means that its function must be investigated. [Brunsson (1990)](#brunsson-1990)

Feldman and March (1981) similarly examine information as signal and symbol. Collecting and displaying information may communicate competent management even when its contribution to a particular choice is limited. More information on a screen is therefore not sufficient evidence of a better decision process. [Feldman and March (1981)](#feldman-and-march-1981)

**Fictional AI application.** A dashboard shows a confidence score, citations and a completed approval trail. These features may support useful checking. They may also reassure an audience that the system is controlled while leaving the decisive assumptions difficult to challenge. The inquiry should examine which information changed a judgement, whether disagreement could alter the result and what happened after a recorded approval.

This is where **traceability** and **accountability** separate. Traceability makes selected events reconstructable. Accountability requires an answerability relationship: an actor can be required to explain conduct, and the explanation can have consequences. An execution log may support that relationship, but the log does not create it on its own. A service needs a practical route from an identified problem to an actor who can explain, correct or change the arrangement.

## Study pause: follow a threshold backwards

An assistant recommends automatic processing below £50. Identify the judgements hidden behind that apparently simple rule.

**Worked response:** Someone chose the amount, defined the eligible case population, decided which evidence is sufficient, set the exception conditions and accepted the consequences of mistakes. Review should examine those premises as well as whether the comparison in code is correct. The threshold is a teaching assumption, not a recommended policy.

## Continue with the course

Apply these concepts to [the pilot's worked business design](../../modules/01-standalone-foundations/06-business-design.md) and [the exercises](../../modules/01-standalone-foundations/07-assessment.md). The [standalone curriculum](../../CURRICULUM.md) identifies how later planned modules will develop the technical and organisational questions together.

## References

### Simon (1955)

Simon, H. A. (1955). A behavioral model of rational choice. *Quarterly Journal of Economics, 69*(1), 99–118. [Publication](https://doi.org/10.2307/1884852) · [Carnegie Mellon archival reprint](https://iiif.library.cmu.edu/file/Simon_box00063_fld04838_bdl0001_doc0001/Simon_box00063_fld04838_bdl0001_doc0001.pdf).

### Simon (1997)

Simon, H. A. (1997). *Administrative Behavior: A Study of Decision-Making Processes in Administrative Organizations* (4th ed.). Free Press.

### March and Simon (1993)

March, J. G., and Simon, H. A. (1993). *Organizations* (2nd ed.). Blackwell. Originally published in 1958.

### Aghion and Tirole (1997)

Aghion, P., and Tirole, J. (1997). Formal and real authority in organizations. *Journal of Political Economy, 105*(1), 1–29. [Publication](https://doi.org/10.1086/262063).

### Bovens and Zouridis (2002)

Bovens, M., and Zouridis, S. (2002). From street-level to system-level bureaucracies: How information and communication technology is transforming administrative discretion and constitutional control. *Public Administration Review, 62*(2), 174–184. [Publication](https://doi.org/10.1111/0033-3352.00168).

### Joseph and Gaba (2020)

Joseph, J., and Gaba, V. (2020). Organizational structure, information processing, and decision-making: A retrospective and road map for research. *Academy of Management Annals, 14*(1), 267–302. [Publication](https://doi.org/10.5465/annals.2017.0103).

### Brunsson (1990)

Brunsson, N. (1990). Deciding for responsibility and legitimation: Alternative interpretations of organizational decision-making. *Accounting, Organizations and Society, 15*(1–2), 47–58. [Publication](https://doi.org/10.1016/0361-3682%2890%2990012-J).

### Feldman and March (1981)

Feldman, M. S., and March, J. G. (1981). Information in organizations as signal and symbol. *Administrative Science Quarterly, 26*(2), 171–186. [Publication](https://doi.org/10.2307/2392467).
