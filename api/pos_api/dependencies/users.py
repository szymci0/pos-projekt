from typing import Tuple

import jwt
from fastapi_users import FastAPIUsers
from fastapi_users.db import MongoDBUserDatabase

from pos_api.models.users import (
    User,
    UserCreate,
    UserDB,
    UserUpdate,
    jwt_authentication,
)

from pos_api.mongodb import get_db_client
from pos_pkg.config import MONGODB_DB_NAME

def create_users_app():
    mongo_client = get_db_client()
    db = mongo_client[MONGODB_DB_NAME]
    collection = db["users"]
    user_db = MongoDBUserDatabase(UserDB, collection)

    fastapi_users = FastAPIUsers(
        user_db, [jwt_authentication], User, UserCreate, UserUpdate, UserDB,
    )
    fastapi_users.collection = collection

    return fastapi_users