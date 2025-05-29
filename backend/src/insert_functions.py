import sqlite3
from .db import get_db_connection

def insert_teacher(teacher_ID, name, phone_number, school_name, email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        if (phone_number is not None):
            cursor.execute('''
                INSERT INTO Teacher (teacher_ID, name, phone_number, school_name, email, password)
                        VALUES (?, ?, ?, ?, ?, ?)
                        ''', (teacher_ID, name, phone_number, school_name, email, password))
            conn.commit()
        else:
            cursor.execute('''
                INSERT INTO Teacher (teacher_ID, name, school_name, email, password)
                        VALUES (?, ?, ?, ?, ?, ?)
                        ''', (teacher_ID, name, None, school_name, email, password))
            conn.commit()
        return True
    except sqlite3.Error as e:
        print("Database error:", e)
        return False
    