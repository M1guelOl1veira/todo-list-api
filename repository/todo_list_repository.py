from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.session import async_session
from utils.database import async_session
from utils.db_models import TodoList

class TodoListRepository:
    async def get_todo_list_by_user_id(user_id):
        async with async_session() as session:
            result = await session.execute(select(TodoList).where(TodoList.user_id == user_id))
            return result.scalars().all()