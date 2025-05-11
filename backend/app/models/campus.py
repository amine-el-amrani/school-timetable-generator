from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.models.base import Base

class Campus(Base):
    __tablename__ = 'campuses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)

    def __repr__(self):
        return f"<Campus(name={self.name}, location={self.location})>"
