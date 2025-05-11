from sqlalchemy import Column, Table, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Table de jointure entre Group et Campus
group_campus_association = Table(
    'group_campus_association',
    Base.metadata,
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True),
    Column('campus_id', Integer, ForeignKey('campuses.id'), primary_key=True)
)
