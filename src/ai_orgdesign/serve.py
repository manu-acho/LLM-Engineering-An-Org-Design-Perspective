"""Run the local teaching service with configuration from the root .env."""

import uvicorn

from ai_orgdesign.labs.m19 import create_app
from ai_orgdesign.provider import Gateway
from ai_orgdesign.workspace import live_mode, project_root, require_api_key


def main():
    token = require_api_key("COURSE_SERVICE_TOKEN")
    output = project_root() / "outputs"
    output.mkdir(exist_ok=True)
    gateway = Gateway(max_requests=20) if live_mode() else None
    app = create_app(
        output / "harbour.db",
        {token: {"id": "local-manager", "role": "manager", "tenant": "north"}},
        gateway=gateway,
    )
    uvicorn.run(app, host="127.0.0.1", port=4192)


if __name__ == "__main__":
    main()
