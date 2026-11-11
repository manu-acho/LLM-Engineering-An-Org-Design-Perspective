# Lesson 1.2: Reading and running a small Python program

[Download the lesson notebook](/downloads/02-python-first-steps.ipynb) · [Notebook setup and study workflow](../../STUDY-WORKSPACE.md)

[Previous lesson](01-model-and-application.md) · [Module route](README.md) · [Next: learning](03-learning-and-generation.md)

## What you'll learn and why it matters

Read a short Python program and explain what each line stores, calculates or displays. Harbour needs these rules to keep a missing number or a customer report from turning into a confirmed figure.

## Business context: Harbour

Start with the subtraction on paper: twelve boxes recorded, ten reported, a difference of two. Python is a language for writing instructions a computer can follow. The first example gives a name to each number before asking Python to subtract them. Read the right side of each line first and then see where the result is kept. The program can find the difference; only the names explain what was compared.

The investigator needs to read quantities and source labels reliably; the first Python operations make those distinctions visible.

[Company and supply-chain context](../../HARBOUR.md) · [Module 1 business situation](../../reference/harbour-learning-journey.md#module-1)

## A program is a sequence of explicit operations

Begin with the three lines under “Names and values”. The Python **interpreter** is the program that reads the instructions and carries them out. In a notebook, each **cell** holds a block of instructions or an explanation. Run one code cell at a time in the matching notebook, or read the lines on the page and predict the result. A line beginning with `#` is a comment for the reader.

The complete lab lives in `foundations_lab.py`. Running a file from the terminal is another way to ask Python to carry out instructions. It is useful after the first example, but is optional for reading the lesson.

The [setup guide](../../SETUP.md) prepares the checkout. In the checkout’s `examples/01-foundations` folder, the command below starts the word prediction example. The terminal is where this command goes; the three-line subtraction belongs in a Python cell.

```sh
python3 foundations_lab.py model
```

On Windows, use `py -3` in place of `python3`. `model` is an argument passed to the program. The command-line parser accepts `model`, `brief` or `request`; an unrecognised choice produces an error rather than quietly running a different example.

## Names and values

An assignment gives a value a name:

```python
ordered = 12
reported_received = 10
difference = ordered - reported_received
print(difference)
```

The first line stores twelve under the name `ordered`. The second stores ten under `reported_received`. The third reads those two values, subtracts ten from twelve and stores two under `difference`. The final line displays `2`. Change just the second line to `reported_received = 11` and the displayed value becomes `1`. This change alters the calculation's input; it does not verify a delivery.

`=` assigns a value; it is not a mathematical claim that two expressions are always equal. `12` is an integer, a whole number. `"reported"` is a string, text between quotation marks. Clear names communicate the meaning of the values. Calling the second value `actual_received` would hide a qualification before any model was involved.

A **dictionary** holds values under named keys. A **list** holds values in an order. The lab's case uses a dictionary containing smaller dictionaries:

```python
order = {"quantity": 12, "source_id": "order-17"}
facts = [order]
```

`order["quantity"]` retrieves twelve. `facts[0]` retrieves the first item, because Python counts positions from zero. `order.get("quantity")` retrieves the value when present and returns `None` otherwise. `None` is a special value used here to represent absence. It does not mean zero.

## Functions make a contract visible

A **function** groups operations under a name. Its parameters name the inputs, and `return` supplies an output:

```python
def compare(ordered, reported_received):
    return ordered - reported_received

result = compare(12, 10)
```

`def` begins the definition. Indentation identifies the function's body. Parentheses in `compare(12, 10)` call the function. The returned value is assigned to `result`. The function does not print it automatically.

For any function, identify four things: inputs, output, side effects and failures. A **side effect** changes something outside the returned value, such as writing a file or sending a request. The lab's evidence preparation returns a new brief without changing the input. Its command-line entry point prints the result. It makes no remote request.

## Conditions, loops and explicit failure

An `if` statement selects behaviour according to a condition. A `for` loop repeats operations over a collection. The brief builder checks each required record before adding it to the output. If a record is missing, it raises `ValueError`, an exception indicating an unacceptable value.

```python
quantity = order.get("quantity")
if type(quantity) is not int or quantity < 0:
    raise ValueError("Expected a nonnegative whole quantity")
```

Read the check as “If the value is not a whole number or is below zero, stop and report that it was invalid.” The colon opens the block that runs if the check finds a problem. The check keeps missing quantities from becoming zero. It also rejects `True`, a **boolean** or yes/no value, so it cannot be counted as one box. This strict rule suits the toy input contract. A different application might accept decimal weights, but it would need to state the unit and validation rules explicitly.

## Modules and the entry point

`import json` makes Python's standard JSON tools available. An **import** can also load another local file, which is why the tests and lab file must remain together. The **standard library** is the collection distributed with Python; no additional package installation is needed here.

The final guard is:

```python
if __name__ == "__main__":
    main()
```

When the file is run as the program, it calls `main`. When the tests import the file to examine its functions, that command-line entry point does not run. Separating reusable functions from the entry point makes checks easier.

## A first reading exercise

Predict what `order.get("missing")` returns and why the lab should not treat it as a delivered quantity.

**Worked response:** it returns `None`. The missing field supplies no quantity. Substituting zero would create a factual claim not contained in the record. The [decision-premises discussion](../../reference/research/03-decisions.md#decision-premises) explains why such defaults can matter to subsequent choices.

The [official Python introduction](https://docs.python.org/3/tutorial/introduction.html) provides further explanation of assignments, numbers and strings. The runnable lab and subsequent lessons supply the patterns needed for this module.

## What to remember

A variable gives a value a name, a function groups operations, and a check can refuse unsuitable input. A missing quantity carries different information from zero.

## What this means for the business process

Agree the meaning of each quantity with the people who supply and use it before writing the check. For H-17, a missing receipt count should send the adviser to the source, because substituting zero silently supplies a premise for a later remedy decision.

For the research behind this design choice, read [Decision premises](../../reference/research/03-decisions.md#decision-premises).

## Next lesson

Having traced a rule written by a programmer, you can now trace a rule the program derives from examples by counting what follows each word. [Lesson 1.3: Train a tiny language model](03-learning-and-generation.md).
