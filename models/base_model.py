from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, SmallInteger, Text, DateTime, ForeignKey, Table
from datetime import datetime

Base = declarative_base()

user = 'kwikclass_admin'
password = 'Mydreams98'
host = '127.0.0.1'
port = 3306
database = 'kwikclass_db'

pricing_association_table = Table(
    "Pricing",
    Base.metadata,
    Column("student_id", ForeignKey("Students.id"), primary_key=True),
    Column("course_id", ForeignKey("Courses.id"), primary_key=True),
)

engine=create_engine(url="mysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
            ), echo=True)

class BaseModel():
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    

