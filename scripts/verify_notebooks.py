"""Execute each published notebook in a fresh kernel; never save learner edits."""

import json
import os

os.environ["COURSE_OFFLINE_TEST"] = "1"
import tempfile

import nbformat
from nbclient import NotebookClient

from ai_orgdesign.workspace import project_root

root = project_root()
manifest = json.loads((root / "study-manifest.json").read_text())
for lesson in manifest["lessons"]:
    if lesson.get("network_calls") or lesson.get("requires_api_keys"):
        raise RuntimeError(
            "Service-dependent notebook requires an explicit opt-in verification policy: "
            + lesson["notebook"]
        )
    notebook = nbformat.read(root / lesson["notebook"], as_version=4)
    nbformat.validate(notebook)
    with tempfile.TemporaryDirectory(prefix="ai-orgdesign-notebook-") as directory:
        # An unrelated working directory detects accidental dependence on where Jupyter starts.
        NotebookClient(
            notebook,
            timeout=180,
            kernel_name="ai-orgdesign",
            resources={"metadata": {"path": directory}},
        ).execute()
    count = sum(cell.cell_type == "code" for cell in notebook.cells)
    print(f"PASS {lesson['notebook']} ({count} code cells)", flush=True)
print(f"Executed {len(manifest['lessons'])} notebooks. No source notebooks were overwritten.")
