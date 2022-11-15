from models.engine.db_storage import DB_Storage
from models.models import Student
from api.views import app_views
from flask import Flask, jsonify, current_app
from flask import Blueprint

student = Blueprint('student', __name__)


storage = DB_Storage()

@student.route('/students/', methods = ['GET'], strict_slashes=False)
def get_student():
        """
        new_list = []
        all_students = storage.all(cls=Student)
        for student in all_students:
            new_list.append(student)
        """
        return ("<h1>hello<h1>")


