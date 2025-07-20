from ..db import get_db_connection

# add subs to volunteersinschool, ie the place which makes it such that certain subs can volunteer for the school
def add_sub_to_volunteers_in_school(teacher_ID, substitute_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if teacher is subcoord
        cursor.execute('''
                        SELECT authority_level FROM SubstituteCoordinator
                        WHERE teacher_ID = ?
                        ''', (teacher_ID,))
        result = cursor.fetchone()

        if result is None or result[0] < 5:
            return {"success": False, "error": "Not authorized to add subs to school volunteer list"}
        
        # Get school_ID
        cursor.execute('''
                       SELECT school_ID FROM Teacher
                       WHERE teacher_ID = ?
                       ''', (teacher_ID))
        school_ID = cursor.fetchone()

        if school_ID is None:
            return {"success": False, "error": "Teacher not found or has no school ID attached"}
        school_ID = school_ID[0]

        # Check if sub is already in list
        cursor. execute('''
                        SELECT 1 from VolunteersInSchool
                        WHERE substitute_ID = ? AND school_ID = ?
                        ''', (substitute_ID, school_ID))
        in_list = cursor.fetchone()
        if in_list:
            return {"success": False, "error": "Substitute is already in substitute list for this school"}
        
        # Add to VolunteersInSchool
        cursor.execute('''
                       INSERT INTO VolunteersInSchool (substitute_ID, school_ID)
                       VALUES (?, ?)
                       ''', (substitute_ID, school_ID))
        conn.commit()
        return {"success": True, "message": "Substitute add to the substitute list for this school"}
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()
