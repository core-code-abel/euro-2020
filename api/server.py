from app import app
from config import PORT
import controllers.root_controller
import controllers.events_controller
import controllers.masters_controller

app.run("0.0.0.0", PORT)