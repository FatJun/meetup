from pydantic import BaseModel, constr


class UserCreate(BaseModel):
    first_name: str = constr(max_length=100)
    last_name: str = constr(max_length=100)

    username: str = constr(max_length=100)
    password: str = constr(max_length=100)
