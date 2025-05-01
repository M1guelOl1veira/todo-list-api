from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.session import async_session
from schemas.item_schema import ItemCreate
from utils.database import async_session
from utils.db_models import Item


class ItemRepository:
    async def get_by_todo_list_id(todo_list_id: int):
        async with async_session() as session:
            result = await session.execute(select(Item).where(Item.todo_list_id == todo_list_id))
            return result.scalars().all()
    
    async def get_item_by_id(item_id: int):
        async with async_session() as session:
            result = await session.execute(select(Item).where(Item.item_id == item_id))
            return result.scalar()
        
    async def add_item(item_id: int, todo_list_id: int, titulo: str, descricao: str):
        async with async_session() as session:
            session.add(Item(item_id= item_id, todo_list_id = todo_list_id, titulo = titulo, descricao = descricao))
            await session.commit()



        