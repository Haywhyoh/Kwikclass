from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, SmallInteger, Text, DateTime, ForeignKey, Table, Boolean
from datetime import datetime
import uuid

Base = declarative_base()

user = 'kwikclass_admin'
password = 'Mydreams98'
host = '127.0.0.1'
port = 3306
database = 'kwikclass_db'

engine=create_engine(url="mysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
            ), echo=True)

Session=sessionmaker(bind=engine, expire_on_commit=False)
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def to_dict(self):
        new_dict = {}
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

class Student(BaseModel, Base):
    __tablename__ = 'student'
    user_name =Column(String(60), nullable=False)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    active_courses = Column(Integer())
    certificate_earned = Column(Integer())
    course_enrolled = Column(Integer())
    hours_watched = Column(Integer())
    country = Column(String(40), nullable=False)
    sex = Column(String(15), nullable=False)
    date_of_birth = Column(String(10), nullable=False)
    schedules = Column(Integer())
    email = Column(String(60), unique=True)
    profile_picture = Column(String(50))
    courses = relationship('Courses',secondary='enrollment', back_populates='parents')

    def __repr__(self):
        return f"Student: {self.first_name} , {self.last_name}, {self.active_courses}, {self.certificate_earned},{self.course_enrolled}, {self.hours_watched}, {self.country}, {self.sex}, {self.date_of_birth}, {self.schedules}, {self.email}, {self.profile_picture}"

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

class Instructor(BaseModel, Base):
    __tablename__ = 'instructor'
    user_name =Column(String(60), nullable=False)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email = Column(String(60), unique=True)
    no_of_courses = Column(SmallInteger(), default=0)
    total_earning = Column(SmallInteger(), default=0)
    country = Column(String(40), nullable=False)
    sex = Column(String(15), nullable=False)
    date_of_birth = Column(String(10), nullable=False)
    profile_picture = Column(String(50), unique=True)
    courses = relationship('Courses',secondary='created', back_populates='parents')


class Courses(BaseModel, Base):
    __tablename__ = 'courses'
    title = Column(Text(), nullable=True)
    no_of_reviews = Column(SmallInteger(), default=0)
    no_enrolled = Column(SmallInteger(), default=0)
    banner_link = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    no_of_sections = Column(SmallInteger(), nullable=False)
    no_of_lectures = Column(SmallInteger(), nullable=False)
    estimated_time = Column(SmallInteger(), nullable=False)
    course_desc = Column(Text(), nullable=False)
    no_of_document = Column(SmallInteger(), nullable=False)
    pricing = relationship("Pricing", uselist=False, back_populates="parent", cascade="all, delete")
    student = relationship(Student,secondary='enrollment', back_populates='children')
    instructors = relationship(Instructor,secondary='created', back_populates='children')


class Enrollment(BaseModel, Base):
     __tablename__ = 'enrollment'
     course_id = Column(String(60), ForeignKey('courses.id'), primary_key = True)
     student_id = Column(String(60), ForeignKey('student.id'), primary_key=True)

class Pricing(Base, BaseModel):
    __tablename__ = 'course_pricing'
    base_price = Column(SmallInteger(), nullable=False)
    promo_price = Column(SmallInteger())
    paid = Column(Boolean(), nullable=False)
    course_id = Column(String(60), ForeignKey("courses.id", ondelete="CASCADE"))
    course = relationship("Courses", back_populates='child')

class Created(Base):
    __tablename__ = 'created'
    course_id = Column(String(60), ForeignKey('courses.id'), primary_key = True)
    instructor_id = Column(String(60), ForeignKey('instructor.id'), primary_key=True)

# enrollment = Table('enrollment', Base.metadata,
#                     course_id = Column(String(60), ForeignKey('courses.id'), primary_key = True),
#                     student_id = Column(String(60), ForeignKey('student.id'), primary_key=True))

# created =  Table('created', Base.metadata,
#     course_id = Column(String(60), ForeignKey('courses.id'), primary_key = True),
#     instructor_id = Column(String(60), ForeignKey('instructor.id'), primary_key=True))

Base.metadata.create_all(engine)

if "__init__" == "__main__":
    Base.metadata.create_all(engine)