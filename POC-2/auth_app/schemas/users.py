from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    username: str
    password:str
    first_name: str
    last_name: str
    age: int
    gender: str
    bio: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserProfile(BaseModel):
    first_name: str
    last_name: str
    bio: str

class UserPasswordChange(BaseModel):
    old_password: str
    new_password: str