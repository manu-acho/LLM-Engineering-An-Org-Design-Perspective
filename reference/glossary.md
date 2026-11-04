# Working glossary

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
| MRR | Mean reciprocal rank; the course helper uses keyword first-hit ranks |
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
| Technology-in-practice | Structures enacted through recurrent situated interaction with technology in the practice lens discussed by Stream 6; not a feature list |
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
