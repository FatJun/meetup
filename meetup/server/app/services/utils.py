import bcrypt
import httpx

from config import WEBHOOK_API_TOKEN


def generate_response(msg: str = "", *, success: bool = True, status_code: int = 200, **payload):
    return {"msg": msg, "success": success, "status_code": status_code, "payload": payload}

