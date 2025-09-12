from sqlalchemy import func
from ..models.chore_assignments import ChoreAssignment
from ..models.chores import Chore
from ..models.users import User
from ..models.children import Child
from sqlalchemy.orm import Session
from ..schemas.dashboard import ParentDashboardOut

def get_child_dashboard(db:Session,childId:str):
    childChores=db.query(Chore).join(ChoreAssignment,Chore.id==ChoreAssignment.chore_id).filter(ChoreAssignment.child_id==childId).order_by(Chore.due_date.desc()).all()
    choresData=[]
    for chore in childChores:
        choresData.append( {
            **chore["chores"],  # spread/merge dictionary (like ...c.chores)
            "status": chore["chore_assignments"]["status"],
            "assignmentId": chore["chore_assignments"]["id"],
            "verifiedAt": chore["chore_assignments"]["verifiedAt"],
            "comments": chore["chore_assignments"]["comment"],
        })
    return choresData

def get_parent_dashboard(db:Session,parentId:str):
    result= db.query(Chore.id,                         # ← chores table included
        Chore.title,
        Chore.description,
        Chore.value,
        Chore.due_date,
        ChoreAssignment.status,           # ← joined table
        ChoreAssignment.id.label("assignmentId"),
        Child.id.label("childId"),      # ← joined table
        func.concat(User.first_name, " ", User.last_name).label("childName"),).join(ChoreAssignment,Chore.id==ChoreAssignment.chore_id).join(Child,Child.id==ChoreAssignment.child_id).join(User, Child.user_id == User.id).filter(Child.parent_id==parentId).all()
    
    parent_dashboard = [
        ParentDashboardOut(
            id=res.id,
            title=res.title,
            description=res.description,
            value=res.value,
            dueDate=res.dueDate,
            assignmentId=res.assignmentId,
            childId=res.childId,
            childName=res.childName,
            status=res.status
        )
        for res in result
    ]
    return parent_dashboard