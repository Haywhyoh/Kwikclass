from models.engine.db_storage import DB_Storage
from models.models import Instructor
from flask import Flask, jsonify, abort, make_response, request
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

@instructor.route('/instructors/<instructor_id>', methods=['DELETE'], strict_slashes=False)
def delete_instructor(instructor_id):
        """
        Deletes a user Object
        """
        instructor = storage.local_session.query(instructor).filter_by(id=instructor_id).delete(synchronize_session=False)
        if not instructor:
            abort(404)
        storage.save()
        return make_response(jsonify({'status' : "Succesfully deleted"}), 200)

@instructor.route('/instructors', methods=['POST'], strict_slashes=False)
def post_instructor():
    """
    Creates a instructor
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = Instructor(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)