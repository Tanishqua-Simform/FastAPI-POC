from typing import List, Optional
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from repository.todo_repo import ToDoRepository
from schemas.todo_schema import ToDoCreateIn, ToDoUpdateIn, ToDoOut

class ToDoService:
    ''' Service Class which holds the business logic.
    It mediates between ROUTER Layer and the database connected REPOSITORY Layer.'''

    def __init__(self, session: Session):
        ''' Initializes the Service Object with Object of Repository Class. '''
        self.repository = ToDoRepository(session)
    
    def create(self, data: ToDoCreateIn) -> ToDoOut:
        ''' Calls create function of Repo Object and handles validations. '''
        if self.repository.todo_exists_by_title(data.title):
            raise HTTPException(status_code=400, detail="Todo already exists!")
        return self.repository.create(data)
    
    def get_all(self) -> List[Optional[ToDoOut]]:
        ''' Calls get_all function of Repo Object. '''
        return self.repository.get_all()
    
    def update(self, uid: UUID4, data: ToDoUpdateIn) -> ToDoOut:
        ''' Checks if object is present using repo and then updates it if present. '''
        if not self.repository.todo_exists_by_id(uid):
            raise HTTPException(status_code=404, detail="Todo not Found!")
        todo = self.repository.get_by_id(uid)
        return self.repository.update(todo, data)
    
    def delete(self, uid: UUID4) -> bool:
        ''' Checks if the object is present, and if it is then deletes it. '''
        if not self.repository.todo_exists_by_id(uid):
            raise HTTPException(status_code=404, detail="Todo not Found!")
        todo = self.repository.get_by_id(uid)
        return self.repository.delete(todo)