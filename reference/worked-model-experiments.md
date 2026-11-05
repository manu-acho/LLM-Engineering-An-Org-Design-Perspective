# Worked model experiments: observations, corrections and limits

[Live-model guide](live-model-guide.md) · [Case data](case-data-guide.md) · [Verification](verification.md)

These are observations from course development on 5 November 2026. They use fictional data and the configurations identified below. They are examples for interpreting an experiment, not expected outputs guaranteed on every run.

## A fluent answer added an unsupported fact

A request supplied an order quantity of twelve and a customer report of ten. A GPT-4.1 Mini response described the order as indicating that twelve boxes were shipped. That inference was unsupported: an order quantity is not a shipment record. The call completed and returned 46 input tokens and 52 output tokens, but successful execution did not make the answer source-faithful.

This is the purpose of the first live exercise. Identify the supplied facts, calculations and new claims separately. A more polished sentence is not a more reliable evidential basis. The course's later structured brief preserves quantities, source identifiers and an explicit unverified-receipt status, while keeping free-text claims subject to review.

The earlier model remains part of this recorded observation. New exercises default to GPT-6 Luna rather than silently treating an old model as the current recommendation. The actual model identifier is retained in each run record.

## A small local instruction model made a visible error

The pinned `HuggingFaceTB/SmolLM2-135M-Instruct` exercise received order twelve and customer report ten. In the observed CPU run it called the discrepancy ten boxes and also claimed the customer had not supplied an exact count. Both statements conflict with the prompt. The arithmetic discrepancy is two, and the reported count is ten; what remains unverified is actual receipt.

This result shows that loading trained weights and obtaining a sentence is not enough. The model is small enough for a CPU exercise, but that hardware convenience is not evidence of task adequacy. Compare it with the hosted result and with an ordinary calculation. See the [model repository](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) for provenance and licence information. Weights are downloaded at the revision included in `model_revisions.py`, not distributed in the course archive.

## Real text adaptation changed a tiny experiment

The adaptation exercise uses the pretrained `prajjwal1/bert-tiny` encoder, LoRA attention updates and a trainable classification head. It trains on twelve invented finance/delivery messages and evaluates four different invented messages. In the recorded forty-step run, test accuracy changed from 0.5 to 1.0, and reloaded predictions matched. There were 4,354 trainable parameters out of 4,390,532 total parameters.

These numbers establish the observed training and reconstruction behaviour on that declared split. They do not establish enterprise routing performance, a generally superior adaptation method or a QLoRA result. A classifier head is newly initialised for the task; the loading warning about its new weights is therefore expected and needs explanation before training. The [base repository](https://huggingface.co/prajjwal1/bert-tiny) identifies its provenance; [PEFT documentation](https://huggingface.co/docs/peft/quicktour) explains the adaptation library. The full experiment code and split are included here.

## Live checks found defects in the application arrangement

The first integration pass exposed a timeout, a brittle validation rule and the use of a synchronous client where the agent SDK required an asynchronous client. These are different failures. Increasing model capability would not repair the client interface, and repeating a timed-out request without inspecting the attempt would conceal uncertainty about usage.

The brittle validation demanded one exact phrase for unknown receipt. It was replaced with a typed `receipt_status` fixed to `unverified`, plus a nonempty list of unresolved questions. This makes the declared field meaningful without treating one spelling as a universal truth detector. Tests still compare quantities and source identifiers with the supplied case. They do not claim to verify every summary sentence.

## Retrieval and label meaning affected the evaluation

A lexical query failed to retrieve the damage-policy passage for a crushed box. An explicit query-expansion rule connected those terms, and the case was checked again. The rule is inspectable and narrow; it is not a claim that lexical retrieval now handles every paraphrase.

A later GPT-6 Luna comparison also exposed an ambiguous category. The model sometimes used `needs_evidence` when actual receipt remained unverified, even though a customer-reported count was available. The teaching reference used that category specifically for a missing reported count. This was a definition problem as well as a model-output issue.

The `grounded-v3` profile makes the category meanings explicit. It distinguishes a null report, a supplied quantity discrepancy, a damage report with equal quantities and an invoice/tax issue. The case guide defines those routes. The earlier comparison is retained as a failed or partial prototype observation; it is not rewritten as an accurate result. The capstone calculates a fresh comparison from its actual returned routes and usage.

## Inspect the current experiment instead of borrowing its verdict

The live capstone returns per-case reference labels, predictions, validation results, accuracy, rejected evidence-contract counts and observed token usage. Its `cost` field is explicitly a token-resource proxy, not a monetary charge. It does not automatically promote a candidate. A more accurate candidate can still increase resource use or reviewer burden, and a two-case comparison is too small to support an enterprise conclusion.

Keep the result, configuration and data identity together. A later run can differ. Use the workbook to explain which correction addresses which mechanism, what remains uncertain and who can decide the next operating step. The [research chapters](literature-guide.md) connect this reasoning to categories, coordination, fit and recurrent work, with their scholarly references.

## A subsequent clarified comparison

In the recorded GPT-6 Luna check, the clarified profile matched the reference route on five teaching cases. A separate two-case capstone run changed route agreement from zero out of two to two out of two. Those are observations of tiny, invented examples, not estimates for an enterprise population. The candidate used more tokens and the promotion rule still blocked it for resource tolerance and absent approval. This is a worked decision, not an automatic success story.
