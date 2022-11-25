from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, SmallInteger

class Enrollment(BaseModel, Base):
    __tablename__ = 'enrollment'