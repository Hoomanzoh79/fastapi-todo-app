from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .engine import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True,index=True)

    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column()

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="user", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True,index=True)

    name : Mapped[str] = mapped_column(String(100))
    is_done : Mapped[bool] = mapped_column(default=False)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="tasks")