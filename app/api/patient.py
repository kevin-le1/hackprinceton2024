from flask_smorest import Blueprint
from app.database_scripts.database import fetch_all_patients, insert_patient, delete_patient, update_patient
from flask import request

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

@ns.route("/", methods=["PUT"])
def edit_patient():
    json = request.get_json()
    data = json.get("data")
    update_patient(
        patient_id = data["patient_id"],
        patient_name = data["patient_name"],
        specialist_type = data["specialist_type"],
        risk_score = data["risk_score"],
        bmi = data["bmi"],
        heart_rate = data["heart_rate"],
        blood_pressure = data["blood_pressure"],
    )
    return {"message": f"Patient with ID {data} edited successfully"}, 204

# DONT TOUCH START INFERENCE

@ns.route("/inference", methods=["POST"])
def startInference():
    print("inference")
    return {"message": "Patient inserted successfully"}, 201


# This might be bad, but I am just going to code ollama in here you can put it in a different file but im ok !!! even imports
import pandas as pd
import ollama

def generateInference():
    patients = fetch_all_patients()
    
    df = pd.DataFrame(patients, columns=["ID", "Name", "Specialty", "Risk", "BMI", "HR", "BP"])
    df = df.drop(columns=["ID", "Risk"])
    print(df)
    
    content = f'''
    I am going to give you patient csv data please asses the risk score of these don't give the same risk score to 
    anyone make sure these risk scores are actually distinguishable enought to determine who should be treated first
    don't give me a function you should calculate it on the spot and display it make values from 0 to 100 Patient Name, 
    Necessary Specialist, BMI, Heart Rate, Blood Pressure
    
    {df}
    '''

    response = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': content}]
    )

    print(response['message']['content'])
generateInference()