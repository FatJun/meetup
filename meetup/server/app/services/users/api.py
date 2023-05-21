from typing import Annotated

from fastapi import APIRouter, status
from fastapi import HTTPException

from app.services.auth.hasher import Hasher
from app.services.auth import dependencies as dp
from app.services.utils import generate_response
from database.users.models import User
from database.users import crud, query
from . import responses
from . import schemas

router = APIRouter()
prefix = "/users"
tags = ["users"]


@router.post("/", response_model=responses.User)
async def create_user(user_form: schemas.UserCreate):
    hashed_password = Hasher.get_hashed_password(user_form.password)
    user = await crud.create_user(hashed_password=hashed_password, **user_form.dict())
    serialized_user = await schemas.UserSchema.from_tortoise_orm(user)
    return generate_response(user=serialized_user)


@router.get("/", response_model=responses.Users, dependencies=[dp.get_current_active_user])
async def get_users():
    users = await query.get_active_and_registered_in_telegram_users()
    serialized_users = await schemas.UserSchema.from_queryset(users)
    return generate_response(users=serialized_users)


@router.get("/current", response_model=responses.CurrentActiveUserResponse)
async def get_current_active_user(user: Annotated[User, dp.get_current_active_user]):
    serialized_user = await schemas.UserSchema.from_tortoise_orm(user)
    return generate_response(user=serialized_user, authenticated=True)


@router.get("/{username}", response_model=responses.User, dependencies=[dp.get_current_active_user])
async def get_user(username: str):
    user = await crud.get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    serialized_user = await schemas.UserSchema.from_tortoise_orm(user)
    return generate_response(user=serialized_user)
