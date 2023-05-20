from tortoise.expressions import Q

from database.users.models import User
from .models import Meet


async def get_meet_by_id(meet_id: int) -> Meet | None:
    meet = await Meet.get_or_none(id=meet_id)
    return meet


async def get_registered_in_telegram_bot_members(meet: Meet) -> list[User]:
    members = await meet.members.filter(Q(registered_in_telegram=True))
    return members
