from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, SmallInteger


class instructor(Base):
    __tablename__ = 'instructor'
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email = Column(String(), unique=True)
    no_of_courses = Column(SmallInteger(), defailt=0)
    total_earning = Column(SmallInteger(), default=0)
    country = Column(String(), nullable=False)
    sex = Column(String(), nullable=False)
    date_of_birth = Column(DateTime(), nullable=False)
    profile_picture = Column(String(), unique=True)
