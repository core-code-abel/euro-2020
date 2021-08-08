from utils.db_connection import execute_query
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.json_response import json_response
from utils.sql_utils import format_alias, parse_where
from flask import request
from app import app
import re
query = {
    "team": '''
        SELECT {cols}
        FROM events
        JOIN teams ON teams.team_id=events.team_id
        WHERE {conditions}
        GROUP BY {group_by}
        ORDER BY {order_by} DESC
        ;
    ''',
    "player": '''
        SELECT {cols}
        FROM events
        WHERE {conditions}
        GROUP BY {group_by}
        ORDER BY {order_by} DESC
        ;
    '''
}

no_query_params_message = {
    "status": "error",
    "message": "Empty params"

}

def get_response(select, where, group_by, order_by):
    return json_response(
        execute_query(
            query['team'].format(
                cols = ', '.join(select),
                conditions = parse_where(where),
                group_by = group_by,
                order_by = order_by
            )
        ),
        select
    )


    
@app.route("/events")
@handle_error
def goals():
    event_type = request.args.get("type")
    if not event_type:
        return(no_query_params_message, 200)
    select = [
        'teams.team_name',
        f'count(teams.team_name) AS {format_alias(event_type)}'
    ]
    where = {
        'AND' : [
            f"events.type='{event_type}'"
        ]
    }
    group_by = "teams.team_name"

    return get_response(select, where, group_by, format_alias(event_type))


@app.route("/events-player")
@handle_error
def goals_player():
    event_type = request.args.get("type")
    event_player = request.args.get("player", 1)
    if not event_type:
        return(no_query_params_message, 200)
    select = [
        f'action_player_{event_player}',
        f'count(action_player_{event_player}) AS {format_alias(event_type)}'
    ]
    where = {
        'AND' : [
            f"type='{event_type}'"
        ]
    }
    group_by = f"events.action_player_{event_player}"
    
    return get_response(select, where, group_by, format_alias(event_type))



@app.route("/events-team/<team>")
@handle_error
def goals_team(team):
    event_type = request.args.get("type")
    event_player = request.args.get("player", 1)
    if not event_type:
        return(no_query_params_message, 200)
    select = [
        f'events.action_player_{event_player}',
        f'count(events.action_player_{event_player}) AS {format_alias(event_type)}'
    ]
    where = {
        'AND' : [
            f"events.type='{event_type}'",
            f"teams.team_name='{team}'"
        ]
    }
    group_by = f"events.action_player_{event_player}"
    
    return get_response(select, where, group_by, format_alias(event_type))
    
