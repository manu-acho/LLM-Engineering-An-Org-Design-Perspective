"""Real local neural forward pass. Random weights demonstrate mechanics, not competence."""

import torch
from transformers import GPT2Config, GPT2LMHeadModel

VOCAB = ["<start>", "<end>", "check", "the", "order", "record", "evidence", "review"]


def local_inference():
    torch.manual_seed(7)
    config = GPT2Config(
        vocab_size=len(VOCAB),
        n_positions=16,
        n_ctx=16,
        n_embd=16,
        n_layer=1,
        n_head=2,
        bos_token_id=0,
        eos_token_id=1,
        pad_token_id=1,
    )
    model = GPT2LMHeadModel(config).eval()
    tokens = torch.tensor([[0, 2, 3]])
    with torch.no_grad():
        logits = model(tokens).logits[:, -1, :]
        probabilities = logits.softmax(dim=-1)[0]
    return {
        "input_ids": tokens.tolist(),
        "shape": list(logits.shape),
        "probabilities": probabilities.tolist(),
        "parameter_count": sum(p.numel() for p in model.parameters()),
        "weights": "randomly initialised; not pretrained",
        "device": str(next(model.parameters()).device),
    }


def pretrained_inference(model_id="sshleifer/tiny-gpt2", revision=None):
    """Explicit network/download opt-in. Cache externally; never vendor weights."""
    from transformers import AutoModelForCausalLM, AutoTokenizer

    if not revision:
        raise ValueError("Specify the model repository commit for reproducibility")
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    model = AutoModelForCausalLM.from_pretrained(model_id, revision=revision).eval()
    inputs = tokenizer("The delivery record", return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            **inputs, max_new_tokens=8, do_sample=False, pad_token_id=tokenizer.eos_token_id
        )
    return {
        "model": model_id,
        "revision": revision,
        "text": tokenizer.decode(output[0], skip_special_tokens=True),
    }


def demo():
    return local_inference()
