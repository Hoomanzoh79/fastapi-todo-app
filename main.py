from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio

from routers.users import router as user_router
from db.engine import engine,Base


async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    asyncio.create_task(init_tables())
    yield
    # Run on shutdown (if required)
    print('Shutting down...')

app = FastAPI(lifespan=lifespan)

app.include_router(user_router,prefix="/users")
