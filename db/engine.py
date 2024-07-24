from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from sqlalchemy.orm import DeclarativeBase,MappedAsDataclass

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
)

class Base(DeclarativeBase,MappedAsDataclass):
    pass

async def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        await db.close()