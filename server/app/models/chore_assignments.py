

from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import BaseModel

class ChoreAssignment(BaseModel):
    """Chore assignment model"""
    __tablename__ = "chore_assignments"
    
    chore_id = Column(UUID(as_uuid=True), ForeignKey("chores.id"), nullable=False)
    child_id = Column(UUID(as_uuid=True), ForeignKey("children.id"), nullable=False)
    status = Column(String(50), nullable=False, default="pending")
    completed_at = Column(DateTime(timezone=True))
    verified_at = Column(DateTime(timezone=True))
    comment = Column(Text)
    
    # Relationships
    chore = relationship("Chore", back_populates="assignments")
    child = relationship("Child", back_populates="chore_assignments")
