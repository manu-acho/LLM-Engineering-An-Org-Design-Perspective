"""Create an unpublished notebook draft matching an existing lesson.

Example: uv run python scripts/new_notebook.py --lesson modules/02-example/01-topic.md --folder 02-example
This does not add the draft to the public study manifest.
"""

import argparse
import json
import re

from ai_orgdesign.workspace import project_root

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--lesson", required=True)
parser.add_argument("--folder", required=True)
args = parser.parse_args()
root = project_root()
if not re.fullmatch(r"modules/[a-z0-9-]+/\d{2}-[a-z0-9-]+\.md", args.lesson):
    parser.error("Use a numbered lesson path under modules/.")
if not re.fullmatch(r"[a-z0-9-]+", args.folder):
    parser.error("Notebook folder must contain lowercase letters, numbers or hyphens.")
lesson = root / args.lesson
if not lesson.is_file():
    parser.error("Write the lesson before creating its notebook.")
notebook_path = root / "notebooks" / args.folder / lesson.with_suffix(".ipynb").name
if notebook_path.exists():
    parser.error("Notebook already exists; it was not overwritten.")
template = json.loads((root / "templates/lesson.ipynb").read_text())
title = lesson.read_text().splitlines()[0].removeprefix("# ")
template["cells"][0]["source"] = (
    f"# {title}\n\nDraft companion to `{args.lesson}`. Complete and verify before publication."
)
notebook_path.parent.mkdir(parents=True, exist_ok=True)
notebook_path.write_text(json.dumps(template, indent=2) + "\n")
print(notebook_path.relative_to(root))
print("Draft only. Add to study-manifest.json after completing and verifying the teaching content.")
