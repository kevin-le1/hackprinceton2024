from flask_smorest import Blueprint
from app.database_scripts.database import fetch_all_scheduling_with_details
# from flask import request

ns = Blueprint("schedule", "schedule", url_prefix="/schedule", description="schedule")


@ns.route("/all")
def get_patient_data():
    return fetch_all_scheduling_with_details()
