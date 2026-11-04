# Lesson 7.5: Train, save and reconstruct a small adapted system

[Module route](README.md) · [Next: decide whether specialisation is worthwhile](06-design-lab.md)

## Inspect the source contract first

The course's [Week 7 preparation](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/pricer/items.py) creates prompts ending in `Price is $` and stores completions separately. Some splits use rounded targets; test examples retain original price representations. Those choices affect what is learned and measured.

The [later serving implementation](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/pricer_service2.py) reconstructs the base and tokenizer, attaches a pinned adapter, rebuilds the input prefix, generates and parses a number. A changed tokenizer or prompt contract can invalidate the intended comparison even if loading succeeds.

The remote training lesson could not be inspected. The following is a new, complete local mechanics lab. It requires `torch`, `transformers` and `peft`; it downloads nothing, trains random tiny weights through LoRA and writes only within a temporary directory. Integer tokens are invented symbols. This is not a useful language model or a QLoRA performance experiment.

```python
from tempfile import TemporaryDirectory
from pathlib import Path
import torch
from transformers import GPT2Config, GPT2LMHeadModel
from peft import LoraConfig, PeftModel, get_peft_model

torch.manual_seed(11)
configuration = GPT2Config(
    vocab_size=16, n_positions=16, n_embd=16, n_layer=1, n_head=2,
    bos_token_id=1, eos_token_id=15, pad_token_id=0,
    resid_pdrop=0.0, embd_pdrop=0.0, attn_pdrop=0.0,
)
ids = torch.tensor([[1, 2, 3, 4], [1, 5, 6, 7]])
labels = torch.tensor([[-100, -100, 3, 4], [-100, -100, 6, 7]])
mask = torch.ones_like(ids)

with TemporaryDirectory() as directory:
    base_path = Path(directory) / "base"
    adapter_path = Path(directory) / "adapter"
    base = GPT2LMHeadModel(configuration)
    base.save_pretrained(base_path)
    adapted = get_peft_model(base, LoraConfig(
        task_type="CAUSAL_LM", r=2, lora_alpha=4,
        target_modules=["c_attn"], fan_in_fan_out=True,
    ))
    optimizer = torch.optim.AdamW(
        [p for p in adapted.parameters() if p.requires_grad], lr=0.01
    )
    frozen = {name: p.detach().clone() for name, p in adapted.named_parameters() if not p.requires_grad}
    adapted.train()
    losses = []
    for step in range(8):
        optimizer.zero_grad()
        loss = adapted(input_ids=ids, attention_mask=mask, labels=labels).loss
        losses.append(float(loss.detach()))
        loss.backward()
        optimizer.step()
    adapted.eval()
    assert all(torch.equal(frozen[name], p.detach()) for name, p in adapted.named_parameters() if name in frozen)
    with torch.no_grad():
        expected = adapted(input_ids=ids, attention_mask=mask).logits
    adapted.save_pretrained(adapter_path)
    restored = PeftModel.from_pretrained(
        GPT2LMHeadModel.from_pretrained(base_path), adapter_path
    ).eval()
    with torch.no_grad():
        actual = restored(input_ids=ids, attention_mask=mask).logits
    assert torch.allclose(expected, actual, atol=1e-5)
    assert len(losses) == 8
```

## Read the update lifecycle

The base is saved before attaching the adapter so reload uses the same frozen starting system. `get_peft_model` adds the selected adaptation. The optimizer receives trainable parameters only. Each step clears gradients, computes a masked token loss, differentiates and updates. Saving the adapter stores the adaptation, not a complete replacement for the base.

The `frozen` snapshot lets the lab check that parameters excluded from training remain unchanged. The saved copies cost additional memory, so this is a tiny teaching check, not a suggestion to clone every frozen tensor of a large production model.

The final assertion compares logits after reconstruction in evaluation mode. It checks that the saved pieces reconstruct the same numerical behaviour on these inputs. It does not check generalisation. Separate holdout sequences and a meaningful task would be needed for that.

Eight steps are chosen to keep the exercise small. Do not interpret the last recorded training loss as a business-quality estimate. For real text, a tokenizer, template, completion boundary, padding policy and dataset split must also be retained. The invented mapping in this exercise exists only to expose the mechanics.

## Connect back to four-bit serving

In the source service, `BitsAndBytesConfig` specifies four-bit loading, NF4, double quantization and a compute dtype. `PeftModel.from_pretrained` attaches the selected adapter revision. These settings rely on a compatible hardware/software environment. Adding a quantization configuration to the tiny CPU lab would not establish a valid large-model training environment.

The source parser extracts a number after the price prefix and returns zero if parsing fails. For evaluation, preserve an explicit invalid status instead. A generated zero price and a failed parser should not become the same observation.

**Worked exercise:** A saved adapter loads successfully but scores worse after deployment. Compare base revision, tokenizer, prompt prefix, truncation, numerical parser and task population before assuming the adapter weights changed. The running system is a chain of compatible artefacts.

**Further reading:** [PEFT quicktour](https://huggingface.co/docs/peft/en/quicktour) and [bitsandbytes integration](https://huggingface.co/docs/transformers/en/quantization/bitsandbytes). The local lab and the source's large-model service have deliberately different resource requirements.
