from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database.users import crud

tg_router = Router()


@tg_router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    is_user_registered = await crud.register_user_in_telegram(message.from_user.username, message.chat.id)
    if is_user_registered is False:
        await message.answer(f"Сначала зарегистрируйтесь на нашем сайте.")
    elif is_user_registered is True:
        await message.answer(f"Вы успешно подписались на уведомления о встречах!")