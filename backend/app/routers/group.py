from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Group, Campus
from schemas import GroupCreate, GroupRead
from database import get_db

router = APIRouter(prefix="/groups", tags=["groups"])

@router.post("/", response_model=GroupRead)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    campus = db.query(Campus).get(group.campus_id) if group.campus_id else None
    db_group = Group(name=group.name, campus=campus)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@router.get("/", response_model=list[GroupRead])
def read_groups(db: Session = Depends(get_db)):
    return db.query(Group).all()

@router.get("/{group_id}", response_model=GroupRead)
def read_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Group).get(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

@router.put("/{group_id}", response_model=GroupRead)
def update_group(group_id: int, updated: GroupCreate, db: Session = Depends(get_db)):
    group = db.query(Group).get(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    group.name = updated.name
    group.campus_id = updated.campus_id
    db.commit()
    db.refresh(group)
    return group

@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Group).get(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(group)
    db.commit()
    return {"detail": "Group deleted"}
