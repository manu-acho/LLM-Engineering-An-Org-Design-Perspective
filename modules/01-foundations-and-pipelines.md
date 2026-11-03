# Module 1: Foundations and LLM pipelines

[Guide index](../README.md) · [Next module](02-conversation-and-tools.md)

## What you should be able to do

Explain tokens, inference, context and prompts; trace a URL-to-summary pipeline; distinguish Python data structures from model behaviour; and design a useful document-generation task with an observable evidence trail.

**Course walkthrough:** [day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day1.ipynb), [day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day2.ipynb), [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day4.ipynb), [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day5.ipynb), [scraper](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/scraper.py), [Ollama solution](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/solution.py), and the [week exercise](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/week1%20EXERCISE.ipynb). There is no root-level day 3 notebook in this snapshot; do not infer that its lecture content was reviewed.

## 1. Concepts: what happens when you call a model?

An LLM maps an input token sequence to a distribution over possible next tokens. Generation repeatedly extends that sequence. A token can be a word, a fragment, punctuation or encoded bytes. Token counts are therefore different from word counts and depend on the tokenizer.

**Training** changes learned parameters. **Inference** uses those parameters to produce a result. Adding a paragraph to a prompt changes the information available during inference; it does not retrain the model. This distinction later separates prompting, retrieval and fine-tuning.

The **context window** limits the token sequence available for a request, subject to the model's input/output rules. A large window makes information available, but does not guarantee that the model uses every relevant detail correctly. Context selection is an engineering decision.

In the course's direct chat calls, messages are sent explicitly. A follow-up that contains only “What is my name?” omits the earlier introduction. Sending the earlier user and assistant messages makes the answer possible. This is application-managed state, not a parameter update. Products and APIs can also manage stored conversation state; the important question is which earlier information reaches this inference request. See the [official API state and migration distinctions](https://developers.openai.com/api/docs/guides/migrate-to-responses).

A system instruction specifies the task and response expectations. A user message supplies the current request and evidence. Neither guarantees factual accuracy. A plausible continuation can still be an unsupported claim.

For a founder, this means that “the model knows our business” is too vague to guide a build. Specify whether knowledge comes from training, supplied documents, retrieved records or a live tool.

## 2. What the code does

### Day 1: compose a pipeline from small functions

Follow `summarize(url)` through these stages:

1. `fetch_website_contents(url)` performs an HTTP request.
2. BeautifulSoup parses the returned HTML. The scraper extracts a title, removes selected non-content elements, and gets text from the body.
3. The scraper returns at most 2,000 characters. This is an early information-loss point.
4. `messages_for(website)` constructs a list of two dictionaries, each containing `role` and `content`.
5. The client sends that list to an inference endpoint.
6. `response.choices[0].message.content` extracts one generated response from the returned object.
7. `display_summary` renders the returned string as Markdown in the notebook.

Notice the boundary between data preparation and generation. The model never sees the whole website automatically; it sees the string the scraper returned. If the scraper misses a section, a better prompt cannot recover it.

`load_dotenv(override=True)` loads configuration into environment variables and can replace existing values. `os.getenv` reads one. A key-prefix check is only a local heuristic, not authentication. Avoid copying the course's key-prefix printing into shared logs.

### Day 2: change the endpoint behind a similar interface

The course introduces local inference. In `solution.py`, an OpenAI-compatible client points to a local Ollama URL. The request shape is similar, but actual model capabilities, supported arguments, performance and error behaviour must be checked separately. Shared syntax does not establish equivalent services.

This illustrates the **adapter pattern**: hide an implementation behind a stable interface so you can compare or replace it. A small application-owned `generate(messages)` function is often sufficient; a framework is optional.

### Day 4: observe tokenization and reconstruct history

`encoding.encode(text)` returns integer token IDs; `encoding.decode(ids)` maps IDs back to text. Inspecting one ID at a time helps build intuition, although byte boundaries can make isolated decoded tokens look odd. The notebook's chosen encoding is a proxy for its example model, not evidence that every model uses that encoding.

The conversation examples rebuild `messages`. A list is ordered; order matters for dialogue. Each dictionary is one message record. Reassigning `messages` replaces the previous Python list rather than silently appending to it.

### Day 5: selection, gathering and synthesis

