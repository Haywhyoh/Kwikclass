from flask import Flask
from api.views import app_views
from flask import jsonify, make_response
from models.engine.db_storage import DB_Storage

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.teardown_appcontext
def close_db(error):
    DB_Storage.close()

@app.route('/status')
def status():
    return jsonify({'staus' : "OK"})

@app.errorhandler
def not_found(error):
    make_response(jsonify({'error':"Not Found"}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)