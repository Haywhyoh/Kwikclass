from models.engine.db_storage import DB_Storage
from models.models import Student
from flask import Flask, jsonify, abort
from flask import Blueprint
import json

student = Blueprint('student', __name__)
storage = DB_Storage()

@student.route('/students', strict_slashes=False)
def get_students():
    new_list = []
    all_students = storage.all(cls=Student)
    for student in all_students:
        student = student.__dict__ 
        if student['_sa_instance_state']:
            del student['_sa_instance_state']
        new_list.append(student)
    return jsonify((new_list))

@student.route('/students/<student_id>', strict_slashes=False)
def get_student(student_id):
    """ Retrieves an user """
    student = storage.get(cls=Student, id=student_id)
    if not student:
        abort(404)
    return jsonify(student)

    

