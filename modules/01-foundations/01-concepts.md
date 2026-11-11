# Lesson 1.1: What a language model does with your request

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Begin with the short delivery

Harbour sells packaging to other businesses. A customer says ten of the twelve boxes it ordered arrived, and an adviser asks an assistant to draft an investigation brief. Before asking how the assistant knows what to write, start with a simpler question: how does a phone suggest the next word?

Imagine typing `the parcel is` and seeing a phone suggest `delayed`. The text already typed is a **sequence**: pieces of text in a particular order. A **continuation** is whatever gets added next. If the suggestion is accepted, the sequence becomes `the parcel is delayed`. The phone could then suggest another piece, such as a full stop. Each accepted piece becomes part of what comes before the next suggestion.

Where could the first suggestion come from? Suppose a very simple program has seen ten examples that begin with `the parcel is`. In six, the next word was `delayed`; in three it was `ready`; in one it was `missing`.

| Possible next word | Count out of ten examples | Estimated probability in this example |
| --- | ---: | ---: |
| delayed | 6 | 60% |
| ready | 3 | 30% |
| missing | 1 | 10% |

A **probability** expresses how likely a particular possibility is under a stated assumption or model. In this counting example, the estimate for `ready` is three out of ten, or 30%. It applies when the preceding words are `the parcel is`. A different beginning could give very different estimates. The 60% estimate describes the word that follows those three words in the examples. To estimate the chance that a particular parcel is delayed, Harbour would need evidence about that delivery.

A **language model** learns patterns in text that it can use to give possible next pieces different chances. A piece of text used by the model is called a **token**. It can be a word, part of a word, punctuation or another piece. The phone example uses whole words and simple counting so the arithmetic is visible. Large language models (LLMs) learn much richer numerical patterns; they do not have to find ten identical openings and count the following words. A model can build a longer answer by selecting a piece, adding it to the text and repeating the process. Different ways of selecting pieces can produce different answers.

The assistant can draft a plausible sentence such as “Two boxes went missing in the warehouse.” The records do not establish that cause. Harbour needs a person to check what each source says and where the accounts disagree. The **application** is the software around the model. It can look up records, prepare a request and check the draft, provided it has the relevant connections and permissions. For the model to use an order record, the application must include it in the request or make it available through a permitted lookup.

[Meet Harbour and follow the delivery investigation](../../HARBOUR.md).

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

In the phone example, what does the 30% describe? Then explain why a model can write a convincing answer without verifying the complaint. What changes when you include an order record in the prompt?

**Worked response.** Three of the ten examples use `ready` after `the parcel is`. The model generates a continuation from available input and learned patterns. Convincing language is not an independent check against the order system. Supplying the record changes the evidence available during inference; it does not establish that the record is accurate, that the model used it correctly or that the model has been retrained.

**Reading connection:** The compact [week 1 chapter](../01-foundations-and-pipelines.md) links the original notebook and scraper functions. Technical source notes are in the [source map](../../SOURCE-MAP.md).

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Input selection changes which evidence is available for later work. The research chapter explains [information demand and capacity](../../reference/research/01-organisation-design.md#information-demand-and-capacity).
