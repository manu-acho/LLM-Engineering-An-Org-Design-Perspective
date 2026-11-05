# Lesson 9.5: Read the digital twin from tool schema to notification

[Module route](README.md) · [Next: design the service promise](06-design-lab.md)

## Find the final implementation

In Ed Donner's [foundations lab 3](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/1_foundations/3_lab3.ipynb), the `chat` function evolves through the notebook. The final version handles successive tool requests. Notebook execution order matters: a later definition replaces an earlier binding, while a running process can retain imported modules. Read the function that the final interface actually calls.

The [digital-twin lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/1_foundations/4_lab4.ipynb) adds supplied background, notifications and a web interface. This creates a chain from user conversation to a real external effect. The instruction to record interest is part of that source application's behaviour; reading it here does not authorise sending a notification.

## Walk the tools module in order

The inspected [tools file](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/1_foundations/twin/tools.py) loads configuration, defines `push`, defines record functions, declares schemas and builds `tool_map`. The schemas describe operations to the model. The mapping connects those names to Python callables.

`handle_tool_calls` loops through requests. It reads each function name, parses argument JSON, finds the callable, invokes it with `**arguments`, then returns a tool message containing the same `tool_call_id`. That identifier preserves the link to the request. An unknown name returns an error string in this implementation.

`record_user_details` calls `push` with supplied values and returns `OK`. The name sounds like durable record storage, but the visible effect is a notification request. `requests.post` does not itself prove that a notification was delivered, and the inspected helper does not check the returned status. A consumer should not interpret `OK` as evidence of a completed CRM update.

## Connect to the real model loop

Use the complete exchange from [Lesson 2.5](../02-conversation/05-source-walkthrough.md) with an explicit schema for a permitted read-only order lookup. The provider proposes JSON arguments. The dispatcher validates the name, fields, types and scope. The tool result is serialized and returned with the matching identifier before the next model request.

```python
lookup_schema = {
    "type": "function",
    "function": {
        "name": "lookup_order",
        "description": "Read the quantities recorded for a permitted order",
        "parameters": {
            "type": "object",
            "properties": {"order_id": {"type": "string"}},
            "required": ["order_id"],
            "additionalProperties": False,
        },
    },
}
```

This is a Chat Completions tool description, matching the course's interface family. A Responses tool uses a different shape. The dictionary contains no executable lookup. Its description helps model selection; the application must still supply the corresponding dispatcher and enforce the scope.

The optional real exchange requires a configured provider client and may incur charges. The schema above can be inspected without making requests. No original notification tool is called by the lesson.

## Improve one boundary at a time

The course also illustrates `globals().get`, which looks for a name in the current global namespace. An explicit registry is easier to review because it lists only intentionally exposed operations. Schema validation can reject malformed input. A trusted policy service can determine record scope. A checked response can improve evidence about notification acceptance. These improvements solve different problems.

Adding all of them does not settle what the public-facing service should promise. If it says “I have recorded your enquiry”, the operating arrangement must define where the record exists, who receives it, how quickly they respond and how a failure becomes visible.

**Worked trace:** A visitor supplies an email, the tool is called, the notification service returns an error page and the helper returns `OK`. The runtime trace can establish that a call occurred. It cannot establish delivery or follow-up. A better result contract returns an explicit accepted/error status tied to a request ID, and the service promise identifies the receiving owner.

## Read the organisational connection

An engineering agent can request actions without thereby acquiring legitimate authority or accountability. The research chapter explains [agency and responsibility](../../reference/research/06-technology-in-practice.md#agency-does-not-imply-responsibility).
