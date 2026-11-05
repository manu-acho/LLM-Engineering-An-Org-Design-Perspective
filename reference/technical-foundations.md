# Technical foundations: small examples before larger systems

[Start here](../START-HERE.md) · [Glossary](glossary.md) · [Programming patterns](python-patterns.md)

These introductions supply the numerical and systems ideas used across the course. Each begins with a small example. Return to the relevant section before a lesson uses the term; no calculus or database background is assumed.

## Vectors, matrices and tensors

A **scalar** is one number, such as twelve. A **vector** is an ordered collection of numbers, such as `[12, 10]` for an ordered quantity and a reported quantity. Position matters: swapping those values changes their meaning. A **matrix** is a rectangular table of numbers. Two cases with two quantities each can be represented as `[[12, 10], [8, 8]]`.

A **tensor** is a numerical array that can have zero, one, two or more dimensions. A scalar, vector and matrix are therefore particular tensor shapes. A shape describes the size of each dimension. A table containing two cases and three features has shape `[2, 3]`. In a language-model batch, a shape such as `[2, 4, 8]` can mean two sequences, four positions and eight vocabulary scores at each position. The interpretation comes from the operation, not from the word tensor alone.

**Matrix multiplication** combines compatible tables by multiplying and summing corresponding entries. A row `[2, 3]` multiplied by a column `[4, 5]` produces `2 × 4 + 3 × 5 = 23`. The number of columns in the first table must match the number of rows in the second. Python's `@` operator expresses matrix multiplication for the tensor objects used here. It differs from multiplying corresponding entries separately.

In Module 7, a two-by-one matrix multiplied by a one-by-two matrix produces a two-by-two update. Its entries are constrained by that construction. **Rank** describes the number of independent directions a matrix can represent. A rank-one update has only one such direction; it cannot represent every possible two-by-two change. This restriction is the mechanism that the low-rank lab exposes.

## Scores, probabilities and attention

A score is a number used to compare candidates. It does not automatically mean a probability. **Softmax** exponentiates a collection of scores and divides each resulting weight by their sum. For two equal scores, the probabilities are one half and one half. For unequal scores, the larger score receives more probability. Subtracting the same constant from every score leaves the mathematical distribution unchanged and can improve numerical stability.

A **logit** is a model score before that probability conversion. A distribution over next tokens answers which continuation the model assigns probability to under its computation. It does not give a probability that the delivery record is factually correct. This distinction remains true even when the output is a confident sentence.

**Attention** computes how information at one position is combined with information at other permitted positions. A query representation is compared with key representations to obtain scores; normalised scores weight value representations. These names describe mathematical roles, not a database lookup or a claim that the model understands a person. A causal mask prevents a next-token prediction from using future positions during the relevant computation.

A **head** is one attention calculation with its own learned transformations. Several heads can provide different combinations before later transformations combine their outputs. An **embedding** maps a token identifier into a numerical representation. These representations are model-specific learned quantities; coordinate number five does not normally have a simple human-readable meaning.

The local Module 3 model has random initial parameters. It executes this architecture without having learned useful language. The optional pretrained exercise supplies previously trained parameters and the matching tokenizer. Architecture, learned weights and input formatting are all needed to interpret what runs.

## Loss, gradients and an optimiser

A **loss** is a numerical objective comparing model outputs with training targets. Consider a scalar model `prediction = w × x`, with input two and target six. At weight one, the prediction is two. Squared error is `(2 - 6)² = 16`. At weight two, the prediction is four and squared error is four. The lower loss here corresponds to a closer training prediction.

A **gradient** describes the local rate and direction of change of the loss with respect to a parameter. For this example the gradient at weight one is negative sixteen. With a learning rate of 0.1, the simple update `new_weight = weight - learning_rate × gradient` gives 2.6. The next prediction is 5.2 and squared error is 0.64. This worked step illustrates how a calculated direction can reduce an objective; it does not guarantee that every step size or complex training run improves.

