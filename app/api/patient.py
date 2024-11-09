from flask_smorest import Blueprint
from app.database_scripts.database import fetch_all_patients, insert_patient, delete_patient

ns = Blueprint("patient", "patient", url_prefix="/patient", description="patient")


@ns.route("/all")
def get_patient_data():
    return fetch_all_patients()

@ns.route("")
def post_patient():
    insert_patient()
    return

@ns.route("/<string:patient_id>")
def delete_patient(patient_id):
    delete_patient(patient_id)
    return