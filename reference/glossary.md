# Glossary: concepts and examples

[Guide index](../README.md)

| Term | Meaning in this guide |
|---|---|
| Adapter, software | A wrapper that exposes a stable interface over a particular service |
| Adapter, model | Added trainable parameters used to specialise a base model |
| Agent | A system/component that uses observations and state to choose or perform actions; inspect its actual control flow |
| Affordance | A possibility for a specified actor to act through a technical arrangement under relevant conditions; not a feature alone |
| Affordance actualisation | The actions and processes through which actors realise a technological possibility over time; not installation alone |
| Attention mask | Marks usable versus padded input positions for relevant model operations |
| Authority | The legitimate scope to observe, recommend, decide or execute |
| Baseline | A simpler comparator used to establish whether added complexity improves an outcome |
| Batch | A group of examples/requests; distinguish training minibatches from remote batch jobs |
| Callback | A function registered for another component to invoke later |
| Chat template | Model-specific formatting of roles and turns into a token sequence |
| Chunk | A retrieval unit of text with associated metadata |
| Collator | Code that constructs training batches, often including padding and labels |
| Completion | Generated continuation, or a desired target continuation in training data |
| Context | Information available to the current model request |
| Constraint, relational | A condition through which an arrangement limits an actor's pursuit of a goal; the same arrangement can enable another goal |
| Context window | The supported token capacity, subject to model input/output rules |
| Corpus | The collection of source material available for retrieval |
| Data leakage | Use of information during development/evaluation that would not be available for legitimate prediction |
| Distribution shift | Difference between development examples and encountered operational examples |
| Embedding | A numerical representation used for comparison or downstream modelling |
| Epoch | One pass through the training examples |
| Evaluation | A defined method of assessing behaviour on relevant cases |
| Fine-tuning | Further training that changes a model or adapter's learned parameters |
| Grounding | Tying generated claims to appropriate evidence |
| Hallucination | Generated content that is fabricated or unsupported in its context |
| Holdout | Examples reserved from fitting and selection for a later assessment |
| Idempotency | Retrying an operation with the same identity does not repeat its business effect |
| Inference | Computing predictions/generation using learned parameters |
| JSON / JSONL | Structured text representation / one JSON value per line |
| Label | The target answer or category assigned to a supervised example |
| Latency | Elapsed time until a defined stage or full result completes |
| LoRA | Adaptation using trainable low-rank weight updates |
| Loss | Numerical training objective comparing predictions with targets |
| Loss mask | Selects target positions that contribute to the training objective |
| MAE | Mean absolute error, in target units |
| Metadata | Descriptive fields such as source, version, date, scope or owner |
| Materiality | Properties and arrangements, including digital ones, that make actions possible, difficult, visible, durable or unavailable |
| MRR | Mean reciprocal rank; average of the reciprocal position of the first relevant result under stated relevance labels |
| nDCG | A ranking-quality measure relative to a defined ideal ordering; inspect relevance labels and candidate scope |
| PEFT | Parameter-efficient fine-tuning |
| Prompt | Input that frames the task and supplies context |
| Provenance | Traceable origin and transformation history of information |
| QLoRA | Low-rank adaptation using a quantized frozen base model |
| Quantization | Representing numerical values at reduced precision |
| RAG | Retrieval-augmented generation: supply retrieved evidence at inference time |
| Reranking | Reordering retrieved candidates for a query |
| RMSE | Root mean squared error, with stronger emphasis on large errors than MAE |
| Schema | A declared structure and constraints for data |
| Side effect | A change or interaction beyond computing a return value, such as writing a file or sending a message |
| Sociomateriality | A family of approaches examining social/material relations in practice, including constitutive entanglement; not a synonym for any use of technology by people |
| State | Information retained by an application or workflow across steps/runs |
| Streaming | Incremental delivery of output/events |
| Tensor | A multidimensional numerical array |
| Technology-in-practice | Structures enacted through recurrent situated interaction with technology in the practice lens discussed by Research chapter 6; not a feature list |
| Token | A model/tokenizer-specific unit of encoded text or other input/output |
| Tool call | A model's request for an application-defined capability with arguments |
| Validation | Checking data constraints, or assessing models during selection; specify which meaning applies |
| Vector store | Storage and search over embeddings with associated records |

These are engineering working definitions. Research constructs such as coordination, expertise and accountability need explicit theoretical definitions in a research project; a glossary entry is not a substitute for that work.

## Terms developed in the extended lessons

