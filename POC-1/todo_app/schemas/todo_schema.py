from pydantic import BaseModel, UUID4
from datetime import date, datetime

class ToDoCreateIn(BaseModel):
    title: str
    description: str
    due_date: date
    status: str

class ToDoUpdateIn(BaseModel):
    status: str

class ToDoOut(ToDoCreateIn):
    uid: UUID4
    created_at: datetime
    updated_at: datetime