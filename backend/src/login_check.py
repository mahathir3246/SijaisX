import sqlite3
from .db import get_db_connection


# check for password match
def check_password(email, password_attempt):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT teacher_ID AS user_ID, 'teacher' AS role
            FROM Teacher
            WHERE email = ? AND password = ?
            ''', (email, password_attempt))
        result = cursor.fetchone()
        if result:  # if found result, then return values otherwise we keep going
            return {'user_ID': result[0], 'role': result[1]}
        
        
        cursor.execute('''
            SELECT substitute_ID AS user_ID, 'substitute' AS role
            FROM Substitute
            WHERE email = ? AND password = ?
            ''', (email, password_attempt))
        result = cursor.fetchone()

        if result:   # if found result among subs, return id as value
            return {'user_ID': result[0], 'role': result[1]}
        
        return None  # return nothing if nothing found
    
    except sqlite3.Error as e:
        print("Database error:", e)
        return None
