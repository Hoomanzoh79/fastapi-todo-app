from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    password: str

class UserUpdateInput(BaseModel):
    old_username: str
    new_username: str

class TaskInput(BaseModel):
    name : str
    is_done : bool
    user_id : int