# Start here: learning AI engineering without a technical background

Imagine that an operations manager receives this message: “The customer says the delivery arrived short, but the warehouse record says complete. Can we issue a credit?” Answering well involves more than writing a courteous sentence. Someone must identify the customer and order, understand what the records mean, reconcile the disagreement, know the rules, and locate a person with authority to act.

AI engineering concerns how to build a system that can perform selected parts of that work reliably. Organisation design concerns how those parts connect to other work, who owns them, and what happens when they do not fit the expected pattern. The guide explains the two together and opens up the code so you can see what is being built.

You do not need to arrive knowing Python, statistics, cloud computing or machine learning. When an unfamiliar term is needed, a lesson introduces it before relying on it. Some concepts take several encounters. Being able to repeat a definition is different from being able to trace an example; the worked lessons are there to support that second step.

## Inspired by Ed Donner's LLM Engineering course

This guide is inspired by and builds on [Ed Donner's LLM Engineering course](https://github.com/ed-donner/llm_engineering). His course provides the engineering foundation: a practical sequence of notebooks and projects covering model requests, conversation and tools, open models, evaluation, retrieval, training and agents. The eight modules here follow that broad progression. Credit for the original course, its projects and its implementation examples belongs to Ed and the contributors credited in his repository.

This guide develops that foundation in three connected ways:

- **Step-by-step explanations of concepts and code.** Concepts are introduced in ordinary language. Small code examples explain what enters a program, what each important instruction does, what comes back and how it can fail. Alternatives help show why a pattern might be useful and when a simpler approach would do.
- **A connection from technical behaviour to business decisions.** Each module asks what a mechanism would change in work, how its value could be assessed and what evidence would justify using it. A faster answer, for example, may still leave a delivery dispute unresolved.
- **An organisation-design perspective throughout.** Literature from organisation design research helps examine handoffs, shared understanding, decision authority, routines and the conditions needed for a feature to become useful. The continuing Harbour Services case connects these questions across the modules.

The purpose of these additions is to help readers move between understanding a mechanism and judging its use at work. Managers and executives can explore the concepts and organisational choices, while readers who want technical depth can follow the code.

### How the links connect the two

The code lessons and compact engineering references link to the relevant notebooks and helper files in Ed's GitHub repository. For example, Module 1 connects its small evidence-to-brief program to [the original first notebook](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day1.ipynb). Follow those links to compare the explanation here with the original implementation. The small worked examples in this guide are identified separately from the original course code.

Course-file links use the repository version used to prepare these explanations, so a reference stays aligned with the code it discusses. [Ed's current repository](https://github.com/ed-donner/llm_engineering) may include newer material. The [source guide](SOURCE-MAP.md) maps the modules to the original course and explains coverage limits, including remote lessons that were not available for review.

This is an independent companion. It does not reproduce the full course or its videos, and it does not imply Ed's endorsement. It can be read alongside his course, with the original projects providing a route into further practice.

## How to use the guide

Start with the concepts in each module, then follow the code and the business application. Each part answers a different question: How does it work? What do the instructions do? What would this change in an organisation?

If a code passage is unfamiliar, read its explanation and trace a small example before trying to run it. Write down what enters the program, what changes and what comes back. You do not need to memorise every symbol or install every library to understand the pattern.

For an initial overview, you can read the concepts and business applications first. Return to the code when you want to inspect how a claim becomes an actual operation. The [workbook](WORKBOOK.md) helps you connect the three parts through short exercises.

Harbour Services is a fictional case used throughout the guide. The examples explore possible designs and consequences; they do not report results from a real deployment.

## What is a computer program?

A program is a set of instructions a computer can execute. A person might instruct a colleague to “look up the order, compare the quantities and flag any difference.” A computer needs those operations expressed in a language it can run, with precisely specified inputs and rules. Python is one such programming language.

The following is Python:

```python
ordered = 12
received = 10
difference = ordered - received
```

`ordered` is a **variable**, a name associated with a value. The first line associates the name with the number 12. The equals sign assigns a value; it is not asking whether two values are equal. The third line subtracts received from ordered and stores the result under another name. The computer calculates 2. It does not know whether a shortage occurred, whether the records are trustworthy or whether a credit is appropriate.

That distinction is already organisationally important: a correct calculation can be an input to a disputed business interpretation.

## Files, folders and running code

A **file** stores information, such as text, a photograph or a program. A **folder** groups files. A filename ending in `.md` contains Markdown, ordinary text with conventions for headings, links and code blocks. The files you are reading are Markdown. A `.py` file contains Python code. A `.ipynb` file is a Jupyter notebook, which contains separate cells of explanation and code, sometimes with saved outputs.

To **run** code is to ask an interpreter or runtime to execute it. Reading a `.py` file does not run it. Opening a notebook does not mean that all its cells have executed. Its **kernel** is the running Python process associated with it. A cell can create a variable that a later cell uses. Running later cells first can therefore fail. Restarting the kernel removes that in-memory state, even though the notebook file still exists.

A **terminal** accepts text commands for operating the computer. A **code editor** helps you read and edit program files. A **library** is reusable code written for others to call. `import json` makes Python's JSON library available. Installing a library and importing it are different acts: installation makes its files available in an environment; import makes its functions available to a running program.

An **environment** is a particular collection of Python and installed libraries. Two notebooks can look identical while using different environments. This explains many “it works in one place” problems without implying that the underlying concept is wrong.

## Functions, inputs, outputs and effects

A **function** groups an operation under a name:

```python
def shortage(ordered, received):
    return ordered - received

result = shortage(12, 10)
```

`def` introduces the function. Names inside the parentheses are **parameters**, the placeholders it will use. `shortage(12, 10)` calls the function with **arguments**, actual values. `return` sends a result back to the caller. Indentation indicates which lines belong inside the function.

An **input** is information supplied to an operation. An **output** is what it produces. A **side effect** is an interaction beyond producing a value, such as saving a file, sending an email or changing an order. A function that drafts a credit explanation and one that issues the credit have very different effects, even if both accept the same input.

In every code lesson, ask four questions: What enters? What changes? What comes back? What happens if a step fails?

## How programs talk to other systems

An **interface** is an agreed way to interact. A restaurant order form specifies the information a diner supplies; the kitchen can work behind that interface without exposing every internal action. A software **API**, or application programming interface, serves a related purpose for programs. It specifies operations, inputs and responses. The analogy is limited: APIs also have precise data formats, authentication and error rules.

An **endpoint** is an address for a particular service operation. **HTTP** is a protocol commonly used to send requests and responses over a network. A Python program can request a webpage or ask an inference service to generate text. Those are distinct requests to distinct services.

A **client** is code that makes requests. A **server** receives them and performs or delegates work. “Cloud” means that some computing happens on infrastructure accessed over a network, rather than necessarily on your own laptop. It does not by itself specify who can see the data or how the service is governed.

**Authentication** establishes which identity is making a request. **Authorisation** determines what that identity may do. An API key can identify a program to a service; it is not a substitute for defining the business actions that program should be allowed to perform.

## Structured data and generated language

A **string** is text. A **list** is an ordered collection. A **dictionary** associates keys with values:

```python
request = {"id": "R-17", "ordered": 12, "received": 10}
```

`request["received"]` retrieves the value associated with that key. The quotation marks distinguish text from variable names. JSON is a text format for exchanging structured values between programs. Python dictionaries and JSON resemble one another, but they are not the same representation: JSON must be parsed before ordinary Python code can use its fields.

An LLM can generate text that resembles a record. That text needs checks before it becomes operational input. A correctly shaped record can still contain a wrong order number or an invented approval. The lessons separate checking shape, checking evidence and checking authority.

## A model is one component

A **model** is a learned numerical system used to make predictions or generate output. An **application** combines models with user interaction, data preparation, business tools, state and error handling. A **workflow** specifies how activities connect. When a demo fails, the model may not be the failing component. The webpage extractor may have returned nothing, the wrong record may have been retrieved or an execution receipt may have been ignored.

Learning to locate the failure is part of learning the mechanism. Breaking an application into these parts makes its behaviour easier to understand and investigate.

## Learning through one continuing situation

Harbour Services, our fictional organisation, receives delivery complaints and internal service requests. Sales knows the customer relationship; operations sees fulfilment records; finance controls credits; specialists handle exceptions. In later lessons, the short-delivery example becomes a summary, a conversation, an evidence retrieval task, a classification exercise and a proposed workflow.

The continuity is intentional. You can see what each technical addition changes without needing to learn a new business situation every time. Additional short cases show when the same design should not be transferred mechanically.

When you encounter a difficult term, return to an example and explain what the computer or person does. If you can say, “This function turns a question into a search request, but does not decide which policy is legitimate,” you understand more than the acronym alone conveys.

[Begin Module 1](modules/01-foundations/README.md) · [Curriculum index](README.md)
