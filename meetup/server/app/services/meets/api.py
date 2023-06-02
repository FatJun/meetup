from typing import Annotated

from fastapi import APIRouter, status, HTTPException

from app.services.auth import dependencies as dp
from app.services.utils import generate_response
from database.users.models import User
from database.meets import crud
from . import responses
from . import schemas
from . import forms

router = APIRouter()
prefix = "/meets"
tags = ["meets"]


@router.post("/", response_model=responses.Meet)
async def create_meet(user: Annotated[User, dp.get_current_active_user], meet_form: forms.MeetCreate):
    if meet_form.creator_id != user.id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"msg": "Meet creator id not match"})
    meet = await crud.create_meet(**meet_form.dict())
    serialized_meet = await schemas.MeetSchema.from_tortoise_orm(meet)
    return generate_response("Meet was successfully created", meet=serialized_meet, status_code=status.HTTP_201_CREATED)


@router.get("/current_active_user", response_model=responses.Meets)
async def get_current_active_user_meets(user: Annotated[User, dp.get_current_active_user]):
    serialized_own_meets = await schemas.MeetSchema.from_queryset(user.own_meets.all())
    serialized_meets = await schemas.MeetSchema.from_queryset(user.meets.all())
    return generate_response(meets=serialized_own_meets + serialized_meets)
