import streamlit as st
import pandas as pd
from drive_image import download_file_from_google_drive

st.set_page_config(
    "Auction Platform",
    "💰",
    initial_sidebar_state="collapsed",
    layout="centered",
)
# Event Logos
c1, c2, c3 = st.columns(3)
c1.image("./event-img/jito-1.png")
c2.image("./event-img/jpl-logo.png")
c3.image("./event-img/jito-3.png")

# Team Data Import
team = open("./data/team_names.txt", "r")
team_names = team.read()
team_name_list = team_names.split("\n")
team.close()

# Player Data Import
player_info = pd.read_csv("./data/jito-4-team-list.csv")
player_name_all = player_info["Name"]
with st.expander("All Players List"):
    st.write(player_info.iloc[:, [1, 3, 8, 9, 10, 11]])

index = st.selectbox("Select Player", range(len(player_name_all)), format_func=lambda x: player_name_all[x])

# Player data from forms
player_name = player_info.iat[index, 1]
player_age = player_info.iat[index, 3]
player_specialist = player_info.iat[index, 8]
player_batsman = player_info.iat[index, 9]
player_bowler = player_info.iat[index, 10]
player_played_before = player_info.iat[index, 11]
player_image = player_info.iat[index, 14]

# Display player info
if player_played_before == "Yes":
    st.success("Player Played Before")
else:
    st.error("Not Played Before")


# Parse URL
from urllib.parse import urlparse

link = urlparse(player_image)
image_id = link.query[3:]

# Download all image files
destination = './img/{}-{}.jpg'.format(index, player_name)

# Run this line only once
#download_file_from_google_drive(image_id, destination)

co1, co2, co3, co4 = st.columns([1, 1, 2, 1])
co1.image(destination)
co2.write("Category")
co3.header(player_name)
co4.header(player_age)

col1, col2, col3 = st.columns(3)
col1.subheader(player_specialist)
col2.subheader(player_batsman)
col3.subheader(player_bowler)

# Submit player auction details
st.form("Player Auction Details", clear_on_submit=True)
with st.form(key='player_team_form'):
    team_name = st.selectbox('Team', team_name_list)
    amount = st.number_input('Amount', 1000, 100000)
    submitted = st.form_submit_button('Submit')
    if submitted:
        print(player_info.append())
        st.balloons()

# Built By

st.markdown('<div style="text-align: center">Made with ❤️ by <a href="https://hirawat.in">Vishal Hirawat</a></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Made with ❤️ by [Vishal Hirawat](https://hirawat.in)")
    st.image("./hirawat-tech-500-logo.png")