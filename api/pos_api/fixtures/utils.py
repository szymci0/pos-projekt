from pathlib import Path

from fastapi_users.user import UserAlreadyExists
from pkg_resources import resource_filename

from pos_api.models import db
from pos_api.app import create_app
from pos_api.models.users import UserCreate
from pos_api.models.position import Position
from pos_api.models.county import County

from pos_pkg.files.utils import read_from_json
from pos_pkg.config import MONGODB_DB_NAME
from mongoengine.queryset.visitor import Q 
import pandas as pd


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


async def inject_positions():
    positions = read_from_json(Path(resource_filename(__name__, "positions.json")))
    for pos in positions:
        Position(**pos).save()
    print(f"Injected {len(positions)} positions")


async def inject_counties():
    counties_df = pd.read_feather(Path(resource_filename(__name__, "county_TERYT.feather")))
    counties = counties_df.to_dict(orient="records")
    for county in counties:
        County(name=county["name"], teryt=str(county["teryt"])).save()
    print(f"Injected counties TERYT information")


async def inject_fixtures():
    await inject_counties()
    await inject_users()
    await inject_positions()
