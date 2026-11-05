"""Train, save and reload a low-rank update on an original tiny linear task."""

from pathlib import Path

import torch


class LowRank(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.register_buffer("base", torch.eye(2))
        self.a = torch.nn.Parameter(torch.tensor([[0.1, -0.1]]))
        self.b = torch.nn.Parameter(torch.zeros(2, 1))

    def forward(self, x):
        return x @ (self.base + self.b @ self.a).T


def adapt(path):
    torch.manual_seed(7)
    model = LowRank()
    x = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [-1.0, 1.0]])
    target = x @ torch.tensor([[1.5, -0.5], [0.0, 1.0]]).T
    before = torch.nn.functional.mse_loss(model(x), target).item()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
    for _ in range(120):
        optimizer.zero_grad()
        loss = torch.nn.functional.mse_loss(model(x), target)
        loss.backward()
        optimizer.step()
    torch.save(model.state_dict(), path)
    restored = LowRank()
    restored.load_state_dict(torch.load(Path(path), weights_only=True))
    after = torch.nn.functional.mse_loss(restored(x), target).item()
    return {
        "loss_before": before,
        "loss_after": after,
        "reload_equal": bool(torch.allclose(model(x), restored(x))),
        "base_unchanged": bool(torch.equal(restored.base, torch.eye(2))),
        "boundary": "Real gradient updates on a linear toy; no LLM fine-tuning or quantization",
    }


def demo():
    import tempfile

    with tempfile.TemporaryDirectory() as folder:
        return adapt(Path(folder) / "adapter.pt")
