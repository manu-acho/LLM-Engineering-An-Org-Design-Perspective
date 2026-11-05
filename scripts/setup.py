"""Recreate the locked study environment. Run with: python3 scripts/setup.py"""

import shutil
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
uv = shutil.which("uv")
if not uv:
    sys.exit(
        "Install uv using https://docs.astral.sh/uv/getting-started/installation/ and rerun this script."
    )
subprocess.run([uv, "sync", "--locked"], cwd=root, check=True)
env_file = root / ".env"
if not env_file.exists():
    env_file.write_text((root / ".env.example").read_text())
    env_file.chmod(0o600)
subprocess.run(
    [
        uv,
        "run",
        "--locked",
        "python",
        "-m",
        "ipykernel",
        "install",
        "--prefix",
        str(root / ".venv"),
        "--name",
        "ai-orgdesign",
        "--display-name",
        "AI & Organisation Design (.venv)",
    ],
    cwd=root,
    check=True,
)
subprocess.run(
    [uv, "run", "--locked", "python", "scripts/configure_local_environment.py"],
    cwd=root,
    check=True,
)
print("Ready. Open a notebook in VS Code and select this project's .venv Python kernel.")
