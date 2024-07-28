from pydantic import BaseModel


class RegisterOutput(BaseModel):
    username: str
    id: int