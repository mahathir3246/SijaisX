from ..db import get_db_connection

def cancel_confirmed_application_for_batch(substitute_ID: str, batch_ID: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Sanity checks
        cursor.execute('SELECT 1 FROM Batch WHERE batch_ID = ?', (batch_ID,))
        if not cursor.fetchone():
            return {"success": False, "error": "Batch does not exist"}

        # Get all assignments where this sub is assigned
        cursor.execute('''
            SELECT assignment_ID
            FROM Assignment
            WHERE substitute_ID = ? AND batch_ID = ?
        ''', (substitute_ID, batch_ID))
        assignments = [row[0] for row in cursor.fetchall()]
        if not assignments:
            return {"success": False, "error": "No applications found for this batch by the substitute"}

        # Remove the sub from all assignments at once
        cursor.execute(f'''
            UPDATE Assignment
            SET substitute_ID = NULL
            WHERE assignment_ID IN ({','.join('?' for _ in assignments)})
        ''', assignments)

        # Remove this sub from AssignmentVolunteers in bulk
        cursor.execute(f'''
            DELETE FROM AssignmentVolunteers
            WHERE assignment_ID IN ({','.join('?' for _ in assignments)}) AND substitute_ID = ?
        ''', assignments + [substitute_ID])

        # Update assignment statuses based on remaining volunteers
        cursor.execute(f'''
            SELECT assignment_ID,
                   CASE WHEN EXISTS (
                       SELECT 1
                       FROM AssignmentVolunteers
                       WHERE assignment_ID = a.assignment_ID
                       LIMIT 1
                   ) THEN 'pending' ELSE 'searching' END AS new_status
            FROM Assignment a
            WHERE assignment_ID IN ({','.join('?' for _ in assignments)})
        ''', assignments)

        # Apply the new statuses in bulk
        status_updates = cursor.fetchall()
        if status_updates:
            for assignment_id, new_status in status_updates:
                cursor.execute(
                    "UPDATE Assignment SET status = ? WHERE assignment_ID = ?",
                    (new_status, assignment_id)
                )
        
        # Remove the sub from BatchVolunteers
        cursor.execute('DELETE FROM BatchVolunteers WHERE batch_ID = ? AND substitute_ID = ?', (batch_ID, substitute_ID))

        cursor.execute(
            'SELECT 1 FROM BatchVolunteers WHERE batch_ID = ? LIMIT 1',
            (batch_ID,)
        )
        new_batch_status = 'pending' if cursor.fetchone() else 'searching'

        cursor.execute(
            'UPDATE Batch SET status = ? WHERE batch_ID = ?',
            (new_batch_status, batch_ID)
        )

        conn.commit()
        return {"success": True, "message": f"{len(assignments)} applications canceled for batch {batch_ID}"}

    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        conn.close()