
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel

class User(BaseModel):
    """User model for both parents and children"""
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False, default="parent")
    
    # Relationships
    parent_profile = relationship("Parent", back_populates="user", uselist=False)
    child_profile = relationship("Child", back_populates="user", uselist=False)
   