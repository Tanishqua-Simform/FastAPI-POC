from typing import List, Optional, Type
from datetime import datetime
from pydantic import UUID4
from sqlalchemy.orm import Session
from models.todo_model import ToDoModel
from schemas.todo_schema import ToDoCreateIn, ToDoUpdateIn, ToDoOut

class ToDoRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, data: ToDoCreateIn) -> ToDoOut:
        todo_dict = data.model_dump()
        new_todo = ToDoModel(**todo_dict)
        self.session.add(new_todo)
        self.session.commit()
        self.session.refresh(new_todo)
        return ToDoOut(**new_todo.__dict__)

    def get_all(self) -> List[Optional[ToDoOut]]:
        todos = self.session.query(ToDoModel).all()
        return [ToDoOut(**todo.__dict__) for todo in todos]
    
    def get_by_id(self, uid: UUID4) -> Type[ToDoModel]:
        return self.session.query(ToDoModel).filter(ToDoModel.uid==uid).first()
    
    def todo_exists_by_id(self, uid: UUID4) -> bool:
        todo = self.session.query(ToDoModel).filter(ToDoModel.uid==uid).first()
        return todo is not None
    
    def todo_exists_by_title(self, title: str) -> bool:
        todo = self.session.query(ToDoModel).filter(ToDoModel.title==title).first()
        return todo is not None
    
    def update(self, todo: Type[ToDoModel], data: ToDoUpdateIn) -> ToDoOut:
        todo.status = data.status
        todo.updated_at = datetime.now()
        self.session.commit()
        self.session.refresh(todo)
        return ToDoOut(**todo.__dict__)
    
    def delete(self, todo: Type[ToDoModel]) -> bool:
        self.session.delete(todo)
        self.session.commit()
        return True