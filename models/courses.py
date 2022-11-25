from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, Text
from sqlalchemy.orm import relationship
from models.student import Student
class Courses:
    __tablename__ = 'courses'
    title = Column(Text(), nullable=True)
    no_of_reviews = Column(SmallInteger(), default=0)
    no_erolled = Column(SmallInteger(), default=0)
    banner_link = Column(String, nullable=False)
    category = Column(String(), nullable=False)
    no_of_sections = Column(SmallInteger(), nullable=False)
    no_of_lectures = Column(SmallInteger(), nullable=False)
    estimated_time = Column(SmallInteger(), nullable=False)
    course_desc = Column(Text(), nullable=False)
    no_of_document = Column(SmallInteger(), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    updated_at = Column(DateTime(), nullable=False)
    pricing = relationship("Pricing")
    student = relationship(Student,secondary='enrollment')

