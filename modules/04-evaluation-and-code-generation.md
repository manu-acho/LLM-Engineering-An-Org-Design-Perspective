# Module 4: Model evaluation and generated code

[Previous module](03-open-models-and-inference.md) · [Guide index](../README.md) · [Next module](05-knowledge-and-rag.md)

## What you should be able to do

Explain the difference between demonstration, benchmark and operational evaluation; trace a code-generation/compilation pipeline; understand subprocess calls and output capture; and separate correctness, algorithmic improvement and runtime speed.

**Course walkthrough:** Root-level week 4 notebooks available here are [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/day3.ipynb), [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/day4.ipynb) and [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/day5.ipynb), with [system information helpers](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/system_info.py) and [UI styling](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week4/styles.py). Days 1–2 have no root-level notebooks in this snapshot; this module enriches the available code-generation work with evaluation principles rather than inventing a walkthrough of those days.

## 1. Concepts: define success before comparing models

A demonstration establishes that something can work on an example. An evaluation asks how often, under which conditions, at what cost and with what consequences. A benchmark is a specified collection of tasks and scoring rules. A good benchmark for code translation should test functional equivalence, failure behaviour and performance on relevant inputs.

Separate three questions:

1. Does the generated program produce acceptable results?
2. Is it faster under a clearly defined measurement procedure?
3. Does the gain justify review, deployment and maintenance effort?

The target language alone does not answer any of them. A model may replace a quadratic algorithm with a linear one; much of the speedup then comes from algorithm selection rather than from C++ or Rust itself. Conversely, aggressive compiler flags may change floating-point behaviour. Faster output with unacceptable numerical error is a failed translation.

Use exact equality for discrete results where appropriate and explicitly justified tolerances for numerical approximations. Include edge cases such as empty input, all-negative arrays, large integers and unusual parameter values. Performance should be measured only after these gates pass.

## 2. What the code does

### Day 3: prompt, write, compile and execute

`retrieve_system_info()` gathers platform context. The notebook asks a model for compiler advice, then stores a `compile_command` and `run_command` as Python lists. Each list element is a process argument. This is different from building a shell command string.

`user_prompt_for(python)` includes the source program, machine context and chosen compiler arguments. `messages_for` packages instructions and user content. `port(client, model, python)` calls the selected model, removes Markdown fence strings and writes `main.cpp`.

Read the transformation chain:

```text
Python source string → prompt → generated source string
→ source file → compiler process → executable → stdout
```

Each arrow needs its own validity check. Removing code fences is cosmetic cleanup, not a parser or a correctness check. A compiler accepting code does not prove equivalence to the source program.

`subprocess.run(..., check=True, text=True, capture_output=True)` runs a process, raises on a non-zero exit code, and captures decoded stdout/stderr. The notebook compiles and executes the program repeatedly. The program's internal timing excludes compilation and may exclude process startup. Report exactly what was measured.

### Day 4: select the implementation through a registry

A `clients` dictionary maps model names to client instances. `port(model, python)` looks up the client rather than branching through a long series of `if` statements. This is a strategy/registry pattern, similar to module 2's tool dispatcher.

The UI connects a model dropdown and source textbox to `port`. It also defines `run_python`, which executes a string with `exec`. Supplying a globals dictionary with normal built-ins does **not** isolate that program. It still has the power of ordinary Python in the process. Inspecting this code does not require running it.

`io.StringIO()` is an in-memory text buffer. The function temporarily assigns it to `sys.stdout`, captures printed output and restores the previous stream in `finally`. Restoration matters even if execution raises an exception. Redirecting process-global stdout can also interfere with concurrent requests; separate worker processes are a more robust boundary for a real service.

### Day 5: generalise the language and test a harder algorithm

`language` chooses Rust or C++; `extension` chooses the filename suffix. The model output is now returned to an editable UI component before compilation. This adds an opportunity for human inspection.

The harder example generates pseudo-random integers using a linear congruential generator, computes the maximum contiguous subarray sum and repeats it over multiple seeds. The nested-loop version is quadratic in array length. A translation may discover a better algorithm. Keep the number-generation semantics and integer widths consistent across languages before comparing results.

The lesson's stored speedup figures describe particular historical experiments. They are neither a fresh ranking nor a transferable forecast for your workloads. The Rust compiler path also belongs to the author's machine; configuration should supply your actual toolchain path.

## 3. Learn the coding patterns and an algorithmic alternative

