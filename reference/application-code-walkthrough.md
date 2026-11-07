# Read the application code from input to accepted contribution

[Live-model guide](live-model-guide.md) · [Programming patterns](python-patterns.md) · [Technical foundations](technical-foundations.md)

The notebooks expose small steps; shared files keep their implementations consistent. This guide opens those files in the order information travels through them. A helper name should become a shorthand for understood operations, rather than a box that must be trusted.

## Start with the case data

`src/ai_orgdesign/case_data.py` contains the original fictional cases and policy passages. Each case has a case identifier, region, order quantity, customer-reported quantity, report text and source identifiers. The evaluator also has an expected route and grouping label. `get_case` removes those last two fields before returning a copy for the model. The target answer therefore does not enter the prompt through that function.

A copy matters because an experiment should not silently edit the shared fixture. A dictionary maps names to values; selecting `case['reported']` obtains one value. `None` means that no customer count was supplied. It does not mean that zero boxes arrived. `get_case` also checks scope before returning any case, so a forbidden case is refused before prompt construction.

H-17 is a case, O-17 is its order and customer-17 is a source identifier. The [case guide](case-data-guide.md) distinguishes them. When following a printed object, identify both the value and the object it describes.

## Read the session object

`src/ai_orgdesign/provider.py` defines Gateway. A session retains the selected model, request ceiling, output ceiling, attempt count and run records. Creating the session configures these values and constructs a client; a generation method makes the network request. This distinction lets a learner inspect configuration without assuming that every import or constructor sends customer content.

`self` refers to the particular session object. `self.records` belongs to that session. The lock groups changes to the attempt counter when concurrent specialist calls share it. It does not impose a limit across other sessions or computers. Restarting the notebook can create a new session with a new counter.

The helper loads the local environment through `workspace.py`. A nonempty terminal setting takes precedence over the file. The key is passed to the official client and never included in the returned experiment record. No key should be placed in a prompt.

## Follow an actual request

The request method first reserves an attempt. It constructs named request settings: model, input messages, instructions, disabled response storage and an output limit. When appropriate it adds tools or an output schema. The course's current GPT-6 configuration selects no reasoning effort; another model can require different supported settings.

`client.responses.create(**kwargs)` sends the request. The double asterisk unpacks a dictionary into named inputs. For example, a dictionary containing `model` and `input` is passed as those labelled arguments. This is ordinary Python syntax, not a second model operation.

The method measures duration, retains returned usage and checks status. A timeout is handled differently from an incomplete returned response. Both remain failures to obtain an accepted answer. The helper does not repeat the request automatically. A completed response is then examined for a refusal; a refusal is not returned as an ordinary investigation result.

## Read text and structured output

`generate` appends the new prompt as a user message after any supplied conversation history. Without history, the new prompt is the only input message. It builds a new list so that the saved history is not changed by this operation. It obtains the raw response and record, then extracts answer text. Empty text is rejected. If a schema was requested, it parses the text as JSON and returns both the text and parsed value.

JSON parsing establishes that the text can be represented as structured values. It does not establish a correct customer quantity. The application therefore validates the returned object against the supplied case. Keeping `text`, `value` and `record` separate helps distinguish the language output, its machine-readable structure and the observation that a request executed.

## Follow streaming without confusing a prefix with completion

The stream method obtains successive events. A text-delta event supplies newly arrived characters. A notebook can append or print them. The terminal response carries the status and usage needed to interpret the complete operation.

A stream ending without a completion record raises an error. If some text was already displayed, it remains partial output. The application should not turn that prefix into a completed customer answer. Closing the stream releases its network resources; it does not undo already transmitted data or usage.

## Read the embedding operation

The embedding method validates a nonempty text list, reserves an attempt and calls the embedding endpoint. Returned rows have indices identifying which input each vector belongs to. Sorting and checking those indices prevents a vector from silently being attached to the wrong text.

An embedding is a numerical representation. Its dimensions are not business fields such as price or quantity. The notebook computes cosine similarity from actual returned vectors and compares that geometry with lexical TF-IDF. Neither score determines source authority. Embedding usage is recorded separately from generated-text usage because its pricing basis differs.

## Follow permitted retrieval

The lexical implementation in `labs/m05.py` selects active documents in the caller's region before fitting its vocabulary. `fit_transform` learns the text-to-column mapping and builds document vectors. `transform` applies the same mapping to the query. Cosine similarity scores candidate directions; a stable document-ID tie break makes equal-score ordering inspectable.

The extended `policy_hits` function in `investigation.py` builds a query from the report. It contains a small explicit expansion for damage terms such as crushed or broken. The development example needed that correction because the policy used different wording. This rule is a maintained choice, not evidence that lexical search understands every paraphrase.

The returned hit retains its document identifier, version and scope. Inspect these intermediate objects before looking at an answer. Retrieval can return a relevant-looking passage that is still unsuitable, incomplete or in conflict with another source.

## Construct and check the brief

`draft` gets the permitted case and policy hits, serialises them and calls the model with an instruction profile and Brief schema. The profile describes the task; the schema describes allowed fields and types. Neither replaces the next application checks.

`validate_brief` compares case identity, ordered quantity and reported quantity with the original input. It checks source membership, retains case source identifiers and requires unresolved questions. The typed `receipt_status` remains unverified for these fixtures. A brief that fails the contract raises an error instead of being silently repaired into an apparent model success.

These checks deliberately have limits. They do not establish that every summary sentence follows from its cited source, that the reference route is universally appropriate or that a reviewer accepts the contribution. The lesson asks the learner to examine those remaining questions explicitly.

