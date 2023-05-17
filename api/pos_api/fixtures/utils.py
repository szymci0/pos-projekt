from pathlib import Path

from fastapi_users.user import UserAlreadyExists
from pkg_resources import resource_filename

from pos_api.models import db
from pos_api.app import create_app
from pos_api.models.users import UserCreate

from pos_pkg.files.utils import read_from_json
from pos_pkg.config import MONGODB_DB_NAME
from mongoengine.queryset.visitor import Q 


def drop_database():
    print("Drop database")
    db.drop_database(MONGODB_DB_NAME)


async def inject_users():
    app = create_app()

    users = read_from_json(Path(resource_filename(__name__, "users.json")))
    for user in users:
        try:
            await app.users.create_user(UserCreate(**user, is_verified=True))
        except UserAlreadyExists:
            ...
    print(f"Injected {len(users)} users")

async def inject_fixtures():
    await inject_users()
