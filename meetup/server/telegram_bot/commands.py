from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.users import crud

tg_router = Router()


@tg_router.message(Command(commands=["start"]))
async def command_start_handler(message: Message):
    is_user_registered = await crud.register_user_in_telegram(message.from_user.username, message.chat.id)
    if not is_user_registered:
        return await message.answer(f"Сначала зарегистрируйтесь на нашем сайте.")
    await message.answer(f"Вы успешно подписались на уведомления о встречах!")
