from fastapi import FastAPI

from routers.users import router as user_router
from db.engine import engine
from db import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user_router,prefix="/users")