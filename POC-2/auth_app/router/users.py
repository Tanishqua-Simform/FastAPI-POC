from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, DataError
from schemas.users import UserIn, UserLogin, UserProfile, UserPasswordChange
from config.database import get_db
from models.users import User
from utils.password_hash import Hash
from utils.jwt import login_for_access_token, get_active_user

user_router = APIRouter(
    prefix='/auth',
    tags=['User Profile']
)

@user_router.post('/register')
def register(data: UserIn, session: Session = Depends(get_db)):
    data.password = Hash.bcrypt(data.password)
    new_user = User(**data.model_dump())
    try:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail='Username and/or Email Id already exists!')
    except DataError:
        raise HTTPException(status_code=400, detail="Gender value should either be 'FEMALE', 'MALE' or 'TRANSGENDER'.")
    return new_user

@user_router.post('/login')
def login(data: UserLogin, session: Session = Depends(get_db)):
    user = session.query(User).filter(User.username==data.username).first()
    if not user or not Hash.verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail='User credentials provided are incorrect.')
    return "Login Successful"

@user_router.post('/token')
def jwt_login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Annotated[Session, Depends(get_db)]):
    return login_for_access_token(user_data, session)

@user_router.put('/profile')
def profile(modified_data: UserProfile, user: Annotated[User, Depends(get_active_user)], session: Annotated[Session, Depends(get_db)]):
    user.first_name = modified_data.first_name
    user.last_name = modified_data.last_name
    user.bio = modified_data.bio

    session.commit()
    session.refresh(user)
    return user


@user_router.put('/change-password')
def password_change(modified_data: UserPasswordChange, user: Annotated[User, Depends(get_active_user)], session: Annotated[Session, Depends(get_db)]):
    if not Hash.verify_password(modified_data.old_password, user.password):
        raise HTTPException(status_code=400, detail='Wrong Password Entered.')
    user.password = Hash.bcrypt(modified_data.new_password)

    session.commit()
    return "Password Changed Successfully!"