| Term | Plain-language meaning |
|---|---|
| Logit | A model score for a candidate token before the probability transformation |
| Causal mask | A restriction preventing a prediction position from using future tokens |
| Loss mask | A rule excluding selected target positions from the training objective |
| Temperature | A supported generation setting affecting concentration of token selection, not factual truth |
| Top-p | A sampling rule retaining candidates up to a cumulative probability threshold |
| Cosine similarity | Comparison of vector direction using dot product divided by vector lengths |
| Precision | Relevant or correct positive results divided by all returned or predicted positive results |
| Recall | Relevant or correct positive results found divided by all relevant or actual positive cases |
| Gradient descent | Updating parameters in a direction calculated to reduce a loss locally |
| Closure | A function that retains access to values from its enclosing scope |
| Prompt cache | Reuse of eligible input computation, distinct from saving complete answers or conversation state |
| Transactional outbox | Recording intended external work transactionally with local state so it can be dispatched and reconciled |
| Equifinality | Possibility that different coherent configurations achieve an appropriate result under their conditions |
| Modularity | Dividing a system into parts with limited interactions, with benefits dependent on the work's interdependence |
| Satisficing | Searching for an acceptable choice under criteria and practical limits rather than an all-knowing optimum |
| Relational coordination | Coordination involving shared goals, shared knowledge, mutual respect and suitable problem-solving communication |

## Additional terms for agent engineering

| Term | Meaning in this guide |
|---|---|
| Agent loop | Repeated model proposals, permitted tool operations and returned results, with stopping conditions |
| Agent-as-tool | A specialist returns a contribution to a coordinating agent that retains the final-answer role |
| A2A | A protocol for communication between agent services; it does not assign business authority |
| Checkpoint | A saved graph-state record at an execution boundary |
| Coroutine | An asynchronous operation that can suspend while awaiting compatible work |
| Crew | Agents and tasks assembled under a selected runtime process |
| DAG | A directed dependency graph with no cycle; useful for staged task relationships |
| Discovery | Learning which capabilities a service advertises, distinct from permission to invoke them |
| Guardrail | An automatic check at a particular input, output or tool boundary; inspect its actual coverage |
| Handoff | Transfer of a conversation branch to another agent; distinguish it from accepted business ownership |
| Interrupt | A workflow pause awaiting external input before continuation |
| Lease | Time-limited ownership of work, normally requiring renewal or expiry rules |
| MCP | Model Context Protocol, an interface for applications to use tools and context capabilities |
| Middleware | Code that intercepts or augments a runtime step, such as a tool call or model request |
| Orchestration | How steps, dependencies, context and failures are coordinated |
| Principal | The authenticated person or service on whose behalf an operation runs |
| Reducer | A rule defining how a state field incorporates an update |
| Task contract | The required inputs, output, status meanings, checks and responsibility for a contribution |
| Thread identifier | An identity associating state and continuation with a particular interaction or work item |
| Tool registry | An explicit mapping from permitted operation names to implementations |
| Trace | Connected runtime events used to inspect execution; not proof of a business outcome alone |

## Worked numerical and systems vocabulary

Short definitions are a starting point. The [technical foundations](technical-foundations.md) works through the examples, and the [further reading guide](further-learning.md) offers selected external explanations.

| Term | Meaning and small example |
|---|---|
| Acceptance example | A particular input and expected outcome, such as a wrong-region read returning a refusal |
| Acceptance owner | The role that decides whether a contribution is usable for the next activity, distinct from network delivery |
| Architecture | The model's computational arrangement, such as layers and attention heads; it does not specify learned weights by itself |
| Authentication | Establishing identity under a mechanism, such as a validated token |
| Authorisation | Checking whether that identity may perform this operation on this resource |
| Automatic differentiation | Computing gradients through recorded supported operations, as when backward calculates parameter gradients |
| Backpressure | Slowing or refusing upstream intake when downstream work cannot safely keep up |
| Configuration hash | A digest of specified configuration bytes; it identifies change but does not certify quality or approval |
| Concurrency | Overlapping progress, such as two requests waiting for different services |
| Cosine similarity | Comparing vector direction; it measures representation geometry, not evidence authority |
| Dense representation | A numerical representation with many populated coordinates, often produced by a neural model |
| Fencing | Rejecting operations from a former owner after a newer lease or generation takes over |
| Forward pass | Computing outputs from inputs using current model parameters; the Module 3 pass uses random weights unless the optional pretrained exercise is enabled |
| Generalisation | Performance on relevant cases beyond those used for fitting; lower training loss alone does not establish it |
| Harness | The application arrangement around a model: instructions, tools, context, loop, limits and records |
| HTTP | A request/response protocol; GET reads in the teaching service, while POST submits a decision command |
| Idempotency key | A stable command identity linked to its content, so an identical retry can retrieve the prior result |
| Immutable version | An identified artefact that is not edited in place after evaluation or release |
| Learning rate | An optimiser setting influencing update size; too large a step can overshoot a useful region |
| Least privilege | Granting only capabilities needed for the task, such as a case read without payment access |
| Liveness | Whether a process responds under a declared check; it is different from readiness to serve its task |
| Matrix | A rectangular numerical table, such as two cases by two quantities |
| Monotonic clock | A clock suitable for measuring elapsed duration without wall-clock adjustments |
| Optimistic concurrency | Reading a version and accepting an update only if that version is still current |
| Parallelism | Computation occurring simultaneously on multiple execution resources; not the same as overlapping waiting |
| Principal | A person or service identity with associated scope; it must come from a trusted identity mechanism |
| Prompt injection | An attempt to make untrusted content redirect model behaviour beyond its intended role as data |
| Rank | The number of independent directions in a matrix; a rank-one update constrains the changes it can express |
| Readiness | Whether a service meets declared conditions to receive work, including necessary dependencies |
| Reconciliation | Resolving an uncertain or inconsistent outcome by checking authoritative records and correcting it |
| Rollback | Selecting a previous configuration for new work; it does not automatically undo earlier consequences |
| Scalar | One number, such as a quantity of twelve |
| Semaphore | A local mechanism limiting how many tasks enter a region concurrently |
| Sparse representation | A vector with many zero entries, as in a word-count vocabulary |
| Tensor | A numerical array; shape [2, 3] can represent two cases with three features each |
| TF-IDF | A lexical weighting of words within and across documents; it is not a neural embedding model |
| Threat model | An account of assets, actors, trust boundaries, attacks and consequences used to plan controls |
| Transaction | A database commit-or-rollback unit; it does not automatically include external side effects |
| Vector | An ordered collection of numbers, such as [12, 10] for ordered and reported quantities |
| Vertical slice | One end-to-end contribution through the necessary layers, rather than one disconnected layer |

