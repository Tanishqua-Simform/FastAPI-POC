from datetime import date, datetime
from pydantic import BaseModel, UUID4, field_validator

class ToDoUpdateIn(BaseModel):
    status: str

    @field_validator('status')
    @classmethod
    def validate_status(cls, value: str):
        if value != 'Pending' and value != 'Completed':
            raise ValueError("Status can either be set to Pending or Completed")
        return value

class ToDoCreateIn(ToDoUpdateIn):
    title: str
    description: str
    due_date: date

    @field_validator('due_date')
    @classmethod
    def validate_due_date(cls, value: date):
        if value < date.today():
            raise ValueError("Due Date can only be set for future dates.")
        return value

class ToDoOut(BaseModel):
    uid: UUID4
    title: str
    description: str
    due_date: date
    status: str
    created_at: datetime
    updated_at: datetime