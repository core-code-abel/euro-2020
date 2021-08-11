from .utils import get_master
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")

def render_tab_statistics(st):

    cols = st.columns((5, 2, 12, 1, 5, 1))
    teams = get_master('teams', 'team_name')
    with cols[0]:
        st.subheader('Team 1')
        team1 = st.selectbox('', teams, key="t1")
        st.subheader('Team 2')
        team2 = st.selectbox('', teams, key="t2")
        
    with cols[2]:
        st.image("images/statistics.jpg")

    with cols[4]:
        st.subheader('Solve on penalty')
        res = requests.get(f"{API_URL}/penalty?type=all")
        df = pd.DataFrame(res.json())
        total_duels = len(df['solve_on_pens'])
        pens_duels = len(df[df['solve_on_pens'] == True])
        st.markdown(f'''
            <div style='padding-top: 20px'>
                <div style='font-size: 3em;'>
                    {pens_duels}
                </div>
                <div style='font-size: 5em; transform: translate(50px, -100px);'>
                    / {total_duels}
                </div>
            </div>
        ''', unsafe_allow_html=True)

        

    res1 = requests.get(f"{API_URL}/match-statistics/{team1}")
    res2 = requests.get(f"{API_URL}/match-statistics/{team2}")
    res3 = requests.get(f"{API_URL}/match-statistics/All")
    df1 = pd.DataFrame(res1.json()).mean()
    df2 = pd.DataFrame(res2.json()).mean()
    df3 = pd.DataFrame(res3.json()).mean()
    columns = {"duels_won": "Duels Won", "possession": "Possesion", "total_shots": "Total Shoots", "shots_on_target": "Shoots on Target"}
    rows = {0: team1, 1: team2, 2: "Global"}
    df = pd.DataFrame([df1, df2, df3])
    df['duels_won'] = df['duels_won'].apply(lambda x: f'{round(x * 100, 2)}%')
    df['possession'] = df['possession'].apply(lambda x: f'{round(x * 100, 2)}%')
    df['total_shots'] = df['total_shots'].apply(lambda x: f'{round(x, 2)}')
    df['shots_on_target'] = df['shots_on_target'].apply(lambda x: f'{round(x, 2)}')
    df['Team'] = [team1, team2, "Global"]
    df.set_index('Team', inplace=True)
    df.rename(columns, axis="columns", inplace = True)
    st.table(df)
