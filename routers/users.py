from fastapi import APIRouter,Body

from schema._input import RegisterInput

router = APIRouter()

@router.post("/register")
async def register(data: RegisterInput = Body()):
    return data

@router.post("/login")
async def login():
    ...

@router.get("/")
async def get_user_profile():
    ...

@router.put("/")
async def user_update_profile():
    ...
