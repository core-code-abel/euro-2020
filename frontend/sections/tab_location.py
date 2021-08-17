from .utils import get_master
import plotly.express as px
import requests
import json
import pandas as pd
import numpy as np
from .config import API_URL

def render_tab_location(st):
    country = st.selectbox('', ['Global player location'] + (get_master('teams', 'team_name')))
    res = requests.get(f"{API_URL}/players-location{f'/{country}' if country != 'Global player location' else ''}")
    df = pd.DataFrame(res.json())
    c_lat = (df["lat"].max()+df["lat"].min())/2
    c_lon = (df["long"].max()+df["long"].min())/2
    my_map = px.scatter_mapbox(
        df,
        lat="lat",
        lon="long",
        hover_name="player_name",
        mapbox_style="carto-positron",
        zoom=1,
        center={"lat":c_lat,"lon":c_lon}
    )

    my_map.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":10,"l":120,"b":0},
        height=500
    )
    st.markdown("<div style='height: 20px; color: white'>.<\div>", unsafe_allow_html=True)
    st.plotly_chart(my_map, use_container_width=True)