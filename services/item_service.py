
from repository.item_repository import ItemRepository

class ItemService:
    async def get_by_todo_list_id(todo_list_id: int):
            return await ItemRepository.get_by_todo_list_id(todo_list_id)
    
    async def get_item_by_id(item_id: int):
            return await ItemRepository.get_item_by_id(item_id)

    
    