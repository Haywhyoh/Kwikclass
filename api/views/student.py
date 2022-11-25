from models.engine.db_storage import DB_Storage
from models.models import Student
from flask import jsonify, abort, make_response, request
from flask import Blueprint


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

@student.route('/students/<student_id>',  methods=['GET'], strict_slashes=False)
def get_student(student_id):
    """ Retrieves an user """
    student = storage.get(cls=Student, id=student_id)
    if not student:
        abort(404)
    return jsonify(student)

@student.route('/students/<student_id>', methods=['DELETE'], strict_slashes=False)
def delete_student(student_id):
        """
        Deletes a user Object
        """
        student = storage.local_session.query(Student).filter_by(id=student_id).delete(synchronize_session=False)
        if not student:
            abort(404)
        storage.save()
        return make_response(jsonify({'status' : "Succesfully deleted"}), 200)

@student.route('/students', methods=['POST'], strict_slashes=False)
def post_student():
    """
    Creates a student
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = Student(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

