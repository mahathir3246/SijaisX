from insert_functions import *
from ID_generator import *
from ..get_functions import *

def add_school(school_name):
    school_ID = generate_unique_school_id(school_name)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       INSERT INTO School (school_ID, school_name)
                       VALUES (?, ?)
                       ''', (school_ID, school_name))
        conn.commit()
        return school_ID
    
    except sqlite3.Error as e:
        print("Database error:", e)
        return None
    
    finally:
        if conn:
            conn.close()

def add_teacher(name, phone_number, school_name, email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        result = cursor.execute('''
                                   SELECT school_ID
                                   FROM School
                                   WHERE school_name = ?
                                   ''', (school_name,)).fetchone()
        if result is not None:
            school_ID = result[0]
        else:
            school_ID = add_school(school_name)
            if school_ID is None:
                return False
            
        teacher_ID = generate_unique_teacher_id(name, school_name)
        success = insert_teacher(teacher_ID, name, phone_number, school_name, email, password)
        return success
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False
    
    finally:
        if conn:
            conn.close()

#def add_substitute()