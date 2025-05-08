from sqlalchemy.orm import Session
from repository.todo_repo import ToDoRepository
from schemas.todo_schema import ToDoCreateIn, ToDoOut

class ToDoService:
    def __init__(self, session: Session):
        self.repository = ToDoRepository(session)
    
    # def create(self, data: ToDoCreateIn) -> ToDoOut:
    #     if self.repository.re