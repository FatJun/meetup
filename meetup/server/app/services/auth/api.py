from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from app.services.responses import BaseResponse
from app.services.utils import generate_response
from .utils import authenticate_user, create_access_token
from .config import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter()
prefix = "/auth"
tags = ["auth"]


@router.post("/login", response_model=BaseResponse)
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response = JSONResponse(generate_response("Success Login In"))
    response.set_cookie("Authorization", value=f"Bearer {access_token}", httponly=True,
                        expires=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    return response


@router.get("/logout", response_model=BaseResponse)
async def logout_user():
    response = JSONResponse(generate_response("Success Login Out"))
    response.delete_cookie("Authorization", httponly=True)
    return response
