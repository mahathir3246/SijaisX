from ..db import get_db_connection

def volunteer_for_assignment(substitute_ID, assignment_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       SELECT status, class_ID 
                       FROM Assignment 
                       WHERE assignment_ID = ?''', (assignment_ID,))
        result = cursor.fetchone()

        if not result:
            return {"success": False, "error": "Assignment not found"}

        status, class_ID = result

        if status not in ('searching', 'pending'):
            return {"success": False, "error": "Assignment not open for volunteers"}

        # Check if already volunteered
        cursor.execute('''
        SELECT 1 FROM Volunteers 
        WHERE substitute_ID = ? AND class_ID = ?
        ''', (substitute_ID, class_ID))

        if cursor.fetchone():
            return {"success": False, "error": "Already volunteered"}

        # Add to Volunteers table
        cursor.execute('''
            INSERT INTO Volunteers (substitute_ID, class_ID)
            VALUES (?, ?)
        ''', (substitute_ID, class_ID))

        # Check total volunteers for class
        cursor.execute('''
            SELECT COUNT(*) FROM Volunteers
            WHERE class_ID = ?
        ''', (class_ID,))
        total_volunteers = cursor.fetchone()[0]

        # Update assignment status if needed
        new_status = 'pending' if (total_volunteers > 0 and status == 'searching') else 'searching'
        cursor.execute('''
            UPDATE Assignment 
            SET status = ?
            WHERE assignment_ID = ?
        ''', (new_status, assignment_ID))

        conn.commit()
        return {"success": True, "status": new_status}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()

def update_assignment_status(assignment_ID, teacher_ID, new_status, substitute_ID=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if teacher is owner
        cursor.execute('''
                       SELECT teacher_ID 
                       FROM Assignment 
                       WHERE assignment_ID = ?''', (assignment_ID,))
        result = cursor.fetchone()
        if not result:
            return {"success": False, "error": "Assignment not found"}

        assignment_teacher_ID = result[0]
        if assignment_teacher_ID != teacher_ID:
            return {"success": False, "error": "Unauthorized"}

        if new_status == "accepted":
            if not substitute_ID:
                return {"success": False, "error": "No substitute specified"}

            cursor.execute('''
                UPDATE Assignment 
                SET status = ?, substitute_ID = ?
                WHERE assignment_ID = ?
            ''', (new_status, substitute_ID, assignment_ID))

        elif new_status == "revoked":
            cursor.execute('''
                UPDATE Assignment 
                SET status = ?, substitute_ID = NULL
                WHERE assignment_ID = ?
            ''', (new_status, assignment_ID))
        else:
            return {"success": False, "error": "Invalid status change"}

        conn.commit()
        return {"success": True}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()

