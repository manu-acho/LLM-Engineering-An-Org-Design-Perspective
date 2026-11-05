# Lesson 1.2: Reading and running a small Python program

[Download the lesson notebook](/downloads/02-python-first-steps.ipynb) · [Notebook setup and study workflow](../../STUDY-WORKSPACE.md)

[Previous lesson](01-model-and-application.md) · [Module route](README.md) · [Next: learning](03-learning-and-generation.md)

## A program is a sequence of explicit operations

The pilot lab is a text file, `foundations_lab.py`. A Python interpreter reads the file and executes its statements. Instructions inside a function run when that function is called. A comment begins with `#` and explains the code to a reader; Python does not execute the comment.

The [setup page](../../START-HERE.md) explains how to obtain Python and download both lab files. In the folder containing them, the command below starts the model example:

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
```

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

The check prevents missing quantities from becoming zero. It also rejects `True`: Python booleans are related to integers, so the example deliberately checks the exact type. This strict rule suits the toy input contract. A different application might accept decimal weights, but it would need to state the unit and validation rules explicitly.

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
