"""Report readiness without exposing credentials or contacting providers."""

import importlib.metadata
import os
import sys
from pathlib import Path

from ai_orgdesign.workspace import live_mode, load_local_environment, project_root

root = project_root()
assert sys.version_info[:2] == (3, 12), "Use the Python 3.12 course environment."
assert Path(sys.prefix).resolve() == (root / ".venv").resolve(), (
    "Select this project's .venv kernel."
)
for package in ["jupyterlab", "ipykernel", "nbformat", "nbclient", "python-dotenv"]:
    print(f"{package}: {importlib.metadata.version(package)}")
print("Course environment: ready")
load_local_environment()
print("OpenAI key:", "configured" if os.environ.get("OPENAI_API_KEY") else "not configured")
print("Selected model:", os.environ.get("OPENAI_MODEL") or "gpt-6-luna")
print("Live learning mode:", live_mode())
print("Local .env:", "present" if (root / ".env").is_file() else "absent (optional for pilot)")
