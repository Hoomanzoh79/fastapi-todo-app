from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from routers.users import router as user_router
from routers.tasks import router as task_router
from routers.index import router as index_router
from db.engine import engine
from db import models

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    # Update with specific origins in production
    allow_origins=["localhost"],
    allow_methods=["GET", "POST","PUT","DELETE",],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(bind=engine)

app.include_router(user_router,prefix="/users")
app.include_router(task_router,prefix="/tasks")
app.include_router(index_router,prefix="/index")