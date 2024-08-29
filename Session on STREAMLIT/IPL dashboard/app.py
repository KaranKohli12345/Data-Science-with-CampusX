import streamlit as st
import pandas as pd

ipl = pd.read_csv(r'csv\ipl-matches.csv')

st.set_page_config(page_title='IPL Analysis')

st.sidebar.title('IPL Analysis')
option = st.sidebar.selectbox('Select one', ['Teams','Players'])

team_images = {
    'Chennai Super Kings': ['Images/csk1.jpeg', 'Images/csk2.jpeg'],
    'Deccan Chargers': ['Images/dc1.jpeg', 'Images/dc2.jpeg'],
    'Delhi Capitals': ['Images/dlc1.jpeg', 'Images/dlc2.jpeg'],
    'Delhi Daredevils': ['Images/dd1.webp', 'Images/dd2.jpeg'],
    'Gujarat Lions': ['Images/gl1.webp', 'Images/gl2.png'],
    'Gujarat Titans': ['Images/gt1.jpeg', 'Images/gt2.jpeg'],
    'Kings XI Punjab': ['Images/kp1.jpeg', 'Images/kp2.jpeg'],
    'Kochi Tuskers Kerala': ['Images/ktk1.jpeg', 'Images/ktk2.webp'],
    'Kolkata Knight Riders': ['Images/kkr1.jpeg', 'Images/kkr2.jpeg'],
    'Lucknow Super Giants': ['Images/lsg1.jpeg', 'Images/lsg2.jpeg'],
    'Mumbai Indians': ['Images/mi1.jpeg', 'Images/mi2.jpeg'],
    'Pune Warriors': ['Images/pw1.jpeg', 'Images/pw2.jpeg'],
    'Punjab Kings': ['Images/pk1.jpeg', 'Images/pk2.jpeg'],
    'Rajasthan Royals': ['Images/rr1.png', 'Images/rr2.jpeg'],
    'Rising Pune Supergiant': ['Images/rps1.jpeg', 'Images/rps2.jpeg'],
    'Rising Pune Supergiants': ['Images/rps1.jpeg', 'Images/rps2.jpeg'],
    'Royal Challengers Bangalore': ['Images/rcb1.jpeg', 'Images/rcb2.jpeg'],
    'Sunrisers Hyderabad': ['Images/srh1.png', 'Images/srh2.jpeg']
}

if option == 'Teams':
    team = st.sidebar.selectbox('Select team',sorted(set(list(ipl['Team1']) + list(ipl['Team2']))))
    btn1 = st.sidebar.button('Submit')

    if btn1:
        st.title(team)

        col1, col2 = st.columns(2)
        with col1:
            st.image(team_images[team][0])
        with col2:
            st.image(team_images[team][1])

        

elif option == 'Players':
    # dekhna baaki hai abhi
    player_columns = ['Player_of_Match', 'Team1Players', 'Team2Players']
    players = set()
    for column in player_columns:
        if column in ipl.columns:
            players.update(ipl[column].dropna().unique())
    player_list = sorted(players)
    
    player = st.sidebar.selectbox('Select player',player_list)
    btn2 = st.sidebar.button('Submit')

    if btn2:
        st.title(player)







