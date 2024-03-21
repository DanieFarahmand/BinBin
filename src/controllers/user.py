import sqlalchemy as sa

from src.models.user import User
from src.core.sqldb.database import AsyncSession


class UserController:

    def __init__(self, sqldb_session: AsyncSession):
        self.sqldb_session = sqldb_session

    async def create_user(self, email, password):
        select_query = sa.select(User).where(User.email == email)
        existing_user = await self.sqldb_session.scalar(select_query)
        if not existing_user:
            new_user = User(
                email=email,
                password=password
            )
            async with self.sqldb_session:
                self.sqldb_session.add(new_user)
                await self.sqldb_session.commit()
            return new_user
        else:
            return None

    async def delete_user(self, user_id):
        async with self.sqldb_session:
            user = await self.sqldb_session.execute(
                sa.select(User).filter(User.id == user_id)
            )
            user = user.scalar()
            if user:
                await self.sqldb_session.delete(user)
                await self.sqldb_session.commit()
                return user
            else:
                return None
