from ..models.children import Child
from ..models.users import User
from sqlalchemy.orm import Session
from ..schemas.child import CreateChild,CreateChildOut
from passlib.hash import bcrypt
import uuid
from ..models.children import Child
from ..models.users import User

def check_existing_child(email:str,db:Session):
    user=db.query(User).filter(User.email == email).first()
    child=db.query(Child).filter(Child.user_id==user.id).first()
    if child:
       return True
    return False

def create_child(data:CreateChild,db:Session):
    passwordHash = bcrypt.hash(data.password)
    user=User(email=data.email,passwordHash=passwordHash,firstName=data.firstName,lastName=data.lastName,role="child")
    db.add(user)
    db.commit()
    db.refresh(user)
    child=Child(userId=user.id,parentId=data.parentId,baseAllowance=data.baseAllowance)
    db.add(child)
    db.commit()
    db.refresh(child)
    return CreateChildOut(
        password=user.password,
        baseAllowance=child.baseAllowance,
        parentId=child.parentId,
        childId=child.id,
        id=user.id,
        email=user.email,
        firstName=user.first_name,
        lastName=user.last_name,
    ) 

def get_children_details(db:Session,parentId:uuid.UUID):
    children=db.query(Child).join(User,User.id==Child.user_id).filter(Child.parent_id==parentId).all()
    return children

def update_child(db:Session,child):
    pass


def delete_child(id:uuid.UUID,db:Session):
    child=db.query(Child).filter(Child.id==id).first()
    db.delete(child)
    db.commit()
    return child
