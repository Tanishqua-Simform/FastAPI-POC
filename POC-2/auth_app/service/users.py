from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, DataError
from schemas.users import UserIn, UserLogin, UserProfile, UserPasswordChange
from models.users import User
from repository.users import UserRepository
from utils.password_hash import Hash

class UserService:
    ''' Service Class to mediate between the ROUTER layer and REPOSITORY layer.
    It holds the business logic for the App.'''
    
    def __init__(self, session: Session):
        ''' Initializes Service Object with an instance of repository class. '''
        self.repository = UserRepository(session)

    def register(self, data: UserIn) -> User:
        ''' Registers the user. Handles if email/username already exists. Proper Gender Values should be entered. '''
        data.password = Hash.bcrypt(data.password)
        try:
            registered_user = self.repository.create(data)
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=f"{ve}")
        except IntegrityError:
            raise HTTPException(status_code=400, detail='Username and/or Email Id already exists!')
        except DataError:
            raise HTTPException(status_code=400, detail="Gender value should either be 'FEMALE', 'MALE' or 'TRANSGENDER'.")
        return registered_user

    def login(self, data: UserLogin) -> str:
        ''' Verifies the user credentials and logs in. '''
        user = self.repository.get_user_by_username(data.username)
        if not user or not Hash.verify_password(data.password, user.password):
            raise HTTPException(status_code=400, detail='User credentials provided are incorrect.')
        return "Login Successful"

    def change_profile(self, modified_data: UserProfile, user: User) -> User:
        ''' Updates the user profile. '''
        updated_user = self.repository.update_profile(modified_data, user)
        return updated_user

    def change_password(self, modified_data: UserPasswordChange, user: User) -> str:
        ''' Changes Password after validating it, followed by hashing of new password. '''
        if not Hash.verify_password(modified_data.old_password, user.password):
            raise HTTPException(status_code=400, detail='Wrong Password Entered.')
        if modified_data.old_password == modified_data.new_password:
            raise HTTPException(status_code=400, detail="New password should be different from the older one!")
        hashed_password = Hash.bcrypt(modified_data.new_password)
        self.repository.update_password(hashed_password, user)
        return "Password Changed Successfully!"