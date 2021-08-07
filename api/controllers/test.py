from utils.db_connection import execute_query
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.json_response import json_response
from utils.sql_utils import parse_where
from app import app


@app.route("/test")
@handle_error
def test():
    select = ['team_id', 'team_name']
    where = {
        'OR' : [
            'team_id=4',
            'team_id=6'
        ]
    }
    query = '''
        SELECT {cols}
        FROM teams
        WHERE {conditions}
        ;
    '''
    return json_response(
        execute_query(
            query.format(
                cols = ', '.join(select),
                conditions = parse_where(where)
            )
        ),
        select
    )
