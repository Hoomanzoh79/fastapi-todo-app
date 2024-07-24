from fastapi import APIRouter,Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from schema._input import RegisterInput
from db.engine  import get_db
from operations.users import UserOperation

router = APIRouter()

@router.post("/register")
async def register(db_session:Annotated[AsyncSession, Depends(get_db)],
                   data: RegisterInput = Body(),
):
    user = await UserOperation(db_session).create(username=data.username,password=data.password)
    return user

@router.post("/login")
async def login():
    ...

@router.get("/")
async def get_user_profile():
    ...

@router.put("/")
async def user_update_profile():
    ...
