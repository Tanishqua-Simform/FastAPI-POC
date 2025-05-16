from typing import List
from pydantic import UUID4
from sqlalchemy.orm import Session
from models.users import User
from schemas.admin import UserChangeIn

class AdminRepository:
    ''' Repository Class for Admin users to perform CRUD on database.
    This layer is the abstraction for Database Actions. '''
    def __init__(self, session: Session):
        ''' Initializes a Repo object with Database Session. '''
        self.session = session

    def all(self) -> List[User]:
        ''' Retrieves all users from the database. '''
        users = self.session.query(User).all()
        return users

    def get_by_id(self, id: UUID4) -> User:
        ''' Retrieves an user object, if it exists, else returns None. '''
        user = self.session.query(User).filter(User.id==id).first()
        return user
    
    def update_user(self, data: UserChangeIn, user: User) -> User:
        ''' Updates the User's Role and Account Delete flag. '''
        user.deleted = data.deleted
        user.role = data.role
        self.session.commit()
        self.session.refresh(user)
        return user