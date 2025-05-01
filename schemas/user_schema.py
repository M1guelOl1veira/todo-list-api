from typing import List
from pydantic import BaseModel

from schemas.todo_list_schema import TodoList

class UserPublic(BaseModel):
    user_id: int
    nome_usuario: str
    email: str
    token: str
    todo_list: List[TodoList]
    
class UserInDB(UserPublic):
    hashed_password: str