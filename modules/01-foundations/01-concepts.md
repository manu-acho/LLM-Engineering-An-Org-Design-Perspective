# Lesson 1.1: What a language model does with your request

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Begin with the short delivery

A customer ordered twelve boxes and reports receiving ten. The account manager asks an AI assistant: “Summarise the problem and suggest what we should check.” It produces a sensible paragraph. What happened between the request and the answer?

The application first assembled some text: the customer's message, perhaps the order record, and instructions about the answer. It sent that input to a model. The model generated a continuation. The application displayed it. Looking fluent is one property of the output. Whether it used the right order, preserved the uncertainty and suggested a permitted next step are different questions.

This lesson opens that chain. We will use **language model** for a learned system that processes and generates language, and **application** for the larger program around it. A model by itself does not automatically open the order system or know your company's credit policy.

## Text becomes tokens

Computers calculate with numerical representations. Before a model processes text, a **tokenizer** converts it into units called **tokens**, each associated with a numerical identifier. A unit might be a whole word, part of a word, a space combined with a word, punctuation or another fragment. Different tokenizers divide the same text differently.

Imagine a toy tokenizer dividing “delivery delayed” into `delivery`, ` delay` and `ed`. This is an illustration, not the output of a particular real tokenizer. The important point is that tokens are not equivalent to words. A 1,000-word report does not have an invariant 1,000-token representation.

Why should an executive care? Services often constrain and measure inputs in tokens. More importantly, someone must decide what information reaches the model. A technical limit can become an organisational attention limit: the qualification at the end of a complaint may be excluded while the opening allegation remains.

## Predicting a continuation

At a generation step, the model calculates scores for possible next tokens based on the sequence already available. Those scores determine a probability distribution, a set of probabilities over alternatives. The system selects a token according to its generation settings, adds it to the sequence and repeats.

“Probability” here concerns a possible continuation. It does not mean the probability that a statement is true. A false statement can be a familiar and therefore likely continuation. The model also uses patterns learned across many training examples; it is not simply copying the most recent sentence from a database.

Suppose the input ends “The customer reports a shortage of”. Producing “two boxes” may be supported if the quantities are supplied. Producing “two boxes because the warehouse miscounted” adds a causal claim. The subtraction can be right while the explanation is invented. A useful prompt asks the model to distinguish supplied facts, calculations and unresolved explanations.

## Training and inference are different activities

**Training** changes numerical parameters, the model's learned values. A training procedure presents examples, measures a numerical error called a loss, and adjusts selected parameters. You will examine that process in Modules 6 and 7.

**Inference** uses learned parameters to produce an output for an input. When you paste the delivery complaint into a request, you are normally supplying inference input. You are not retraining the model simply by adding that paragraph. This explains why providing a policy in a conversation can help that conversation without establishing a durable update to the underlying model.

Think of a calculator with a particular implementation and numbers entered for one calculation. Entering twelve and ten changes the current calculation, not the calculator's arithmetic rules. The analogy helps distinguish parameters from inputs, although a language model's behaviour is learned and much less transparent than basic arithmetic.

## Prompts specify a task and supply evidence

A **prompt** is the input framing and content supplied to the model. It may include instructions, a question, examples and documents. The application often gives messages different roles, such as system instructions and user requests. A role is part of the interface for organising input; it does not make a factual assertion true.

Compare two instructions:

> Explain why the warehouse failed to deliver the full order.

> Summarise the customer's report. Distinguish reported quantities from verified quantities. List evidence needed before assigning a cause.

The first presupposes a warehouse failure. The second leaves that conclusion open. Prompting is therefore partly the design of a task and its acceptable claims, not just finding persuasive wording.

An example answer can clarify the intended structure. This is often called **few-shot prompting** when several examples are supplied, or **one-shot prompting** for one example. Examples can also bias the answer toward their categories. Ask whether an important case falls outside those examples.

## Context is what is available now

The **context** is the information available for a particular model computation. The **context window** is a model-specific token capacity, subject to its input and output rules. The application must assemble what fits: instructions, conversation, evidence and room for a response.

If the customer earlier wrote “Do not issue a credit until we recount,” but that turn is absent, the model may not account for it. Conversation continuity depends on the application providing or managing relevant state. A remembered-looking answer does not show that model parameters have changed.

Longer context makes more material available. It does not guarantee that every relevant qualification will be used. We therefore need checks on what was supplied and what the answer claims, rather than relying on context size as a quality measure.

## A first application architecture

The original week 1 summariser follows a simple sequence: fetch a webpage, extract readable text, construct messages, request generation, extract the answer and display it. Fetching and extraction occur before generation. If extraction returns only the navigation menu, the model cannot recover the missing report from that input.

This is a **pipeline**: a sequence of operations in which one output becomes a later input. The word is useful because it directs attention to individual stages. Did the program gather the right material? Did it prepare the task fairly? Did generation remain grounded? Did the interface display a complete answer?

The next lesson traces an intentionally small pipeline with no network access. The size is deliberate: you should be able to account for every value before introducing a real provider.

## Explain it back

In your own words, explain why a model can write a convincing answer without verifying the complaint. Then explain what changes when you include an order record in the prompt.

**Worked response:** The model generates a continuation from available input and learned patterns. Convincing language is not an independent check against the order system. Supplying the record changes the evidence available during inference; it does not establish that the record is accurate, that the model used it correctly or that the model has been retrained.

**Reading connection:** The compact [week 1 chapter](../01-foundations-and-pipelines.md) links the original notebook and scraper functions. Technical source notes are in the [source map](../../SOURCE-MAP.md).

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Input selection changes which evidence is available for later work. The research chapter explains [information demand and capacity](../../reference/research/01-organisation-design.md#information-demand-and-capacity).
