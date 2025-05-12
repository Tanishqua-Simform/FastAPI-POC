from pydantic import BaseModel, UUID4

class UserListOut(BaseModel):
    id: UUID4
    email: str
    username: str
    first_name: str
    last_name: str
    age: int
    gender: str
    role: str
    bio: str
    deleted:bool
    pg_16: bool

class UserChangeIn(BaseModel):
    deleted: bool
    role: str