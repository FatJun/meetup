from datetime import datetime
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from database.meets.models import Meet

MeetSchema = pydantic_model_creator(Meet)


class MeetBase(BaseModel):
    name: str
    description: str
    start_at: datetime


class MeetCreate(MeetBase):
    members: list[str]
