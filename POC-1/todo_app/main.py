from fastapi import FastAPI
from router.todo_router import router
from utils.init_db import create_table

create_table()

app = FastAPI(
    title="To Do List API",
    summary="Built a RESTful API for managing to-do tasks. I have implemented CRUD operations, data validation and dependency injection in this POC.",
    description="1. To-Do List CRUD API Endpoint\n"
    "2. Data Validation - "
    "i. Title should be unique. "
    "ii. Due Date should be for future dates. "
    "iii. Status should either be Pending or Completed. \n"
    "3. Dependency Injection - Connected SQLite.\n"
    "4. Error Handling - Handled non-existent Todos during Put and Delete Operations\n"
    "5. Interactive Documentation - Created title, summary, description and tags for Docs."
)

app.include_router(router)
