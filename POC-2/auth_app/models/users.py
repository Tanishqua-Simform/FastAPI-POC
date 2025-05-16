import enum
from uuid import uuid4
from regex import regex
from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, event, UUID
from sqlalchemy.orm import validates
from config.database import Base

class GenderEnum(enum.Enum):
    ''' Enum values for Gender types - Male, Female and Transgender'''
    MALE = 'male'
    FEMALE = 'female'
    TRANSGENDER = 'transgender'

class RoleEnum(enum.Enum):
    ''' Enum values for Role types - Admin and User'''
    ADMIN = 'admin'
    USER = 'user'

class User(Base):
    ''' Model class to map User Class with the users table in database. 
    It validates the email id at time of creation. '''
    __tablename__ = "users"

    id = Column(UUID(as_uuid = True), primary_key=True, default=uuid4)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(Enum(GenderEnum), nullable=False)
    bio = Column(String)
    deleted = Column(Boolean, default=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)
    pg_16 = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    @validates('email')
    def validate_email(self, key, value):
        ''' Validate Email with the help of Regular Expression. '''
        expression = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
        if not regex.match(expression, value):
            raise ValueError('Invalid Email ID.')
        return value
    
@event.listens_for(User, 'before_insert')
def validate(mapper, connection, target):
    ''' Validates whether the User should be given Parental Guidance on basis of their age.
    This function acts as an event listener for User table.'''
    if target.age > 16:
        target.pg_16 = False