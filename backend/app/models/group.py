from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base
class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String)  # Exemple : "BTS 1ère année"
    campus_ids = Column(String)  # Liste des campus

    campuses = relationship("Campus", secondary="group_campus_association")
    subjects = relationship("Subject", back_populates="group")  # Ajout de la relation avec Subject

    def __repr__(self):
        return f"<Group(name={self.name}, level={self.level}, campus_ids={self.campus_ids})>"

