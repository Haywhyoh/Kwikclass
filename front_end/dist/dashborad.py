from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
courses = requests.get("http://127.0.0.1:5000/api/courses").json()

@app.route('/overview', strict_slashes=False)
def dashboard():
    return render_template('overview.html')

@app.route('/courses', strict_slashes=False)
def courses_route():
    # courses = requests.get("http://127.0.0.1:5000/api/courses").json()
    return render_template('courses.html', courses=courses)

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)


def home():
    new_list = []
    for course in courses:
        if course['no_enrolled'] >= 90:
            new_list.append(course)
    return render_template( 'index.html', courses=new_list)

@app.route('/login',  strict_slashes=False )
def login():
    return render_template('login.html')

@app.route('/signup',  strict_slashes=False )
def signup():
    return render_template('signup.html')

@app.route('/course_page', strict_slashes=False)
def course_page():
    return render_template('course_page.html', courses=courses)

@app.route('/checkout', strict_slashes=False)
def cart_page():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(port=5500, debug=True)
