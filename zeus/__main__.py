import os

import uvicorn

from .api import create_app

uvicorn.run(create_app(), host=os.environ.get("ZEUS_HOST", "127.0.0.1"), port=int(os.environ.get("ZEUS_PORT", "8080")),
            log_level=os.environ.get("ZEUS_LOG_LEVEL", "info"))
