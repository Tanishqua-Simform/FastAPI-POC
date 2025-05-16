from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.users import UserIn, UserLogin, UserProfile, UserPasswordChange, UserOut
from config.database import get_db
from models.users import User
from service.users import UserService
from utils.jwt import get_active_user, login_for_access_token

user_router = APIRouter(
    prefix='/auth'
)

@user_router.post('/register', response_model=UserOut, tags=['Register and Login'])
def register(data: UserIn, session: Session = Depends(get_db)):
    ''' New users can register. Make sure that the email and username should not already be registered.'''
    service = UserService(session)
    return service.register(data)

@user_router.post('/login', tags=['Register and Login'])
def login(data: UserLogin, session: Session = Depends(get_db)):
    ''' Users can login using their Credentials. '''
    service = UserService(session)
    return service.login(data)


@user_router.post('/token', tags=['JWT'])
def jwt_login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Annotated[Session, Depends(get_db)]):
    ''' On Successful login, users would receive Bearer Token. '''
    return login_for_access_token(user_data, session)

@user_router.get('/test-auth', response_model=UserOut, tags=['JWT'])
def test_jwt_token(user: Annotated[User, Depends(get_active_user)]):
    ''' To check for authentication. It authenticates only Active Users (with deleted flag set to False.)'''
    return user

@user_router.put('/change-profile', response_model=UserOut, tags=['Modify Profile'])
def change_profile(modified_data: UserProfile, user: Annotated[User, Depends(get_active_user)], session: Annotated[Session, Depends(get_db)]):
    ''' Users can changes their profile. They are allowed to modify their First and Last name and Bio.'''
    service = UserService(session)
    return service.change_profile(modified_data, user)

@user_router.put('/change-password', tags=['Modify Profile'])
def reset_password(modified_data: UserPasswordChange, user: Annotated[User, Depends(get_active_user)], session: Annotated[Session, Depends(get_db)]):
    ''' Using this Service, users can change their password. Make sure to write correct Old password. New Password should not be same as the older one.'''
    service = UserService(session)
    return service.change_password(modified_data, user)