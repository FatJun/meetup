import asyncio
from multiprocessing import Process

from database.utils import init_db, close_db_connections
from telegram_bot.config import dp, bot
from .app.main import main as web_app_startup
from .commands import tg_router


async def main():
    Process(target=web_app_startup).start()
    await init_db()
    dp.include_router(tg_router)
    await dp.start_polling(bot)
    await close_db_connections()

if __name__ == '__main__':
    asyncio.run(main())
