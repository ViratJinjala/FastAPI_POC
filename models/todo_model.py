from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, ForeignKey, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.sql import func
from config.database import Base
from sqlalchemy.orm import relationship


class ToDo(Base):
 
    __tablename__ = "todo"
 
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(Date, nullable=True)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    user_id = Column(UUID(as_uuid = True), ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="todo")
    