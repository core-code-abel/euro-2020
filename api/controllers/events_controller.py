from flask import request
from app import app
from utils.handle_error import handle_error
from utils.sql_queries import get_response, no_query_params_message

@app.route("/events")
@handle_error
def events():
    event_type = request.args.get("type")
    if not event_type:
        return(no_query_params_message, 200)
    select = [
        'teams.team_name',
        'events.time',
    ]
    where = {
        'OR' : [
            f"events.type='{event_type}'"
        ]
    }
    if event_type == 'Goal':
        where['OR'].append("events.type='Penalty'")

    return get_response('team', select, where)


@app.route("/events-player")
@handle_error
def events_player():
    event_type = request.args.get("type")
    event_player = request.args.get("player", 1)
    if not event_type:
        return(no_query_params_message, 200)
    select = [
        f'action_player_{event_player}',
        'time'
    ]
    where = {
        'OR' : [
            f"type='{event_type}'"
        ]
    }
    if event_type == 'Goal':
        where['OR'].append("events.type='Penalty'")

    return get_response('team', select, where)


@app.route("/events-team/<team>")
@handle_error
def events_team(team):
    event_type = request.args.get("type")
    event_player = request.args.get("player", 1)
    if not event_type:
        return(no_query_params_message, 200)
    select = [
        f'events.action_player_{event_player}',
        'events.time'
    ]
    where = {
        'AND' : [
            f"events.type='{event_type}'",
            f"teams.team_name='{team}'"
        ]
    }
    if event_type == 'Goal':
        where['AND'][0] = "events.type IN ('Goal', 'Penalty')"
    return get_response('team', select, where)
    
