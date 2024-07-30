from sqlalchemy.orm import Session
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

from db.models import User
import exceptions
from utils.secrets import password_manager
from utils.jwt import JWTHandler
from schema.jwt import JWTResponsePayload
from schema.output import RegisterOutput

class UserOperation:
    def __init__(self,db_session: Session) -> None:
        self.db_session = db_session

    def create(self,username,password) -> User:
        user_pwd = password_manager.hash(password)
        user = User(password=user_pwd,username=username)

        with self.db_session as session:
            try:
                session.add(user)
                session.commit()
                session.refresh(user)
            except IntegrityError:
                raise exceptions.UserAlreadyExistsException

        return RegisterOutput(id=user.id,username=user.username) # type: ignore

    def get_user_by_username(self,username):
        query = sa.select(User).where(User.username == username)
        with self.db_session as session:
            user_data = session.scalar(query)
            if user_data is None:
                raise exceptions.UserNotFoundException

        return RegisterOutput(id=user_data.id,username=user_data.username) # type: ignore

    def update_username(self,old_username,new_username):
        query = sa.select(User).where(User.username == old_username)
        update_query = sa.update(User).where(User.username == old_username).values(username=new_username)
        with self.db_session as session:
            user = session.scalar(query)
            if user is None:
                raise exceptions.UserNotFoundException
            session.execute(update_query)
            session.commit()

        user.username = new_username

        return RegisterOutput(id=user.id,username=user.username) # type: ignore

    def delete(self,username: str):
        query = sa.select(User).where(User.username == username)
        delete_query = sa.delete(User).where(User.username == username)
        with self.db_session as session:
            user_data =  session.scalar(query)
            if user_data is None:
                raise exceptions.UserNotFoundException
            session.execute(delete_query)
            session.commit()
        return {"msg": "user has been deleted sucessfully"}

    def login(self,username: str,password: str) -> JWTResponsePayload:
        query = sa.select(User).where(User.username == username)
        with self.db_session as session:
            user =  session.scalar(query)
            if user is None:
                raise exceptions.InvalidUsernameOrPasswordException

        if not password_manager.verify(password,user.password): # type: ignore
            raise exceptions.InvalidUsernameOrPasswordException

        return JWTHandler.generate(username)