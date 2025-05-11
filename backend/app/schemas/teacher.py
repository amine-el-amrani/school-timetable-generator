from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str
    subject_id: int

class TeacherRead(TeacherCreate):
    id: int

    class Config:
        orm_mode = True
