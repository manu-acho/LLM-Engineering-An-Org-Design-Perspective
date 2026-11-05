# Verification: what executed and what the evidence supports

[Live-model guide](live-model-guide.md) · [Worked experiments](worked-model-experiments.md) · [Curriculum](../CURRICULUM.md)

## Distinct kinds of evidence

The course separates arithmetic examples, code checks, actual model calls, protocol exchanges and organisational outcome claims. A successful assertion supports its stated property. A completed provider response establishes a request outcome. Neither establishes that an organisation benefited.

All cases, reference labels, prices explicitly labelled as assumptions and simulated review identities are teaching material. The research chapters contain the scholarly argument and references. Their organisational applications remain interpretations with the original studies' setting boundaries preserved.

## Offline learning and checks

Each lesson has a mapped notebook with a distinct practical focus. Written mechanism examples are included where executable, independent attempts precede labelled solutions, and selected lessons include programming tasks with contrasting checks. The automatic verifier executes notebooks in fresh kernels from unrelated working directories without overwriting them.

It also forces `COURSE_OFFLINE_TEST=1`. This override prevents a learner's live-mode setting or configured key from triggering paid calls during routine verification. Local MCP subprocesses, neural arithmetic, database transactions and in-process HTTP checks still execute. CPU-model downloads remain explicitly disabled in that path.

The behavioural suite checks real SDK response parsing through an offline transport, incomplete and empty responses, request ceilings, usage handling, scoped data, generated-code restrictions, evidence contracts, specialist integration, checkpointed review, policy/version conflicts, persisted drafts and governed configuration changes. Controlled fixture responses are labelled as fixtures; their scores are not provider observations.

## Actual live development checks

The revised course was exercised with actual provider calls using fictional fixtures. Checks covered generation and streaming, structured briefs, neural embeddings, model-proposed tools, parallel specialists, model-backed LangGraph and OpenAI Agents SDK paths, a model using actual MCP stdio tools, a graph review pause and resume, restricted generated routing code, an instruction-like customer report and measured evaluation through the local service capstone.

The initial checks exposed defects and ambiguous definitions. These are retained in the [worked experiment discussion](worked-model-experiments.md). Corrected paths were rechecked. Recorded API execution and evidence-contract acceptance remain distinct from reference-route agreement; a valid brief can still be routed differently from the teaching reference.

The course default is configurable GPT-6 Luna, using the Responses API and no reasoning effort in the helper. Earlier GPT-4.1 Mini observations remain historical development records. Account access and future model behaviour are not assumed from those records. Every new run should retain its returned model, settings, data and usage identity.

## Actual local model experiments

The numerical model exercise runs a small random GPT-2 architecture. The pretrained CPU extension loads a pinned SmolLM2 instruction checkpoint and inspects its generated answer. A recorded wrong answer is part of the lesson rather than evidence that the task succeeded.

The text-adaptation extension performs actual LoRA and classification-head training on a pinned BERT encoder, saves the adapter, reloads it and compares predictions. It uses a twelve-message training split and four-message test split. It is not a QLoRA or GPU-training benchmark, and the tiny test score is not an enterprise performance estimate.

## Local service and operating boundaries

The HTTP service supports authenticated case reads, role-gated live draft preparation, persisted draft reads and versioned simulated decisions. A local socket check is separate from the in-process client. Review and policy conditions still apply after a model finishes. No payment tool, real customer message or live enterprise data integration is included.

Cloud deployment, distributed failover, real identity-provider integration, load capacity and backup restoration require separate environments and evidence. The course teaches their design requirements; it does not report those unexecuted operations as verified. The static reader supplies notes and downloads rather than executing Python.

## Reproduce the local checks

From the course root:

```sh
uv run --locked pytest
uv run --locked python scripts/check_learning_path.py
uv run --locked python scripts/verify_notebooks.py
node browser-reader/scripts/check.mjs
```

The learning-path check examines mapping, practical coverage and independent workspaces. It cannot certify pedagogy by counting files. Human review must still assess whether explanations, examples, exercises and transitions allow a new learner to make the intended progress.

To deliberately run paid checks with the private workspace key:

```sh
uv run --locked python scripts/verify_live.py --confirm-live
uv run --locked python scripts/verify_live.py --confirm-live --scenario capstone
```

The smoke route uses two requests; the capstone uses five. Both have a six-attempt ceiling and save actual outputs and usage under ignored `outputs/`. The capstone keeps promotion subject to its resource and approval conditions. Inspect the saved answers as well as execution status. Repeating either command incurs new usage.
