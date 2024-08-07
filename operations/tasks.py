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

        if len(name) > 100:
            raise exceptions.TaskNameLengthException

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

    def get_tasks_by_username(self,username:str):
        user = sa.select(User).where(User.username==username)

        with self.db_session as session:
            user_data = session.scalar(user)
            if user_data is None:
                raise exceptions.UserNotFoundException
            tasks_query = sa.select(Task).where(Task.user_id==user_data.id)
            user_tasks  = list(session.scalars(tasks_query))

        if len(user_tasks) == 0:
            return "This user has no tasks yet"
        return user_tasks

    # def get_task_by_id(self,task_id:int):
    #     task = sa.select(Task).where(Task.id==task_id)

    #     with self.db_session as session:
    #         task_data = session.scalar(task)
    #         if task_data is None:
    #             raise exceptions.TaskNotFoundException
    #         user = task_data.user

    #     return TaskOutput(id=task_data.id,name=task_data.name,
    #                       is_done=task_data.is_done,user_id=task_data.user_id,
    #                       user=user.username # type: ignore
    #                       ) # type: ignore

    def update(self,task_id):
        task = sa.select(Task).where(Task.id==task_id)
        update_query_task_done = sa.update(Task).where(Task.id == task_id).values(is_done=True)
        update_query_task_undo = sa.update(Task).where(Task.id == task_id).values(is_done=False)
        with self.db_session as session:
            task_data = session.scalar(task)
            if task_data is None:
                raise exceptions.TaskNotFoundException
            if task_data.is_done == False:
                session.execute(update_query_task_done)
            else:
                session.execute(update_query_task_undo)
            session.commit()

        return task_data

    def delete(self,task_id):
        query = sa.select(Task).where(Task.id == task_id)
        delete_query = sa.delete(Task).where(Task.id == task_id)
        with self.db_session as session:
            task_data =  session.scalar(query)
            if task_data is None:
                raise exceptions.TaskNotFoundException
            session.execute(delete_query)
            session.commit()
        # return {"msg": "task has been deleted sucessfully"}