from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

from database.users.models import User

UserSchema = pydantic_model_creator(User, exclude=("hashed_password",))


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str


class UserCreate(UserBase):
    password: str
