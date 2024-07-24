from pydantic import BaseModel


class RegisterInput(BaseModel):
    username: str
    password: str