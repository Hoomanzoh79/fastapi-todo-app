from pydantic import BaseModel


class JWTResponsePayload(BaseModel):
    access: str


class JWTPayload(BaseModel):
    username: str
    exp: int