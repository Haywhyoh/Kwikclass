from models.engine.db_storage import DB_Storage
from models.models import Student
from api.views import app_views
from flask import Flask, jsonify
from flask import Blueprint
import json

student = Blueprint('student', __name__)
storage = DB_Storage()

@student.route('/students', strict_slashes=False)
def get_student():
    new_list = {}
    all_students = storage.all(cls=Student)
    for student in all_students:
        student = student.__dict__ 
        if student['_sa_instance_state']:
            del student['_sa_instance_state']
        new_list.update(student)
    return jsonify((new_list))