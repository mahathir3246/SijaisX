import sqlite3
import os
from backend.src.assignment_functions.assignment_queries import create_batch_assignment, volunteer_for_batch_assignment
import backend.src.assignment_functions.assignment_queries as queries

DB_PATH = "test_assignments.db"

# --- Ensure clean start ---
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# --- Mock DB connection (file-based) ---
def mock_get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# --- Setup test DB ---
def setup_test_db():
    conn = mock_get_db_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""CREATE TABLE School (school_ID TEXT PRIMARY KEY, school_name TEXT)""")
    cursor.execute("""CREATE TABLE Teacher (teacher_ID TEXT PRIMARY KEY, name TEXT, email TEXT)""")
    cursor.execute("""CREATE TABLE Class (class_ID TEXT PRIMARY KEY, subject TEXT, grade TEXT, beginning_time TEXT, ending_time TEXT, duration INTEGER, room TEXT, school_ID TEXT)""")
    cursor.execute("""CREATE TABLE Assignment (assignment_ID TEXT PRIMARY KEY, date TEXT, status TEXT, notes TEXT, teacher_ID TEXT, class_ID TEXT, substitute_ID TEXT)""")
    cursor.execute("""CREATE TABLE VolunteersInSchool (substitute_ID TEXT, school_ID TEXT)""")
    cursor.execute("""CREATE TABLE AssignmentVolunteers (assignment_ID TEXT, substitute_ID TEXT)""")
    cursor.execute("""CREATE TABLE Teaches (teacher_ID TEXT, class_ID TEXT)""")

    # Insert schools
    cursor.execute("INSERT INTO School VALUES ('school_001', 'Test High School')")
    cursor.execute("INSERT INTO School VALUES ('school_002', 'Central Primary')")

    # Insert teacher
    cursor.execute("INSERT INTO Teacher VALUES ('teacher_001', 'Laura Niemi', 'laura@school.fi')")

    # Insert classes
    cursor.execute("""INSERT INTO Class VALUES 
        ('class_001', 'Mathematics', '8A', '09:00', '09:45', 45, 'Room 204', 'school_001'),
        ('class_002', 'Physics', '8A', '10:00', '10:45', 45, 'Lab 3', 'school_001')""")

    # Map teacher to classes
    cursor.execute("INSERT INTO Teaches VALUES ('teacher_001', 'class_001')")
    cursor.execute("INSERT INTO Teaches VALUES ('teacher_001', 'class_002')")

    # Volunteers
    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_001', 'school_001')")
    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_002', 'school_001')")

    conn.commit()
    conn.close()

# --- Test runner ---
def run_batch_test():
    setup_test_db()
    queries.get_db_connection = mock_get_db_connection  # patch to use our file DB

    # Step 1: Teacher creates batch assignments
    teacher_ID = "teacher_001"
    assignments = [
        {"class_ID": "class_001", "date": "2025-09-15", "notes": "Algebra practice"},
        {"class_ID": "class_002", "date": "2025-09-16", "notes": "Physics experiments"}
    ]
    print("Creating batch assignments...")
    result = create_batch_assignment(teacher_ID, assignments)
    print(result)
    print("-" * 50)

    if not result["success"]:
        return

    # Step 2: Sub volunteer applies to the batch
    substitute_ID = "sub_001"
    assignment_batch = [{"assignment_ID": aid} for aid in result["assignments"]]
    print(f"Substitute {substitute_ID} volunteering for batch...")
    volunteer_result = volunteer_for_batch_assignment(substitute_ID, assignment_batch)
    print(volunteer_result)
    print("-" * 50)

    # Step 3: Another sub volunteer
    substitute_ID2 = "sub_002"
    print(f"Substitute {substitute_ID2} volunteering for batch...")
    volunteer_result2 = volunteer_for_batch_assignment(substitute_ID2, assignment_batch)
    print(volunteer_result2)
    print("-" * 50)

    # Step 4: Show final assignments and volunteers
    conn = mock_get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Assignment")
    assignments_data = cursor.fetchall()
    print("Final assignments table:")
    for a in assignments_data:
        print(dict(a))

    cursor.execute("SELECT * FROM AssignmentVolunteers")
    volunteers_data = cursor.fetchall()
    print("Final AssignmentVolunteers table:")
    for v in volunteers_data:
        print(dict(v))
    conn.close()


if __name__ == "__main__":
    run_batch_test()
