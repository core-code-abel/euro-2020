from flask import request
from app import app
import json
from utils.handle_error import handle_error
from utils.sql_queries import get_response, no_query_params_message


@app.route("/players-location")
@handle_error
def players_location():
    select = ["player_name", "born_city", "long", "lat"]
    return get_response('players_location', select)

@app.route("/players-location/<country>")
@handle_error
def players_location_team(country):
    select = ["player_name", "born_city", "long", "lat"]
    where = {"OR": [f"country='{country}'"]}
    return get_response('players_location', select, where)

@app.route("/players-club")
@handle_error
def players_club_grouped():
    select = ["club", "count(player_name) AS players"]
    order_by = "players DESC"
    group_by = "club"
    return get_response('players_club_grouped', select, order_by=order_by, group_by=group_by)

@app.route("/players-club/<club>")
@handle_error
def players_club(club):
    select = ["players.player_name", "teams.team_name", "teams.flag"]
    where = {"OR": [f"club='{club}'"]}
    order_by="country"
    return get_response('players_club', select, where, order_by)