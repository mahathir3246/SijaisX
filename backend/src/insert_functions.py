import sqlite3
from .db import get_db_connection

def insert_teacher(teacher_ID, name, phone_number, school_name, email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Teacher (teacher_ID, name, phone_number, school_name, email, password)
                       VALUES (?, ?, ?, ?, ?, ?)
                       ''', (teacher_ID, name, phone_number, school_name, email, password))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("Database error:", e)
        return False
    