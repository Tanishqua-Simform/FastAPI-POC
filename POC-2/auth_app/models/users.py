import enum
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, event, UUID
from sqlalchemy.orm import validates
from config.database import Base

class Gender_Enum(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'
    TRANSGENDER = 'transgender'

class Role_Enum(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid = True), primary_key=True, default=uuid4)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(Enum(Gender_Enum), nullable=False)
    bio = Column(String)
    deleted = Column(Boolean, default=False)
    role = Column(Enum(Role_Enum), default=Role_Enum.USER, nullable=False)
    pg_16 = Column(Boolean, default=True)
    # skills = Column() -> Multiple select field with help of relationships
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    @validates('email')
    def validate_email(self, key, value):
        if not value.endswith("@gmail.com"):
            raise ValueError('Email should be a valid Google mail ID.')
        return value
    
@event.listens_for(User, 'before_insert')
def validate(mapper, connection, target):
    if target.age > 16:
        target.pg_16 = False