from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Teacher, Subject, Group
from schemas import TeacherCreate, TeacherRead
from database import get_db

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.post("/", response_model=TeacherRead)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    subject = db.query(Subject).get(teacher.subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    db_teacher = Teacher(name=teacher.name, subject=subject)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@router.get("/", response_model=list[TeacherRead])
def read_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()

@router.get("/{teacher_id}", response_model=TeacherRead)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).get(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.put("/{teacher_id}", response_model=TeacherRead)
def update_teacher(teacher_id: int, updated: TeacherCreate, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).get(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    subject = db.query(Subject).get(updated.subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    teacher.name = updated.name
    teacher.subject_id = updated.subject_id
    db.commit()
    db.refresh(teacher)
    return teacher

@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).get(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(teacher)
    db.commit()
    return {"detail": "Teacher deleted"}
