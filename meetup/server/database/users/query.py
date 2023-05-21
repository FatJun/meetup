from tortoise.expressions import Q
from tortoise.queryset import QuerySet

from .models import User


async def get_user_by_username(username: str) -> User | None:
    user = await User.get_or_none(username=username)
    return user


async def get_users_by_usernames(usernames: list[str]) -> list[User]:
    users = await User.filter(username__in=usernames)
    return users


async def get_active_and_registered_in_telegram_users() -> QuerySet[User]:
    users = User.filter(Q(registered_in_telegram=True) & Q(is_active=True)).all()
    return users
