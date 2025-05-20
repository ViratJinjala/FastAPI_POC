import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.sql import func
from config.database import Base
from sqlalchemy.orm import relationship


class User(Base):
 
    __tablename__ = "user"
 
    id = Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    username = Column(String(length=50), unique=True, nullable=False)
    email = Column(String(length=100), unique=True, nullable=False)
    first_name = Column(String(length=50), nullable=False)
    last_name = Column(String(length=50))
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now() ,default=func.now())
    
    todo = relationship("ToDo", back_populates = "user", cascade="all, delete")