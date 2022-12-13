from models.engine.db_storage import DB_Storage
from models.models import Courses
from flask import Flask, jsonify, abort, make_response, request
from flask import Blueprint
from sqlalchemy import desc
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

@courses.route('/courses/<courses_id>', methods=['DELETE'], strict_slashes=False)
def delete_course(course_id):
        """
        Deletes a user Object
        """
        course = storage.local_session.query(Courses).filter_by(id=course_id).delete(synchronize_session=False)
        if not course:
            abort(404)
        storage.save()
        return make_response(jsonify({'status' : "Succesfully deleted"}), 200)

@courses.route('/courses/popular', methods=['GET'], strict_slashes=False)
def popular():
    new_list = []
    course_list = []
    all_courses = storage.all(cls=Courses)
    for course in all_courses:
        course = course.__dict__ 
        if course['_sa_instance_state']:
            del course['_sa_instance_state']
        new_list.append(course)
    for course in new_list:
        if course["no_enrolled"] > 90:
            course_list.append(course)
    return jsonify(course_list)


@courses.route('/courses', methods=['POST'], strict_slashes=False)
def post_course():
    """
    Creates a course
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = Courses(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

