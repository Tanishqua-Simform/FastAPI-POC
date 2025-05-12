from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError
from config.database import get_db
from models.users import User, Role_Enum
from schemas.admin import UserListOut, UserChangeIn
from utils.jwt import get_active_user

admin_router = APIRouter(
    prefix='/admin',
    tags=['Admin']
)

def is_admin(user: Annotated[User, Depends(get_active_user)]):
    if user.role != Role_Enum.ADMIN:
        raise HTTPException(status_code=403, detail='Permission Denied!')
    return user

@admin_router.get('/users', response_model=List[UserListOut])
def get_all(admin: Annotated[User, Depends(is_admin)], session: Session = Depends(get_db)):
    users = session.query(User).all()
    return users

@admin_router.put('/user/{id}', response_model=UserListOut)
def change_user(admin: Annotated[User, Depends(is_admin)], id: UUID4, data: UserChangeIn, session: Session = Depends(get_db)):
    user = session.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not Found.')
    try:
        user.deleted = data.deleted
        user.role = data.role
        session.commit()
        session.refresh(user)
    except DataError:
        raise HTTPException(status_code=400, detail="Role value should either be 'ADMIN' or 'USER'.")
    return user