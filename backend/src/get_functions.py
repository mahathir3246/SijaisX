import sqlite3
from .db import get_db_connection

def get_teacher_info(teacher_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM Teacher
                       WHERE teacher_ID = ?
                        ''', (teacher_ID,))
        
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None

def get_substitute_info(substitute_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM Substitute
                       WHERE substitute_ID = ?
                        ''', (substitute_ID,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None

def get_feedback_to_sub(feedback_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM FeedbackToSub
                       WHERE feedback_ID = ?
                        ''', (feedback_ID,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None

def get_feedback_to_teacher(feedback_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM FeedbackToTeacher
                       WHERE feedback_tunnus = ?
                        ''', (feedback_ID,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None
    
def get_availability(availability_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM Availability
                       WHERE availability_ID = ?
                        ''', (availability_ID,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None

def get_single_substitute_preference(preference_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM SubstitutePreference
                       WHERE preference_ID = ?
                        ''', (preference_ID,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None
    
def get_class_info(class_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM Class
                       WHERE class_ID = ?
                        ''', (class_ID,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None
    
def get_school_info(school_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT * 
                       FROM School
                       WHERE school_ID = ?
                       ''', (school_ID, ))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
    except sqlite3.Error as e:
        print('Database error:', e)
        return None

def get_single_assignment(assignment_ID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM Assignment
                       WHERE assignment_ID = ?
                        ''', (assignment_ID,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        else:
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None