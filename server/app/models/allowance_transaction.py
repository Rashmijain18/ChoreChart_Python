

from sqlalchemy import Column, String, ForeignKey, Numeric, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import BaseModel

class AllowanceTransaction(BaseModel):
    """Allowance transaction model"""
    __tablename__ = "allowance_transactions"
    
    child_id = Column(UUID(as_uuid=True), ForeignKey("children.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    type = Column(String(50), nullable=False)  # 'earned', 'spent', 'bonus', etc.
    description = Column(Text)
    transaction_date = Column(DateTime(timezone=True), nullable=False)
    
    # Relationships
    child = relationship("Child", back_populates="allowance_transactions")

