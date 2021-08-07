from app import app
from config import PORT
import controllers.root_controller
import controllers.events_controller
import controllers.test

app.run("0.0.0.0", PORT)