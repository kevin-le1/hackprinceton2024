import sys
import os
import contextlib
import sqlite3
import uuid

DATABASE_URL = "./hospital_database.sqlite"

# Makes call to SQLite database with passed-in SQL statement
def fetch(sql_statement, params):
    try:
        if not os.path.exists(DATABASE_URL):
            raise Exception("Unable to open database file")
        with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
            with contextlib.closing(connection.cursor()) as cursor:
                cursor.execute(sql_statement, params or [])
                table = cursor.fetchall()
                return table
    except Exception as ex:
        print(f"{sys.argv[0]}:", ex, file=sys.stderr)
        sys.exit(1)

# Generates a UUID v4 as a string
def generate_uuid():
    return str(uuid.uuid4())

# Function to insert a new patient
def insert_patient(patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure):
    patient_id = generate_uuid()
    sql_statement = '''
        INSERT INTO Patient (patient_id, patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    params = (patient_id, patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure)
    fetch(sql_statement, params)
    return patient_id

# Function to insert a new scheduling record
def insert_scheduling(patient_id, order_in_queue, specialist_id):
    p_key = generate_uuid()
    sql_statement = '''
        INSERT INTO Scheduling (p_key, patient_id, order_in_queue, specialist_id)
        VALUES (?, ?, ?, ?)
    '''
    params = (p_key, patient_id, order_in_queue, specialist_id)
    fetch(sql_statement, params)
    return p_key

# Function to insert a new specialist
def insert_specialist(specialist_type, specialist_name):
    specialist_id = generate_uuid()
    sql_statement = '''
        INSERT INTO Specialist (specialist_id, specialist_type, specialist_name)
        VALUES (?, ?, ?)
    '''
    params = (specialist_id, specialist_type, specialist_name)
    fetch(sql_statement, params)
    return specialist_id

# Function to fetch all patients
def fetch_all_patients():
    sql_statement = "SELECT * FROM Patient"
    return fetch(sql_statement, [])

# Function to fetch a specific patient by ID
def fetch_patient_by_id(patient_id):
    sql_statement = "SELECT * FROM Patient WHERE patient_id = ?"
    params = (patient_id,)
    return fetch(sql_statement, params)

# Function to fetch all scheduling records
def fetch_all_scheduling():
    sql_statement = "SELECT * FROM Scheduling"
    return fetch(sql_statement, [])

# Function to fetch scheduling by patient ID
def fetch_scheduling_by_patient(patient_id):
    sql_statement = "SELECT * FROM Scheduling WHERE patient_id = ?"
    params = (patient_id,)
    return fetch(sql_statement, params)

# Function to fetch all specialists
def fetch_all_specialists():
    sql_statement = "SELECT * FROM Specialist"
    return fetch(sql_statement, [])

# Function to fetch patient matching info for specified specialist typ
def fetch_patients_by_specialist_type(specialist_type):
    sql_statement = '''
        SELECT 
            Scheduling.order_in_queue,
            Specialist.specialist_id,
            Specialist.specialist_name,
            Patient.patient_name
        FROM 
            Patient
        INNER JOIN 
            Scheduling ON Patient.patient_id = Scheduling.patient_id
        INNER JOIN 
            Specialist ON Scheduling.specialist_id = Specialist.specialist_id
        WHERE 
            Specialist.specialist_type = ?
        ORDER BY 
            Scheduling.order_in_queue ASC
    '''
    params = (specialist_type,)
    return fetch(sql_statement, params)

# Function to update patient information
def update_patient(patient_id, patient_name=None, specialist_type=None, risk_score=None, bmi=None, heart_rate=None, blood_pressure=None):
    updates = []
    params = []
    
    if patient_name:
        updates.append("patient_name = ?")
        params.append(patient_name)
    if specialist_type:
        updates.append("specialist_type = ?")
        params.append(specialist_type)
    if risk_score is not None:
        updates.append("risk_score = ?")
        params.append(risk_score)
    if bmi is not None:
        updates.append("bmi = ?")
        params.append(bmi)
    if heart_rate is not None:
        updates.append("heart_rate = ?")
        params.append(heart_rate)
    if blood_pressure:
        updates.append("blood_pressure = ?")
        params.append(blood_pressure)

    if updates:
        sql_statement = f"UPDATE Patient SET {', '.join(updates)} WHERE patient_id = ?"
        params.append(patient_id)
        fetch(sql_statement, params)

# Function to update scheduling record
def update_scheduling(p_key, patient_id=None, order_in_queue=None, specialist_id=None):
    updates = []
    params = []
    
    if patient_id:
        updates.append("patient_id = ?")
        params.append(patient_id)
    if order_in_queue is not None:
        updates.append("order_in_queue = ?")
        params.append(order_in_queue)
    if specialist_id is not None:
        updates.append("specialist_id = ?")
        params.append(specialist_id)
    
    if updates:
        sql_statement = f"UPDATE Scheduling SET {', '.join(updates)} WHERE p_key = ?"
        params.append(p_key)
        fetch(sql_statement, params)

# Function to update specialist information
def update_specialist(specialist_id, specialist_type=None, specialist_name=None):
    updates = []
    params = []
    
    if specialist_type:
        updates.append("specialist_type = ?")
        params.append(specialist_type)
    if specialist_name:
        updates.append("name = ?")
        params.append(specialist_name)
    
    if updates:
        sql_statement = f"UPDATE Specialist SET {', '.join(updates)} WHERE specialist_id = ?"
        params.append(specialist_id)
        fetch(sql_statement, params)

# Function to delete a patient by ID
def delete_patient(patient_id):
    sql_statement = "DELETE FROM Patient WHERE patient_id = ?"
    params = (patient_id,)
    fetch(sql_statement, params)

# Function to delete a scheduling record by p_key
def delete_scheduling(p_key):
    sql_statement = "DELETE FROM Scheduling WHERE p_key = ?"
    params = (p_key,)
    fetch(sql_statement, params)

# Function to delete a specialist by specialist_id
def delete_specialist(specialist_id):
    sql_statement = "DELETE FROM Specialist WHERE specialist_id = ?"
    params = (specialist_id,)
    fetch(sql_statement, params)

def main():
    patients = [
    ("Alice Smith", "Cardiologist", 8.5, 24.5, 72, "120/80"),
    ("Bob Johnson", "Orthopedic", 5.2, 29.4, 78, "130/85"),
    ("Clara Davis", "Neurologist", 7.1, 22.3, 65, "118/75"),
    ("David Martinez", "Cardiologist", 9.2, 30.1, 80, "140/90"),
    ("Eva Green", "Orthopedic", 4.8, 27.6, 74, "125/82"),
    ("Frank Moore", "Neurologist", 6.5, 23.8, 68, "117/78"),
    ("Grace Lee", "Cardiologist", 6.9, 26.1, 75, "122/82"),
    ("Henry Kim", "Orthopedic", 7.3, 28.0, 70, "128/84"),
    ("Ivy Wilson", "Neurologist", 6.2, 25.7, 66, "119/76"),
    ("Jack Brown", "Cardiologist", 8.0, 24.0, 73, "121/79"),
    ("Karen Adams", "Orthopedic", 5.9, 27.5, 77, "126/83"),
    ("Liam Scott", "Neurologist", 7.5, 23.9, 64, "115/72")
    ]

    specialists = [
    ("Cardiologist", "Dr. Emily Carter"),
    ("Cardiologist", "Dr. George Wang"),
    ("Orthopedic", "Dr. Sarah Chen"),
    ("Orthopedic", "Dr. James Patel"),
    ("Neurologist", "Dr. Olivia Jones"),
    ("Neurologist", "Dr. Michael Smith")
    ]

    # Populate Patient and Specialist tables
    patient_ids = {}
    specialist_ids = {}

    for patient in patients:
        patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure = patient
        patient_id = insert_patient(patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure)
        patient_ids[patient_name] = (patient_id, specialist_type)

    for specialist in specialists:
        specialist_type, name = specialist
        specialist_id = insert_specialist(specialist_type, name)
        if specialist_type not in specialist_ids:
            specialist_ids[specialist_type] = []
        specialist_ids[specialist_type].append((specialist_id, name))

    # Populate the Scheduling table with order_in_queue for each patient-specialist match
    order_in_queue_tracker = {}
    for patient_name, (patient_id, specialist_type) in patient_ids.items():
        if specialist_type not in order_in_queue_tracker:
            order_in_queue_tracker[specialist_type] = 1
        
        specialist_list = specialist_ids.get(specialist_type, [])
        if specialist_list:
            # Round-robin selection of specialists for the same type
            assigned_specialist_id, specialist_name = specialist_list[
                (order_in_queue_tracker[specialist_type] - 1) % len(specialist_list)
            ]
            
            # Insert into Scheduling
            insert_scheduling(patient_id, order_in_queue_tracker[specialist_type], assigned_specialist_id)
            
            # Increment order in queue
            order_in_queue_tracker[specialist_type] += 1
    
    patients = fetch_all_patients()
    specialist = fetch_all_specialists()
    scheduling = fetch_all_scheduling()
    
    print(f"Patients: {patients}")
    print()
    print(f"Specialist: {specialist}")
    print()
    print(f"Scheduling: {scheduling}")
    print()

    scheduling_for_cardio = fetch_patients_by_specialist_type("Cardiologist")
    print(f"Scheduling for cardio: {scheduling_for_cardio}")
    print()
    scheduling_for_orthopedic = fetch_patients_by_specialist_type("Orthopedic")
    print(f"Scheduling for ortho: {scheduling_for_orthopedic}")
    print()
    scheduling_for_neuro = fetch_patients_by_specialist_type("Neurologist")
    print(f"Scheduling for neuro: {scheduling_for_neuro}")
if __name__ == '__main__':
    main()