from pydantic import BaseModel, EmailStr,Field
import uuid
from typing import Literal
from datetime import datetime,timezone

class User(BaseModel):
    id: uuid.UUID
    email: EmailStr
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    role: Literal['parent', 'child']= 'parent'
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), alias="createdAt")
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), alias="updatedAt")

    class Config:
        populate_by_name = True  # allows using both "firstName" and "first_name"



