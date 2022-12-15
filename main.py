import streamlit as st
import pandas as pd

# Team Data Import
team = open("team_names.txt", "r")
team_names = team.read()
team_name_list = team_names.split("\n")
team.close()

# Player Data Import
player_info = pd.read_csv("player_details.csv")
player_name = player_info["Player Name"]
st.subheader("All Players List")
st.write(player_info)
st.write('---')

index = st.selectbox("Select Player", range(len(player_name)), format_func=lambda x: player_name[x])

# Player data from forms
player_name = player_info.iat[index, 0]
player_team = player_info.iat[index, 1]
player_skills = player_info.iat[index, 2]

# Display player info
co1, co2 = st.columns([1, 2])
co1.image('sachin.jpg')
co2.header(player_name)

col1, col2, col3 = st.columns(3)
col2.subheader(player_team)
col3.subheader(player_skills)

# Submit player auction details
st.form("Player Auction Details", clear_on_submit=True)
with st.form(key='player_team_form'):
    team_name = st.selectbox('Team', team_name_list)
    amount = st.number_input('Amount', 1000, 100000)
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.balloons()