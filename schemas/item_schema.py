
from pydantic import BaseModel

class ItemPublic(BaseModel):
    item_id: int
    descricao: str
    concluido: bool
    titulo: str
    
class ErrorOutput(BaseModel):
    detail: str


    