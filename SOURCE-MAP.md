# Sources and further reading

[Guide index](README.md) · [Literature foundation](reference/literature-guide.md)

## The engineering course

This is an independent learning companion to [Ed Donner's LLM Engineering course repository](https://github.com/ed-donner/llm_engineering). The course supplies the sequence of engineering topics and the original notebooks and helper programs. This guide adds plain-language explanations, small worked examples, alternatives, and business and organisation-design discussions. It does not claim affiliation with or endorsement by the original course author.

The [acknowledgement in Start here](START-HERE.md#inspired-by-ed-donner-s-llm-engineering-course) explains the relationship, the additions and how to use the two resources together.

Links to course files point to revision `103f4bf045180f3b8b7721fd55b7897305a72672`. This keeps the references aligned with the version used to prepare these lessons. [The current repository](https://github.com/ed-donner/llm_engineering) may contain newer examples. Model names, libraries and service interfaces can change, so check the relevant provider documentation before running an integration.

The original course repository has an [MIT licence](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/LICENSE). Course files open on GitHub rather than being bundled into this reader. Separately supplied videos and slides are outside this guide's coverage.

## The organisation-design literature

The organisational lessons draw on literature from organisation design research, covering how work is divided, coordination, decision-making, system implementation, routines and technology in practice. The [literature guide](reference/literature-guide.md) introduces the ideas and links directly to six reviews.

The reviews use enterprise software, including SAP, as a research setting. Here, selected concepts help us examine fictional AI examples. A finding from an enterprise-system study does not establish that an AI application will have the same result.

The reviews are the sources consulted for this synthesis. References to original authors identify where ideas come from; they do not imply that every original article was independently read for this guide. The literature links use a fixed revision so their content stays aligned with the explanations.

## What the guide covers

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

## Reading the cases and evidence

Harbour Services is a fictional organisation. Its delivery dispute connects the modules so you can follow the same problem through different technical and organisational choices. Its events, figures and outcomes are fictional examples, not reported findings.

The guide distinguishes what software is designed to do, how it is configured, how people use it, and what results follow. A working demonstration does not establish a business benefit. Similarly, checks of example-code syntax and selected examples do not certify that every original notebook or integration will run in a new environment.

For detailed research claims, consult the original study and check the relevant edition and passages. The cases here support learning and comparison; they do not establish operational benefits or certify a working deployment.
