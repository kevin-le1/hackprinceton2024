import sqlite3
import uuid

# Define the database filename
db_name = 'hospital_database.sqlite'

# Connect to SQLite (this will create the file if it doesn't exist)
connection = sqlite3.connect(db_name)

# Create a cursor to execute SQL commands
cursor = connection.cursor()


# Create the Patient table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Patient (
        patient_id TEXT PRIMARY KEY,  -- Using TEXT to store UUID as a string
        patient_name TEXT,
        specialist_type TEXT,
        risk_score REAL,
        bmi REAL,
        heart_rate INTEGER,
        blood_pressure TEXT,
        age INTEGER,
        hospitalizations_in_last_year INTEGER,
        previous_surgeries INTEGER,
        cholestoral_level INTEGER,
        respiratory_rate INTEGER
    )
''')

# Create the Specialist table first
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Specialist (
        specialist_id TEXT PRIMARY KEY,  -- Using TEXT to store UUID as a string
        specialist_type TEXT,                 
        specialist_name TEXT
    )
''')

# Create the Scheduling table, referencing both Patient and Specialist tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Scheduling (
        p_key TEXT PRIMARY KEY,  -- Primary key for Scheduling
        patient_id TEXT,         -- Foreign key referencing Patient table
        order_in_queue INTEGER,
        specialist_id TEXT,      -- Foreign key referencing Specialist table
        FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
        FOREIGN KEY (specialist_id) REFERENCES Specialist (specialist_id)
    )
''')

# Commit changes to the database
connection.commit()

# Close the connection
connection.close()

print(f"Database '{db_name}' created successfully with the 'Patient', 'Scheduling', and 'Specialist' tables.")
