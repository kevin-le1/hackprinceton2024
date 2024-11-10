import sqlite3
import sys
import database as db
import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL", "")
if DATABASE_URL == "":
    raise Exception("no database url configured")


patients_user = {
    1: [
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
    ],
    2: [
        ("Samantha White", "Cardiologist", 7.9, 25.2, 69, "121/77", 48, 1, 2, 180, 14),
        ("John Miller", "Orthopedic", 5.8, 28.3, 75, "132/86", 46, 0, 1, 190, 17),
        ("Lena Harris", "Neurologist", 7.4, 23.1, 72, "120/78", 63, 2, 3, 210, 16),
        ("Tom Walker", "Cardiologist", 8.3, 26.0, 70, "135/88", 53, 3, 1, 240, 19),
        ("Olivia Brown", "Orthopedic", 6.1, 27.9, 78, "125/84", 41, 0, 0, 200, 18),
        ("Mason Clark", "Neurologist", 6.8, 24.4, 66, "119/74", 57, 1, 2, 220, 15),
        ("Rachel King", "Cardiologist", 7.2, 25.3, 72, "124/79", 49, 1, 1, 210, 16),
        ("Ryan Scott", "Orthopedic", 5.5, 29.0, 77, "128/82", 44, 0, 0, 180, 19),
        ("Isabella Lewis", "Neurologist", 6.9, 22.7, 68, "118/76", 58, 2, 1, 200, 14),
        ("Daniel Adams", "Cardiologist", 8.1, 26.5, 74, "130/85", 51, 1, 3, 230, 17),
        ("Lucas Miller", "Orthopedic", 5.6, 28.1, 76, "133/84", 45, 0, 1, 175, 18),
        ("Evelyn Green", "Neurologist", 6.6, 23.2, 70, "117/73", 60, 1, 2, 215, 16),
    ],
    3: [
        ("Emma Collins", "Cardiologist", 8.0, 24.9, 71, "125/80", 50, 1, 2, 190, 17),
        ("Michael Harris", "Orthopedic", 5.4, 29.2, 79, "128/84", 43, 0, 1, 200, 18),
        ("Sophia Young", "Neurologist", 7.3, 22.8, 70, "119/77", 61, 2, 3, 205, 16),
        ("Benjamin Wilson", "Cardiologist", 8.2, 26.3, 72, "132/88", 55, 3, 1, 220, 19),
        ("Lily Cooper", "Orthopedic", 6.0, 28.4, 74, "130/87", 47, 0, 0, 195, 17),
        ("Aiden Scott", "Neurologist", 7.6, 23.5, 69, "120/75", 59, 1, 2, 210, 15),
        ("Maya Turner", "Cardiologist", 7.8, 25.6, 73, "134/90", 54, 1, 1, 200, 16),
        ("James Thompson", "Orthopedic", 5.9, 27.1, 76, "128/83", 42, 0, 0, 185, 18),
        ("Charlotte Lee", "Neurologist", 6.4, 23.0, 72, "117/72", 60, 2, 1, 215, 16),
        ("Oliver King", "Cardiologist", 8.4, 25.0, 70, "136/91", 52, 1, 3, 225, 18),
        ("Mia Turner", "Orthopedic", 5.7, 28.6, 77, "133/85", 46, 0, 1, 180, 17),
        ("William White", "Neurologist", 6.7, 22.9, 68, "119/74", 58, 1, 2, 210, 16),
    ],
    4: [
        ("Charlotte Harris", "Cardiologist", 7.6, 24.8, 69, "127/79", 51, 1, 2, 185, 17),
        ("Henry Carter", "Orthopedic", 5.3, 28.7, 73, "130/82", 44, 0, 1, 195, 18),
        ("Lily Moore", "Neurologist", 7.2, 22.4, 75, "120/76", 59, 2, 3, 210, 16),
        ("Samuel Gray", "Cardiologist", 8.6, 25.4, 70, "135/86", 52, 3, 1, 220, 18),
        ("Ella Perez", "Orthopedic", 6.3, 27.3, 74, "125/81", 46, 0, 0, 180, 17),
        ("Mason Bell", "Neurologist", 6.9, 23.8, 72, "119/70", 58, 1, 2, 210, 15),
        ("Madeline Lee", "Cardiologist", 7.7, 25.5, 72, "134/89", 53, 1, 1, 200, 16),
        ("Leo Walker", "Orthopedic", 5.1, 29.3, 76, "128/84", 42, 0, 0, 190, 18),
        ("Nora Scott", "Neurologist", 7.0, 22.5, 73, "117/73", 59, 2, 1, 215, 17),
        ("Sophia Green", "Cardiologist", 7.9, 24.3, 74, "132/87", 50, 1, 3, 230, 16),
        ("Max Wilson", "Orthopedic", 5.6, 28.9, 79, "133/86", 45, 0, 1, 180, 18),
        ("Zoe Thompson", "Neurologist", 6.8, 23.4, 77, "120/75", 57, 1, 2, 200, 15),
    ],
}

specialists = [
    ("Cardiologist", "Dr. Emily Carter"),
    ("Cardiologist", "Dr. George Wang"),
    ("Orthopedic", "Dr. Sarah Chen"),
    ("Orthopedic", "Dr. James Patel"),
    ("Neurologist", "Dr. Olivia Jones"),
    ("Neurologist", "Dr. Michael Smith"),
]

def main():
    # Check for a user argument in the command line
    if len(sys.argv) != 2:
        print("Usage: python seed.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    if user_id not in [1, 2, 3, 4]:
        print("Usage: <user_id> must be 1, 2, 3, or 4")
        sys.exit(1)

    db.clear_all_tables()

    # Populate the Patient and Specialist tables
    patient_ids = {}
    specialist_ids = {}

    for patient in patients_user[user_id]:
        (
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
            respiratory_rate,
        ) = patient
        patient_id = db.insert_patient(
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
            respiratory_rate,
        )
        patient_ids[patient_name] = (patient_id, specialist_type)

    for specialist in specialists:
        specialist_type, name = specialist
        specialist_id = db.insert_specialist(specialist_type, name)
        if specialist_type not in specialist_ids:
            specialist_ids[specialist_type] = []
        specialist_ids[specialist_type].append((specialist_id, name))

    patients = db.fetch_all_patients()
    specialist = db.fetch_all_specialists()
    scheduling = db.fetch_all_scheduling()

    print(f"Patients: {patients}")
    print()
    print(f"Specialist: {specialist}")
    print()
    print(f"Scheduling: {scheduling}")
    print()

if __name__ == "__main__":
    main()


