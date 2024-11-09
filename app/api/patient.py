from flask_smorest import Blueprint
from app.database_scripts.database import fetch_all_patients, insert_patient, delete_patient

ns = Blueprint("patient", "patient", url_prefix="/patient", description="patient")


@ns.route("/all")
def get_patient_data():
    return fetch_all_patients()

@ns.route("", methods=["POST"])
def post_patient():
    insert_patient()
    return {"message": "Patient inserted successfully"}, 201

@ns.route("/<string:patient_id>", methods=["DELETE"])
def delete_patient_route(patient_id):
    delete_patient(patient_id)
    return {"message": f"Patient with ID {patient_id} deleted successfully"}, 204

@ns.route("/<string:document_id>", methods=["PUT"])
def edit_patient(patient_id):
    delete_patient(patient_id)
    return {"message": f"Patient with ID {patient_id} edited successfully"}, 204