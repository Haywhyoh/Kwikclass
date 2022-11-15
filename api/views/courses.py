from models.engine.db_storage import DB_Storage
from models.models import Courses
from flask import Flask, jsonify, abort
from flask import Blueprint
import json

courses = Blueprint('courses', __name__)
storage = DB_Storage()

@courses.route('/courses', strict_slashes=False)
def get_courses():
    new_list = []
    all_courses = storage.all(cls=Courses)
    for course in all_courses:
        course = course.__dict__ 
        if course['_sa_instance_state']:
            del course['_sa_instance_state']
        new_list.append(course)
    return jsonify((new_list))

@courses.route('/courses/<course_id>', strict_slashes=False)
def get_course(course_id):
    """ Retrieves an user """
    course = storage.get(cls=Courses, id=course_id)
    if not course:
        abort(404)
    return jsonify(course)


