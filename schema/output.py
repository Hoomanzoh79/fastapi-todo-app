from pydantic import BaseModel


class RegisterOutput(BaseModel):
    id: int
    username: str