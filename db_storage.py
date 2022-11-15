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
        all_students = self.all(cls)
        for student in all_students:
            student = student.__dict__ 
            del student['_sa_instance_state']
            if(student['id'] == id):
                if "created_at" in student and student["created_at"] is not None:
                    student["created_at"] = student["created_at"].strftime(time)
                if "updated_at" in student and student["updated_at"] is not None:
                    student["updated_at"] =student["updated_at"].strftime(time)
                return json.dumps(student)

    def delete_user(self, user_id):
        """
        Deletes a user Object
        """

        user = self.get(Student, user_id)


        self.delete(user)
        self.save()
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
   
    #student1 =  db.new(new_student)
    #student = db.all(Student)
    #student = db.get_student()
    #student = db.get(id='Sam', cls=Student)
    student = db.get(cls=Student, id="da6ba7d3-baaf-4b15-9965-caf2faa36b47")
    #db.local_session.query(Student).filter_by(id="da6ba7d3-baaf-4b15-9965-caf2faa36b47").delete(synchronize_session=False)
    db.save()
    #print(student)
   # print (type(student))
    db.close()
