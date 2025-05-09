from typing import List
from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.todo_schema import ToDoCreateIn, ToDoUpdateIn, ToDoOut
from service.todo_service import ToDoService

router = APIRouter(
    prefix="/todo",
    tags=['CRUD']
)

@router.post("", status_code=201, response_model=ToDoOut)
def create(data: ToDoCreateIn, session: Session = Depends(get_db)):
    service = ToDoService(session)
    return service.create(data)

@router.get("", status_code=200, response_model=List[ToDoOut])
def get_all(session: Session = Depends(get_db)):
    service = ToDoService(session)
    return service.get_all()

@router.put("/{uid}", status_code=200, response_model=ToDoOut)
def update(uid: UUID4, data: ToDoUpdateIn, session: Session = Depends(get_db)):
    service = ToDoService(session)
    return service.update(uid, data)

@router.delete("/{uid}", status_code=204)
def delete(uid: UUID4, session: Session = Depends(get_db)):
    service = ToDoService(session)
    return service.delete(uid)