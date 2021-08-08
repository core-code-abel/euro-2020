import requests
import os
import json
import numpy as np
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

medals = {
    0: '🥇',
    1: '🥈',
    2: '🥉',
}

API_URL = os.getenv("API_URL")

def get_master(table, key):
    res = requests.get(f"{API_URL}/masters/{table}/{key}")
    return [x[key] for x in res.json()]

def render_tab_events(st):
    body = st.columns((1, 2, 2, 1))
    with body[1]:
        st.header("Event Type")
        events = sorted(get_master('events', 'type') + ['Substitution IN', 'Substitution OUT'])
        events.remove('Substitution')
        event_type = st.selectbox('', events)
        player = False
        if event_type != "Disallowed goal":
            player = st.checkbox("Player")
        st.empty()
    with body[2]:
        st.header("Team")
        team = st.selectbox('', ['All'] + (get_master('teams', 'team_name') if player else []))
        st.empty()

    body = st.columns((1, 8, 12, 12, 1))

    with body[1]:
        st.header("Top Five")
        section = "events"
        if player and team != 'All':
            section += f'-team/{team}'
        if player and team == 'All':
            section += f'-player'
        player_selector = ''
        if event_type in ['Substitution IN', 'Substitution OUT']:
            player_selector = f"&player={1 if 'IN' in event_type else 2}"
            event_type = "Substitution"
        res = requests.get(f"{API_URL}/{section}?type={event_type}{player_selector}")
        if len(res.json()) != 0:
            ds = pd.DataFrame(res.json())
            for i, row in enumerate(ds[ds.columns[0]].value_counts()[:5].items()):
                st.write(medals[i] if i < 3 else "&nbsp;"*5, row[0], row[1])
        else:
            st.write("Nothing happened with this conditions")
        st.empty()

    with body[2]:
        st.header("When did it happened?")
        st.empty()

    with body[3]:
        st.empty()
        st.image(f"images/{event_type.lower().replace(' ', '-')}.jpg")