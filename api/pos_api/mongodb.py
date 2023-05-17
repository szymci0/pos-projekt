from motor.motor_asyncio import AsyncIOMotorClient

from pos_pkg.config import MONGO_URL


client = {"mongodb": None}


def get_db_client() -> AsyncIOMotorClient:
    return client["mongodb"]


def connect_db():
    client["mongodb"] = AsyncIOMotorClient(
        MONGO_URL,
        uuidRepresentation="standard",
    )


async def close_db():
    client["mongodb"].close()