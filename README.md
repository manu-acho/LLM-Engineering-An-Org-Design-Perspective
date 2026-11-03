# AI engineering and organisation design

A fluent AI answer can look like a finished piece of work. But where did its information come from? What did the program check? Who can act on the answer, and who handles a mistake?

This guide explores those questions through eight modules. It explains how AI applications work and what it takes to make them useful in an organisation. It is written for managers, executives, practitioners and anyone curious about AI. No programming background is required.

Inspired by [Ed Donner's LLM Engineering course](https://github.com/ed-donner/llm_engineering), it builds on the original engineering projects with step-by-step code explanations, business applications and ideas from organisation design research. [Read how the two connect](START-HERE.md#inspired-by-ed-donner-s-llm-engineering-course).

## What you will learn

You will learn to follow a request through an AI application, recognise common programming patterns, compare design alternatives and judge claims about business value. Along the way, you will examine how AI changes handoffs, decision-making, responsibility and everyday work.

The technical and organisational explanations belong together. Understanding a permission check helps explain who can act. Understanding a retrieval filter helps explain which evidence an answer can use. Understanding training data helps reveal whose past decisions a model may reproduce.

## Find a starting point

Start with [the orientation](START-HERE.md) if terms such as API, model or Python are unfamiliar. It introduces the vocabulary used in the lessons through a simple delivery problem.

Each module has three connected parts:

1. **Concepts:** understand the mechanism through an example.
2. **Code:** follow a small program, see what its instructions do and compare alternatives.
3. **Business and organisation:** examine what the design means for people, decisions and the wider workflow.

Read all three parts for the fullest understanding. For an initial overview, begin with concepts and business applications, then return to the code. The code lessons explain their examples step by step; you can follow them on paper without running paid services or training a model. Module 8 includes an additional lesson that brings the ideas together.

## Explore the modules

| Module | Understand the mechanism | Work through the code | Apply organisational judgement |
|---|---|---|---|
| [1. Foundations](modules/01-foundations/README.md) | [Requests, tokens, training and context](modules/01-foundations/01-concepts.md) | [Trace a brief through functions](modules/01-foundations/02-code-workshop.md) | [Information preparation and integration](modules/01-foundations/03-business-and-organisation.md) |
| [2. Conversation](modules/02-conversation/README.md) | [History, state and tools](modules/02-conversation/01-concepts.md) | [Dispatch, permissions and streaming](modules/02-conversation/02-code-workshop.md) | [Premises, review and authority](modules/02-conversation/03-business-and-organisation.md) |
| [3. Open models](modules/03-open-models/README.md) | [Weights, tokenizers and inference](modules/03-open-models/01-concepts.md) | [Encode, generate and decode](modules/03-open-models/02-code-workshop.md) | [Meeting notes as organisational records](modules/03-open-models/03-business-and-organisation.md) |
| [4. Evaluation](modules/04-evaluation/README.md) | [Correctness, performance and value](modules/04-evaluation/01-concepts.md) | [Compare behaviour before speed](modules/04-evaluation/02-code-workshop.md) | [Metrics, fit and end-to-end work](modules/04-evaluation/03-business-and-organisation.md) |
| [5. Organisational knowledge](modules/05-rag/README.md) | [Search, embeddings, chunks and RAG](modules/05-rag/01-concepts.md) | [Filter and retrieve evidence](modules/05-rag/02-code-workshop.md) | [Knowledge boundaries and source authority](modules/05-rag/03-business-and-organisation.md) |
| [6. Data and baselines](modules/06-data/README.md) | [Features, labels, learning and evaluation](modules/06-data/01-concepts.md) | [Fit and inspect a baseline](modules/06-data/02-code-workshop.md) | [Historical assignments and desired work](modules/06-data/03-business-and-organisation.md) |
| [7. Specialisation](modules/07-specialisation/README.md) | [Fine-tuning, LoRA and QLoRA](modules/07-specialisation/01-concepts.md) | [Prompt/completion and loss labels](modules/07-specialisation/02-code-workshop.md) | [Categories, discretion and change](modules/07-specialisation/03-business-and-organisation.md) |
| [8. Agents and operations](modules/08-agents/README.md) | [Workflows, state and bounded action](modules/08-agents/01-concepts.md) | [Simulate checks and receipts](modules/08-agents/02-code-workshop.md) | [Design an operating organisation](modules/08-agents/03-business-and-organisation.md) |

## Follow one problem as it develops

Harbour Services is a fictional organisation handling a disputed delivery. The customer reports missing boxes, the warehouse record says the order is complete, and finance needs evidence before issuing a credit.

Across the modules, this situation becomes a brief, an assistant conversation, meeting notes, a search task, a classification problem and a proposed workflow. Following the same situation makes it easier to see what each technical addition changes. The case figures and events are invented for learning, not reported implementation results.

## Use the supporting material

The [workbook](WORKBOOK.md) offers exercises and templates for applying the lessons. The [glossary](reference/glossary.md) explains unfamiliar terms, and [Python patterns](reference/python-patterns.md) gives a closer look at common code structures. Each module also links to a compact engineering reference for exploring the original implementations.

The organisational discussions draw on literature from organisation design research. The [literature guide](reference/literature-guide.md) introduces the six topics and links to the reviews. The [source guide](SOURCE-MAP.md) explains the engineering material, its coverage and its limits.

Links to original notebooks open on GitHub so you can connect an explanation to the code it discusses.
