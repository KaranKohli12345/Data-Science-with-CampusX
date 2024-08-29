from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = sorted(response.json()['teams'])
    return render_template('index.html', teams=teams)

@app.route('/teamVsTeam')
def teamVsTeam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = requests.get('http://127.0.0.1:5000/api/teamVsTeam?team1={}&team2={}'.format(team1,team2))
    result = response.json()

    response_ = requests.get('http://127.0.0.1:5000/api/teams')
    teams = sorted(response_.json()['teams'])

    return render_template('index.html', result=result, teams=teams)

app.run(debug=True, port=8080)



