# Lesson 4.5: Inspect a generated program from prompt to timing result

[Module route](README.md) · [Next: decide what the measured gain means](06-design-lab.md)

## Read the course as a sequence of artefacts

In [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/day3.ipynb), find the Python source string, system-information helper, model prompt, returned C++, written file, compiler invocation and executable run. A failure can occur at each boundary. A successful later stage cannot retrospectively establish that an earlier semantic choice was correct.

The source program becomes part of a prompt. The model returns text. Removing Markdown fences prepares that text for a source file, but does not parse the language or check the business rule. The compiler checks requirements of the target language. Tests must then examine behaviour.

The notebook times execution separately from some preparation work. In [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/day5.ipynb), a harder maximum-subarray task also introduces the possibility of algorithmic improvement. A speedup can combine language, algorithm, compilation and measurement effects. Separate them before explaining the result.

## Work the algorithm before trusting its translation

For the sequence `[3, -5, 4, 2, -1]`, the best non-empty contiguous section is `[4, 2]`, summing to 6. A simple reference tries every starting point and extends it through every ending point. A linear method retains the best section ending at each position.

```python
def reference(values):
    if not values:
        raise ValueError("A non-empty sequence is required")
    best = values[0]
    for start in range(len(values)):
        subtotal = 0
        for end in range(start, len(values)):
            subtotal += values[end]
            best = max(best, subtotal)
    return best

def candidate(values):
    if not values:
        raise ValueError("A non-empty sequence is required")
    ending = best = values[0]
    for value in values[1:]:
        ending = max(value, ending + value)
        best = max(best, ending)
    return best

for case in [[3, -5, 4, 2, -1], [-4, -2], [0], [2, 2]]:
    assert reference(case) == candidate(case)
assert candidate([3, -5, 4, 2, -1]) == 6
assert candidate([-4, -2]) == -2
```

At each position, `ending` either starts a new section or extends the previous one. Initialising with the first value preserves the non-empty rule. Initialising with zero instead would return zero for all-negative input, changing the problem to one allowing an empty section. That small implementation choice is a semantic decision.

The nested reference performs many more additions as length grows. The linear method carries two running values. Compare these in the same language first. Then compare equivalent implementations across languages. This makes the contribution of each change interpretable.

## Build the experiment record

Retain test inputs, expected outputs, generated source, compiler command and version, run configuration, timings, failures and any manual edits. Use separate working directories for concurrent runs. A shared `main.cpp` can allow one user's source to overwrite another's.

Measure at least two questions: how long does the accepted program run, and how much end-to-end effort does producing and maintaining it require? The latter includes generation, compilation, inspection, repairs and future changes. Repeated timing samples should use a declared aggregation rule, such as median and range, rather than selecting the fastest run.

The original [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/day4.ipynb) also runs Python text using `exec` and captures output through `StringIO`. That is useful to read, but ordinary Python execution is not isolation for untrusted generated code. This lesson executes only its own deterministic Python algorithms; it does not execute model-generated programs.

**Worked diagnosis:** A C++ result differs only for large values. Inspect integer widths and overflow before concluding that sampling made the model unreliable. A source program using arbitrary-precision integers and a translation using fixed-width integers can implement different numerical semantics while looking algorithmically similar.
