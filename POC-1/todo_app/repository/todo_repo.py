from typing import List, Type
from pydantic import UUID4
from sqlalchemy.orm import Session
from models.todo_model import ToDoModel
from schemas.todo_schema import ToDoCreateIn, ToDoOut

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

    def get_all(self) -> List[ToDoOut]:
        return self.session.query(ToDoModel).all()
    
    # def get_by_id(self, _id: UUID4) -> Type[ToDoModel]:
