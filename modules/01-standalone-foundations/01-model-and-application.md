# Lesson 1.1: A model, an application and a business problem

[Download the lesson notebook](/downloads/01-model-and-application.ipynb) · [Notebook setup and study workflow](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: first Python steps](02-python-first-steps.md)

## What you'll learn and why it matters

Explain how a model builds a reply one piece at a time, and distinguish drafting text from checking a delivery. This distinction helps Harbour decide which parts of an investigation to assign to AI.

## Business context: Harbour

This lesson begins with a next-word suggestion and ends with a real question about work: what can an adviser tell a customer when two records disagree? The example and study questions can be followed without a notebook or API key.

[Company and supply-chain context](../../HARBOUR.md) · [Module 1 business situation](../../reference/harbour-learning-journey.md#module-1)

## From the business to the discrepancy

Harbour sells and delivers packaging to other businesses. One customer ordered twelve boxes so it could pack its own goods. The order says twelve, the dispatch record says twelve went out, and the customer says ten arrived. A customer service adviser has to tell the customer what Harbour knows and what it will investigate. The fictional case is called H-17.

The adviser can report a difference of two between the dispatch record and the customer's account. The adviser cannot yet say where two boxes went, or even confirm how many arrived. The warehouse record could be wrong, something might have happened during delivery, or the customer could have counted before all the boxes were unpacked. Checking the records with the people who handled the delivery is a separate step from writing a clear account of it. [The Harbour case](../../HARBOUR.md) describes the wider business; these are all the facts needed for this lesson.

## The application around the model

### Start with a suggestion on a phone

Imagine typing `the parcel is` and seeing a phone suggest `delayed`. The text already typed is a **sequence**: pieces of text in a particular order. A **continuation** is whatever gets added next. If the suggestion is accepted, the sequence becomes `the parcel is delayed`. The phone could then suggest another piece, such as a full stop. Each accepted piece becomes part of what comes before the next suggestion.

Where could the first suggestion come from? Suppose a very simple program has seen ten examples that begin with `the parcel is`. In six, the next word was `delayed`; in three it was `ready`; in one it was `missing`.

| Possible next word | Count out of ten examples | Estimated probability in this example |
| --- | ---: | ---: |
| delayed | 6 | 60% |
| ready | 3 | 30% |
| missing | 1 | 10% |

A **probability** expresses how likely a particular possibility is under a stated assumption or model. In this counting example, the estimate for `ready` is three out of ten, or 30%. It applies when the preceding words are `the parcel is`. A different beginning could give very different estimates. Crucially, 60% is an estimate about the next word in text. It is not a 60% chance that a real parcel is delayed.

A **language model** learns patterns in text that it can use to give possible next pieces different chances. A piece of text used by the model is called a **token**. It can be a word, part of a word, punctuation or another piece. The phone example uses whole words and simple counting so the arithmetic is visible. Large language models (LLMs) learn much richer numerical patterns; they do not have to find ten identical openings and count the following words. A model can build a longer answer by selecting a piece, adding it to the text and repeating the process. Different ways of selecting pieces can produce different answers. [Lesson 1.3](03-learning-and-generation.md) runs a small version of that process.

### Now return to Harbour

“Two boxes were lost in the warehouse” sounds like a natural continuation of a report about a discrepancy. The available records do not support that claim. The skill of producing a plausible sentence differs from the work of checking what happened.

An **application** is the software that helps someone do a job. In this case it can collect the order and dispatch records, include the customer's account, calculate the recorded difference and show where each number came from. It may ask a language model to draft a sentence using those details. The model sees only the material the software supplies or lets it request. It does not gain access to the current order merely because the application has a screen labelled Orders.

That separation also helps Harbour find faults. If the dispatch record never reached the draft, inspect how the software gathered the records. If the draft says the warehouse caused the shortage despite being given the right records, inspect how the draft was produced and checked. These failures call for different fixes.

## What is learned and what is written as a rule?

To subtract ten from twelve, a developer can write an explicit rule. With the same numbers, the same subtraction gives two every time. Such an operation is **deterministic**. It does not need to learn anything from examples. To make suggestions based on previous text, the simple program above instead has to collect examples and count what follows what.

**Training** is the step in which examples change what the model stores or learns, such as the counts in the table. **Inference** is the step in which a trained model is used on an input, such as when the phone sees the three words and makes a suggestion. Giving a model today's order record supplies material for this request. That alone does not retrain the model. A correction in a conversation can help with the next reply if included in that conversation; this does not show the model itself has permanently changed.

The lab separates the two jobs. `train` learns from four short sentences and `generate` uses the counts to continue a phrase. `build_brief` takes the supplied case records and prepares the facts under written rules. These are names for parts of the program. There is no need to run or read Python yet; [Lesson 1.2](02-python-first-steps.md) starts with three lines and explains them one by one.

## Input, output and action

A **prompt** is the material sent to ask the model to do something. It might say, “Draft a brief for the adviser. Keep the recorded dispatch quantity separate from the customer's report,” followed by the three records. A **response** is what the model sends back. An **action** changes something outside the response, such as assigning a case or issuing a credit.

For H-17, the application can prepare a brief for an adviser, who can check the sources and ask the warehouse and carrier what happened. The brief is not an authorisation to credit the account. The software can reinforce that boundary by showing where the figures came from, flagging open questions and leaving credit controls out of the drafting tool.

## Study pause

1. In the phone example, what is estimated at 30%? Is this about a real delivery?
2. Harbour adds a new note about H-17 to the prompt. What has changed, and what has not necessarily changed?
3. What can Harbour say about H-17 after subtracting ten from twelve? What still needs checking?

**Worked response.** The 30% refers to `ready` as the next word after `the parcel is` in the toy model. The note changes what the model has for this request; adding the note does not by itself train the model. The subtraction finds a difference of two between the dispatch figure and the customer's report. It does not verify receipt or establish a cause. The [chapter on decisions](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow) develops this distinction between calculating, recommending, authorising and acting.

## Try the live model

This experiment can wait until after the first Python lesson. The [live-model guide](../../reference/live-model-guide.md) prepares the API configuration. The matching notebook adds a real request and records the returned model, status, usage and duration. Inspect every factual claim. In a development run, the model inferred shipped quantity from an order record; the source did not establish that inference. The [worked experiment record](../../reference/worked-model-experiments.md) explains this observed failure and the later corrections.

## What to remember

The phone example estimates which word follows a phrase. At Harbour, ordinary code can calculate a difference, and a language model can put that calculation into words. The records still determine which claims the adviser can support.

## What this means for the business process

Let the application collect and label the records, use an explicit rule for the subtraction, and give the model the drafting step. The adviser should check the sources and decide what to investigate. Keep credit under its own approval process. The decisions chapter explains why preparing information, recommending a remedy and authorising it are separate acts.

For the research behind this design choice, read [Distinct acts in one workflow](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow).

## Next lesson

You have separated writing a brief from establishing a fact. Next you will use Python to calculate the difference and give the quantities names that tell a reader what was compared. [Lesson 1.2: Reading and running a small Python program](02-python-first-steps.md).
