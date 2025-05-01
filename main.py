from fastapi import APIRouter, FastAPI

from routers.auth_router import auth_router
from routers.todo_list_router import todo_list_router
from routers.item_router import item_router
app = FastAPI()
router = APIRouter()

app.include_router(item_router)
app.include_router(todo_list_router)
app.include_router(auth_router)

