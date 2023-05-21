from pydantic import BaseModel

from app.services.responses import BaseResponse
from .schemas import MeetSchema


class Meet(BaseResponse):
    class Payload(BaseModel):
        meet: MeetSchema

    payload: Payload


class Meets(BaseResponse):
    class Payload(BaseModel):
        meets: list[MeetSchema]

    payload: Payload
