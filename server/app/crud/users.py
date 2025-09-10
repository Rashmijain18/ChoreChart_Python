from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from ..models.users import User
from ..models.parents import Parent
from ..models.children import Child
from ..schemas.users import UserCreate
from ..schemas.login import Login
from sqlalchemy import create_engine, select

def get_user_by_email(db: Session, email: str):
	return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
	hashed_pw = bcrypt.hash(user.password)
	db_user = User(email=user.email, password_hash=hashed_pw, first_name=user.first_name, last_name=user.last_name, role=user.role)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	add_parent(db, db_user.id)
	return db_user


def add_parent(db: Session, user_id: str):
	db_parent = Parent( user_id=user_id)
	db.add(db_parent)
	db.commit()
	db.refresh(db_parent)
	return db_parent

def check_valid_user(details:Login,db:Session):
	hashed_pw = bcrypt.hash(details.password)

	db_user = db.query(User).filter(User.email == details.email and User.password_hash == hashed_pw).first()
	if not db_user:
		return None

	print("rashmi",db_user)
	parent = db.query(Parent).filter(Parent.user_id == db_user.id).first()
	child = db.query(Child).filter(Child.user_id == db_user.id).first()

	print("rashmi data",  parent, child)
	return {
        "id": str(db_user.id),
        "email": db_user.email,
        "role": db_user.role,
        "parentId": str(parent.id) if parent else None,
        "childId": str(child.id) if child else None,
        "firstName": db_user.first_name,
        "lastName": db_user.last_name,
        "createdAt": db_user.created_at,
        "updatedAt": db_user.updated_at,
    }

