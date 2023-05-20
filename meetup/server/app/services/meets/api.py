from typing import Annotated

from fastapi import APIRouter, HTTPException, status

from app.services.auth import dependencies as dp
from app.services.utils import generate_response
from database.meets.models import Meet
from database.users.models import User
from database.meets import crud
from database.meets import query
from . import responses
from . import schemas

router = APIRouter()
prefix = "/meets"
tags = ["meets"]


@router.post("/", response_model=responses.GetMeetResponse)
async def create_meet(user: Annotated[User, dp.get_current_active_user], meet_form: schemas.MeetCreate):
    meet = await crud.create_meet(creator=user, **meet_form.dict())
    serialized_meet = await schemas.MeetSchema.from_tortoise_orm(meet)
    return generate_response("Meet was successfully created", meet=serialized_meet, status_code=status.HTTP_201_CREATED)


@router.get("/", response_model=responses.GetMeetsResponse)
async def get_meets(offset: int = 0, limit: int = 100) -> list[schemas.MeetSchema]:
    meets = Meet.all().offset(offset).limit(limit)
    serialized_meets = await schemas.MeetSchema.from_queryset(meets)
    return generate_response(meets=serialized_meets)


@router.get("/current_active_user", response_model=responses.GetMeetsResponse)
async def get_current_active_user_meets(user: Annotated[User, dp.get_current_active_user]):
    serialized_meets = await schemas.MeetSchema.from_queryset(user.meets.all())
    return generate_response(meets=serialized_meets)


@router.get("/{meet_id}", response_model=responses.GetMeetResponse)
async def get_meet(meet_id: int):
    meet = await query.get_meet_by_id(meet_id)
    if meet is None:
        return
    serialized_meet = await schemas.MeetSchema.from_tortoise_orm(meet)
    return generate_response(meet=serialized_meet)
