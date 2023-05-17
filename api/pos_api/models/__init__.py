from mongoengine import connect

from pos_pkg.config import (
    MONGODB_DB_NAME,
    MONGODB_HOST,
    MONGODB_PASSWORD,
    MONGODB_PORT,
    MONGODB_USER,
)

db = connect(
    db=MONGODB_DB_NAME,
    host=MONGODB_HOST,
    port=MONGODB_PORT,
    username=MONGODB_USER,
    password=MONGODB_PASSWORD,
)