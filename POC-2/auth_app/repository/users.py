from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserIn, UserProfile

class UserRepository:
    ''' Repository Class to manage the database access.
    It is the abstraction layer for database. '''
    def __init__(self, session: Session):
        ''' Initializes a Repo object with Database Session. '''
        self.session = session
        
    def create(self, data: UserIn) -> User:
        ''' Creates and saves user data in database. '''
        new_user = User(**data.model_dump())
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def get_user_by_username(self, username: str) -> User:
        ''' Retreives the User object using its username field, if it exists, else None. '''
        user = self.session.query(User).filter(User.username==username).first()
        return user

    def update_profile(self, modified_data: UserProfile, user: User) -> User:
        ''' Updates the user object's Profile information. '''
        user.first_name = modified_data.first_name
        user.last_name = modified_data.last_name
        user.bio = modified_data.bio

        self.session.commit()
        self.session.refresh(user)
        return user

    def update_password(self, hashed_password: str, user: User):
        ''' Resets the password for the user. '''
        user.password = hashed_password
        self.session.commit()