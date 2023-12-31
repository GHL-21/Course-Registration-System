import re
from flask import Flask, request, render_template, redirect, url_for
from .db import connection

app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route("/register", methods =["GET", "POST"])
def register():
    msg = ""
    cursor = connection.cursor()

    if request.method == "POST" and "username" in request.form and "password" in request.form and "email" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        cursor.execute("SELECT * FROM user WHERE name = ?", (username,))
        account = cursor.fetchone()

        if account:
            msg = "Account already exists"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "Username must contain only characters and numbers"
        elif not username or not password or not email:
            msg = "Please fill out the form"
        else:
            # People are automatically made not an admin, the type is set to STUDENT
            cursor.execute(
                "INSERT INTO user (name, password, email, type) VALUES (?, ?, ?, 'STUDENT')",
                (username, password, email)
            )
            connection.commit()
            msg = "You have successfully registered"

    elif request.method == "POST":
        msg = "Please fill out the form"

    return render_template("register.html", msg = msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

@app.route("/create-course", methods=["GET", "POST"])
def create_course():
    msg = ""
    # cursor = connection.cursor()

    # if request.method == "POST":
        # pass

    return render_template("create_course.html", msg = msg)
