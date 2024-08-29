import streamlit as st
import requests

st.set_page_config(page_title='IPL Analysis 2.0')

st.sidebar.title('IPL Dashboard 2.0')
option = st.sidebar.selectbox('What do you want to know about?', ['Team','Player','Team Vs Team','Batter','Bowler'])

team_images = {
    'Chennai Super Kings': 'images/csk.jpg',
    'Deccan Chargers': 'images/dc.jpeg',
    'Delhi Capitals': 'images/dlc.png',
    'Delhi Daredevils': 'images/dd.jpg',
    'Gujarat Lions': 'images/gl.png',
    'Gujarat Titans': 'images/gt.png',
    'Kings XI Punjab': 'images/kp.png',
    'Kochi Tuskers Kerala': 'images/ktk.png',
    'Kolkata Knight Riders': 'images/kkr.png',
    'Lucknow Super Giants': 'images/lsg.png',
    'Mumbai Indians': 'images/mi.jpg',
    'Pune Warriors': 'images/pw.png',
    'Punjab Kings': 'images/pk.webp',
    'Rajasthan Royals': 'images/rr.jpg',
    'Rising Pune Supergiant': 'images/rps.jpeg',
    'Rising Pune Supergiants': 'images/rps.jpeg',
    'Royal Challengers Bangalore': 'images/rcb.jpeg',
    'Sunrisers Hyderabad': 'images/srh.png'
}

if option == 'Team':
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = sorted(response.json()['teams'])

    team = st.sidebar.selectbox('Select team', teams)

    btn = st.sidebar.button('View record')

    if btn:
        st.header(team)

        team_record = requests.get('http://127.0.0.1:5000/api/team-record?team={}'.format(team))

        st.json(team_record.json())

    

elif option == 'Player':
    response = requests.get('http://127.0.0.1:5000/api/players')
    players = sorted(response.json()['Players'])

    st.sidebar.selectbox('Select player', players)

    btn = st.sidebar.button('View record')

    if btn:
        pass

elif option == 'Team Vs Team':
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = sorted(response.json()['teams'])

    team1 = st.sidebar.selectbox('Select Team1', teams)
    team2 = st.sidebar.selectbox('Select Team2', teams)

    btn = st.sidebar.button('View record')

    if btn:
        st.subheader('{} Vs {}'.format(team1, team2))

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(team_images[team1])
        with col2:
            st.title('Vs')
        with col3:
            st.image(team_images[team2])

        response_ = requests.get('http://127.0.0.1:5000/api/teamVsTeam?team1={}&team2={}'.format(team1, team2)) 

        # st.json(response_.json())

        for i in response_.json():
            st.text(i + ' : ' + str(response_.json()[i]))

elif option == 'Batter':
    response = requests.get('http://127.0.0.1:5000/api/players')
    players = sorted(response.json()['Players'])

    st.sidebar.selectbox('Select Batter', players)

elif option == 'Bowler':
    response = requests.get('http://127.0.0.1:5000/api/players')
    players = sorted(response.json()['Players'])

    st.sidebar.selectbox('Select Bowler', players)
