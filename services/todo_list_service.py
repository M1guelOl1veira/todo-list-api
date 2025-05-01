
from repository.todo_list_repository import TodoListRepository

class TodoListService:
    async def get_todo_list_by_user_id(user_id: int):
        return await TodoListRepository.get_todo_list_by_user_id(user_id)