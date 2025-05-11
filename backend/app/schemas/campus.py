from pydantic import BaseModel

class CampusCreate(BaseModel):
    name: str

class CampusRead(CampusCreate):
    id: int

    class Config:
        orm_mode = True
