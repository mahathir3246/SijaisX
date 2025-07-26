from ..db import get_db_connection

def add_to_assignment_list(substitute_ID, assignment_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # get the school_ID of assignment
        cursor.execute('''
                       SELECT school_ID
                       FROM Teacher
                       JOIN Assignment ON Teacher.teacher_ID = Assignment.teacher_ID
                       WHERE Assignment.assignment_ID = ?
                       ''', (assignment_ID,))
        school_ID = cursor.fetchone()
        if not school_ID:
            return {"success": False, "message": "Assignment not found"}
        
        school_ID = school_ID[0]

        # check if sub is in school list
        cursor.execute('''
                       SELECT *
                       FROM VolunteersInSchool
                       WHERE substitute_ID = ? AND school_ID = ?
                       ''', (substitute_ID, school_ID))
        if not cursor.fetchone():
            return {"success": False, "message": "Substitute not in the school list"}   

        # check if sub already in list
        cursor.execute('''
                       SELECT *
                       FROM AssignmentVolunteers
                       WHERE substitute_ID = ? AND assignment_ID = ?
                       ''', (substitute_ID, assignment_ID))
        if cursor.fetchone():
            return {"success": False, "message": "Substitute already in the assignment list"}
        
        # else add to list
        cursor.execute('''
                       INSERT INTO AssignmentVolunteers (assignment_ID, substitute_ID)
                       VALUES (?, ?)
                       ''', (assignment_ID, substitute_ID))
        conn.commit()
        return {"success": True, "message": "Substitute added to the assignment list"}
    
    except Exception as e:
        return {"success": False, "message": str(e)}
    
    finally:
        cursor.close()
        conn.close()


        