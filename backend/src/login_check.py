import sqlite3

conn = sqlite3.connect("main_database.db")
cursor = None


# check for password match
def check_password(email, password_attempt):
    try:
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
            SELECT substitute_ID AS user_ID, 'substitute_coordinator' AS role
            FROM SubstituteCoordinate
            WHERE email = ? AND password = ?
            ''', (email, password_attempt))
        result = cursor.fetchone()
        if result:   # if found result among sub_coord, return id as value
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

def get_teacher_info(teacher_ID):
    try:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM Teacher
                       WHERE teacher_ID = ?
                        ''', (teacher_ID,))
        result = cursor.fetchone()
        if result:
            return result
        else: 
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None

def get_substitute_info(substitute_ID):
    try:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT *
                       FROM Substitue
                       WHERE substitute_ID = ?
                        ''', (substitute_ID,))
        result = cursor.fetchone()
        if result:
            return result
        else: 
            return None
        
    except sqlite3.Error as e:
        print('Database error:', e)
        return None