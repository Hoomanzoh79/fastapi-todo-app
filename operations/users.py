from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User

class UserOperation:
    def __init__(self,db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self,username: str,password: str) -> User:
        user = User(password=password,username=username)

        async with self.db_session as session:
            session.add(user)
        return user