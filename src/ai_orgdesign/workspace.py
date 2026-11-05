"""Locate this editable course checkout and configure local credentials."""

import os
from pathlib import Path

from dotenv import load_dotenv


def project_root():
    root = Path(__file__).resolve().parents[2]
    if not (root / "pyproject.toml").is_file():
        raise RuntimeError("Run uv sync in the course checkout to install the editable package.")
    return root


def load_local_environment():
    """Load only this checkout's .env; existing shell variables take precedence."""
    return load_dotenv(project_root() / ".env", override=False)


def require_api_key(name):
    """Return a configured value without printing it or making a network call."""
    load_local_environment()
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Set {name} in the local .env file before running this service lesson.")
    return value
