from app import app
import os

PORT = os.getenv('PORT', 5000)

import controllers.root_controller
import controllers.events_controller
import controllers.masters_controller
import controllers.matches_controller
import controllers.penalty_controller
import controllers.players_controller

app.run("0.0.0.0", PORT)