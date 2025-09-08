
from sqlalchemy import Column, ForeignKey, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import BaseModel

class Child(BaseModel):
    """Child model"""
    __tablename__ = "children"
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("parents.id"), nullable=False)
    base_allowance = Column(Numeric(10, 2), nullable=False, default=0)
    avatar_url = Column(Text)
    
    # Relationships
    user = relationship("User", back_populates="child_profile")
    parent = relationship("Parent", back_populates="children")
    chore_assignments = relationship("ChoreAssignment", back_populates="child")
    allowance_transactions = relationship("AllowanceTransaction", back_populates="child")
