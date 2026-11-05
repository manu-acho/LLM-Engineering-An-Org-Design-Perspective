"""Check mappings, independent activities and missing executable lesson mechanisms."""

import ast
import json
from pathlib import Path

import nbformat

from ai_orgdesign.workspace import project_root

root = project_root()
manifest = json.loads((root / "study-manifest.json").read_text())
modules = {}
live = 0
for row in manifest["lessons"]:
    note = root / row["lesson"]
    assert note.is_file(), row["lesson"]
    notebook = nbformat.read(root / row["notebook"], as_version=4)
    nbformat.validate(notebook)
    code = [cell.source for cell in notebook.cells if cell.cell_type == "code"]
    for source in code:
        compile(source, row["notebook"], "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    content = "\n".join(cell.source for cell in notebook.cells)
    assert "Independent" in content or "independent" in content, (
        f"No independent activity: {row['notebook']}"
    )
    if row.get("live_recommended"):
        live += 1
        assert "RUN_LIVE" in content and "gateway" in content
    module = Path(row["lesson"]).parent.name
    modules.setdefault(module, []).append(tuple(code))
for module, activities in modules.items():
    assert len(set(activities)) == len(activities), f"Repeated full executable activity in {module}"
assert len(modules) == 20 and len(manifest["lessons"]) == 124
print(
    {
        "modules": len(modules),
        "distinct_lesson_activities": 124,
        "recommended_live_activities": live,
    }
)
print(
    "These structural checks do not certify the quality of an explanation or a learner's understanding."
)
