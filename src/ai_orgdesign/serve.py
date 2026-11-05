"""Run the local teaching service with configuration from the root .env."""

import uvicorn

from ai_orgdesign.labs.m19 import create_app
from ai_orgdesign.workspace import project_root, require_api_key


def main():
    token = require_api_key("COURSE_SERVICE_TOKEN")
    output = project_root() / "outputs"
    output.mkdir(exist_ok=True)
    app = create_app(
        output / "harbour.db",
        {token: {"id": "local-manager", "role": "manager", "tenant": "north"}},
    )
    uvicorn.run(app, host="127.0.0.1", port=4192)


if __name__ == "__main__":
    main()
