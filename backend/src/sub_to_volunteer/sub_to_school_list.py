from ..db import get_db_connection

def add_to_school_list(teacher_ID, substitute_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # check if teacher is subcoord
        cursor.execute('''
                       SELECT authority_level
                       FROM SubstituteCoordinator
                       WHERE teacher_ID = ?
                       ''', (teacher_ID,))
        authority_level = cursor.fetchone()
        if not authority_level or authority_level[0] < 5:
            return {"success": False, "message": "You do not have permission to add substitutes to the school list."}
        
        # check the school of the teacher
        cursor.execute('''
                       SELECT school_ID
                       FROM Teacher
                       WHERE teacher_ID = ?
                       ''', (teacher_ID,))
        school_ID = cursor.fetchone()
        if not school_ID:
            return {"success": False, "message": "Teacher not found"}
        
        school_ID = school_ID[0]

        # check if sub already in list
        cursor.execute('''
                       SELECT *
                       FROM VolunteersInSchool
                       WHERE substitute_ID = ? AND school_ID = ?
                       ''', (substitute_ID, school_ID))
        if cursor.fetchone():
            return {"success": False, "message": "Substitute already in the school list."}
        
        # else add sub to school list
        cursor.execute('''
                       INSERT INTO VolunteersInSchool (substitute_ID, school_ID)
                       VALUES (?, ?)
                       ''', (substitute_ID, school_ID))
        conn.commit()
        return {"success": True, "message": "Substitute added to the school list."}
    except Exception as e:
        return {"success": False, "message": str(e)}
    finally:
        cursor.close()
        conn.close()

