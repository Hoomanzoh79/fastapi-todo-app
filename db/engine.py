from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy import create_engine


# SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Alishab13@localhost:5432/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()