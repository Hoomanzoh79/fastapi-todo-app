from sqlalchemy.orm import Session
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

from db.models import User,Task
import exceptions
from utils.secrets import password_manager
from utils.jwt import JWTHandler
from schema.jwt import JWTResponsePayload
from schema.output import TaskOutput

class TaskOperation:
    def __init__(self,db_session: Session) -> None:
        self.db_session = db_session

    def create(self,name,is_done,user_id):
        task = Task(name=name,is_done=is_done,user_id=user_id)

        with self.db_session as session:
            try:
                session.add(task)
                session.commit()
                session.refresh(task)
            except IntegrityError:
                raise Exception("task already exists")

        return TaskOutput(id=task.id,name=task.name, # type: ignore
                          is_done=task.is_done, # type: ignore
                          user_id=task.user_id # type: ignore
                          )