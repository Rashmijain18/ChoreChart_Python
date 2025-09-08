
from sqlalchemy import Column, String, Text, Numeric, DateTime
from sqlalchemy.orm import relationship
from .base import BaseModel

class Chore(BaseModel):
    """Chore model"""
    __tablename__ = "chores"
    
    title = Column(String(255), nullable=False)
    description = Column(Text)
    value = Column(Numeric(10, 2), nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=False)
    
    # Relationships
    assignments = relationship("ChoreAssignment", back_populates="chore")

