from .utils import get_master
import plotly.express as px
import requests
import os
import json
import pandas as pd
import numpy as np
from .utils import MEDALS

from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")

def render_tab_club(st):

    cols = st.columns((2, 3, 3))

    with cols[0]:
        res = requests.get(f"{API_URL}/players-club")
        df = pd.DataFrame(res.json())
        st.subheader("Top 10 club representation")
        # st.markdown("<div style='height: 20px; color: white'>.<\div>", unsafe_allow_html=True)
        for i, row in df[:10].iterrows():
            st.write(MEDALS[i] if i < 3 else "&nbsp;"*5, row['club'], row['players'])


    with cols[1]:
        st.subheader('Players by club')
        club = st.selectbox('', (get_master('players', 'club')))
        res = requests.get(f"{API_URL}/players-club/{club}")
        df = pd.DataFrame(res.json())
        for i, row in df[:10].iterrows():
            st.markdown(f"<div><img style='width: 20px; margin: 10px' src='{row['flag']}'>{row['player_name']} - <strong>{row['team_name']}</strong</div>", unsafe_allow_html=True)

    with cols[2]:
        st.markdown("<div style='height: 165px; color: white'>.<\div>", unsafe_allow_html=True)
        for i, row in df[10:].iterrows():
            st.markdown(f"<div><img style='width: 20px; margin: 10px' src='{row['flag']}'>{row['player_name']} - <strong>{row['team_name']}</strong</div>", unsafe_allow_html=True)
