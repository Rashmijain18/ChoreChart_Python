from fastapi import  Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import router
from ..crud.dashboard import get_child_dashboard,get_parent_dashboard
from ..schemas.dashboard import ParentDashboardOut,ChildDashboardOut
from typing import List

@router.get("/childdashboard/{childId}",response_model=List[ChildDashboardOut])
def get_child_dashboard_details(childId:str, db: Session = Depends(get_db)):
    if not childId:
        raise HTTPException(status_code=400, detail="Access denied. Not a child account.")
    return get_child_dashboard(db,childId)
 
@router.get("/parentdashboard/{parentId}",response_model=List[ParentDashboardOut] )
def get_parent_dashboard_details(parentId:str, db: Session = Depends(get_db)):
    if not parentId:
        raise HTTPException(status_code=400, detail="Access denied. Not a parent account.")
    return get_parent_dashboard(db,parentId)
   
 