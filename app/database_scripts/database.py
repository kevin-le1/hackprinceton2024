import sys
import os
import contextlib
import sqlite3
import uuid

DATABASE_URL = (
    "/Users/zaeem/Desktop/HackPrinceton 2024/hackprinceton2024/app/database_scripts/hospital_database.sqlite"
)


# Makes call to SQLite database with passed-in SQL statement
def fetch(sql_statement, params):
    try:
        if not os.path.exists(DATABASE_URL):
            raise Exception("Unable to open database file")
        with sqlite3.connect(
            DATABASE_URL, isolation_level=None, uri=True
        ) as connection:
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
def insert_patient(
    patient_name=None,
    specialist_type=None,
    risk_score=None,
    bmi=None,
    heart_rate=None,
    blood_pressure=None,
    age=None,
    hospitalizations_in_last_year=None,
    previous_surgeries=None,
    cholestoral_level=None,
    respiratory_rate=None

):
    patient_id = generate_uuid()
    sql_statement = """
        INSERT INTO Patient (patient_id, patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure, age, hospitalizations_in_last_year, previous_surgeries, cholestoral_level, respiratory_rate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = (
        patient_id,
        patient_name,
        specialist_type,
        risk_score,
        bmi,
        heart_rate,
        blood_pressure,
        age,
        hospitalizations_in_last_year, 
        previous_surgeries, 
        cholestoral_level, 
        respiratory_rate
    )
    fetch(sql_statement, params)
    return patient_id


# Function to insert a new scheduling record
def insert_scheduling(patient_id, order_in_queue, specialist_id):
    p_key = generate_uuid()
    sql_statement = """
        INSERT INTO Scheduling (p_key, patient_id, order_in_queue, specialist_id)
        VALUES (?, ?, ?, ?)
    """
    params = (p_key, patient_id, order_in_queue, specialist_id)
    fetch(sql_statement, params)
    return p_key


# Function to insert a new specialist
def insert_specialist(specialist_type, specialist_name):
    specialist_id = generate_uuid()
    sql_statement = """
        INSERT INTO Specialist (specialist_id, specialist_type, specialist_name)
        VALUES (?, ?, ?)
    """
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

def fetch_specialists_by_type(specialist_type):
    sql_statement = '''
        SELECT specialist_id, specialist_name
        FROM Specialist
        WHERE specialist_type = ?
    '''
    params = (specialist_type,)
    return fetch(sql_statement, params)

# Function to fetch patient matching info for specified specialist typ
def fetch_patients_by_specialist_type(specialist_type):
    sql_statement = """
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
    """
    params = (specialist_type,)
    return fetch(sql_statement, params)


# Function to update patient information
def update_patient(
    patient_id,
    patient_name=None,
    specialist_type=None,
    risk_score=None,
    bmi=None,
    heart_rate=None,
    blood_pressure=None,
    age=None,
    hospitalizations_in_last_year=None,
    previous_surgeries=None,
    cholestoral_level=None,
    respiratory_rate=None
):
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
    if age:
        updates.append("age = ?")
        params.append(age)
    if hospitalizations_in_last_year:
        updates.append("hospitalizations_in_last_year = ?")
        params.append(hospitalizations_in_last_year)
    if previous_surgeries:
        updates.append("previous_surgeries = ?")
        params.append(previous_surgeries)
    if cholestoral_level:
        updates.append("cholestoral_level = ?")
        params.append(cholestoral_level)
    if respiratory_rate:
        updates.append("respiratory_rate = ?")
        params.append(respiratory_rate)
    
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
        sql_statement = (
            f"UPDATE Specialist SET {', '.join(updates)} WHERE specialist_id = ?"
        )
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

def clear_all_tables():
    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
            with contextlib.closing(connection.cursor()) as cursor:
                # Disable foreign key constraints temporarily to avoid issues with foreign key dependencies
                cursor.execute("PRAGMA foreign_keys = OFF")
                
                # Clear all tables
                cursor.execute("DELETE FROM Patient")
                cursor.execute("DELETE FROM Specialist")
                cursor.execute("DELETE FROM Scheduling")
                
                # Re-enable foreign key constraints
                cursor.execute("PRAGMA foreign_keys = ON")
                
                print("All tables cleared successfully.")
    except Exception as ex:
        print(f"Error clearing tables: {ex}")

def round_robin_schedule(specialist_patient_map):
    """
    Schedule patients with specialists in a round-robin fashion based on order_in_queue.

    Args:
    specialist_patient_map (dict): A dictionary where each key is a specialist type (str),
                                   and each value is a list of tuples where tuple[0] is the order_in_queue
                                   and tuple[1] is the patient_id.

    Example input:
    {'Cardiologist': [(2, 1), (1, 897), (3, 36)], 'Orthopedic': [(0, 2), (2, 48)]}
    """

    # Iterate through each specialist type in the input dictionary
    for specialist_type, patient_queue in specialist_patient_map.items():
        # Fetch all specialists of the given type
        specialists = fetch_specialists_by_type(specialist_type)
        if not specialists:
            print(f"No specialists found for type: {specialist_type}")
            continue
        
        # Sort patients by order_in_queue
        patient_queue.sort(key=lambda x: x[0])
        
        # Round-robin assign specialists to patients based on sorted order_in_queue
        num_specialists = len(specialists)
        for i, (order_in_queue, patient_id) in enumerate(patient_queue):
            # Use round-robin to select a specialist
            specialist_id, specialist_name = specialists[i % num_specialists]
            
            # Insert into the Scheduling table
            insert_scheduling(patient_id, order_in_queue, specialist_id)

    print("Round-robin scheduling completed.")

def main():
    clear_all_tables()
    patients = [
    ("Alice Smith", "Cardiologist", 8.5, 24.5, 72, "120/80", 52, 1, 2, 190, 16),
    ("Bob Johnson", "Orthopedic", 5.2, 29.4, 78, "130/85", 45, 0, 1, 180, 18),
    ("Clara Davis", "Neurologist", 7.1, 22.3, 65, "118/75", 60, 2, 3, 200, 15),
    ("David Martinez", "Cardiologist", 9.2, 30.1, 80, "140/90", 55, 3, 1, 230, 20),
    ("Eva Green", "Orthopedic", 4.8, 27.6, 74, "125/82", 40, 0, 0, 170, 16),
    ("Frank Moore", "Neurologist", 6.5, 23.8, 68, "117/78", 58, 1, 2, 210, 17),
    ("Grace Lee", "Cardiologist", 6.9, 26.1, 75, "122/82", 47, 1, 1, 180, 16),
    ("Henry Kim", "Orthopedic", 7.3, 28.0, 70, "128/84", 49, 0, 0, 190, 19),
    ("Ivy Wilson", "Neurologist", 6.2, 25.7, 66, "119/76", 62, 2, 1, 185, 15),
    ("Jack Brown", "Cardiologist", 8.0, 24.0, 73, "121/79", 54, 1, 3, 200, 17),
    ("Karen Adams", "Orthopedic", 5.9, 27.5, 77, "126/83", 42, 0, 1, 175, 18),
    ("Liam Scott", "Neurologist", 7.5, 23.9, 64, "115/72", 59, 2, 2, 195, 15),
    ]
    specialists = [
        ("Cardiologist", "Dr. Emily Carter"),
        ("Cardiologist", "Dr. George Wang"),
        ("Orthopedic", "Dr. Sarah Chen"),
        ("Orthopedic", "Dr. James Patel"),
        ("Neurologist", "Dr. Olivia Jones"),
        ("Neurologist", "Dr. Michael Smith"),
    ]

    # Populate the Patient and Specialist tables
    patient_ids = {}
    specialist_ids = {}

    for patient in patients:
        patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure, age, hospitalizations_in_last_year, previous_surgeries, cholestoral_level, respiratory_rate  = (
            patient
        )
        patient_id = insert_patient(
            patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure, age, hospitalizations_in_last_year, previous_surgeries, cholestoral_level, 
        respiratory_rate
        )
        patient_ids[patient_name] = (patient_id, specialist_type)

    for specialist in specialists:
        specialist_type, name = specialist
        specialist_id = insert_specialist(specialist_type, name)
        if specialist_type not in specialist_ids:
            specialist_ids[specialist_type] = []
        specialist_ids[specialist_type].append((specialist_id, name))

    patients = fetch_all_patients()
    specialist = fetch_all_specialists()
    scheduling = fetch_all_scheduling()

    print(f"Patients: {patients}")
    print()
    print(f"Specialist: {specialist}")
    print()
    print(f"Scheduling: {scheduling}")
    print()

    specialist_patient_map = {"Cardiologist": [(2, '213bd1bd-198d-400d-905f-c8f7d55d92ea'), (4, '38dd04d9-f763-4bff-944a-a2e627234d1d'), (1, 'e72ac10b-efd3-4a77-bb98-9467ef3a2e0b'), (7, 'e0a3c3c0-013f-47fc-a335-157bc3f91f9b')], "Orthopedic": [], "Neurologist": []}
    round_robin_schedule(specialist_patient_map)

    scheduling = fetch_all_scheduling()
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


if __name__ == "__main__":
    main()







# Populate Patient and Specialist tables
    # patient_ids = {}
    # specialist_ids = {}

    # for patient in patients:
    #     patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure, age, hospitalizations_in_last_year, previous_surgeries, cholestoral_level, respiratory_rate  = (
    #         patient
    #     )
    #     patient_id = insert_patient(
    #         patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure, age, hospitalizations_in_last_year, previous_surgeries, cholestoral_level, 
    #     respiratory_rate
    #     )
    #     patient_ids[patient_name] = (patient_id, specialist_type)

    # for specialist in specialists:
    #     specialist_type, name = specialist
    #     specialist_id = insert_specialist(specialist_type, name)
    #     if specialist_type not in specialist_ids:
    #         specialist_ids[specialist_type] = []
    #     specialist_ids[specialist_type].append((specialist_id, name))

    # # Populate the Scheduling table with order_in_queue for each patient-specialist match
    # order_in_queue_tracker = {}
    # for patient_name, (patient_id, specialist_type) in patient_ids.items():
    #     if specialist_type not in order_in_queue_tracker:
    #         order_in_queue_tracker[specialist_type] = 1

    #     specialist_list = specialist_ids.get(specialist_type, [])
    #     if specialist_list:
    #         # Round-robin selection of specialists for the same type
    #         assigned_specialist_id, specialist_name = specialist_list[
    #             (order_in_queue_tracker[specialist_type] - 1) % len(specialist_list)
    #         ]

    #         # Insert into Scheduling
    #         insert_scheduling(
    #             patient_id,
    #             order_in_queue_tracker[specialist_type],
    #             assigned_specialist_id,
    #         )

    #         # Increment order in queue
    #         order_in_queue_tracker[specialist_type] += 1