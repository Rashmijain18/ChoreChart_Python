from pydantic import BaseModel, EmailStr
import uuid
from .user import User

class UserCreate(User):
	password: str
	id: None = None  # Exclude id from input 
	

class UserOut(User):
	class Config:
		orm_mode = True