**Teaching example: dependency-free behavioural comparison:**

```python
def max_subarray_reference(values):
    if not values:
        raise ValueError("Expected at least one value")
    best = values[0]
    for start in range(len(values)):
        total = 0
        for value in values[start:]:
            total += value
            best = max(best, total)
    return best

def max_subarray_linear(values):
    if not values:
        raise ValueError("Expected at least one value")
    current = best = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

for case in ([3, -5, 4, 2], [-8, -2, -7], [0], [5]):
    assert max_subarray_reference(case) == max_subarray_linear(case)
```

The reference enumerates possible starts and ends. The linear method tracks the best subarray ending at the current value: extend the previous one, or start again. Both define an empty input as invalid and allow a non-empty all-negative result. A different convention allowing an empty subarray would change expected outputs.

This is a small instance of **differential testing**: compare an optimised implementation against a simpler reference. Passing these cases is useful but not a proof. Broaden the input space before relying on the result.

The course also illustrates **file/process boundaries**, **exception-safe cleanup**, **strategy selection**, **UI callback wiring** and **configuration separation**.

| Course approach | Alternative | When to consider it |
|---|---|---|
| Translate a whole program | Optimise the algorithm in Python first | Algorithmic complexity dominates |
| Plain Python numeric loops | Vectorised library operations or a suitable JIT | You can preserve the Python application and accelerate a hotspot |
| Generated executable | Reviewed library function with a narrow interface | Integration and maintainability matter more than a demo |
| One prompt and one result | Repeated runs under a fixed rubric | Output variability is material |
| Shared `main.cpp` / `main` files | Per-run temporary workspace | Concurrent runs could overwrite each other |
| In-process `exec` | Isolated execution worker with resource limits | Generated or user-supplied code is evaluated |

For subprocess semantics, see the [Python standard-library documentation](https://docs.python.org/3/library/subprocess.html). Timeouts, isolation and resource limits address different concerns; a timeout alone does not restrict file or network access.

## 4. A defensible experiment

Freeze the input cases, correctness rules, toolchain settings and measurement procedure. Compare against an existing baseline. Record prompt, model identifier, generated source, configuration, correctness outcomes and timing distribution.

Use warm-up runs when relevant and several measured repetitions. Report a median and variation rather than one best run. Distinguish generation latency, compilation time, startup and steady-state computation. Keep hardware and workload size consistent, or explain differences.

Model capability is multidimensional. A cheaper model may generate more incorrect programs and create more review work. A more expensive model may lower total delivery cost. Assess the full workflow, including reviewer expertise, repair cycles and future maintenance.

## 5. Business application and organisation design

For Harbour, imagine a slow reconciliation calculation delaying an operational report. First profile the actual process. If most delay comes from waiting for approval or locating missing data, faster arithmetic will have limited effect. This connects technical bottleneck analysis to workflow analysis.

Keep the domain specialist responsible for semantic acceptance, the engineer responsible for integration and runtime behaviour, and the process owner responsible for the operational outcome. Those responsibilities may overlap in a small firm, but should still be explicit.

A reusable evaluation report helps a project team explain its evidence: it shows what was tested, where the solution works and what remains uncertain. Avoid translating a microbenchmark into an unqualified claim about organisation-wide productivity.

## 6. Experiment, diagnose and reflect

**Exercise:** Extend the teaching comparison to every list of length 1–4 with values from `{-2, 0, 3}`. Define expected empty-input behaviour. If comparing a generated implementation later, score correctness before speed and retain failed outputs in the report.

**Business extension:** Estimate end-to-end time saved if the calculation occupies 5% of a process and becomes ten times faster. The new total is roughly `0.95 + 0.05/10 = 0.955` of the original: about 4.5% improvement under these assumptions. Explain which waiting and coordination costs this calculation omits.

**Common failures:** a missing compiler is an environment issue; `CalledProcessError.stderr` explains many compilation failures; an extremely fast wrong result is not a performance success; repeated tests on one input can conceal semantic changes.

**Check your understanding:** Why does successful compilation not establish correctness? Why could a Python algorithm beat translated C++? What does `finally` protect? Why should the reviewer see failed model outputs?

**Answer cues:** compilation checks language rules, not business semantics; complexity can dominate language overhead; cleanup occurs despite exceptions; failures reveal the actual reliability and review burden.

**Decision note:** State the acceptance gates, measured workload, error tolerance, execution boundary and owner who can approve the generated implementation.
