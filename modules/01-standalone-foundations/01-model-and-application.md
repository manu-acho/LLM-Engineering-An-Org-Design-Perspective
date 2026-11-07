# Lesson 1.1: A model, an application and a business problem

[Download the lesson notebook](/downloads/01-model-and-application.ipynb) · [Notebook setup and study workflow](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: first Python steps](02-python-first-steps.md)

## Business context: Harbour

An adviser needs to distinguish a recorded dispatch quantity from verified receipt before making a promise to the customer.

[Company and supply-chain context](../../HARBOUR.md) · [Module 1 business situation](../../reference/harbour-learning-journey.md#module-1)

## From the business to the discrepancy

**Fictional teaching case.** Harbour distributes packaging materials to businesses that use them to pack and dispatch their own goods. Its service connects purchasing and inventory with warehouse fulfilment, transport, customer service and finance. Read [Meet Harbour](../../HARBOUR.md) for the company, roles and complete business workflow.

The first task is narrower than that workflow: prepare an investigation brief for case H-17. Its order record says twelve boxes. The shipment record also says twelve. The customer reports receiving ten. An adviser wants a short investigation brief.

Three claims are available. The records state what their systems contain; the customer supplies an account of receipt. The difference between twelve and ten is two. The cause is unknown. A useful brief can preserve those distinctions while making the next investigation easier.

An AI demonstration might instead produce: “The warehouse failed to send two boxes.” That sentence adds both a confirmed shortage and a cause. Neither follows from the available information. A convincing sentence and a supported claim are different properties.

## The application around the model

A **model** is a learned system used to produce an output from an input. A **language model** estimates probabilities over language sequences or continuations. A modern language model may be one component within a larger **application**, the program that gathers information, prepares a task, calls services, checks results and presents them.

The application can retrieve an order record if a developer supplies that connection and access permits it. The language model does not automatically know the current order merely because the application has a screen labelled Orders. The record must reach the model through input or an available tool path.

The distinction also identifies failures. A wrong brief can originate in a missing source, an incorrect transformation, an unsuitable instruction, generation, an inadequate check or misleading display. Replacing the model addresses only some of these possibilities.

## What is learned and what is written as a rule?

In ordinary deterministic code, a developer specifies operations such as subtracting one quantity from another. Given the same valid inputs and implementation, the calculation returns the same result. A learned model acquires parameters or statistical counts from examples. Its output depends on what was learned and how inference selects a result.

The pilot includes both. `build_brief` is deterministic evidence preparation. `train` estimates word-transition counts from four supplied sentences. `generate` uses those learned counts to select a continuation. The brief builder is not a pretend LLM, and the tiny model is not a pretend order-verification system.

**Training** changes the learned representation using examples. **Inference** uses that representation for an input. Supplying an order record as context ordinarily changes the current input, not the model's learned parameters. Correcting an answer in a conversation does not by itself demonstrate a persistent training update.

## Input, output and action

A **prompt** supplies a task and relevant material. A **response** is the returned output. An **action** changes something, such as creating a case assignment or issuing a credit. These operations may be connected in an application, but generating a response is not permission to execute an action.

At Harbour, the first permitted contribution is an investigation brief. The recipient can inspect sources and request clarification. The prototype neither confirms a cause nor changes a customer account. That bounded scope makes the output assessable before adding more responsibility.

The application can help preserve the boundary by carrying source identifiers, labelling reported and recorded quantities, retaining unresolved questions and restricting available operations. Those mechanisms do not prove that a future generated answer is correct. They make particular assumptions and checks inspectable.

## Study pause

Which part of the system should calculate twelve minus ten, and what would that calculation establish?

**Worked response:** ordinary code can calculate the difference as two. It establishes the difference between the selected inputs under their stated meanings. It does not independently verify receipt or identify the cause. A model can help express the comparison, but no generation is required for the subtraction.

The [decision research chapter](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow) explains why calculation, recommendation, authorisation and execution need separate examination. The next lesson makes these distinctions visible in a small program.

## Try the live model

The [live-model guide](../../reference/live-model-guide.md) prepares the API configuration. The matching notebook adds a real request and records the returned model, status, usage and duration. Inspect every factual claim. In a development run, the model inferred shipped quantity from an order record; the source did not establish that inference. The [worked experiment record](../../reference/worked-model-experiments.md) explains this observed failure and the later corrections.
