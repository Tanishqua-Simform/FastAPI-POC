from pydantic import BaseModel

class UserOut(BaseModel):
    ''' Schema to constrict the data to be shown in response to Users.'''
    email: str = "sample@mail.com"
    username: str = "john_doe"
    first_name: str = "John"
    last_name: str = "Doe"
    age: int = "12"
    gender: str = "GENDER"
    bio: str = "Hey, i am john doe, naam toh suna hoga."

class UserIn(UserOut):
    ''' Schema for Registration '''
    password:str = "password"

class UserLogin(BaseModel):
    ''' Schema for Login '''
    username: str = "john_doe"
    password: str = "password"

class UserProfile(BaseModel):
    ''' Schema for Users to Change their Profile '''
    first_name: str = "John"
    last_name: str = "Doe"
    bio: str = "Hey, i am john doe, naam toh suna hoga."

class UserPasswordChange(BaseModel):
    ''' Schema for Users to Reset their Password '''
    old_password: str = "purana_password"
    new_password: str = "naya_raapchik_password"