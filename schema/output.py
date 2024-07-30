from pydantic import BaseModel


class RegisterOutput(BaseModel):
    id: int
    username: str

class TaskOutput(BaseModel):
    id: int
    name: str
    is_done: bool
    user_id:  int