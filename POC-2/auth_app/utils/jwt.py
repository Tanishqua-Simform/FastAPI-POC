import os
from dotenv import load_dotenv
from datetime import timedelta, datetime
from jose import jwt
from typing import Optional, Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from config.database import get_db
from utils.password_hash import Hash
from models.users import User

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_TIME = os.getenv("ACCESS_TOKEN_EXPIRE_TIME")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=os.getenv('TOKEN_FETCH_URL'))

def create_access_token(data: dict, expires_delta: Optional[timedelta]) -> str:
    ''' Encodes the data and creates the token. '''
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=15))
    to_encode['exp'] = expire
    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return token

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Annotated[Session, Depends(get_db)]) -> User:
    ''' Decodes the token and retreives user object from database. '''
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username = payload.get('sub')
        if not username:
            raise HTTPException(status_code=401, detail='Invalid Token!')
    except:
        raise HTTPException(status_code=401, detail='Invalid Token!')
    user = session.query(User).filter(User.username==username).first()
    if not user:
        raise HTTPException(status_code=401, detail='Invalid Token!')
    return user

def get_active_user(current_user: Annotated[User, Depends(get_current_user)]) -> User:
    ''' Raises exception if the user has deleted flag set.'''
    if current_user.deleted:
        raise HTTPException(status_code=400, detail='Account Inactive')
    return current_user

def login_for_access_token(data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Annotated[Session, Depends(get_db)]) -> dict:
    ''' Returns Bearer tokens for users, on successful credentials check. '''
    user = session.query(User).filter(User.username==data.username).first()
    if not user or not Hash.verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail='Invalid Credentials!')
    access_token_expire = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_TIME))
    access_token = create_access_token({'sub': user.username}, access_token_expire)
    return {"access_token": access_token, "token_type": "bearer"}