import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
from ._404 import render_404
from .utils import get_master, MEDALS

from dotenv import load_dotenv
load_dotenv()


API_URL = os.getenv("API_URL")
print ('-----------------', API_URL)
def render_tab_events(st):
    body = st.columns((1, 2, 2, 1))
    masters = get_master('events', 'type')
    with body[1]:
        st.subheader("Event Type")
        events = sorted(masters + ['Substitution IN', 'Substitution OUT'])
        events.remove('Substitution')
        event_type = st.selectbox('', events)
        player = False
        if event_type != "Disallowed goal":
            player = st.checkbox("Player")
    with body[2]:
        st.subheader("Team")
        team = st.selectbox('', ['All'] + (get_master('teams', 'team_name') if player else []))
        st.empty()

    body = st.columns((1, 10, 1, 6, 12, 1))

    section = "events"
    if player and team != 'All':
        section += f'-team/{team}'
    if player and team == 'All':
        section += f'-player'
    player_selector = ''
    if event_type in ['Substitution IN', 'Substitution OUT']:
        player_selector = f"&player={1 if 'IN' in event_type else 2}"
        event_type = "Substitution"
    try:
        with body[1]:
            res = requests.get(f"{API_URL}/{section}?type={event_type}{player_selector}")
            df = pd.DataFrame(res.json())
            st.markdown("<div style='height: 100px; color: white'>.<\div>", unsafe_allow_html=True)
            st.image(f"images/{event_type.lower().replace(' ', '-')}.jpg")
    except:
        df = []
        render_404(st)



    with body[3]:
        if len(list(df)) != 0:
            st.subheader("Top 6")
            st.markdown("<div style='height: 20px; color: white'>.<\div>", unsafe_allow_html=True)
            for i, row in enumerate(df[df.columns[0]].value_counts()[:6].items()):
                st.write(MEDALS[i] if i < 3 else "&nbsp;"*5, row[0], row[1])
        else:
            st.write("Nothing happened with this conditions")

    with body[4]:
        if len(list(df)) != 0:
            plt.hist(df["time"], bins=range(0, 130, 10))
            plt.gcf().set_size_inches(6, 3)
            st.subheader("When did it happened?")
            st.pyplot(plt)
