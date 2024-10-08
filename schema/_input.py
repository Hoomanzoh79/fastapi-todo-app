from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    password: str

class UserUpdateInput(BaseModel):
    old_username: str
    new_username: str

class TaskInput(BaseModel):
    name : str
    user_id : int

class TaskUpdateInput(BaseModel):
    task_id: int
    new_name: str
    is_done: bool