**Automatic differentiation** records supported calculations and computes their gradients. In PyTorch, `loss.backward()` calculates gradients and an optimiser's `step()` uses them to update parameters. `zero_grad()` clears accumulated gradients before the next ordinary training step. Adam is an optimiser that maintains additional state and adapts updates; it is not identical to the simple arithmetic rule above.

Training repeatedly adjusts parameters. Inference computes outputs with the current parameters. `eval()` selects evaluation behaviour for relevant layers; `no_grad()` stops gradient recording. These have different purposes, so both may appear during inference. A lower training loss does not establish generalisation. Evaluation on appropriate examples not used for fitting is a separate activity.

## Similarity and retrieval

A sparse word vector can store one number per vocabulary term, with many zeros. **TF-IDF** combines how often a word appears in a document with a weight related to how widely it appears across documents. It is a lexical representation. A dense neural embedding instead represents text through a trained model; similar-looking numbers do not make the two methods equivalent.

A **dot product** multiplies corresponding vector entries and sums them. Cosine similarity divides the dot product by the product of the vector lengths. Identical nonzero directions have cosine one; perpendicular directions have cosine zero. The value measures the chosen representation's geometry, not policy authority or factual truth.

A **chunk** is a selected piece of a source document used as a retrieval unit. Splitting can make passages more focused, but can detach a rule from its exception. Retain source identity and the context needed to interpret the passage. A **reranker** compares an initial set more closely; it cannot rescue evidence that the initial retrieval never included.

## State, transactions and versions

**State** is information retained so work can continue. A notebook variable is state, but disappears when its kernel ends. A database can preserve state beyond that process. Persistence alone does not guarantee correctness: a stale or mistaken value can also be stored durably.

A **transaction** groups database operations under a commit-or-rollback boundary. In the case store, checking a version, recording a decision, storing its command key and writing its audit event belong together. If one fails, a partial decision should not remain committed. SQLite supplies transaction behaviour for its database; it does not automatically include an external email or payment in the same atomic unit.

An **optimistic version check** lets a client work from a snapshot, then rejects its update if the authoritative record changed. Two managers can read version one. After the first commits version two, the second must refresh rather than overwrite the new state. It is called optimistic because the system permits concurrent reading and detects a conflict at update time.

**Idempotency** concerns the effect of repeating an operation under a declared identity. The example stores a command fingerprint with its result. The identical retry receives the previous result; a different command using the same key is refused. This is a local database guarantee with a defined scope. It is not a claim that every networked side effect occurs exactly once.

## Asynchronous execution and leases

A **coroutine** is an operation that can suspend at an `await`, allowing compatible work to proceed while it waits. `async def` defines one; calling it creates an awaitable object rather than automatically finishing the operation. In a notebook, top-level `await` can run it. In an ordinary entry-point script, `asyncio.run` starts the event loop. Do not call that launcher inside an already running notebook event loop.

A **semaphore** limits how many tasks enter a region at once. It controls local overlap, not the number of workers in a separate distributed system. A **lease** records temporary ownership of a job. An expired owner may still be running, so the authoritative completion operation must check current ownership. External actions may require additional fencing or reconciliation.

## HTTP, identity and failure

An **HTTP route** combines a method and path, such as `GET /cases/H-17` for reading and `POST /cases/H-17/decisions` for submitting a command. A **header** carries request metadata; a **body** carries submitted content. JSON is a structured text format used for the body. A schema checks declared structure and types, not whether a statement is true.

Authentication establishes an identity under a mechanism. Authorisation checks what that identity may do. In the teaching HTTP app, a server-controlled mapping resolves an opaque token into a principal with identity, role and tenant. Allowing a request body to name its own manager role would defeat this boundary.

A timeout says the caller did not receive completion in time. It does not establish whether the server committed an operation. Separate failed, unknown and confirmed outcomes. Retrying an unknown action safely may need a stable command identity and reconciliation. An HTTP success response likewise does not establish that the customer's wider problem is resolved.

## Check understanding

