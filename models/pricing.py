from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Boolean, SmallInteger, ForeignKey

class Enrollment(Base, BaseModel):
    __tablename__ = 'course_pricing'
    base_price = Column(SmallInteger(), nullable=False)
    promo_price = Column(SmallInteger())
    paid = Column(Boolean(), nullable=False)
    course_id = Column(Integer, ForeignKey("Courses.id"))