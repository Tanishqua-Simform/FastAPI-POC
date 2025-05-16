from fastapi import FastAPI
from router.todo_router import router
from utils.init_db import create_table

create_table()

app = FastAPI(
    title="POC-1: To Do List API",
    summary="Built a RESTful API for managing to-do tasks. I have implemented CRUD operations, data validation and dependency injection in this POC.",
    description="### 1. API Endpoints\n"
    "* Created APIs to handle CRUD operations for Todos. \n"

    "### 2. Data Validation \n"
    "* Title should be unique. \n"
    "* Due Date should be for future dates. \n"
    "* Status should either be Pending or Completed. \n"

    "### 3. Dependency Injection \n"
    "* Connected SQLite for database.\n"

    "### 4. Error Handling \n"
    "* Handled non-existent Todos during Put and Delete Operations\n"

    "### 5. Interactive Documentation \n"
    "* Added Docstrings for Router Handler Functions.\n"
    "* Added Title, Summary, Description and Tags parameters inside FastAPI Instance.\n"
    "* Created placeholder values for all Pydantic Schemas."
)

app.include_router(router)
