from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from config.database import Base

class ToDoModel(Base):
    ''' Model Class For Todo, to map this class with todos table in Database. '''
    __tablename__ = 'todos'

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String)
    description = Column(String)
    due_date = Column(Date)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)