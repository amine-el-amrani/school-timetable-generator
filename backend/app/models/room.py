from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    campus_id = Column(Integer, ForeignKey('campuses.id'))

    campus = relationship("Campus", back_populates="rooms")

    def __repr__(self):
        return f"<Room(name={self.name}, capacity={self.capacity}, campus_id={self.campus_id})>"
