import streamlit as st

# Team Data Import
team = open("team_names.txt", "r")
team_names = team.read()
team_name_list = team_names.split("\n")
team.close()

# Player Data Import
player_name = ["Sachin Tendulkar", "Rahul Dravid", "Virat Kohli"]
player = st.selectbox("Select Player", player_name)

st.header('Player Details')
col1, col2, col3 = st.columns(3)
col1.subheader(player)
col2.subheader("Mumbai Indians")
col3.subheader("Batsman")


# Submit Details
st.form("Player Auction Details")
with st.form(key='player_team_form'):
    team_name = st.selectbox('Team', team_name_list)
    amount = st.number_input('Amount', 1000, 100000)
    st.form_submit_button('Submit')