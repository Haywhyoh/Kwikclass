from models.engine.db_storage import DB_Storage
from models.models import Instructor
from flask import Flask, jsonify, abort
from flask import Blueprint
import json

instructor = Blueprint('instructor', __name__)
storage = DB_Storage()

@instructor.route('/instructors', strict_slashes=False)
def get_instructors():
    new_list = []
    all_instructors = storage.all(cls=Instructor)
    for instructor in all_instructors:
        instructor = instructor.__dict__ 
        if instructor['_sa_instance_state']:
            del instructor['_sa_instance_state']
        new_list.append(instructor)
    return jsonify((new_list))

@instructor.route('/instructors/<instructor_id>', strict_slashes=False)
def get_instructor(instructor_id):
    """ Retrieves an instructor """
    instructor = storage.get(cls=Instructor, id=instructor_id)
    if not instructor:
        abort(404)
    return jsonify(instructor)


