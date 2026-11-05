"""CPU-sized text classification with a real pretrained encoder and LoRA.

The dataset is original and intentionally small. Its test accuracy is not a
claim about organisational routing performance. Weight downloads are opt-in.
"""

import json
from pathlib import Path

import torch
from peft import LoraConfig, PeftModel, TaskType, get_peft_model
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "prajjwal1/bert-tiny"
TRAIN = [
    ("invoice has wrong tax", 0),
    ("please correct billing amount", 0),
    ("payment invoice issue", 0),
    ("tax calculation incorrect", 0),
    ("billing correction request", 0),
    ("invoice payment question", 0),
    ("shipment is missing", 1),
    ("delivery arrived damaged", 1),
    ("two boxes did not arrive", 1),
    ("package was crushed", 1),
    ("delivery quantity discrepancy", 1),
    ("shipment delayed at warehouse", 1),
]
TEST = [
    ("correct the invoice", 0),
    ("billing tax question", 0),
    ("damaged shipment", 1),
    ("missing delivery boxes", 1),
]


def train_adapter(output_dir, revision, steps=40):
    if not revision:
        raise ValueError("Pin the public model revision before downloading")
    if type(steps) is not int or not 1 <= steps <= 200:
        raise ValueError("Use 1 to 200 steps for this CPU exercise")
    torch.manual_seed(11)
    previous_threads = torch.get_num_threads()
    torch.set_num_threads(1)
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, revision=revision)
        base = AutoModelForSequenceClassification.from_pretrained(
            MODEL_ID, revision=revision, num_labels=2
        )
        config = LoraConfig(
            task_type=TaskType.SEQ_CLS,
            r=4,
            lora_alpha=8,
            lora_dropout=0.0,
            target_modules=["query", "value"],
            modules_to_save=["classifier"],
            bias="none",
        )
        model = get_peft_model(base, config)
        train_inputs = tokenizer(
            [t for t, _ in TRAIN], padding=True, truncation=True, max_length=32, return_tensors="pt"
        )
        labels = torch.tensor([label for _, label in TRAIN])
        test_inputs = tokenizer(
            [t for t, _ in TEST], padding=True, truncation=True, max_length=32, return_tensors="pt"
        )
        targets = torch.tensor([label for _, label in TEST])

        def accuracy(m):
            m.eval()
            with torch.no_grad():
                pred = m(**test_inputs).logits.argmax(-1)
            return (pred == targets).float().mean().item(), pred.tolist()

        before, _ = accuracy(model)
        optimizer = torch.optim.AdamW((p for p in model.parameters() if p.requires_grad), lr=0.003)
        losses = []
        for _ in range(steps):
            model.train()
            optimizer.zero_grad()
            loss = model(**train_inputs, labels=labels).loss
            loss.backward()
            optimizer.step()
            losses.append(loss.item())
        after, predictions = accuracy(model)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        model.save_pretrained(output_dir)
        tokenizer.save_pretrained(output_dir)
        # Use the same initial classifier seed; the saved trainable head replaces it on load.
        restored_base = AutoModelForSequenceClassification.from_pretrained(
            MODEL_ID, revision=revision, num_labels=2
        )
        restored = PeftModel.from_pretrained(restored_base, output_dir)
        _, reloaded_predictions = accuracy(restored)
        record = {
            "base_model": MODEL_ID,
            "revision": revision,
            "steps": steps,
            "train_n": len(TRAIN),
            "test_n": len(TEST),
            "test_accuracy_before": before,
            "test_accuracy_after": after,
            "predictions": predictions,
            "reload_predictions_equal": predictions == reloaded_predictions,
            "trainable_parameters": sum(p.numel() for p in model.parameters() if p.requires_grad),
            "total_parameters": sum(p.numel() for p in model.parameters()),
            "first_loss": losses[0],
            "last_loss": losses[-1],
            "boundary": "Actual LoRA plus classification-head training on invented text; no QLoRA or enterprise performance claim",
        }
        (output_dir / "experiment.json").write_text(json.dumps(record, indent=2) + "\n")
        return record
    finally:
        torch.set_num_threads(previous_threads)
