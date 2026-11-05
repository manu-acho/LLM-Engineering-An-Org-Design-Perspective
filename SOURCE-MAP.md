# Sources and further reading

[Guide index](README.md) · [Literature foundation](reference/literature-guide.md)

## The engineering course

This is an independent learning companion to [Ed Donner's LLM Engineering course repository](https://github.com/ed-donner/llm_engineering). The course supplies the sequence of engineering topics and the original notebooks and helper programs. This guide adds plain-language explanations, small worked examples, alternatives, and business and organisation-design discussions. It does not claim affiliation with or endorsement by the original course author.

The [acknowledgement in Start here](START-HERE.md#inspired-by-ed-donner-s-llm-engineering-course) explains the relationship, the additions and how to use the two resources together.

Links to course files point to revision `103f4bf045180f3b8b7721fd55b7897305a72672`. This keeps the references aligned with the version used to prepare these lessons. [The current repository](https://github.com/ed-donner/llm_engineering) may contain newer examples. Model names, libraries and service interfaces can change, so check the relevant provider documentation before running an integration.

The original course repository has an [MIT licence](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/LICENSE). Course files open on GitHub rather than being bundled into this reader. Separately supplied videos and slides are outside this guide's coverage.

## The Agents course

[Ed Donner's Agents course](https://github.com/ed-donner/agents) provides the engineering foundation for Modules 9 to 14. The [agents source guide](reference/agents-source-guide.md) maps its six sections to those modules and identifies the selected notebooks, configuration and application code paths examined.

Agents-course file links use revision `542a7036c321a9308379507b06ce8d0deb370d5d`. Part II adds small worked examples, framework comparisons and organisational applications. Original API calls, notifications, browser workflows and trading examples were not executed. The source guide distinguishes source reading, dependency-free examples and integration requirements.

## Organisation design research

The [research reading guide](reference/literature-guide.md) opens six chapters on designing work, coordinating contributions, making decisions, implementation, routines and technology in practice. They explain the concepts through AI-supported business cases and include their own scholarly references, exercises and worked responses.

Individual lessons link to the relevant concepts inside the reader. The research chapters connect technical operations, such as filtering evidence, routing a case or checking a proposal version, with questions about information, responsibility, discretion and organisational outcomes.

The chapters distinguish theory from findings in particular settings and from fictional applications. A simulation of organisational design is not an empirical AI deployment; a successful enterprise-system implementation is not proof of benefit from a language-model service. References identify the publications supporting the conceptual argument.

## Part I coverage

| Module | Original course material | Limits to keep in mind |
|---|---|---|
| 1. Foundations | Week 1 notebooks, scraper and summary pipeline | No root-level day 3 notebook in the inspected version |
| 2. Conversation | Week 2 notebooks, callbacks, lookup and dispatch | Provider examples illustrate patterns, not a current model catalogue |
| 3. Open models | Week 3 local notebooks and visualizer | Most substantive labs link to external Colab notebooks; their remote cells were not reviewed |
| 4. Evaluation | Week 4 days 3 to 5 and code-generation helpers | No root-level days 1 or 2 notebooks; stored results are historical |
| 5. Knowledge and retrieval | Week 5 ingestion, answering and evaluation code | Example knowledge-base facts are not independently verified |
| 6. Data and baselines | Week 6 preparation, parsing, batch and evaluation code | No dataset upload, training or model inference was performed for this guide |
| 7. Specialisation | Week 7 preparation and evaluation helpers, plus week 8 adapter serving | Remote training cells were unavailable; added lifecycle explanations are labelled explanatory examples |
| 8. Agents and operations | Week 8 planners, services, agent framework and interface | Deployments and external actions were not executed |

The eight compact engineering references supplement the fuller module lessons. Notebook-cell references include explanation cells as well as code cells. Small Python examples are separate from integration sketches that need external libraries, accounts, model access or hardware.

## Expanded lesson coverage

Every module includes a [complete reading route](README.md) with six or seven lessons. The expanded routes add numerical mechanisms, inspected original-source walkthroughs, selected local library labs, and completed organisational design comparisons. The original compact references remain supplementary material.

The [local lab guide](reference/local-labs.md) identifies dependencies and separates standard-library code, library exercises, source reading and external integrations. New examples are independently authored and identified separately from Ed Donner's implementations. The local graph, vector-store, adapter and MCP examples illustrate particular interfaces and boundaries; they do not certify the source applications or a business deployment.

The remote Colab lesson contents remain outside inspected coverage. Attempts to retrieve the referenced training and meeting-note notebooks did not expose their cells. Independent local examples supplement those gaps without claiming to reproduce the inaccessible lessons. Lecture videos remain outside the source-reading scope.

Lesson research links open the relevant chapters inside the reader. Scholarly publication links support further study; the explanations and worked cases are available within the course.

## Reading the cases and evidence

Harbour Services is a fictional organisation. Its delivery dispute connects the modules so you can follow the same problem through different technical and organisational choices. Its events, figures and outcomes are fictional examples, not reported findings.

The guide distinguishes what software is designed to do, how it is configured, how people use it, and what results follow. A working demonstration does not establish a business benefit. Similarly, checks of example-code syntax and selected examples do not certify that every original notebook or integration will run in a new environment.

For detailed research claims, consult the original study and check the relevant edition and passages. The cases here support learning and comparison; they do not establish operational benefits or certify a working deployment.
