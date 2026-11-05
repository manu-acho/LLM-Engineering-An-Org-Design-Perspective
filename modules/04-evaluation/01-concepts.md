# Lesson 4.1: What would count as evidence that the system is useful?

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Start with two persuasive demonstrations

One assistant writes a polished response to Harbour's shortage complaint. Another generates a replacement program that runs a calculation much faster. Both demonstrations may be valuable. Neither yet establishes reliable operational performance.

An **evaluation** is an organised way to assess behaviour against stated criteria. It begins with the decision you need to make, not with whichever score a tool conveniently provides. Are you deciding whether to pilot an assistant, permit it to send messages or replace a calculation? Those decisions need different evidence.

## Examples, cases and benchmarks

A **test case** combines an input with an expected behaviour. For the shortage assistant, a case could supply contradictory delivery records and require it to preserve the disagreement. The expected behaviour need not be one exact sentence; it can be a set of required and prohibited claims.

A **benchmark** is a specified collection of tasks and scoring rules. Its value depends on whether the cases represent the intended use. A model ranking on unrelated puzzles cannot settle which system will handle your client's order exceptions.

An evaluation set should include normal work and consequential boundaries: missing evidence, contradictory sources, unusual names, insufficient permissions and questions outside scope. If you select only examples that already worked, you are examining successful demonstrations rather than estimating reliability.

## Correctness comes before speed

The course's week 4 project asks models to translate Python into C++ or Rust. **Compilation** turns source code into an executable program for a target environment. A compiler can reject invalid syntax or types. It cannot generally tell whether the generated program preserves the original business meaning.

A valid program can still calculate the wrong result. A fast program can skip work. Before reporting a speedup, define what outputs must agree, what differences are acceptable and what happens for unusual inputs.

For an invoice amount, rounding rules and currency precision matter. For an approximate scientific calculation, a justified numerical tolerance may be appropriate. A tolerance is a permitted difference, not an excuse introduced after seeing the result.

## Language and algorithm are separate choices

An **algorithm** is a procedure for solving a problem. Imagine checking every pair of delivery records for duplicates. As the collection grows, the number of comparisons can grow much faster than the number of records. A different procedure using a lookup structure may require far fewer comparisons.

Translating the first procedure into a faster language can help. Changing the procedure can help more. If a model does both, attribute the gain carefully. The improvement is not necessarily a property of the target language alone.

The course's maximum-subarray example illustrates this. The task is to find the consecutive section of a numerical sequence with the greatest sum. One algorithm tries many possible sections. Another maintains a running best. The mathematical task is the same; the amount of work differs.

## Measurement needs boundaries

**Latency** is elapsed time to a defined point. Does your measure include preparing input, generating code, compiling it, starting a process or only running the calculation? Those are different quantities. **Throughput** concerns how much work is completed over time. A system can have good throughput and still make an individual user wait.

Repeat measurements when timing varies. A median is the middle observed value after sorting; it is less influenced by one unusually slow run than the mean, which is the arithmetic average. Report the spread as well as a central value. Never select the fastest observation without explaining that selection.

A faster component may barely change the end-to-end process. If a calculation occupies 5% of total elapsed time and becomes ten times faster, the remaining 95% is unchanged. Under that simplified assumption, total time falls to 95.5% of its previous value. The organisation gains about 4.5%, not tenfold improvement.

## Reliability includes failure behaviour

A system that refuses an unsupported request appropriately may be better than one that always produces an answer. Count invalid outputs and failures separately. Otherwise, excluding them can make a weak system look accurate on the subset it happened to complete.

Similarly, include human review and correction. A technically cheap model that requires repeated specialist repair may produce a more expensive workflow. “Cost per model call” and “cost per correct completed case” answer different questions.

## A fair comparison

Freeze a set of cases, define criteria before running, keep a baseline, record configuration and inspect failures. A **baseline** is a simpler comparator, such as a rule, an existing process or a deterministic calculation. It tells you whether added complexity earns its place.

**Check:** A founder says, “Our AI reduced drafting time by 70%, so service productivity rose by 70%.” Explain what remains unknown. Your response should identify review effort, the share of work spent drafting, delays elsewhere, quality and whether freed capacity actually changed an outcome.

[Engineering reference](../04-evaluation-and-code-generation.md) links the source code-generation notebooks and their historical results.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Usefulness requires a defined population, consequence and comparison. The research chapter explains [benefit evidence](../../reference/research/04-implementation.md#benefits-need-a-population-and-a-comparison).
