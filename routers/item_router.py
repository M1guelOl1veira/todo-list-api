from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from schemas.item_schema import ErrorOutput, ItemListPublic
from services.item_service import ItemService
from services.user_service import UserService

item_router = APIRouter(prefix='/item')


@item_router.post(
    '/list/{todo_list_id}',
    response_model=List[ItemListPublic],
    responses={400: {'model': ErrorOutput}}
)
async def items_by_todo_list_id(todo_list_id: int, token: Annotated[str, Depends(UserService.get_current_user)]):
    try:
        result = await ItemService.get_by_todo_list_id(todo_list_id)
        if(not result):
            raise HTTPException(404, "Nenhum item encontrado.")
        return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))