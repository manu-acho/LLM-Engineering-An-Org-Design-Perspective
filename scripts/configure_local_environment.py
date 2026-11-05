"""Add missing blank settings and a local service token, without displaying secrets."""

import secrets

from dotenv import dotenv_values, set_key

from ai_orgdesign.workspace import project_root

root = project_root()
path = root / ".env"
if not path.exists():
    path.write_text((root / ".env.example").read_text())
values = dotenv_values(path)
for name, default in dotenv_values(root / ".env.example").items():
    if name not in values:
        set_key(path, name, default or "")
if not values.get("COURSE_SERVICE_TOKEN", ""):
    set_key(path, "COURSE_SERVICE_TOKEN", secrets.token_urlsafe(32))
path.chmod(0o600)
print("Local settings ready; existing keys preserved. No secret values displayed.")
