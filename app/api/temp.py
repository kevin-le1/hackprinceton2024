from flask_smorest import Blueprint
from app.database_scripts.database import fetch_all_patients, insert_patient, delete_patient, update_patient, fetch_patient_by_id
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
        age = data["age"],
        hospitalizations_in_last_year = data["hospitalizations_in_last_year"],
        previous_surgeries = data["previous_surgeries"],
        cholestoral_level = data["cholestoral_level"],
        respiratory_rate = data["respiratory_rate"]
    )
    return {"message": f"Patient with ID {data} edited successfully"}, 204

# DONT TOUCH START INFERENCE
import re

@ns.route("/inference", methods=["POST"])
def startInference():
    uuids = generateInference()
    print(uuids)
    for uuid in uuids:
        
        patient = fetch_patient_by_id(uuid)
        update_patient(
        patient_id = uuid,
        patient_name = patient[0][1],
        specialist_type = patient[0][2],
        risk_score = uuids[uuid],
        bmi = patient[0][4],
        heart_rate = patient[0][5],
        blood_pressure = patient[0][6],
        age = patient[0][7],
        hospitalizations_in_last_year = patient[0][8],
        previous_surgeries = patient[0][9],
        cholestoral_level = patient[0][10],
        respiratory_rate = patient[0][11]
        )
    
    return {"message": "Patient inserted successfully"}, 201


# This might be bad, but I am just going to code ollama in here you can put it in a different file but im ok !!! even imports
import pandas as pd
import ollama

def generateInference():
    # Fetch patients and create DataFrame
    patients = fetch_all_patients()
    df = pd.DataFrame(patients, columns=["ID", "Name", "Specialty", "Risk", "BMI", "HR", "BP", "Age", "Hospitalizations in Last Year", "Previous Surgeries", "Cholestoral Level", "Respiratory Rate"])
    df = df.drop(columns=["Risk"])
    print(df)

    # Create a concise content prompt with essential details
    content = f'''
    I am going to give you patient csv data please asses the risk score of these don't give the same risk score to
    anyone make sure these risk scores are actually distinguishable enought to determine who should be treated first. Don't give me a
    function, you should calculate it on the spot and display it make values from 0 to 1. Only output the risk scores and their uuid nothing else.
    In this format: - Patient with ID: uuid    Risk Score: score

    Patient Data:
    {df}
    
    '''
    # Call the Ollama API with the cleaned prompt
    response = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': content}]
    )

    # Extract and print the response content
    message = response['message']['content']
    print(message)
    
    # Extract UUID and risk score using regex
    uuid_risk_pairs = re.findall(r'([a-f0-9-]{36})\s+.*?\s+([0-9.]+)', message)

    # Convert to dictionary with UUID as key and risk score as value
    uuid_risk_dict = {uuid: float(score) for uuid, score in uuid_risk_pairs}
    print('done')
    return uuid_risk_dict