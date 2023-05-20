import os

from aiogram import Dispatcher, Bot

TELEGRAM_MESSAGES_PER_SECOND_LIMIT = 30
TELEGRAM_BOT_API_TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

dp = Dispatcher()
bot = Bot(TELEGRAM_BOT_API_TOKEN)
