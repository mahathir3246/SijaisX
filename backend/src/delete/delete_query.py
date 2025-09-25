from ..db import get_db_connection

def is_subcoord(teacher_ID):
    #Check if a teacher is a substitute coordinator (admin).
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT 1 FROM SubstituteCoordinator WHERE teacher_ID = ?", (teacher_ID,)
        )
        row = cursor.fetchone()
        return row is not None
    finally:
        conn.close()


def delete_assignments_query(assignment_ids, teacher_ID, is_subcoord=False):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Ensure assignment_ids is a list (single or multiple)
        if not isinstance(assignment_ids, (list, tuple)):
            assignment_ids = [assignment_ids]

        if not assignment_ids:
            return {"success": False, "error": "No assignment IDs provided"}

        placeholders = ",".join("?" * len(assignment_ids))

        # Subcoord can delete any; regular teacher can delete only their own assignments
        if is_subcoord:
            cursor.execute(
                f"DELETE FROM Assignment WHERE assignment_ID IN ({placeholders})",
                assignment_ids,
            )
        else:
            cursor.execute(
                f"DELETE FROM Assignment WHERE assignment_ID IN ({placeholders}) AND teacher_ID = ?",
                assignment_ids + [teacher_ID],
            )

        deleted_count = cursor.rowcount
        conn.commit()
        deleted_ids = assignment_ids[:deleted_count]
        return {"success": True, "deleted": deleted_count, "deleted_ids": deleted_ids}

    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        conn.close()
