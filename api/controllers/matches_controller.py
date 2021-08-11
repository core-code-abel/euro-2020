from flask import request
from app import app
import json
from utils.handle_error import handle_error
from utils.sql_queries import get_response, no_query_params_message


@app.route("/match-statistics/<team>")
@handle_error
def match_estatistics(team):
    select = ["team_name", "duels_won", "possession", "total_shots", "shots_on_target"]
    where = {
        "OR": [f"teams.team_name='{team}'" if team != 'All' else 'duels_won>0']
    }
    return get_response('match_statistics', select, where)