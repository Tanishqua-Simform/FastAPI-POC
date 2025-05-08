from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.todo_model import ToDoModel
from schemas.todo_schema import ToDoCreateIn, ToDoOut

router = APIRouter(
    tags=['To Do']
)

@router.get('/list-todo', response_model=List[ToDoOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(ToDoModel).all()

@router.post('/list-todo')
def create(todo_data: ToDoCreateIn, db: Session = Depends(get_db)):
    todo_dict = todo_data.model_dump()
    new_todo = ToDoModel(**todo_dict)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo