"""Report readiness without exposing credentials or contacting providers."""

import importlib.metadata
import sys
from pathlib import Path

from ai_orgdesign.workspace import project_root

root = project_root()
assert sys.version_info[:2] == (3, 12), "Use the Python 3.12 course environment."
assert Path(sys.prefix).resolve() == (root / ".venv").resolve(), (
    "Select this project's .venv kernel."
)
for package in ["jupyterlab", "ipykernel", "nbformat", "nbclient", "python-dotenv"]:
    print(f"{package}: {importlib.metadata.version(package)}")
print("Course environment: ready")
print("Pilot API keys: not required")
print("Local .env:", "present" if (root / ".env").is_file() else "absent (optional for pilot)")
