from typing import List, Optional
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from repository.todo_repo import ToDoRepository
from schemas.todo_schema import ToDoCreateIn, ToDoUpdateIn, ToDoOut

class ToDoService:
    def __init__(self, session: Session):
        self.repository = ToDoRepository(session)
    
    def create(self, data: ToDoCreateIn) -> ToDoOut:
        if self.repository.todo_exists_by_title(data.title):
            raise HTTPException(status_code=400, detail="Todo already exists!")
        return self.repository.create(data)
    
    def get_all(self) -> List[Optional[ToDoOut]]:
        return self.repository.get_all()
    
    def update(self, uid: UUID4, data: ToDoUpdateIn) -> ToDoOut:
        if not self.repository.todo_exists_by_id(uid):
            raise HTTPException(status_code=404, detail="Todo not Found!")
        todo = self.repository.get_by_id(uid)
        return self.repository.update(todo, data)
    
    def delete(self, uid: UUID4) -> bool:
        if not self.repository.todo_exists_by_id(uid):
            raise HTTPException(status_code=404, detail="Todo not Found!")
        todo = self.repository.get_by_id(uid)
        return self.repository.delete(todo)