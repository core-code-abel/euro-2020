from flask import request
from app import app
import json
from utils.handle_error import handle_error
from utils.sql_queries import get_response, no_query_params_message


@app.route("/match-statistics/<team>")
@handle_error
def match_estatistics(team):
    # query_type = request.args.get("type")
    # if not query_type:
    #     return(no_query_params_message, 200)
    # select = [query_type, "team_name"]
    select = ["team_name", "duels_won", "possession", "total_shots", "shots_on_target"]
    where = {
        "OR": [f"teams.team_name='{team}'" if team != 'All' else 'duels_won>0']
    }
    return get_response('match-statistics', select, where)