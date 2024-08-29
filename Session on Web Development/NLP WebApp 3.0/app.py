from flask import Flask, render_template, request, redirect, session
import db
import api

dbo = db.Database()
apio = api.API()

# session ek dictionary hota hai jisme ham store kar sakte hai

# request use hota hai html se data ko recieve karne me server ko
# render_template html files ko load karta hai

app = Flask(__name__)

# to display pages
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# to do some action
@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert_data(name, email, password)

    if response:
        return render_template('login.html', message='Registration succesful. Kindly LOGIN to proceed!')
    else:
        return render_template('register.html', message='Email already exists!')


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.verify_login(email, password)

    if response:
        # return render_template('profile.html')
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('register.html', message='Incorrect data... Login Failed!')


@app.route('/profile')
def profile():
    if session['logged_in'] == 1:
        return render_template('profile.html')
    else:
        return redirect('/')


@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    
    response = apio.NER(text)

    return render_template('ner.html', result=response)


@app.route('/Sentiment_Analysis')
def Sentiment_Analysis():
    return 'Sentiment Analysis hoga'

@app.route('/Abuse_Detection')
def Abuse_Detection():
    return 'Abuse_Detection hoga'


# jab bhi data post ke through aata hai toh hame explicitly batana padta hai
app.run(debug=True)

# html se data flask/server tak do type se jata hai:
# get : url ke through
# post : for confidential info like password (not shown on screen)

