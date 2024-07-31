from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers.users import router as user_router
from routers.tasks import router as task_router
from routers.index import router as index_router
from db.engine import engine
from db import models

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)

app.include_router(user_router,prefix="/users")
app.include_router(task_router,prefix="/tasks")
app.include_router(index_router,prefix="/index")