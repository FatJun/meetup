from fastapi import Depends

from .utils import validate_webhook_api_token

validate_webhook_api_token = Depends(validate_webhook_api_token)
