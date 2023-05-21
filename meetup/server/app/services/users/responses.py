from pydantic import BaseModel

from app.services.responses import BaseResponse
from .schemas import UserSchema


class CurrentActiveUserResponse(BaseResponse):
    class Payload(BaseModel):
        user: UserSchema
        authenticated: bool

    payload: Payload


class Users(BaseResponse):
    class Payload(BaseModel):
        users: list[UserSchema]

    payload: Payload


class User(BaseResponse):
    class Payload(BaseModel):
        user: UserSchema

    payload: Payload
