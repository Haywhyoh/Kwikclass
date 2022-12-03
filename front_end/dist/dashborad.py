from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/overview', strict_slashes=False)
def dashboard():
    return render_template('overview.html')

@app.route('/courses', strict_slashes=False)
def courses_route():
    return render_template('courses.html')

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    return render_template('index.html')

@app.route('/login',  strict_slashes=False )
def login():
    return render_template('login.html')

@app.route('/signup',  strict_slashes=False )
def signup():
    return render_template('signup.html')
if __name__ == "__main__":
    app.run(debug=True)