## Vocabulary for the live implementation route

| Term | Plain meaning and example |
|---|---|
| SDK | A software library for using a service; the Python client packages HTTP requests and response objects |
| Gateway, course helper | The included session object that sets request limits, checks completion and retains usage; it is not a separate model |
| Attribute | A named part of an object, accessed with a dot, such as result.text |
| Keyword argument | A labelled function input, such as max_requests=1 |
| Schema | A declared structure and allowed types; it can require a field without establishing the field's truth |
| Typed output | A returned value checked against a declared structure, such as a brief with an integer quantity |
| Null / None | JSON null corresponds to Python None here; both preserve absence rather than inventing a zero |
| Delta | The newly arrived part of streamed output, not necessarily the full text so far |
| Refusal | A model response declining the task; it should not be presented as a completed investigation contribution |
| Incomplete response | A run that ended without a completed answer, potentially after consuming tokens |
| Transport fixture | Controlled local request/response behaviour used in a test; it is not a provider observation |
| Async client | A client whose operations are awaited; passing a synchronous client to an asynchronous framework is an interface mismatch |
| Annotation | Type information attached to a Python definition; its runtime effect depends on the component interpreting it |
| Checkpoint | Saved execution state at a boundary, used here to resume the review graph after reopening its database |
| AST | Abstract syntax tree, a structured representation of code used to inspect allowed operations before a restricted execution |
| Classification head | A task-specific output layer mapping model representations to class scores; new weights need training |
| Query expansion | Adding related search terms under an explicit rule, such as crushed to the damage-policy wording |
| Evidence contract | Declared checks linking returned fields to a case, allowed sources and unresolved facts |
| Route agreement | Fraction of predictions matching the specified reference categories; its interpretation depends on what those categories mean |
| Resource proxy | A measure used to represent one aspect of resource use, such as token counts; it must not be relabelled as an observed financial expense |

The [live-model guide](live-model-guide.md) works through these terms in a request. The [worked experiments](worked-model-experiments.md) show why their distinctions affect actual outcomes.

| Additional term | Meaning |
|---|---|
| Tenant, in this course | The caller's authorised organisational scope; north and south are teaching regions, not evidence of a complete multi-tenant deployment |
| Encoder | A model component producing representations of supplied input; the BERT exercise adds a classification head to them |
| Decoder, autoregressive | A model component predicting successive output tokens under the permitted context |
| Traceback | The sequence of calls shown when Python raises an exception; inspect the final category and the relevant course line |
| Idempotency scope | The boundary within which a repeated command identity has its declared effect, such as one local database |

## Harbour’s supply-chain vocabulary

These terms are introduced in [Meet Harbour](../HARBOUR.md). They describe the business setting; they do not imply that every activity is implemented in the notebooks.

| Term | Meaning and example |
|---|---|
| Business-to-business distributor | A business buying goods from producers and supplying other businesses; Harbour supplies packaging |
| Supply chain | Connected work across suppliers, distributors, delivery partners and customers that makes goods available |
| Inventory | Stock held for use or sale; Harbour’s available packaging stock |
| Replenishment | Arranging more stock to meet future needs; distinct from replacing a disputed delivery |
| Order fulfilment | The work of turning an accepted order into the required supply, including allocation, picking, packing and delivery arrangements |
| Picking and packing | Selecting items from storage and preparing them for transport |
| Dispatch | Entry into the delivery process; a dispatch record does not by itself verify customer receipt |
| Account settlement | Resolving amounts owed and their payment status; different from physically delivering goods |
| Credit | An authorised reduction of an amount charged to a customer; different from a payment or a replacement shipment |
| End-to-end service outcome | What the connected work achieves for the customer; a shorter drafting task alone does not establish an improved resolution |

The course’s north and south scopes demonstrate region-specific access. A permitted regional lookup is an application boundary, rather than a complete design of Harbour’s geographic structure. Ownership of a source, ownership of an unresolved case and authority to approve a remedy remain distinct.
