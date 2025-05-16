from typing import Annotated
from fastapi import Depends, HTTPException
from models.users import User, RoleEnum
from utils.jwt import get_active_user

def is_admin(user: Annotated[User, Depends(get_active_user)]) -> User:
    ''' Raises Forbidden Exception if user is not Admin. '''
    if user.role != RoleEnum.ADMIN:
        raise HTTPException(status_code=403, detail='Permission Denied!')
    return user