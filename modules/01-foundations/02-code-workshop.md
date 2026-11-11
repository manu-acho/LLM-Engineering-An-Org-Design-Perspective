# Lesson 1.2: Follow a piece of information through a program

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

Twelve ordered minus ten reported gives a difference of two. The code below keeps the two source figures, calculates their difference and then hands the evidence to a function that writes a draft. Follow the value two through those steps. The example uses a fixed function for the writing so the calculation and the evidence are easy to inspect.

[Open the companion workshop notebook](../../notebooks/01-foundations.ipynb).

## What we are trying to learn

The aim is to read a program without treating its symbols as decoration. We will build a delivery brief using a deliberately fake generator. No model is called. This lets you understand the arrangement of functions before learning a service's response format.

If variables, dictionaries or functions are unfamiliar, read [Start here](../../START-HERE.md) first. You can trace this lesson on paper; running Python is optional.

## The complete small example

```python
def prepare_evidence(order):
    missing = order["ordered"] - order["reported_received"]
    return (
        f"Order: {order['id']}\n"
        f"Ordered: {order['ordered']} boxes\n"
        f"Customer reports receiving: {order['reported_received']} boxes\n"
        f"Reported difference: {missing} boxes"
    )

def make_messages(evidence):
    return [
        {"role": "system", "content": "Separate reports from verified facts."},
        {"role": "user", "content": evidence},
    ]

def fake_generate(messages):
    return "DRAFT FOR REVIEW\n" + messages[1]["content"]

def build_brief(order, generate):
    evidence = prepare_evidence(order)
    messages = make_messages(evidence)
    return generate(messages)

order = {"id": "O-17", "ordered": 12, "reported_received": 10}
brief = build_brief(order, fake_generate)
print(brief)
```

## Read from the call, then follow the functions

Python first encounters function definitions. Defining a function makes it available; it does not run its body immediately. The actual work begins when `build_brief(order, fake_generate)` is called near the bottom.

`order` is a dictionary. Its keys are strings, such as `"ordered"`; its values include numbers and text. `order["ordered"]` means “retrieve the value under this key.” It retrieves 12. Using a missing key raises a `KeyError`; the program does not invent a value.

The function `build_brief` receives two arguments. One is the order data. The other is a function, `fake_generate`. Functions can be passed around as values. The parameter name `generate` refers to whichever function the caller supplied. This is a practical form of **dependency injection**: a component receives the service it will use instead of constructing one invisibly inside itself.

The first line inside `build_brief` calls `prepare_evidence(order)`. That function subtracts the reported received quantity from the ordered quantity. It stores 2 under the local name `missing`. “Local” means the name belongs to that function's execution; another function cannot assume that name exists in its own scope.

The return expression combines several strings. An `f` before a quoted string marks an **f-string**, which inserts values at expressions inside braces. `\n` means a newline. Parentheses allow the expression to span lines; adjacent string pieces are joined into one returned string.

At this stage, structured numeric data has become a readable evidence string. That transformation is useful for a language model, but it also chooses a representation. The phrase “customer reports” preserves the source of a claim. Calling it “received” without qualification would change what the text asserts.

## Constructing the message list

`make_messages` receives that evidence string and returns a list of two dictionaries. A list preserves order. The system record comes before the user record in this example. Every record has `role` and `content` keys.

The square brackets at the outer level create a list. The curly braces create individual dictionaries. Similar-looking punctuation therefore has different jobs. You can inspect the structure by asking: How many messages exist? Which value is text? Which key identifies the role?

`build_brief` next calls `generate(messages)`. Because the caller supplied `fake_generate`, that function runs. `messages[1]` selects the second list item: Python counts from zero. `messages[1]["content"]` then selects the content field inside that item. The fake adds a heading and returns the text unchanged.

The result returns through `build_brief`, is assigned to `brief`, and is displayed by `print`. Returning and printing are different: return passes a value to another part of the program; print writes a representation to the output stream.

## Expected output and what it proves

```text
DRAFT FOR REVIEW
Order: O-17
Ordered: 12 boxes
Customer reports receiving: 10 boxes
Reported difference: 2 boxes
```

This demonstrates wiring and arithmetic. It demonstrates no language-model capability. The fake deliberately makes it impossible to mistake an integration test for evidence that a model understands the task.

To use a real service later, replace the fake with an adapter that accepts messages and returns text. The real adapter must construct an authenticated request, send it, handle errors and extract the returned text. The original course's `response.choices[0].message.content` is one specific response-access pattern; it should live inside the adapter rather than leak everywhere through your business logic.

## Connecting this example to the original course

Open [week1/day1.ipynb](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day1.ipynb) and [scraper.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/scraper.py). `fetch_website_contents` supplies evidence where our example uses an order dictionary. `messages_for` prepares the request. The model call supplies the generation dependency. `display_summary` presents the result as Markdown.

The course's scraper truncates text to a character limit. Our example does not. If you add truncation, you must identify which information it can remove. A performance shortcut can alter the business claim.

## Alternatives and trade-offs

For this fixed brief, deterministic formatting may already be sufficient. The quantities and headings need no generative model. Add a model when the task involves variable language, synthesis or explanation that justifies its uncertainty and cost.

A class could group the order data and its methods together. Separate functions keep this first example easier to follow. Neither is inherently more professional; choose based on shared state and complexity. Likewise, validate input types before arithmetic in a real application. The ability to subtract assumes numerical values, which a malformed external record may not supply.

## Try a small change

Change the received quantity to 12 and predict the output before running. Then remove the key `reported_received`. Explain the different outcomes.

**What the example shows:** The first change produces a zero reported difference; it does not verify completeness. The second produces an error at dictionary lookup. A useful application would surface missing evidence clearly. Silently substituting zero would create a false shortage and turn a technical default into a business assertion.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A transformation can preserve a reported fact or silently turn it into a stronger claim. The research chapter explains [decision premises](../../reference/research/03-decisions.md#decision-premises).
