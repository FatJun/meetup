import bcrypt
import httpx
import requests

from config import WEBHOOK_API_TOKEN


TELEGRAM_WEBHOOK_URL = "http://telegram-bot:8001/webhook"


async def async_send_webhook(action_type: str, **payload):
    async with httpx.AsyncClient() as client:
        json = {"action": {"type": action_type, "payload": payload}}
        await client.post(TELEGRAM_WEBHOOK_URL, json=json, cookies={"webhook_api_token": hash_webhook_api_token()})


def sync_send_webhook(action_type: str, **payload):
    json = {"action": {"type": action_type, "payload": payload}}
    requests.post(TELEGRAM_WEBHOOK_URL, json=json, cookies={"webhook_api_token": hash_webhook_api_token()})


def hash_webhook_api_token() -> str:
    salt = bcrypt.gensalt()
    hashed_token = bcrypt.hashpw(WEBHOOK_API_TOKEN.encode(), salt)
    return hashed_token.decode()
