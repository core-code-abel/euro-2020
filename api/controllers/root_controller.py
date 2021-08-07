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





@app.route("/saludo")
@handle_error
def saludo_fn():
    print("terminal")
    print(request.args)
    name = request.args.get("name")
    surname = request.args.get("surname")
    #raise ValueError("MEC")
    return {
        "name":"EMOJI" + name,
        "surname":surname,
    }
