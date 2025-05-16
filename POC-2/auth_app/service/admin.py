from typing import List
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError
from models.users import User
from schemas.admin import UserChangeIn
from repository.admin import AdminRepository

class AdminService:
    ''' Service Class to mediate between the ROUTER layer and REPOSITORY layer.
    It holds the business logic for the App.'''

    def __init__(self, session: Session):
        ''' Initializes Service Object with an instance of repository class. '''
        self.repository = AdminRepository(session)

    def get_all_users(self) -> List[User]:
        ''' Retrieves all the users from the Repository Instance.'''
        return self.repository.all()

    def change_user(self, id: UUID4, data: UserChangeIn) -> User:
        ''' Changes the User details, if user exists, else raises appropriate exceptions.'''
        user = self.repository.get_by_id(id)
        if not user:
            raise HTTPException(status_code=404, detail='User not Found.')
        try:
            user = self.repository.update_user(data, user)
        except DataError:
            raise HTTPException(status_code=400, detail="Role value should either be 'ADMIN' or 'USER'.")
        return user