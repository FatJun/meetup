from pydantic import BaseModel, constr


class UserCreate(BaseModel):
    first_name: str
    last_name: str

    username: str
    password: str
