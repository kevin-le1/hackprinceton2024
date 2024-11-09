from flask_smorest import Blueprint

ns = Blueprint("patient", "patient", url_prefix="/patient", description="patient")


@ns.route("/all")
def get_patient_data():
    # patient_data = query()
    # return patient_data
    pass
