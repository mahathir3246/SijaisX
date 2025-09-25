from ..db import get_db_connection

def delete_assignments_query(assignment_ids):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Ensure assignment_ids is a list (can be one or many)
        if not isinstance(assignment_ids, (list, tuple)):
            assignment_ids = [assignment_ids]

        if not assignment_ids:
            return {"success": False, "error": "No assignment IDs provided"}

        # Build placeholders (?, ?, ?)
        placeholders = ",".join("?" * len(assignment_ids))

        cursor.execute(
            f'''
            DELETE FROM Assignment
            WHERE assignment_ID IN ({placeholders})
            ''',
            assignment_ids
        )

        deleted_count = cursor.rowcount
        conn.commit()

        return {"success": True, "deleted": deleted_count}

    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}

    finally:
        conn.close()
