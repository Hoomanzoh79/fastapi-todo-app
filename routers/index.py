from typing import Annotated
from fastapi import Depends, Request,APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlalchemy as sa
from sqlalchemy.orm import Session

from db.engine import get_db
from db.models import Task

class TemplateOperation:
    def __init__(self,db_session: Session) -> None:
        self.db_session = db_session

    def get_all_tasks(self):
        with self.db_session as session:
            tasks_query = sa.select(Task)
            tasks_data  = list(session.scalars(tasks_query))

        return tasks_data

router = APIRouter()

db_dependency = Annotated[Session,Depends(get_db)]

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(db_session:db_dependency,request: Request):
    all_tasks = TemplateOperation(db_session).get_all_tasks()
    return templates.TemplateResponse("index.html", {"request": request, "all_tasks": all_tasks})