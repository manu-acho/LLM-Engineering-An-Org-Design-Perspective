# Lesson 1.5: Walk the original summariser and multi-page builder

[Module route](README.md) · [Next: redesign the information work](06-design-lab.md)

## Start with the entry point

Open Ed Donner's [first notebook](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day1.ipynb) beside [the scraper](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/scraper.py). Follow the invocation of `display_summary`. That function presents a result; `summarize` obtains it. This distinction lets a later web interface reuse the logic without also trying to display notebook Markdown.

`fetch_website_contents` performs the HTTP request and passes the returned bytes to BeautifulSoup. Parsing gives the program a structure it can inspect. `soup.title` looks for a title. The body branch removes scripts, styles, images and inputs, then extracts text with newline separators. Removing an element deletes it from this parsed representation, not from the original website.

The final expression combines title and body, then keeps at most 2,000 characters. Imagine a page whose first 1,900 characters describe ordinary delivery and whose last paragraph explains disputed deliveries. The response can be successful while the important exception never reaches the model. Save or inspect the extracted text when diagnosing the answer.

The original scraper has no explicit request timeout or HTTP-status check. For a maintained application, those are distinct improvements: a timeout bounds waiting; checking status prevents treating an error page as the intended document. Neither ensures that the extracted content is substantively complete.

## Follow the next representation

The notebook's message constructor takes extracted text and places it in a user message alongside system-level task instructions. The model call returns an object. Selecting its first choice and message content yields text for presentation. One input URL has therefore become page bytes, a parsed tree, extracted text, message records, a response object and a displayed summary.

Write down the value at each boundary. If the HTML is good but extracted text is empty, changing the model will not repair extraction. If messages contain correct evidence but the answer overstates it, investigate instructions and generation. This is the practical value of separating functions.

## A real adapter, isolated from the rest of the program

The following is a new optional integration example. It needs the `openai` package, `OPENAI_API_KEY` and an accessible model named in `OPENAI_MODEL`. It performs a paid external request if called. It was not executed as part of preparing this lesson.

```python
def real_generate(messages):
    import os
    from openai import OpenAI

    client = OpenAI(timeout=30.0, max_retries=0)
    response = client.responses.create(
        model=os.environ["OPENAI_MODEL"],
        input=messages,
    )
    if not response.output_text:
        raise ValueError("No text answer was returned")
    return response.output_text
```

`os.environ[...]` requires a configured value and raises if it is absent. Creating the client establishes configuration; the network call occurs in `responses.create`. A finite timeout avoids unlimited waiting. Disabling SDK retries here makes retry ownership visible to the enclosing application. The returned convenience text is suitable for our simple contract, while a richer application should retain response identity, completion status and usage separately.

This adapter can replace `fake_generate` in Lesson 1.2 without changing evidence preparation. It illustrates the [Responses interface](https://developers.openai.com/api/docs/guides/text); it is not a transcription of the notebook's Chat Completions call.

## The multi-page project adds a planning boundary

In [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week1/day5.ipynb), the first model task selects relevant links. The application parses the answer as JSON, fetches the selected pages, labels their contents and asks for a brochure. That is two different uses of a model: selecting evidence and synthesising it.

Parsing establishes JSON structure. Before fetching, compare every selected URL with the allowed original links and permitted destinations. Otherwise the model's proposed source list becomes an uncontrolled fetching instruction. Preserve the page URL beside each extract so the final answer can be checked against its origin.

Streaming changes presentation timing. Accumulating text deltas and replacing a display gives the reader progressive output. A broken stream can leave readable but incomplete text. Store completion status independently from the displayed prefix.

**Practice with feedback:** The output omits the credit exception. Which three things should be inspected first? Check whether the correct page was selected, whether extraction retained the exception and whether the final request included that extract. Only then investigate whether generation failed to use available evidence.
