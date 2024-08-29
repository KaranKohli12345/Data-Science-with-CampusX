from flask import Flask, render_template, request
from db import Database

app = Flask(__name__) # object of Flask class

dbo = Database()

def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=["post"])
def perform_registration():
    name = request.form.get("user'sName")
    email = request.form.get("user'sName")
    password = request.form.get("user'sPassword")

    response = dbo.insert(name, email, password)

    if response:
        return "Registration successfull."
    else:
        return "Email exists."

app.run(debug=True)

