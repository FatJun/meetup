from tortoise.expressions import Q

from .models import User


async def get_user_by_username(username: str) -> User | None:
    user = await User.get_or_none(username=username)
    return user


async def get_users_by_usernames(usernames: list[str]) -> list[User]:
    users = await User.filter(Q(username__in=usernames))
    return users
