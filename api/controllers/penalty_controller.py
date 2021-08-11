from flask import request
from app import app
import json
from utils.handle_error import handle_error
from utils.sql_queries import get_response, no_query_params_message

def parse_pens_res(data):
    teams = {}
    response = {
        'winner': [],
        'looser': []
    }
    for team in json.loads(data):
        if team['match_id'] in teams:
            teams[team['match_id']].append(team)
        else:
            teams[team['match_id']] = [team]
    for match in teams.values():
        if match[0]['pens_score'] > match[1]['pens_score']:
            response['winner'].append(match[0])
            response['looser'].append(match[1])
        else:
            response['winner'].append(match[1])
            response['looser'].append(match[0])
    return response


@app.route("/penalty")
@handle_error
def penalties():
    query_type = request.args.get("type")
    if not query_type:
        return(no_query_params_message, 200)
    select = {
        'all': ["matches.match_id", "team_name", "solve_on_pens"],
        'winner': ["matches.match_id", "team_name", "pens_score"],
        'looser': ["matches.match_id", "team_name", "pens_score"]
    }
    where = {
        'all': {
            "OR": ["stage!='Group stage'"]
        },
        'winner': {
            "OR": ["solve_on_pens=True"]
        },
        'looser': {
            "OR": ["solve_on_pens=True"]
        }
    }
    res = get_response('penalty', select[query_type], where[query_type])
    return res if query_type == 'all' else json.dumps(parse_pens_res(res)[query_type])