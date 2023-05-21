import bcrypt
from fastapi import HTTPException, Request

from config import WEBHOOK_API_TOKEN


def validate_webhook_api_token(request: Request) -> bool:
    hashed_webhook_api_token = request.cookies.get("webhook_api_token", "")
    try:
        if bcrypt.checkpw(WEBHOOK_API_TOKEN.encode(), hashed_webhook_api_token.encode()):
            return True
    except ValueError:
        # Invalid Salt error pass
        pass
    raise HTTPException(500, "Invalid Token")

