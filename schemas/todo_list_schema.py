from typing import List
from pydantic import BaseModel
from schemas.item_schema import ItemListPublic

class TodoList(BaseModel):
    todo_list_id: int
    titulo: str
    item: List[ItemListPublic]
    
class TodoListPublic(BaseModel):
    todo_list_id: int
    titulo: str
    user_id: int
    titulo:str