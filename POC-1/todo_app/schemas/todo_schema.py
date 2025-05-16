from datetime import date, datetime
from pydantic import BaseModel, UUID4, field_validator

class ToDoUpdateIn(BaseModel):
    ''' Schema to constrict updation for only status field. '''
    status: str = "Pending"

    @field_validator('status')
    @classmethod
    def validate_status(cls, value: str):
        ''' Validates the status field. '''
        if value != 'Pending' and value != 'Completed':
            raise ValueError("Status can either be set to Pending or Completed")
        return value

class ToDoCreateIn(ToDoUpdateIn):
    ''' Schema to constrict a few fields along with validations to be created. '''
    title: str = "Sample Title"
    description: str = "Sample Description"
    due_date: date

    @field_validator('due_date')
    @classmethod
    def validate_due_date(cls, value: date):
        ''' Validates the due date to be set for future.'''
        if value < date.today():
            raise ValueError("Due Date can only be set for future dates.")
        return value

class ToDoOut(BaseModel):
    ''' Schema to validate the response data. '''
    uid: UUID4 = "UUID"
    title: str = "Sample Title"
    description: str = "Sample Description"
    due_date: date 
    status: str = "Pending"
    created_at: datetime
    updated_at: datetime