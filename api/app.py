from flask import Flask
from api.views import app_views
from flask import jsonify, make_response
from models.engine.db_storage import DB_Storage
from api.views.student import student
from api.views.courses import courses
from api.views.instructor import instructor
storage = DB_Storage()

app = Flask(__name__)
app.register_blueprint(app_views)
app.register_blueprint(student, url_prefix="/api")
app.register_blueprint(courses, url_prefix="/api")
app.register_blueprint(instructor, url_prefix="/api")


@app.teardown_appcontext
def close_db(error):
    storage.close()

@app.route('/status')
def status():
    return jsonify({'staus' : "OK"})

@app.errorhandler
def not_found(error):
    make_response(jsonify({'error':"Not Found"}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)