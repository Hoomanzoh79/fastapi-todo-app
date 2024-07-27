from pydantic import BaseModel
from uuid import UUID


class RegisterOutput(BaseModel):
    username: str
    id: UUID