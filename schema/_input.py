from pydantic import BaseModel


class RegisterInput(BaseModel):
    username: str
    password: str

class UserUpdateInput(BaseModel):
    old_username: str
    new_username: str