The brochure builder adds a second model task. `get_links_user_prompt` joins scraped links into a string. `select_relevant_links` asks the model to return JSON and uses `json.loads` to parse it into Python objects. `fetch_page_and_all_relevant_links` loops over selected URLs, gathers their text and labels it. A final model call synthesises the brochure.

JSON parsing establishes that a string is valid JSON. It does not establish that `links` exists, that each URL was in the original page, or that the destination is appropriate. Schema validation and URL validation are separate steps. Structured output can enforce supported schema constraints, while evidence still needs checking. [Official structured output guidance](https://developers.openai.com/api/docs/guides/structured-outputs).

Finally, `stream_brochure` asks for streaming output, accumulates text deltas, and updates one display. `delta.content or ''` handles events without text. A partial stream is not necessarily a complete answer.

## 3. Learn the coding patterns

**Teaching example: dependency-free pipeline with an injected generator:**

```python
def make_messages(source_text):
    return [
        {"role": "system", "content": "Summarise evidence; flag uncertainty."},
        {"role": "user", "content": source_text},
    ]

def build_brief(source_text, generate):
    if not source_text.strip():
        raise ValueError("Source text is empty")
    return generate(make_messages(source_text))

def fake_generate(messages):
    return "Draft based on: " + messages[-1]["content"]

brief = build_brief("Requests wait for an operations handoff.", fake_generate)
```

`generate` is a function passed as an argument. This is **dependency injection**: the pipeline receives the service it needs. The fake makes the wiring inspectable without an API account. A real adapter can later implement the same callable contract.

The patterns to recognise are **functional composition** (output feeds the next step), **serialization** (JSON text becomes Python data), and **separation of presentation** (return a result before displaying it). These reduce hidden coupling and make errors easier to locate.

| Course choice | Alternative | When the alternative helps |
|---|---|---|
| HTTP request plus HTML parser | Browser-rendered extraction or a content API | Important content is generated by JavaScript |
| Model selects links | Deterministic domain/path filters, optionally followed by model ranking | Scope is simple or fetching must be tightly controlled |
| Character slicing | Token-budgeted, section-aware selection | The source is long and later sections matter |
| Mutable globals in notebook | Explicit function arguments or a configuration object | Several tasks or users need different settings |
| One large synthesis call | Section summaries with source IDs, then synthesis | The evidence exceeds the context budget |

Multiple calls here form a mostly predetermined workflow. Calling it “agentic” does not tell you how much autonomy it has; inspect who chooses the next action.

## 4. Business application and organisation design

For Harbour Services, replace the brochure with an operational discovery brief. Inputs might be approved process descriptions and public service information. The output separates observed handoffs, stated responsibilities, missing evidence and questions for interviews.

The system should draft hypotheses. It should not turn a website's formal process description into a claim about actual practice. Organisation research distinguishes what actors say should happen from what people do under real constraints. A polished summary can erase that distinction unless the output format preserves it.

Specify a source owner, a reviewer and a correction route. Measure supported-claim rate, omitted critical facts, review time and net time saved. Do not use the number of generated pages as a value metric.

For planning purposes, estimate monthly value as eligible volume × adoption × net time saved × relevant labour cost, less operating and review costs. Treat that as a scenario calculation; saved minutes become business value only if capacity is productively reused or service outcomes improve.

## 5. Experiment, diagnose and reflect

**Exercise:** Write three synthetic paragraphs about Harbour's intake process. Put an important exception in the last paragraph. Produce a brief with fields for claim, evidence ID and open question. Compare full text with an intentionally truncated input. Record which claims disappear or become overstated.

Then change one factor at a time: prompt, evidence order, or generator. Explain why this is a more interpretable experiment than changing all three.

**Common failures:** empty extracted text suggests an extraction issue; a `NameError` usually points to notebook execution order; malformed JSON is an output-contract issue; a fluent unsupported statement is a grounding issue. Diagnose the boundary before changing the model.

**Check your understanding:** Why is `[:5000]` not a 5,000-token limit? Why does providing conversation history not retrain the model? Which function would you replace to change the provider? What evidence would justify automating the brief rather than drafting it manually?

**Answer cues:** characters and tokens differ; history is inference input; replace the generator adapter; compare end-to-end quality and effort on representative work.

**Decision note:** Define one task, its evidence sources, its output contract and the human judgement that remains necessary. Use the [workbook](../WORKBOOK.md).
