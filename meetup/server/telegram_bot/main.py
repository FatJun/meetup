import asyncio
from multiprocessing import Process

from database.utils import init_db, close_db_connections
from telegram_bot.config import dp, bot
from .commands import tg_router
from .app.main import main as app_startup
import logging


async def main():
    Process(target=app_startup).start()
    await init_db()
    dp.include_router(tg_router)
    await dp.start_polling(bot)
    await close_db_connections()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
