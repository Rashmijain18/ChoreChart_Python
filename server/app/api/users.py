from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.users import UserCreate, UserOut
from ..schemas.login import Login, LoginOut
from ..crud.users import create_user, get_user_by_email
from ..database import get_db
from . import router
from ..crud.users import check_valid_user
from ..schemas.login import LoginData


@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)


@router.post("/login",response_model=LoginOut)
def login_user(details:Login,db:Session=Depends(get_db)):
    user=check_valid_user(details,db)
    print("conso",user)
    if not user:
        raise HTTPException(status_code=400,detail="Invalid credentials")
    return LoginOut(data=user, success=True)