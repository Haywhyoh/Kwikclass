from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, SmallInteger
from sqlalchemy.orm import relationship
from models.courses import Courses
from models.base_model import engine

class Student(BaseModel, Base):
    __tablename__ = 'student'
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    active_courses = Column(Integer())
    certificate_earned = Column(Integer())
    course_enrolled = Column(Integer())
    hours_watched = Column(Integer())
    country = Column(String(), nullable=False)
    sex = Column(String(), nullable=False)
    date_of_birth = Column(DateTime(), nullable=False)
    schedules = Column(Integer())
    email = Column(String(), unique=True)
    profile_picture = Column(String(), unique=True)
    courses = relationship(Courses,secondary='enrollment')

if __name__ == "__main__":
    Base.metadata.create_all(engine)
