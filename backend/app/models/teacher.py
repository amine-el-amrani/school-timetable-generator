from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)

    subjects = relationship("Subject", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"

