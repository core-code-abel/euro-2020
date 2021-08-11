from utils.db_connection import execute_query
from utils.sql_utils import parse_where
from utils.json_response import json_response

query = {
    "masters": '''
        SELECT DISTINCT {cols}
        FROM {table}
        ORDER BY {order_by}
        ;
    ''',
    "team": '''
        SELECT {cols}
        FROM events
        JOIN teams ON teams.team_id=events.team_id
        WHERE {conditions}
        ;
    ''',
    "player": '''
        SELECT {cols}
        FROM events
        WHERE {conditions}
        ;
    ''',
    "penalty": '''
        SELECT {cols}
        FROM matches 
        JOIN match_team ON match_team.match_id=matches.match_id
        JOIN teams ON match_team.team_id=teams.team_id
        WHERE {conditions}
        ;
    ''',
    "match-statistics": '''
        SELECT {cols}
        FROM match_team
        JOIN teams ON match_team.team_id=teams.team_id
        WHERE {conditions}
    ''',
    "location": '''
        SELECT player_name, long, lat
        FROM players
        WHERE {conditions}
    '''
}

no_query_params_message = {
    "status": "error",
    "message": "Empty params"
}

def get_response(type, select, where={'OR': "true"}, table='', order_by=''):
    response = execute_query(
            query[type].format(
                cols = ', '.join(select),
                conditions = parse_where(where),
                table = table,
                order_by = order_by
            )
        )
    if len(response) == 0:
        return "[]"
    return json_response(response, select)
        
