import bcrypt
import httpx

from app.config import WEBHOOK_API_TOKEN


def generate_response(msg: str = "", *, success: bool = True, status_code: int = 200, **payload):
    return {"msg": msg, "success": success, "status_code": status_code, "payload": payload}


async def async_send_webhook(action_type: str, **payload):
    async with httpx.AsyncClient() as client:
        url = "http://telegram-bot:8001/webhook"
        json = {"action": {"type": action_type, "payload": payload}}
        await client.post(url, json=json)


def hash_webhook_api_token() -> str:
    salt = bcrypt.gensalt()
    hashed_token = bcrypt.hashpw(WEBHOOK_API_TOKEN.encode(), salt)
    return hashed_token.decode()
