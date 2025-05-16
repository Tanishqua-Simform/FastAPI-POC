from pydantic import BaseModel, UUID4

class UserListOut(BaseModel):
    ''' Schemas to constrict the fields to be shown in response to ADMIN users.'''
    id: UUID4 = "UUID"
    email: str = "sample@mail.com"
    username: str = "john_doe"
    first_name: str = "John"
    last_name: str = "Doe"
    age: int = "12"
    gender: str = "GENDER"
    role: str = "ROLE"
    bio: str = "Hey, i am john doe, naam toh suna hoga."
    deleted:bool = False
    pg_16: bool = True

class UserChangeIn(BaseModel):
    ''' Schema to constrict admins to only change, role and deleted field of User.'''
    deleted: bool = True
    role: str = "ROLE"