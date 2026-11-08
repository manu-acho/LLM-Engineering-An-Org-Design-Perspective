# Further explanations and primary technical resources

[Course home](../README.md) · [Glossary](glossary.md) · [Technical foundations](technical-foundations.md)

The course explains the concepts needed for its exercises. These selected resources offer another explanation, a broader tutorial or an authoritative interface reference. They are optional, and their exercises may require different packages or accounts. API details can change after the versions locked in this checkout.

| Topic and course use | Resource | What to read for |
|---|---|---|
| Python, Modules 1–2 and later syntax | [Python 3.12 tutorial](https://docs.python.org/3.12/tutorial/) | Functions, data structures, exceptions and classes; consult individual sections alongside the smaller course examples |
| Neural calculations, Modules 3 and 7 | [PyTorch: Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | Tensor operations, differentiation and model workflows; its full tutorial uses a different task |
| Transformers and tokenisation, Module 3 | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | A wider teaching sequence on transformer models, their uses and limitations |
| The optional small checkpoint, Module 3 | [sshleifer/tiny-gpt2 repository](https://huggingface.co/sshleifer/tiny-gpt2) | Inspect files and metadata; it is a mechanics checkpoint, not a business-model recommendation |
| Leakage and preprocessing, Modules 4 and 6 | [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Why transformations must be fitted on the appropriate training data |
| Retrieval and ranking, Module 5 | [Sentence Transformers: retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | The distinction between candidate retrieval and a second ranking stage |
| Low-rank adaptation, Module 7 | [LoRA paper](https://arxiv.org/abs/2106.09685) | The original transformer adaptation method; distinguish it from the linear teaching exercise |
| Quantized adaptation, Module 7 | [QLoRA paper](https://arxiv.org/abs/2305.14314) | The original method and its memory choices; the course does not run a GPU QLoRA job |
| Optional provider loop, Modules 2 and 9 | [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling) | The message exchange between model proposals, application execution and returned results |
| Graph runtime, Modules 12–13 | [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) | Nodes, state and execution through the actual framework |
| Capability transport, Module 14 | [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Server/client interfaces and version-specific examples |
| Durable decisions, Modules 8, 12 and 17 | [SQLite transactions](https://www.sqlite.org/lang_transaction.html) | Transaction boundaries and concurrent read/write behaviour |
| Concurrent waiting, Module 17 | [Python coroutines and tasks](https://docs.python.org/3.12/library/asyncio-task.html) | Scheduling, waiting and cancellation; compare them with the semaphore exercise |
| HTTP checks, Module 19 | [FastAPI testing guide](https://fastapi.tiangolo.com/tutorial/testing/) | In-process requests with TestClient; distinguish them from a real network deployment |
| Learning environment | [uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/) | Project environments and notebook kernels |

For organisation design, begin with the nine [in-course research chapters](literature-guide.md). Each develops an argument, worked case and scholarly references. The business applications are teaching interpretations; the cited publications retain their original empirical settings and evidential limits.
