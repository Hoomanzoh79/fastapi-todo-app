from fastapi import APIRouter,Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from schema._input import UserInput,UserUpdateInput
from schema.output import RegisterOutput
from db.engine  import get_db
from operations.users import UserOperation

router = APIRouter()

@router.post("/register")
async def register(db_session:Annotated[AsyncSession, Depends(get_db)],
                   data: UserInput = Body(),
                   ):
    user = await UserOperation(db_session).create(data.username,data.password)
    return RegisterOutput(username=user.username,id=user.id)

@router.post("/login")
async def login(db_session:Annotated[AsyncSession, Depends(get_db)],
                data: UserInput = Body(),
                ):
    token = await UserOperation(db_session).login(data.username,data.password)
    return token

@router.get("/{username}")
async def get_user_profile(db_session:Annotated[AsyncSession, Depends(get_db)],
                           username: str,
                           ):
    user = await UserOperation(db_session).get_user_by_username(username=username)
    return user

@router.put("/")
async def user_update_profile(db_session:Annotated[AsyncSession, Depends(get_db)],
                              data: UserUpdateInput = Body(),
                             ):
    user = await UserOperation(db_session).update_username(data.old_username,
                                                           data.new_username,
                                                           )
    return user


@router.delete("/{username}")
async def user_delete(db_session:Annotated[AsyncSession, Depends(get_db)],
                      username: str,
                      ):
    user = await UserOperation(db_session).delete(username)
    return user