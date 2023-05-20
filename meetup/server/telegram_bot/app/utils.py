import bcrypt
from fastapi import HTTPException

from ..config import WEBHOOK_API_TOKEN


def validate_webhook_api_token(hashed_api_token: str) -> bool:
    print(hashed_api_token)
    if bcrypt.checkpw(WEBHOOK_API_TOKEN.encode(), hashed_api_token.encode()):
        return True
    raise HTTPException(500, "Invalid Token")

