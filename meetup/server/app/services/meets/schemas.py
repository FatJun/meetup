from tortoise.contrib.pydantic import pydantic_model_creator

from database.meets.models import Meet

MeetSchema = pydantic_model_creator(Meet)
