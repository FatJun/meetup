from pydantic import BaseModel

from .schemas import MeetSchema
from ..responses import BaseResponse


class GetMeetResponse(BaseResponse):
    class Payload(BaseModel):
        meet: MeetSchema

    payload: Payload


class GetMeetsResponse(BaseResponse):
    class Payload(BaseModel):
        meets: list[MeetSchema]

    payload: Payload
