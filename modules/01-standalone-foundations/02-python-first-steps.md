# Lesson 1.2: Reading and running a small Python program

[Download the lesson notebook](/downloads/02-python-first-steps.ipynb) · [Notebook setup and study workflow](../../STUDY-WORKSPACE.md)

[Previous lesson](01-model-and-application.md) · [Module route](README.md) · [Next: learning](03-learning-and-generation.md)

## What you'll learn and why it matters

Start with two numbers and learn to read the four lines that give Harbour a difference of two boxes. Then give those numbers a source and teach the program what to do when one is missing. By the end, you should be able to predict what the program will display in each case and explain what the adviser can do with that result.

Read the examples on this page or run them in the matching notebook. Run one code cell at a time from the top. The first cell is the subtraction itself. The examples use ordinary Python and need no API key, model or course package.

## Business context: Harbour

In Lesson 1.1, Harbour's adviser needed to find out why the customer said ten boxes arrived when the dispatch record showed twelve. This lesson uses two of the records for a smaller question: how does the customer's report compare with the order for twelve boxes? The dispatch record will enter the fuller investigation brief in Lesson 1.4.

Try the comparison on paper before reading the code. Write “12 ordered” and “10 reported received”, then subtract ten from twelve. The result is two. Keep the labels beside both numbers, because “ten reported received” tells the adviser where to look next. “Ten received” would treat the customer's account as a confirmed count.

[Company and supply-chain context](../../HARBOUR.md)

## Calculate and display the difference

Python is a language for writing instructions a computer can follow. Here is the complete first program:

```python
ordered = 12
reported_received = 10
difference = ordered - reported_received
print(difference)
```

| Line | What Python does |
| --- | --- |
| `ordered = 12` | Gives twelve the name `ordered`. The equals sign assigns the value on the right to the name on the left. A name used this way is called a **variable**. |
| `reported_received = 10` | Gives ten the name `reported_received`. The underscore keeps the two words together in one name. |
| `difference = ordered - reported_received` | Looks up the two numbers, subtracts ten from twelve, and gives the result the name `difference`. |
| `print(difference)` | Displays the current value of `difference`, which is `2`. The parentheses tell Python to run `print` with that value. |

Change ten to eleven and run all four lines again. The displayed result becomes `1`. The third line has to run again because it calculates the difference from the values available at that moment. Restore ten before continuing in the notebook.

## Keep the source with the quantity

A Harbour adviser needs to see where the figure came from. Store the quantity and source together in a **dictionary**, which is a group of named entries inside curly brackets. Each entry has a name, called a **key**, and a value.

```python
customer_report = {"quantity": 10, "source_id": "customer-17"}
reported_received = customer_report.get("quantity")
print(reported_received)
print(customer_report["source_id"])
```

Inside the curly brackets, `"quantity": 10` pairs the key `"quantity"` with the number ten. The comma separates it from the next entry. The value `"customer-17"` is a **string**, a piece of text between quotation marks. It identifies the record in this exercise. The number `10` has no quotes, so Python can use it in arithmetic.

Both square brackets and `.get()` look up an entry by its key. The example prints `10`, then `customer-17`. We use `.get("quantity")` because a report can arrive without a count. In that case, `.get()` gives back `None`, a special Python value that can represent missing information. Square brackets would stop with an error if the requested key were missing.

## Decide what to do when the count is missing

Imagine that the customer's report arrives with a source identifier and no quantity. On paper there is nothing to subtract. The program can apply the same reasoning.

```python
incomplete_report = {"source_id": "customer-17"}
reported_received = incomplete_report.get("quantity")

if reported_received is None:
    print("Customer count missing. Ask for the quantity.")
else:
    print(ordered - reported_received)
```

Read `if reported_received is None:` as “if the lookup found no value, do the indented step below”. The colon opens that group of instructions. Spaces at the start of the next line show it belongs to the condition. `else` gives the alternative when a number is available. Python runs one of the two branches. Here it displays the request for a count.

A report that gives zero boxes should go through the subtraction branch. Zero is a recorded answer to the question “how many?” An absent count leaves the question open.

## Give the comparison a name

If Harbour uses the check on many reports, it can write the instructions once and reuse them. A **function** is a named group of instructions. Defining it prepares the instructions for later use. Calling it runs them with particular inputs.

```python
def compare_quantities(ordered_boxes, reported_boxes):
    if reported_boxes is None:
        return "Customer count missing. Ask for the quantity."
    return ordered_boxes - reported_boxes

print(compare_quantities(12, 10))
print(compare_quantities(12, None))
```

1. `def` introduces the function. The names in the first pair of parentheses are placeholders for the inputs.
2. `compare_quantities(12, 10)` runs it with twelve under the name `ordered_boxes` and ten under `reported_boxes`. The check finds a number, so the function uses the last line of its indented instructions.
3. `return` hands a result back to whoever called the function and ends that call. The outer `print` displays the returned value, `2`.
4. In the second call, `reported_boxes` is `None`. The first `return` sends back the message straight away, and the subtraction is skipped.

Returning a number or a message makes the two paths easy to see in a first example. In a larger application, callers need a reliable way to distinguish results from problems. Lesson 1.4 shows how the full lab checks required records before building a brief.

## Try it with three reports

Predict what the function gives for each of these inputs. Write down what the adviser can conclude in each case before checking the answer.

- Twelve ordered and thirteen reported received.
- Twelve ordered and zero reported received.
- Twelve ordered and no count supplied.

**Worked answer.** The first result is `-1`. The customer reported one more box than ordered. The second result is `12`, a difference based on a report of zero. In the third case, Python displays a request for the count. That case is still missing an input. Even with a number, the adviser still has a comparison of records to investigate before reaching a conclusion about the delivery.

## What to remember

A variable names a value, a dictionary keeps named values together, and a function lets the program reuse instructions. A condition lets the program ask for missing evidence before calculating. The labels explain what the arithmetic compares, and the result shows the size and direction of the disagreement.

## What this means for the business process

At Harbour, customer service should obtain a missing count before the application calculates a difference. Once a number is available, the brief should carry its source and describe it as reported. An investigator can then decide whether to ask the warehouse or carrier for more evidence. Replacing a blank count with zero would change the information the investigator relies on and could make a missing report look like a reason to consider a full replacement. The decisions chapter explains how the information supplied at one step shapes the choices available later. [Decision premises](../../reference/research/03-decisions.md#decision-premises).

## Next lesson

Here, every rule came from the person writing the program. In the next lesson, you will reuse named values and function calls to follow a program that builds a rule from examples. It counts which word follows another and uses those counts to choose what to write next. [Lesson 1.3: Train a tiny language model](03-learning-and-generation.md).
