from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from schemas.item_schema import ErrorOutput
from schemas.todo_list_schema import TodoListPublic
from services.todo_list_service import TodoListService
from services.user_service import UserService

todo_list_router = APIRouter(prefix='/todo-list')

@todo_list_router.get('/list/{user_id}', response_model=List[TodoListPublic], responses={400: {'model': ErrorOutput}})
async def get_todo_list_by_user_id(user_id: int, user: Annotated[str, Depends(UserService.get_current_user)]):
    try:
        if(user):
            result = await TodoListService.get_todo_list_by_user_id(user_id)
            if(not result):
                raise HTTPException(404, "Nenhuma To-Do List encontrada.")
            return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))