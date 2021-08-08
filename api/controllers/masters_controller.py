from utils.db_connection import execute_query
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.json_response import json_response
from utils.sql_utils import parse_where
from app import app


@app.route("/masters/<table>/<column>")
@handle_error
def masters(table, column):
    query = '''
        SELECT DISTINCT {column}
        FROM {table}
        ORDER BY {column}
        ;
    '''
    return json_response(
        execute_query(
            query.format(
                column = column,
                table = table
            )
        ),
        [column]
    )
