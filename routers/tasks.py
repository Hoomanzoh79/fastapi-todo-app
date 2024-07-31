from fastapi import APIRouter,Body, Depends
from typing import Annotated
from sqlalchemy.orm import Session

from operations.tasks import TaskOperation
from schema._input import TaskInput
from schema.output import RegisterOutput
from db.engine  import get_db
from operations.tasks import TaskOperation

router = APIRouter()

db_dependency = Annotated[Session,Depends(get_db)]

@router.post("/create-task")
async def create_task(db_session:db_dependency,
                      data: TaskInput = Body(),
                      ):
    task = TaskOperation(db_session).create(name=data.name,
                                            user_id=data.user_id
                                            )
    return task

@router.get("/{username}/tasks")
async def get_user_tasks(db_session:db_dependency,
                         username:str,
                         ):
    user_tasks = TaskOperation(db_session).get_tasks_by_username(username)
    return user_tasks