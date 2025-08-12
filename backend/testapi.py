import sqlite3
import backend.src.get_function_specifications.get_specifications_queries as queries

# Mock DB connection
def mock_get_db_connection():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn

# Replace the get_db_connection used in the target module
queries.get_db_connection = mock_get_db_connection

def setup_test_db(conn):
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE School (
            school_ID TEXT PRIMARY KEY,
            school_name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE VolunteersInSchool (
            substitute_ID TEXT,
            school_ID TEXT
        )
    ''')

    # Insert test data
    cursor.execute("INSERT INTO School VALUES ('school_001', 'Test High School')")
    cursor.execute("INSERT INTO School VALUES ('school_002', 'Central Primary')")

    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_001', 'school_001')")
    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_001', 'school_002')")
    cursor.execute("INSERT INTO VolunteersInSchool VALUES ('sub_002', 'school_002')")

    conn.commit()

def run_test(substitute_ID):
    # Get fresh test DB for each run
    conn = mock_get_db_connection()
    setup_test_db(conn)

    # Patch our mock DB connection to always return the same prepared DB
    queries.get_db_connection = lambda: conn

    result = queries.get_all_schools_of_sub(substitute_ID)
    print(f"Testing with substitute_ID={substitute_ID}")
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    run_test("sub_001")  # Should return 2 schools
    run_test("sub_002")  # Should return 1 school
    run_test("sub_fake") # Should return "No schools found"
