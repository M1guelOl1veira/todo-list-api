
from pydantic import BaseModel

class ItemListPublic(BaseModel):
    item_id: int
    descricao: str
    concluido: bool
    titulo: str
    
class ErrorOutput(BaseModel):
    detail: str


    