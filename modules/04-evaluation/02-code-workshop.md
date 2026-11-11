# Lesson 4.2: Build a small correctness check before a performance claim

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

Suppose a candidate program agrees with a trusted calculation when fewer boxes arrive, but disagrees when more arrive. A test case supplies particular records and asks for a result that can be checked. Follow the cases before thinking about speed. The surprising case exposes a business rule the happy path leaves hidden.

[Open the companion workshop notebook](../../notebooks/04-evaluation.ipynb).

## A transparent reference calculation

Suppose Harbour wants the total number of reported missing boxes across several synthetic records. We will compare two implementations. The example is intentionally simple enough that you can calculate the expected answer yourself.

```python
def shortage_total_reference(records):
    total = 0
    for record in records:
        difference = record["ordered"] - record["reported_received"]
        if difference > 0:
            total = total + difference
    return total

def shortage_total_candidate(records):
    return sum(max(0, r["ordered"] - r["reported_received"]) for r in records)

cases = [
    [],
    [{"ordered": 12, "reported_received": 10}],
    [{"ordered": 10, "reported_received": 12}],
    [{"ordered": 5, "reported_received": 5}, {"ordered": 8, "reported_received": 3}],
]

results = []
for case in cases:
    expected = shortage_total_reference(case)
    actual = shortage_total_candidate(case)
    results.append({"expected": expected, "actual": actual, "matches": expected == actual})
```

The reference begins at zero, visits each record, computes a difference and adds only positive differences. The candidate uses `max(0, difference)` to apply the same non-negative rule and `sum` to add the values. The expression inside `sum` produces one value per record.

We are not claiming that the candidate is faster. More compact source code does not necessarily mean faster execution. This comparison first asks whether the rule was preserved.

## Trace one case and inspect the policy

For the final case, the first record contributes zero and the second contributes five. Both implementations return five. For the overdelivery case, both return zero. That result follows from a rule: overdeliveries do not cancel shortages elsewhere.

Another business rule could calculate net difference across all records. It would produce different outputs while still being a coherent calculation. The reference is therefore a statement of intended semantics, not a neutral truth about deliveries.

`expected == actual` compares values and returns a Boolean, `True` or `False`. Unlike `=`, which assigns a value, `==` asks whether two values compare equal. `results` retains every outcome for review rather than hiding failures in one aggregate score.

Expected totals here are `[0, 2, 0, 5]`. Passing these four cases does not prove equivalence for every possible input. Missing keys, text where a number is expected and negative quantities need their own definitions and checks.

## From local checking to generated code

The original [week4/day3.ipynb](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/day3.ipynb) prepares a prompt with Python source and asks a model for C++. It writes the returned text to a file, invokes a compiler and runs the executable. Later notebooks add a UI and a Rust option.

Read those as distinct operations. A generated source string is not yet a file. A file is not yet a compiled program. A compiled program is not yet an executed result. A result is not yet an accepted business result.

`subprocess.run` asks the operating system to run another process. A command represented as a list separates the executable name from its arguments. `check=True` makes a non-zero exit status raise an exception. `capture_output=True` retains printed output, including diagnostic error text; `text=True` asks for decoded strings. See [Python's subprocess documentation](https://docs.python.org/3/library/subprocess.html).

A **process** is a running program with operating-system resources. Running code in a process is not automatically a sufficient isolation boundary for untrusted code. File, network and resource access need separate controls. The course's in-process `exec` example is especially important to recognise: it runs Python text and is not made safe by giving it a dictionary of ordinary built-ins.

## Exceptions and cleanup

An **exception** interrupts the normal path when something fails. A `try` block attempts work; `except` handles specified failures; `finally` performs cleanup whether the attempt succeeds or fails. The course uses this to restore output after redirecting `sys.stdout` to an in-memory buffer.

That pattern is useful, but shared process-level output can still interfere with concurrent users. For an operational evaluation service, separate run directories and execution workers give clearer boundaries than a shared `main.cpp` and a shared output stream.

## Alternatives and practice

Before translating an entire application, profile it: measure which operations consume time. A clearer algorithm, a vectorised library or a narrow compiled component may solve the problem with less maintenance work. The original application may remain mostly Python.

Add a case where one shortage of two and one overdelivery of two occur. Calculate both the “sum of shortages” and “net difference” rules. Explain which one your candidate implements and who should approve that choice.

**What the example shows:** Both programs above return two. A net-difference rule returns zero. This is a semantic choice requiring business judgement, not a compiler optimisation. Testing makes that choice visible before a speed claim obscures it.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A correctness test is valuable without being evidence of an organisational benefit. The research chapter explains [the evidence path](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).
