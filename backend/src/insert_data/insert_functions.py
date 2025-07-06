import sqlite3
from ..db import get_db_connection
from . import ID_generator as idg

def insert_teacher(teacher_ID, name, phone_number, school_name, email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT school_ID FROM School WHERE school_name = ?', (school_name,))
        school = cursor.fetchone()

        if school:
            school_ID = school[0]
        else:
            school_ID = idg.generate_unique_school_id(school_name)
            cursor.execute('INSERT INTO School (school_ID, school_name) VALUES (?, ?)', (school_ID, school_name))

        cursor.execute('''
            INSERT INTO Teacher (teacher_ID, name, phone_number, email, password, school_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (teacher_ID, name, phone_number, email, password, school_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_substitute(substitute_ID, name, phone_number, email, password, experience, highest_education, profile=None, picture=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Substitute (substitute_ID, name, phone_number, email, password, experience, highest_education, profile, picture)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (substitute_ID, name, phone_number, email, password, experience, highest_education, profile, picture))
        conn.commit()
        return True
    
    except sqlite3.Error as e:
        print("Database error:", e)
        return False
    
    finally:
        if conn:
            conn.close()
    
def insert_feedback_to_sub(feedback_ID, date, rating, comments, teacher_ID, substitute_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO FeedbackToSub (feedback_ID, date, rating, comments, teacher_ID, substitute_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (feedback_ID, date, rating, comments, teacher_ID, substitute_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_feedback_to_teacher(feedback_tunnus, date, comments, teacher_ID, substitute_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO FeedbackToTeacher (feedback_tunnus, date, comments, teacher_ID, substitute_ID)
            VALUES (?, ?, ?, ?, ?)
        ''', (feedback_tunnus, date, comments, teacher_ID, substitute_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_availability(availability_ID, substitute_ID, beginning_date = None, ending_date = None, location = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Availability (availability_ID, substitute_ID, beginning_date, ending_date, location)
            VALUES (?, ?, ?, ?, ?)
        ''', (availability_ID, substitute_ID, beginning_date, ending_date, location))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()
    
def insert_substitute_preference(preference_ID, grade, substitute_ID, school_ID, subject = None, location = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO SubstitutePreference (preference_ID, grade, subject, location, substitute_ID, school_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (preference_ID, grade, subject, location, substitute_ID, school_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_class(class_ID, subject, grade, beginning_time, ending_time, room, school_ID, duration = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Class (class_ID, subject, grade, beginning_time, ending_time, duration, room, school_ID)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (class_ID, subject, grade, beginning_time, ending_time, duration, room, school_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_school(school_ID, school_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO School (school_ID, school_name)
            VALUES (?, ?)
        ''', (school_ID, school_name))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_assignment(assignment_ID, date, status, class_ID, teacher_ID, substitute_ID, notes = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Assignment (assignment_ID, date, notes, status, class_ID, teacher_ID, substitute_ID)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (assignment_ID, date, notes, 'seaching', class_ID, teacher_ID, substitute_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_teaches(teacher_ID, class_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Teaches (teacher_ID, class_ID)
            VALUES (?, ?)
        ''', (teacher_ID, class_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_volunteers(substitute_ID, class_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Volunteers (substitute_ID, class_ID)
            VALUES (?, ?)
        ''', (substitute_ID, class_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

def insert_volunteers_in_school(substitute_ID, school_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO VolunteersInSchool (substitute_ID, school_ID)
            VALUES (?, ?)
        ''', (substitute_ID, school_ID))

        conn.commit()
        return True

    except sqlite3.Error as e:
        print("Database error:", e)
        return False

    finally:
        if conn:
            conn.close()

