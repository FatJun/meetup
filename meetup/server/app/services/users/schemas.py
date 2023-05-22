from tortoise.contrib.pydantic import pydantic_model_creator

from database.users.models import User

UserSchema = pydantic_model_creator(User, exclude=("hashed_password",))
