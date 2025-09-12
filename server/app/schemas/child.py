import uuid
from pydantic import EmailStr, int
from .user import User

class CreateChild:
    email:EmailStr
    password:str
    firstName:str
    lastName:str
    baseAllowance:int
    parentId:uuid.UUID

class CreateChildOut(User):
    password: str
    baseAllowance: int
    parentId: uuid.UUID
   

class UpdateChild(User):
    baseAllowance:int
