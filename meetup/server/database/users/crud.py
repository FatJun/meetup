from .exceptions import UserAlreadyRegistered
from .models import User
from .query import get_user_by_username


async def create_user(*, username: str, hashed_password: str, **user_fields) -> User:
    user = await get_user_by_username(username)
    if user is not None:
        raise UserAlreadyRegistered()
    user = await User.create(username=username, hashed_password=hashed_password,
                             **user_fields)
    return user


async def register_user_in_telegram(username: str, telegram_chat_id: int) -> bool:
    user = await get_user_by_username(username)
    if user is None:
        return False
    elif user.registered_in_telegram is True:
        return True
    user.telegram_chat_id = telegram_chat_id
    user.registered_in_telegram = True
    await user.save()
    return True
