from sqlalchemy.orm import Session
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

from db.models import User,Task
import exceptions
from schema.output import TaskOutput

class TaskOperation:
    def __init__(self,db_session: Session) -> None:
        self.db_session = db_session

    def create(self,name,user_id):
        task = Task(name=name,is_done=False,user_id=user_id)
        user = sa.select(User).where(User.id==user_id)

        with self.db_session as session:
            user_data = session.scalar(user)
            try:
                session.add(task)
                session.commit()

            except IntegrityError:
                raise exceptions.InvalidAuthorException

        return TaskOutput(id=task.id,name=task.name, # type: ignore
                          is_done=False,
                          user_id=task.user_id, # type: ignore
                          user=user_data.username # type: ignore
                          )