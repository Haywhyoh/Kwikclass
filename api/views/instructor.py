from models.engine.db_storage import DB_Storage
from models.models import Instructor
from flask import Flask, jsonify
from flask import Blueprint
import json

instructor = Blueprint('instructor', __name__)
storage = DB_Storage()

@instructor.route('/instructors', strict_slashes=False)
def get_instructor():
    new_list = {}
    all_instructors = storage.all(cls=Instructor)
    for instructor in all_instructors:
        instructor = instructor.__dict__ 
        if instructor['_sa_instance_state']:
            del instructor['_sa_instance_state']
        new_list.update(instructor)
    return jsonify((new_list))