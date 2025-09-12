import uuid
from typing import Literal
from pydantic import BaseModel,Field
from datetime import datetime,timezone

class ParentDashboardOut(BaseModel):
    id:uuid.UUID
    title: str
    description: str
    value: float
    dueDate: str=Field(..., alias="due_date")
    assignmentId: uuid.UUID
    childId: uuid.UUID
    childName: str
    status: Literal['pending', 'inProgress', 'completed', 'verified']

class ChildDashboardOut(BaseModel):
    id:uuid.UUID
    title: str
    description: str
    value: float
    dueDate: str=Field(..., alias="due_date")
    assignmentId: uuid.UUID
    childId: uuid.UUID
    childName: str
    status: Literal['pending', 'inProgress', 'completed', 'verified']
    comment:str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), alias="createdAt")
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), alias="updatedAt")
    verified_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), alias="verifiedAt")
