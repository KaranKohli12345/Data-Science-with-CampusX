import streamlit as st
import requests

st.set_page_config(page_title='IPL Analysis 2.0')

st.sidebar.title('IPL Dashboard 2.0')
option = st.sidebar.selectbox('What do you want to know about?', ['Team', 'Team Vs Team','Batter','Bowler'])

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
        col1, col2 = st.columns(2)
        with col1:
            st.header(team)
        with col2:
            st.image(team_images[team])

        team_record_ = requests.get('http://127.0.0.1:5000/api/team-record?team={}'.format(team))

        team_record = team_record_.json()

        st.subheader('Overall record')
        for i in team_record[team]['overall']:
            st.text(i + ' : ' + str(team_record[team]['overall'][i]))

        st.subheader('Against every team')
        for i in team_record[team]['against']:
            st.text(i + ' : ' + str(team_record[team]['against'][i]))


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

    batter = st.sidebar.selectbox('Select Batter', players)

    btn = st.sidebar.button('View record')

    if btn:
        col1, col2 = st.columns(2)
        with col1:
            st.header(batter)
        # with col2:
        #     st.image(team_images[team])

        response = requests.get('http://127.0.0.1:5000/api/batter-record?batsman={}'.format(batter))

        batter_record = response.json()

        st.subheader('Overall record')
        for i in batter_record[batter]['all']:
            st.text(i + ' : ' + str(batter_record[batter]['all'][i]))

        st.subheader('Against every team')
        for i in batter_record[batter]['against']:
            st.text(i + ' : ' + str(batter_record[batter]['against'][i]))

elif option == 'Bowler':
    response = requests.get('http://127.0.0.1:5000/api/players')
    players = sorted(response.json()['Players'])

    bowler = st.sidebar.selectbox('Select Bowler', players)

    btn = st.sidebar.button('View record')

    if btn:
        col1, col2 = st.columns(2)
        with col1:
            st.header(bowler)
        # with col2:
        #     st.image(team_images[team])

        response = requests.get('http://127.0.0.1:5000/api/bowler-record?bowler={}'.format(bowler))

        bowler_record = response.json()

        st.subheader('Overall record')
        for i in bowler_record[bowler]['all']:
            st.text(i + ' : ' + str(bowler_record[bowler]['all'][i]))

        st.subheader('Against every team')
        for i in bowler_record[bowler]['against']:
            st.text(i + ' : ' + str(bowler_record[bowler]['against'][i]))

            