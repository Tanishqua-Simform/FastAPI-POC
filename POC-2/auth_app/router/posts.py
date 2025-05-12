from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from utils.jwt import get_active_user
from models.users import User

post_router = APIRouter(
    prefix='/post',
    tags=['Confidential']
)

security = HTTPBearer()

@post_router.get('/test-auth')
def auth_test(user: Annotated[User, Depends(get_active_user)]):
    return user