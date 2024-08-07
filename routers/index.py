from typing import Annotated
from fastapi import Depends, Request,APIRouter,Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlalchemy as sa
from sqlalchemy.orm import Session

from db.engine import get_db
from db.models import Task
from operations.tasks import TaskOperation

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


@router.post("/create")
async def add_task(db_session:db_dependency,request: Request, task_name: str = Form(...)):
    task = TaskOperation(db_session).create(name=task_name,user_id=12) # will get the user from request.user later
    redirect_url = request.url_for('index')
    return RedirectResponse(redirect_url)