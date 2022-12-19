import streamlit as st
import pandas as pd

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
player_name = player_info["Name"]
#st.subheader("All Players List")
#st.write(player_info)
#st.write('---')

index = st.selectbox("Select Player", range(len(player_name)), format_func=lambda x: player_name[x])

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


co1, co2, co3 = st.columns([1, 2, 1])
co1.image(player_image)
co2.header(player_name)
co3.header(player_age)

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
        st.balloons()

import requests
import pandas as pd

# Parse URL
from urllib.parse import urlparse

image_url = "https://drive.google.com/open?id=1a_MTMISVup-7c22tpmnrRolp4z8TP7RO"
link = urlparse(image_url)
st.write(link.query)
new_url = "https://drive.google.com/file/d/{}/".format(link.query)
st.write(new_url)

r = requests.get(new_url)
#st.write(r.content)
import gdown

id = link.query
output = "./img/{}.jpeg".format(player_name[0:4])
gdown.download(url=image_url, output=output, quiet=False)