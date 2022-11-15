from models.models import Base
from models import models
from sqlalchemy.orm import scoped_session, sessionmaker
from models.models import Student, Instructor, Pricing, Courses, Session
import json

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
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

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
        all_students = self.all(cls)
        for student in all_students:
            student = student.__dict__ 
            del student['_sa_instance_state']
            if(student['id'] == id):
                return json.dumps(student)

if __name__ == "__main__":

    obj = {
        'first_name' : "Ayo",
        'last_name' : "Sam", 
        'active_courses' : 3,
        'certificate_earned' : 5,
        'course_enrolled' : 23,
        'hours_watched' : 65,
        'country' : "Ngeria",
        'sex' : "Male",
        'date_of_birth' : "3/1/1994",
        'schedules' : 2,
        'email' : "adefeyisayo@gmail.com",
        'profile_picture' : "wwwjioajovjavpajdvja"
    }
    new_student = Student(first_name= "Ayo",
        last_name = "Sam",
        active_courses = 3,
        certificate_earned = 5,
        course_enrolled = 23,
        hours_watched = 65,
        country = "Ngeria",
        sex = "Male",
        date_of_birth = "3/1/1994",
        schedules = 2,
        email  = "adefeyisayo@gmail.com",
        profile_picture  = "wwwjioajovjavpajdvja")
    db = DB_Storage()
    #student = db.all(Student)
    #student = db.get_student()
    student = db.get(id='af51479d-6c82-41f2-ac9b-00b2e93322d8', cls=Student)
    print(student)
    print (type(student))
    db.close()
