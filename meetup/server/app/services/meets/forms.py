from datetime import datetime

from pydantic import BaseModel


class MeetCreate(BaseModel):
    name: str
    description: str
    start_at: datetime
    creator_id: int
    members_usernames: list[str]
