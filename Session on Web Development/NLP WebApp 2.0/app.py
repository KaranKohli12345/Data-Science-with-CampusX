from flask import Flask, render_template, request, redirect
from db import Database
import api

app = Flask(__name__)

dbo = Database()

@app.route('/') # decorator -> a kind of url
def index(): # we can name the function anything
    # return "<h1 style='color:yellow'>Hello World!</h1>" 
    # return me HTML file hota hai jo client ko show karna hai
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert_data(name, email, password)

    if response:
        return render_template('login.html', message='Registration successful, kindly login')
    else:
        return render_template('register.html', message='Email already exists!')
    
@app.route('/perform_login', methods=['post'])
def login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.verify(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect data!')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_ka_text')

    response = api.ner(text)
    return render_template('ner.html', result=response)

# html se data flask/server tak do type se jata hai:
# get : url ke through
# post : for confidential info like password (not shown on screen)

app.run(debug=True)
