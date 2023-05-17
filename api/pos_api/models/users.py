from abc import ABC
from datetime import datetime
from typing import Optional, Any

from pos_api.models.blacklisted_tokens import BlacklistedTokens
from bson import ObjectId
from fastapi import Response
from fastapi_users import models
from fastapi_users.models import BaseUserDB
from mongoengine import DynamicDocument, UUIDField
from fastapi_users.authentication import JWTAuthentication
from pydantic import validator

from pos_pkg.config import SECRET_KEY


class User(models.BaseUser):
    created_at: Optional[datetime] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    last_seen:Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @validator("created_at", pre=True, always=True)
    def default_created_at(cls, v):
        return v or datetime.now()


class UserCreate(models.BaseUserCreate):
    @validator("password")
    def valid_password(cls, v: str):
        if len(v) < 6:
            raise ValueError("Password should be at least 6 characters")
        return v


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(models.BaseOAuthAccountMixin, User, models.BaseUserDB):
    pass


class Users(DynamicDocument):
    id = UUIDField()
    meta = {
        'id_field': 'id',
    }


class JWTCustomAuthentication(JWTAuthentication, ABC):
    async def get_login_response(
            self, user: BaseUserDB, response: Response,
    ) -> Any:
        from pos_api.app import app

        user.last_seen = datetime.now()
        await app.users.db.update(user)
        login_response = await super().get_login_response(user, response)
        token = login_response.get('access_token', '')
        if BlacklistedTokens.objects(token=token).first():
            raise ValueError("Token expired")
        return login_response


DAY = 60 * 60 * 24
jwt_authentication = JWTCustomAuthentication(
    secret=SECRET_KEY, lifetime_seconds=DAY, tokenUrl="/auth/jwt/login"
)
