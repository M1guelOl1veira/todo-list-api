from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.session import async_session
from utils.database import async_session
from utils.db_models import User

class UserRepository:
    async def get_user_by_username(username: str):
        async with async_session() as session:
            result = await session.execute(select(User).where(User.nome_usuario == username))
            return result.scalar()