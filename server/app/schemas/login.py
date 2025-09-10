from pydantic import BaseModel, EmailStr
import uuid
from .user import User
from typing import Optional

class Login(BaseModel):
	email: EmailStr
	password: str

class LoginData(User):
  parentId:Optional[str] =None
  childId: Optional[str] =None

class LoginOut(BaseModel):
  data: LoginData
  success: bool

