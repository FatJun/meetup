from database.users.query import get_users_by_usernames
from database.users.models import User
from .models import Meet


async def create_meet(*, members_usernames: list[str], **meet_fields) -> Meet:
    creator = await User.get(id=meet_fields["creator_id"])
    members: list[User] = await get_users_by_usernames(members_usernames)
    meet = await Meet.create(creator=creator, **meet_fields)
    await meet.members.add(*members)
    await meet.save()
    return meet
