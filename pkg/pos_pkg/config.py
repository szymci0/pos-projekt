import os
from pathlib import Path

import pos_pkg

ROOT_DIR = Path(pos_pkg.__file__).parent
PROJECT_DIR = ROOT_DIR.parent.parent

SECRET_KEY = os.environ["SECRET_KEY"]


APIHOST = os.environ["APIHOST"]
WEBHOST = os.environ["WEBHOST"]
MONGODB_HOST = os.environ["MONGODB_HOST"]
MONGODB_USER = os.environ["MONGODB_USER"]
MONGODB_PASSWORD = os.environ["MONGODB_PASSWORD"]
MONGODB_PORT = int(os.environ["MONGODB_PORT"])
MONGODB_DB_NAME = os.environ["MONGODB_DB_NAME"]
MONGO_AUTH = f"{MONGODB_USER}:{MONGODB_PASSWORD}@" if MONGODB_USER else ""
MONGO_URL = (
    f"mongodb://"
    f"{MONGO_AUTH}{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DB_NAME}"
)
MONGODB_SETTINGS = {"db": MONGODB_DB_NAME, "alias": "default"}
