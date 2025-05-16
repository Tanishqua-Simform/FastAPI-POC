from typing import List, Optional, Type
from datetime import datetime
from pydantic import UUID4
from sqlalchemy.orm import Session
from models.todo_model import ToDoModel
from schemas.todo_schema import ToDoCreateIn, ToDoUpdateIn, ToDoOut

class ToDoRepository:
    ''' Repository Class is used to perform CRUD operations on Database.
    It is the third layer in the sequence - ROUTER -> SERVICE -> REPOSITORY. '''

    def __init__(self, session: Session):
        ''' Initializes the Todo Repo object with the Session to DB.'''
        self.session = session
    
    def create(self, data: ToDoCreateIn) -> ToDoOut:
        ''' Created new todo in the db. '''
        todo_dict = data.model_dump()
        new_todo = ToDoModel(**todo_dict)
        self.session.add(new_todo)
        self.session.commit()
        self.session.refresh(new_todo)
        return ToDoOut(**new_todo.__dict__)

    def get_all(self) -> List[Optional[ToDoOut]]:
        ''' Fetches all the todos from the db. '''
        todos = self.session.query(ToDoModel).all()
        return [ToDoOut(**todo.__dict__) for todo in todos]
    
    def get_by_id(self, uid: UUID4) -> Type[ToDoModel]:
        ''' Fetches the Todo with id - uid(parameter). It returns none if no such todo exists. '''
        return self.session.query(ToDoModel).filter(ToDoModel.uid==uid).first()
    
    def todo_exists_by_id(self, uid: UUID4) -> bool:
        ''' Returns a bool representing the presence of Todo object with id - uid(parameter)'''
        todo = self.session.query(ToDoModel).filter(ToDoModel.uid==uid).first()
        return todo is not None
    
    def todo_exists_by_title(self, title: str) -> bool:
        ''' Returns a bool representing the presence of Todo object with title - title(parameter)'''
        todo = self.session.query(ToDoModel).filter(ToDoModel.title==title).first()
        return todo is not None
    
    def update(self, todo: Type[ToDoModel], data: ToDoUpdateIn) -> ToDoOut:
        ''' Updates only the status of the todo'''
        todo.status = data.status
        todo.updated_at = datetime.now()
        self.session.commit()
        self.session.refresh(todo)
        return ToDoOut(**todo.__dict__)
    
    def delete(self, todo: Type[ToDoModel]) -> bool:
        ''' Deletes the todo from the database. '''
        self.session.delete(todo)
        self.session.commit()
        return True