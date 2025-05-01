from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from schemas.item_schema import ErrorOutput, ItemCreate, ItemPublic, RetornoPadrao
from services.item_service import ItemService
from services.user_service import UserService

item_router = APIRouter(prefix='/item')


@item_router.get(
    '/list/{todo_list_id}',
    response_model=List[ItemPublic],
    responses={400: {'model': ErrorOutput}}
)
async def items_by_todo_list_id(todo_list_id: int, user: Annotated[str, Depends(UserService.get_current_user)]):
    try:
        if(user):
            result = await ItemService.get_by_todo_list_id(todo_list_id)
            if(not result):
                raise HTTPException(404, "Nenhum item encontrado.")
            return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@item_router.get('/{item_id}',
    response_model=ItemPublic,
    responses={400: {'model': ErrorOutput}}
)
async def get_item_by_id(item_id: int, user: Annotated[str, Depends(UserService.get_current_user)]):
    try:
        if(user):
            result = await ItemService.get_item_by_id(item_id)
            if(not result):
                raise HTTPException(404, "Nenhum item encontrado.")
            return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@item_router.post('/add', response_model=RetornoPadrao, responses={400: {'model': ErrorOutput}})
async def add_item(item: ItemCreate, user: Annotated[str, Depends(UserService.get_current_user)]):
    try:
        if(user):
            await ItemService.add_item(item_id = item.item_id,todo_list_id=item.todo_list_id, titulo = item.titulo, descricao = item.descricao)
            return RetornoPadrao(message= "Item inserido com sucesso.")
    except Exception as error:
        raise HTTPException(400, detail=str(error))