
from repository.item_repository import ItemRepository
from schemas.item_schema import ItemCreate

class ItemService:
    async def get_by_todo_list_id(todo_list_id: int):
            return await ItemRepository.get_by_todo_list_id(todo_list_id)
    
    async def get_item_by_id(item_id: int):
            return await ItemRepository.get_item_by_id(item_id)
    
    async def add_item(item_id: int, todo_list_id: int, titulo: str, descricao: str):
            return await ItemRepository.add_item(item_id, todo_list_id, titulo, descricao)
    
    
    