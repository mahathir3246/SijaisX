from ..db import get_db_connection

def cancel_confirmed_application_for_batch(substitute_ID: str, batch_ID: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # sanity checks
        # check if batch exists
        cursor.execute('SELECT batch_ID FROM Batch WHERE batch_ID = ?', (batch_ID,))
        if not cursor.fetchone():
            return {"success": False, "error": "Batch does not exist"}
        # check if sub has applied for batch
        cursor.execute('''
                       SELECT assignment_ID
                       FROM Assignment
                       WHERE substitute_ID = ? AND batch_ID = ?
                       ''', (substitute_ID, batch_ID))
        assignments = cursor.fetchall()
        if not assignments:
            return {"success": False, "error": "No applications found for this batch by the substitute"}
        
        # cancel applications
        for (assignment_ID,) in assignments:
            cursor.execute('''
                           UPDATE Assignment
                           SET substitute_ID = NULL
                           WHERE assignment_ID = ?
                           ''', (assignment_ID,))
            cursor.execute('''
                           DELETE FROM AssignmentVolunteers
                           WHERE assignment_ID = ? AND substitute_ID = ?
                           ''', (assignment_ID, substitute_ID)
                           )
            if cursor.rowcount > 0:
                cursor.execute('SELECT 1 FROM AssignmentVolunteers WHERE assignment_ID = ? LIMIT 1', (assignment_ID,))
                has_other_volunteers = cursor.fetchone() is not None
                new_status = 'pending' if has_other_volunteers else 'searching'
                cursor.execute('UPDATE Assignment SET status = ? WHERE assignment_ID = ?', (new_status, assignment_ID))
        cursor.execute('''
                       DELETE FROM BatchVolunteers
                       WHERE batch_ID = ? AND substitute_ID = ?
                       ''', (batch_ID, substitute_ID))
        conn.commit()
        return {"success": True, "message": f"{len(assignments)} applications canceled for batch {batch_ID}"}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        conn.close()