## Read the routing categories

The clarified profile distinguishes a missing reported count from an unverified actual receipt. `needs_evidence` is used for the former. Supplied differing quantities lead to `investigate`; the stated damaged-goods cases with equal quantities lead to `review`; defined billing cases lead to `finance`. These are the teaching task's categories.

The earlier profile did not state that distinction precisely enough. A model could reasonably interpret unknown actual receipt as missing evidence for every case. The correction therefore changes the task explanation before treating disagreement as a training defect. The [decision-making research chapter](research/03-decisions.md) develops the organisational importance of such category definitions.

## Trace the model tool loop

`agent_loop.py` supplies capability descriptions and sends the current history to the model. A function-call item contains the requested tool name, argument text and call identifier. The application parses the arguments, checks the allowlist and scope, performs the operation and appends a function-call result with the matching identifier.

The next request includes that observation. If the model returns a final answer, the loop can finish. Independent limits bound rounds and tool operations, and repeated call identities are refused. These checks belong to the application even when the planner's instructions also mention limits.

The tools read fictional cases and policy. No payment, arbitrary file or shell capability is available. A model requesting an unregistered name cannot create the capability merely by naming it.

## Accept specialists before integrating their work

A specialist returns a typed contribution with a case, findings, sources and unresolved questions. Evidence and policy specialists receive different material. `validate_specialist` checks case identity and source membership before the coordinator receives their contributions.

The sequential route waits for one specialist and then the other. The parallel route uses separate waiting operations through `asyncio.to_thread` and gathers their results before coordination. Running calls concurrently can overlap network waiting; it does not remove the need to integrate both contributions. Cancellation of an awaiting task does not necessarily stop a request already running in a thread, so timeouts and budgets still matter.

The coordinator receives accepted contributions and raw evidence, then returns a brief checked by the same application contract. Agreement among specialists is not independent evidence. Their findings must remain traceable to sources that can support or challenge them.

## Follow a review pause into durable state

`durable_review.py` constructs a real LangGraph workflow. The prepare node obtains a contribution and records the case and policy versions. The review node interrupts and exposes a decision request. A SQLite checkpointer retains graph state beyond the current workflow object and process.

On resume the graph reaches the review node again and receives the explicit choice. Consequential work follows the interrupt. The business CaseStore then checks the current versions and role before committing its simulated decision. The graph checkpoint and business database are separate artefacts: one preserves execution, the other records the authoritative case transition.

The notebook reopens the checkpoint through a child Python process without another model call. It then resumes review and checks that preparation was not repeated. That example is more demanding than preserving a Python dictionary, while still making no claim about distributed failover.

## Compare actual runtimes

`frameworks.py` implements the same evidence contract through a model-backed LangGraph node and the OpenAI Agents SDK. The latter requires an asynchronous client. The SDK supplies its own turn control and usage record; its request is not silently included in a different helper's generation ledger.

The comparison holds factual fields and authority conditions stable. Generated summaries can differ as strings. Equal factual fields on one case do not establish equivalent persistence, cancellation, streaming or deployment behaviour. Those features require their own contracts and checks before a runtime replacement is justified.

## Connect a model to actual MCP capabilities

The MCP exercise starts a real stdio server, initialises a session and lists advertised tools. It converts those descriptions into the model's tool interface. When a permitted call returns, the application invokes the MCP tool, checks for an error and passes the observation back to the model.

The fixed north scope is enforced by the local server. Discovery and schema agreement do not establish permission for every record in an enterprise. Protocol messages also share a stream, so arbitrary debug text on the protocol output can corrupt communication. Context managers close sessions and subprocess resources when the exercise ends.

## Inspect generated routing code

`code_generation.py` asks for one small routing function under an explicit specification. It parses the proposed source into an AST and refuses operations outside the tiny exercise subset. The accepted form cannot call functions, import modules, access attributes, loop or mutate state. Behavioural acceptance examples follow the structural checks.

This is not a general sandbox for generated Python. It is a deliberately restricted teaching problem whose operations are inspectable. A real coding-agent workflow also needs change review, isolated execution where appropriate, independent expected outcomes and evidence about the complete application.

## Follow the HTTP service journey

The service resolves a request token into a server-controlled principal. A caller cannot put a manager identity into the decision body to obtain that role. Case reads use the principal's region. Live draft preparation requires a permitted role and an enabled gateway, then persists the accepted contribution against the case version.

The service checks that the case did not change while the model was working before it saves the draft. Reading that saved draft is a separate request. A manager's simulated decision is another command, with current-version and idempotency checks. None of these operations moves money.

The in-process TestClient exercises route handling without a socket. Starting `python -m ai_orgdesign.serve` adds a local server process on port 4192. Hosting it elsewhere would require persistence, identity, security, support and recovery arrangements beyond the static course reader.

## Measure a candidate and retain governance

`evaluate` obtains actual generated predictions, validates their evidence fields and compares routes with the declared reference labels. It keeps per-case rows rather than only a mean. Rejected evidence contracts and route disagreements are different observations. The returned resource proxy is observed tokens, explicitly not currency.

The version helper records a proposal without switching the active configuration. A promotion decision requires comparable evidence and explicit approval under its local rule. Rollback selects the previous approved configuration. It cannot undo a customer message already sent or substitute for an incident correction.

The capstone joins those operations while retaining their boundaries. Read its actual report, explain the mistakes and resource differences, then decide what additional evidence would justify operating the arrangement outside fictional learning cases.
