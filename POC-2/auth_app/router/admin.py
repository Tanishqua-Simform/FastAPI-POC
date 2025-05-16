from typing import List, Annotated
from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from config.database import get_db
from models.users import User
from schemas.admin import UserListOut, UserChangeIn
from service.admin import AdminService
from utils.permissions import is_admin

admin_router = APIRouter(
    prefix='/admin',
    tags=['Admin']
)

@admin_router.get('/users', response_model=List[UserListOut])
def get_all_users(admin: Annotated[User, Depends(is_admin)], session: Session = Depends(get_db)):
    ''' Only Admins can access this API. It retreives the info of all users. '''
    service = AdminService(session)
    return service.get_all_users()

@admin_router.put('/user/{id}', response_model=UserListOut)
def change_user_role(admin: Annotated[User, Depends(is_admin)], id: UUID4, data: UserChangeIn, session: Session = Depends(get_db)):
    ''' Admins can change the info of its users. It can only modify their Role and Deleted fields. The deleted field can be set or unset depending on the user's activity.'''
    service = AdminService(session)
    return service.change_user(id, data)