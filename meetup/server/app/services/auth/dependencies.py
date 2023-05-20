from fastapi import Depends

from .utils import get_current_active_user

get_current_active_user = Depends(get_current_active_user)
