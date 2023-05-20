from database.users.query import get_users_by_usernames
from database.users.models import User
from .models import Meet


async def create_meet(*, members: list[str], **meet_fields) -> Meet:
    members: list[User] = await get_users_by_usernames(members)
    meet = await Meet.create(**meet_fields)
    await meet.members.add(*members)
    await meet.save()
    return meet
