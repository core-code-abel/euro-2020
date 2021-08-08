from utils.db_connection import execute_query
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.json_response import json_response
from app import app

# Función controladora
@app.route("/")
@handle_error
def root():
    return {
        "message":"welcome to Euro 2020 API"
    }

