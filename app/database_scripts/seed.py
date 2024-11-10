import sqlite3
import sys
import app.database_scripts.database as db
import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL", "")
if DATABASE_URL == "":
    raise Exception("no database url configured")

"""
1: Zaeem
2: Carter
3: Kevin
4: Eugene
"""
patients_user = {
    1: [
        ("Alice Smith", "Cardiologist", 0.85, 24.5, 72, "120/80", 52, 1, 2, 190, 16),
        ("Bob Johnson", "Hematologist", 0.52, 29.4, 78, "130/85", 45, 0, 1, 180, 18),
        ("Clara Davis", "Immunologist", 0.71, 22.3, 65, "118/75", 60, 2, 3, 200, 15),
        ("David Martinez", "Cardiologist", 0.92, 30.1, 80, "140/90", 55, 3, 1, 230, 20),
        ("Eva Green", "Hematologist", 0.48, 27.6, 74, "125/82", 40, 0, 0, 170, 16),
        ("Frank Moore", "Immunologist", 0.65, 23.8, 68, "117/78", 58, 1, 2, 210, 17),
        ("Grace Lee", "Cardiologist", 0.69, 26.1, 75, "122/82", 47, 1, 1, 180, 16),
        ("Henry Kim", "Hematologist", 0.73, 28.0, 70, "128/84", 49, 0, 0, 190, 19),
        ("Ivy Wilson", "Immunologist", 0.62, 25.7, 66, "119/76", 62, 2, 1, 185, 15),
        ("Jack Brown", "Cardiologist", 0.80, 24.0, 73, "121/79", 54, 1, 3, 200, 17),
        ("Karen Adams", "Hematologist", 0.59, 27.5, 77, "126/83", 42, 0, 1, 175, 18),
        ("Liam Scott", "Immunologist", 0.75, 23.9, 64, "115/72", 59, 2, 2, 195, 15),
    ],
    2: [
        ("Samantha White", "Cardiologist", 0.79, 25.2, 69, "121/77", 48, 1, 2, 180, 14),
        ("John Miller", "Hematologist", 0.58, 28.3, 75, "132/86", 46, 0, 1, 190, 17),
        ("Lena Harris", "Immunologist", 0.74, 23.1, 72, "120/78", 63, 2, 3, 210, 16),
        ("Tom Walker", "Cardiologist", 0.83, 26.0, 70, "135/88", 53, 3, 1, 240, 19),
        ("Olivia Brown", "Hematologist", 0.61, 27.9, 78, "125/84", 41, 0, 0, 200, 18),
        ("Mason Clark", "Immunologist", 0.68, 24.4, 66, "119/74", 57, 1, 2, 220, 15),
        ("Rachel King", "Cardiologist", 0.72, 25.3, 72, "124/79", 49, 1, 1, 210, 16),
        ("Ryan Scott", "Hematologist", 0.55, 29.0, 77, "128/82", 44, 0, 0, 180, 19),
        ("Isabella Lewis", "Immunologist", 0.69, 22.7, 68, "118/76", 58, 2, 1, 200, 14),
        ("Daniel Adams", "Cardiologist", 0.81, 26.5, 74, "130/85", 51, 1, 3, 230, 17),
        ("Lucas Miller", "Hematologist", 0.56, 28.1, 76, "133/84", 45, 0, 1, 175, 18),
        ("Evelyn Green", "Immunologist", 0.66, 23.2, 70, "117/73", 60, 1, 2, 215, 16),
    ],
    3: [
        ("Emma Collins", "Cardiologist", 0.80, 24.9, 71, "125/80", 50, 1, 2, 190, 17),
        ("Michael Harris", "Hematologist", 0.54, 29.2, 79, "128/84", 43, 0, 1, 200, 18),
        ("Sophia Young", "Immunologist", 0.73, 22.8, 70, "119/77", 61, 2, 3, 205, 16),
        (
            "Benjamin Wilson",
            "Cardiologist",
            0.82,
            26.3,
            72,
            "132/88",
            55,
            3,
            1,
            220,
            19,
        ),
        ("Lily Cooper", "Hematologist", 0.60, 28.4, 74, "130/87", 47, 0, 0, 195, 17),
        ("Aiden Scott", "Immunologist", 0.76, 23.5, 69, "120/75", 59, 1, 2, 210, 15),
        ("Maya Turner", "Cardiologist", 0.78, 25.6, 73, "134/90", 54, 1, 1, 200, 16),
        ("James Thompson", "Hematologist", 0.59, 27.1, 76, "128/83", 42, 0, 0, 185, 18),
        ("Charlotte Lee", "Immunologist", 0.64, 23.0, 72, "117/72", 60, 2, 1, 215, 16),
        ("Oliver King", "Cardiologist", 0.84, 25.0, 70, "136/91", 52, 1, 3, 225, 18),
        ("Mia Turner", "Hematologist", 0.57, 28.6, 77, "133/85", 46, 0, 1, 180, 17),
        ("William White", "Immunologist", 0.67, 22.9, 68, "119/74", 58, 1, 2, 210, 16),
    ],
    4: [
        (
            "Charlotte Harris",
            "Cardiologist",
            0.76,
            24.8,
            69,
            "127/79",
            51,
            1,
            2,
            185,
            17,
        ),
        ("Henry Carter", "Hematologist", 0.53, 28.7, 73, "130/82", 44, 0, 1, 195, 18),
        ("Lily Moore", "Immunologist", 0.72, 22.4, 75, "120/76", 59, 2, 3, 210, 16),
        ("Samuel Gray", "Cardiologist", 0.86, 25.4, 70, "135/86", 52, 3, 1, 220, 18),
        ("Ella Perez", "Hematologist", 0.63, 27.3, 74, "125/81", 46, 0, 0, 180, 17),
        ("Mason Bell", "Immunologist", 0.69, 23.8, 72, "119/70", 58, 1, 2, 210, 15),
        ("Madeline Lee", "Cardiologist", 0.77, 25.5, 72, "134/89", 53, 1, 1, 200, 16),
        ("Leo Walker", "Hematologist", 0.51, 29.3, 76, "128/84", 42, 0, 0, 190, 18),
        ("Nora Scott", "Immunologist", 0.70, 22.5, 73, "117/73", 59, 2, 1, 215, 17),
        ("Sophia Green", "Cardiologist", 0.79, 24.3, 74, "132/87", 50, 1, 3, 230, 16),
        ("Max Wilson", "Hematologist", 0.56, 28.9, 79, "133/86", 45, 0, 1, 180, 18),
        ("Zoe Thompson", "Immunologist", 0.68, 23.4, 77, "120/75", 57, 1, 2, 200, 15),
    ],
}

specialists = [
    ("Cardiologist", "Dr. Emily Carter"),
    ("Cardiologist", "Dr. George Wang"),
    ("Hematologist", "Dr. Sarah Chen"),
    ("Hematologist", "Dr. James Patel"),
    ("Immunologist", "Dr. Olivia Jones"),
    ("Immunologist", "Dr. Michael Smith"),
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
