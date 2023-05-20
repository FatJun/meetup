from pydantic import BaseModel, PositiveInt


class BaseResponse(BaseModel):
    class Payload:
        pass

    msg: str = ""
    success: bool = True
    status_code: PositiveInt = 200
    payload: BaseModel | None = None
