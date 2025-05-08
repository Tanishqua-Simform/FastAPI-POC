from fastapi import FastAPI
from router.todo_router import router
from utils.init_db import create_table

create_table()

app = FastAPI(
    title='To Do List API',
    description='Built a RESTful API for managing to-do tasks. I have implemented CRUD operations, data validation and dependency injection in this POC.',
)

app.include_router(router)
