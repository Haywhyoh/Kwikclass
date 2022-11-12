from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, String, Integer, SmallInteger, Text, DateTime, ForeignKey, Table, Boolean
from datetime import datetime

Base = declarative_base()

user = 'kwikclass_admin'
password = 'Mydreams98'
host = '127.0.0.1'
port = 3306
database = 'kwikclass_db'

engine=create_engine(url="mysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
            ), echo=True)

class BaseModel():
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Student(BaseModel, Base):
    __tablename__ = 'student'
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    active_courses = Column(Integer())
    certificate_earned = Column(Integer())
    course_enrolled = Column(Integer())
    hours_watched = Column(Integer())
    country = Column(String(20), nullable=False)
    sex = Column(String(10), nullable=False)
    date_of_birth = Column(DateTime(), nullable=False)
    schedules = Column(Integer())
    email = Column(String(60), unique=True)
    profile_picture = Column(String(50), unique=True)
    courses = relationship('Courses',secondary='enrollment')

class Instructor(BaseModel, Base):
    __tablename__ = 'instructor'
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email = Column(String(60), unique=True)
    no_of_courses = Column(SmallInteger(), default=0)
    total_earning = Column(SmallInteger(), default=0)
    country = Column(String(20), nullable=False)
    sex = Column(String(10), nullable=False)
    date_of_birth = Column(DateTime(), nullable=False)
    profile_picture = Column(String(50), unique=True)
    courses = relationship('Courses',secondary='created')


class Courses(BaseModel, Base):
    __tablename__ = 'courses'
    title = Column(Text(), nullable=True)
    no_of_reviews = Column(SmallInteger(), default=0)
    no_erolled = Column(SmallInteger(), default=0)
    banner_link = Column(String(50), nullable=False)
    category = Column(String(15), nullable=False)
    no_of_sections = Column(SmallInteger(), nullable=False)
    no_of_lectures = Column(SmallInteger(), nullable=False)
    estimated_time = Column(SmallInteger(), nullable=False)
    course_desc = Column(Text(), nullable=False)
    no_of_document = Column(SmallInteger(), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    updated_at = Column(DateTime(), nullable=False)
    pricing = relationship("Pricing")
    student = relationship(Student,secondary='enrollment')
    instructors = relationship(Instructor,secondary='created')


class Enrollment(BaseModel, Base):
    __tablename__ = 'enrollment'
    course_id = Column(String(60), ForeignKey('courses.id'), primary_key = True)
    student_id = Column(String(60), ForeignKey('student.id'), primary_key=True)

class Pricing(Base, BaseModel):
    __tablename__ = 'course_pricing'
    base_price = Column(SmallInteger(), nullable=False)
    promo_price = Column(SmallInteger())
    paid = Column(Boolean(), nullable=False)
    course_id = Column(String(60), ForeignKey("courses.id"))

class Created(Base):
    __tablename__ = 'created'
    course_id = Column(String(60), ForeignKey('courses.id'), primary_key = True)
    instructor_id = Column(String(60), ForeignKey('instructor.id'), primary_key=True)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
