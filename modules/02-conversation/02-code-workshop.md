# Lesson 2.2: Follow a conversation through a validated tool

[Download the matching notebook](/downloads/02-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

A conversation can appear coherent while the application has lost the selected case or confused two users. Harbour therefore keeps the selected case as explicit state and treats each tool request as a proposal that still needs validation.

The implementation lives in `src/ai_orgdesign/labs/m02.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

The conversation function creates a fresh history list for each call. A scripted call carries an identifier, a capability name and an arguments dictionary. dispatch permits only lookup_case with exactly one case_id field, then lookup checks the tenant before returning a copy of the record. Serialising that result makes the tool observation inspectable without changing the authoritative record. stream_words yields one word at a time; it demonstrates incremental delivery without pretending that a model produced the words.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m02 import conversation, stream_words
result = conversation()
assert result["state"]["selected_case"] == "H-17"
assert "".join(stream_words("Evidence awaits review")).strip() == "Evidence awaits review"
print(result)
```

The selected case is H-17, its ordered quantity is twelve and its reported quantity is ten. The tool observation has call_id equal to call-1. Joining the stream pieces reconstructs Evidence awaits review, with a trailing space. Nothing approves a remedy.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Request H-18 while keeping the north scope. Predict whether the record will be returned and whether changing a name inside a model message should alter that decision.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** lookup raises PermissionError because H-18 belongs to south. Identity and scope enter through the application, not the request text. A real authentication system would supply that trusted scope; this local function parameter is a teaching boundary, not authentication.

## Consider the alternative

A form with a required case identifier may be more dependable than extracting it from chat. A provider adapter can propose the same tool call, but should not bypass dispatch. Streaming can improve perceived responsiveness while adding partial-output and cancellation problems.

The [organisation design reading](../../reference/research/03-decisions.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
