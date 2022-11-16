from models.models import Base
from models import models
from sqlalchemy.orm import scoped_session, sessionmaker
from models.models import Student, Instructor, Pricing, Courses, Session
import json
from datetime import datetime 

time = "%Y-%m-%dT%H:%M:%S.%f"

classes = {"Student": Student, "Instructor": Instructor,
           "Course": Courses, "Pricing": Pricing}

class DB_Storage:
    __engine = models.engine
    local_session = scoped_session(Session)
    session = local_session()
    def all(self, cls=None):
        new_dict = {}
        if cls not in classes.values():
            return None
        objs = self.local_session.query(cls).all()
        for obj in objs:
            key = obj.__class__.__name__ + '.' + obj.id
            new_dict[key] = obj
        return new_dict.values()


    def new(self, obj):
        """add the object to the current database session"""
        self.local_session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.local_session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.local_session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = self.session(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.local_session.remove()

    def get(self, id, cls):
        new_list = []
        all_data = self.all(cls)
        for data in all_data:
            data = data.__dict__ 
            del data['_sa_instance_state']
            if(data['id'] == id):
                if "created_at" in data and data["created_at"] is not None:
                    data["created_at"] = data["created_at"].strftime(time)
                if "updated_at" in data and data["updated_at"] is not None:
                    data["updated_at"] =data["updated_at"].strftime(time)
                return data