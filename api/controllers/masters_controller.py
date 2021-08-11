from utils.handle_error import handle_error
from utils.sql_queries import get_response, no_query_params_message
from app import app


@app.route("/masters/<table>/<column>")
@handle_error
def masters(table, column):
    return get_response('masters', [column], table=table, order_by=column)

