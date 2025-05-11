from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Campus
from schemas import CampusCreate, CampusRead
from database import get_db

router = APIRouter(prefix="/campuses", tags=["campuses"])

@router.post("/", response_model=CampusRead)
def create_campus(campus: CampusCreate, db: Session = Depends(get_db)):
    db_campus = Campus(name=campus.name)
    db.add(db_campus)
    db.commit()
    db.refresh(db_campus)
    return db_campus

@router.get("/", response_model=list[CampusRead])
def read_campuses(db: Session = Depends(get_db)):
    return db.query(Campus).all()

@router.get("/{campus_id}", response_model=CampusRead)
def read_campus(campus_id: int, db: Session = Depends(get_db)):
    campus = db.query(Campus).get(campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    return campus

@router.put("/{campus_id}", response_model=CampusRead)
def update_campus(campus_id: int, updated: CampusCreate, db: Session = Depends(get_db)):
    campus = db.query(Campus).get(campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    campus.name = updated.name
    db.commit()
    db.refresh(campus)
    return campus

@router.delete("/{campus_id}")
def delete_campus(campus_id: int, db: Session = Depends(get_db)):
    campus = db.query(Campus).get(campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    db.delete(campus)
    db.commit()
    return {"detail": "Campus deleted"}