Explain why an eight-entry probability vector is not an eight-case evaluation; why a lower training loss is not a business benefit; why a stored approval can become stale; and why a timeout can coexist with a committed action. Strong answers identify the particular object and boundary each term describes. The examples above supply the reasoning; later modules make those distinctions executable.

## Read the SQL in the case store

SQL is a language for querying and changing relational tables. A table contains rows and named columns. In the `cases` table, one row represents one fictional case; the `id` column is its primary key, a unique identifier. `CREATE TABLE IF NOT EXISTS` creates the initial structure without replacing an existing table.

`SELECT * FROM cases WHERE id=? AND tenant=?` asks for columns from rows matching both conditions. The question marks are parameter placeholders. The database driver receives the values separately, avoiding the unsafe practice of splicing untrusted strings into SQL syntax. This query's tenant condition is an application access boundary only when the supplied tenant comes from trusted identity.

`INSERT` adds a row. `UPDATE` changes matching rows. The lease claim uses an update whose `WHERE` condition permits only queued or expired work. Checking `rowcount` distinguishes acquiring the lease from merely executing a syntactically valid statement. An update that changes zero rows is not a successful claim.

`BEGIN IMMEDIATE` requests a write transaction before the case decision checks and update. Another writer cannot simultaneously commit a conflicting write inside that transaction. If a validation check raises an exception, the context manager rolls the transaction back. On success it commits, and its `finally` block closes the connection. SQL transaction behaviour does not reach outside this database file.

The example's version check and stored command result make a particular retry contract inspectable. They do not supply distributed consensus, account reconciliation, backup restoration or a schema migration system. These are distinct capabilities that a larger operating design may require.

## Objects and named inputs before SDK code

An object groups values and operations. In `session = Gateway(max_requests=1)`, `Gateway` constructs a session object and the named input sets its attempt ceiling. `session.generate(prompt)` calls an operation belonging to that object. `result.text` reads a named attribute of the returned object. The dot expresses access; it does not imply that a network request happened. Construction, calling and reading are different operations.

A class defines how such objects are constructed and behave. `def` defines a function; a function declared inside a class can act as a method. This is why the shared implementation contains both `class Gateway` and `def generate`. The early live exercise needs only their public input/output contract; the later walkthrough opens the implementation.

A type annotation such as `reported: int | None` describes either a whole number or absence. Pydantic interprets its model annotations during validation. Ordinary Python annotations do not automatically perform all those checks. A valid integer can still describe the wrong case, so the application also compares it with the authoritative input.

## Read a comprehension in ordinary steps

`[row for row in records if row['active']]` creates a list. Read it as: visit each row, keep it when active is true, then place the row into the new list. A longer equivalent starts with an empty list, loops over records, checks an if condition and appends each retained row. A set expression uses braces and retains distinct values. The syntax is concise, but the underlying operations should remain explainable.

## Understand the review pause

The graph first prepares and validates a contribution, then reaches an interrupt. The interrupt records that an external choice is required. A later resume supplies the review choice and continues against the saved state. Code before the interrupt can run again when its node resumes, so consequential effects belong after the pause and still require current-version checks.

The SQLite checkpointer used by the revised lesson persists actual graph execution state. It is distinct from the business database that records case decisions. A model call completed before a checkpoint may still be repeated after a failure between those events, so a checkpoint is not a universal exactly-once guarantee. The application retains idempotency and reconciliation questions at their real boundaries.

## Read generated code without assuming it is safe

An abstract syntax tree represents code as structured nodes. The small routing exercise accepts only a tightly restricted collection of nodes: a function, conditions, comparisons, dictionary reads and returns. It rejects calls, imports, attribute access, loops and mutation before compilation. Its acceptance cases then check behaviour. This is an inspectable exercise restriction, not a general mechanism for safely executing arbitrary Python.

A generated program can parse successfully and still implement the wrong policy. Likewise a test can share the generator's mistaken interpretation. Write some expected outcomes independently, include contrasting cases and inspect the smallest change that could explain a failure.
