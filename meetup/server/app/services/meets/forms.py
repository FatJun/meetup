from datetime import datetime

from pydantic import BaseModel, constr


class MeetCreate(BaseModel):
    name: str = constr(max_length=200)
    description: str = constr(max_length=500)
    start_at: datetime
    creator_id: int
    members_usernames: list[str]
