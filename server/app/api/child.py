
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import router
from ..crud.child import check_existing_child,create_child,get_children_details,update_child,delete_child
from ..schemas.child import CreateChildOut,CreateChild

@router.post("/createchild",response_model=CreateChildOut)
def add_child(child:CreateChild,db:Session=Depends(get_db)):
    #check if child already exists
    isExisting=check_existing_child(db,child.email)
    if isExisting:
        raise HTTPException(status_code=400, detail="child already exists")
    return create_child(db, child)

@router.get("/getchildrenwithdetails/{parentId}",response_model=list[CreateChildOut])
def get_children_details(parentId:str,db:Session=Depends(get_db)):
    if not parentId:
        raise HTTPException(status_code=400, detail="Parent Id not present")
    return get_children_details(db,parentId)

@router.put("/updatechild",response_model=CreateChildOut)
def update_child(child:CreateChild,db:Session=Depends(get_db)):
    return update_child(db,child)


@router.delete("/deletechild/{id}",response_model=CreateChildOut)
def delete_child(id:str,db:Session=Depends(get_db)):
    return delete_child(db,id)
