from pydantic import BaseModel

class GroupCreate(BaseModel):
    name: str
    campus_id: int | None = None  # None si le groupe est sur tous les campus

class GroupRead(GroupCreate):
    id: int

    class Config:
        orm_mode = True
