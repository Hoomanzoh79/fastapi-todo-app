from sqlalchemy.orm import Session
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

from db.models import User
import exceptions
from utils.secrets import password_manager
from utils.jwt import JWTHandler
from schema.jwt import JWTResponsePayload

class UserOperation:
    def __init__(self,db_session: Session) -> None:
        self.db_session = db_session

    def create(self,username,password) -> User:
        user_pwd = password_manager.hash(password)
        user = User(password=user_pwd,username=username)
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)
        return user

    # def get_user_by_username(self,username) -> User:
    #     query = sa.select(User).where(User.username == username)
    #     with self.db_session as session:
    #         user_data = session.scalar(query)
    #         if user_data is None:
    #             raise exceptions.UserNotFoundException

    #     return user_data

    # def update_username(self,old_username,new_username) -> User:
    #     query = sa.select(User).where(User.username == old_username)
    #     update_query = sa.update(User).where(User.username == old_username).values(username=new_username)
    #     with self.db_session as session:
    #         user_data = session.scalar(query)
    #         if user_data is None:
    #             raise exceptions.UserNotFoundException
    #         session.execute(update_query)
    #         session.commit()
    #     user_data.username = new_username

    #     return user_data

    # def delete(self,username: str):
    #     query = sa.select(User).where(User.username == username)
    #     delete_query = sa.delete(User).where(User.username == username)
    #     with self.db_session as session:
    #         user_data =  session.scalar(query)
    #         if user_data is None:
    #             raise exceptions.UserNotFoundException
    #          session.execute(delete_query)
    #          session.commit()
    #     return {"msg": "user has been deleted sucessfully"}

    # def login(self,username: str,password: str) -> JWTResponsePayload:
    #     query = sa.select(User).where(User.username == username)
    #     with self.db_session as session:
    #         user =  session.scalar(query)
    #         if user is None:
    #             raise exceptions.InvalidUsernameOrPasswordException

    #     if not password_manager.verify(password,user.password):
    #         raise exceptions.InvalidUsernameOrPasswordException

    #     return JWTHandler.generate(username)