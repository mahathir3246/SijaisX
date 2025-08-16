import sqlite3
from collections import defaultdict
import backend.src.get_function_specifications.get_specifications_queries as queries

# --- Mock DB connection ---
def mock_get_db_connection():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn

# Patch in our mock connection function
queries.get_db_connection = mock_get_db_connection

# --- Setup test data ---
def setup_test_db(conn):
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE School (
            school_ID TEXT PRIMARY KEY,
            school_name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE Teacher (
            teacher_ID TEXT PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE Class (
            class_ID TEXT PRIMARY KEY,
            subject TEXT,
            grade TEXT,
            beginning_time TEXT,
            ending_time TEXT,
            duration INTEGER,
            room TEXT,
            school_ID TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE Assignment (
            assignment_ID TEXT PRIMARY KEY,
            date TEXT,
            status TEXT,
            notes TEXT,
            teacher_ID TEXT,
            class_ID TEXT,
            substitute_ID TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE VolunteersInSchool (
            substitute_ID TEXT,
            school_ID TEXT
        )
    """)

    # Insert data
    cursor.execute("INSERT INTO School VALUES ('school_001', 'Test High School')")
    cursor.execute("INSERT INTO School VALUES ('school_002', 'Central Primary')")

    cursor.execute("INSERT INTO Teacher VALUES ('teacher_001', 'Laura Niemi', 'laura@school.fi')")
    cursor.execute("INSERT INTO Teacher VALUES ('teacher_002', 'Mikko Saarinen', 'mikko@school.fi')")

    cursor.execute("""
        INSERT INTO Class VALUES 
        ('class_001', 'Mathematics', '8A', '09:00', '09:45', 45, 'Room 204', 'school_001'),
        ('class_002', 'Physics', '8A', '10:00', '10:45', 45, 'Lab 3', 'school_001'),
        ('class_003', 'Chemistry', '9B', '11:00', '11:45', 45, 'Lab 1', 'school_002')
    """)

    cursor.execute("""
        INSERT INTO Assignment VALUES
        ('assign_001', '2025-08-20', 'searching', 'Focus on algebra revision', 'teacher_001', 'class_001', NULL),
        ('assign_002', '2025-08-20', 'pending', 'Chapter 5 experiments', 'teacher_001', 'class_002', NULL),
        ('assign_003', '2025-08-21', 'searching', 'Organic chemistry intro', 'teacher_002', 'class_003', NULL),
        ('assign_004', '2025-08-22', 'accepted', 'Already taken assignment', 'teacher_002', 'class_003', 'sub_001')
    """)

    # Volunteer-substitute mappings
    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_001', 'school_001')")
    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_001', 'school_002')")
    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_002', 'school_002')")

    conn.commit()

# --- Test runner ---
def run_test(substitute_ID):
    conn = mock_get_db_connection()
    setup_test_db(conn)
    queries.get_db_connection = lambda: conn  # always return this populated DB

    result = queries.get_available_assignments_of_sub_as_batch(substitute_ID)
    #result = queries.get_assignments_accepted_by_sub_as_batch(substitute_ID)
    #replace result with the function needed for testing, possibly change the datatables
    
    print(f"Testing available assignments for substitute_ID={substitute_ID}")
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    run_test("sub_001")  # Should return batches from both schools (assign_001, assign_002, assign_003)
    run_test("sub_002")  # Should return batches only from school_002 (assign_003)
    run_test("sub_fake") # Should return error: No schools found
