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

def add_substitute(name, phone_number, email, password, experience, profile = None, picture = None):
    substitute_ID = generate_unique_substitute_id(name)
    try:
        return insert_substitute(substitute_ID, name, phone_number, email, password, experience, profile, picture)
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False

def add_feedback_to_sub(date, rating, comments, teacher_ID, substitute_ID):
    feedback_ID = generate_unique_feedback_to_sub_id(teacher_ID, substitute_ID, date)
    try:
        return insert_feedback_to_sub(feedback_ID, date, rating, comments, teacher_ID, substitute_ID)
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False

def add_feedback_to_teacher(date, comments, teacher_ID, substitute_ID):
    feedback_tunnus = generate_unique_feedback_to_teacher_id(teacher_ID, substitute_ID, date)
    try:        
        return insert_feedback_to_teacher(feedback_tunnus, date, comments, teacher_ID, substitute_ID)
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False

def add_availability(substitute_ID, beginning_date, ending_date, location):
    availability_ID = generate_unique_availability_id(substitute_ID, beginning_date, ending_date, location)
    try:
        return insert_availability(availability_ID, substitute_ID, beginning_date, ending_date, location)
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False
    
def add_substitute_preference(grade, substitute_ID, school_name, subject, location):
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
        
        preference_ID = generate_unique_substitute_preference(substitute_ID, grade, subject, school_ID, location)
        return insert_substitute_preference(preference_ID, grade, substitute_ID, school_ID, subject, location)
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False
    
def add_class(subject, grade, beginning_time, ending_time, room, duration, school_name):
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
        class_ID = generate_unique_class_id(subject, grade, beginning_time, ending_time, duration, room)
        return insert_class(class_ID, subject, grade, beginning_time, ending_time, room, school_ID, duration)
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False
    
def add_assignment(date, status, class_ID, teacher_ID, substitute_ID, notes):
    assignment_ID = generate_unique_assignment_id(date, notes, status, class_ID, teacher_ID, substitute_ID)
    try:
        return insert_assignment(assignment_ID, date, status, class_ID, teacher_ID, substitute_ID, notes)
    
    except sqlite3.Error as e:
        print("Database error: ", e)
        return False
    

