from sqlalchemy import Column,Integer,String

from .engine import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)

    password = Column(String)
    username = Column(String,unique=True)