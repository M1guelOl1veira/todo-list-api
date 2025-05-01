
from pydantic import BaseModel

class ItemPublic(BaseModel):
    item_id: int
    descricao: str
    concluido: bool
    titulo: str
    
class ErrorOutput(BaseModel):
    detail: str

class ItemCreate(BaseModel):
    item_id: int
    todo_list_id: int
    titulo: str
    descricao: str

class RetornoPadrao(BaseModel):
    message: str
    