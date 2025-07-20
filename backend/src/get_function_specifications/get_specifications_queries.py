from ..db import get_db_connection

# get a particular teacher's classes within a specific time range
def get_teacher_classes_within_range(teacher_ID, start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       SELECT Class.class_ID, subject, grade, beginning_time, ending_time, room
                       FROM Class
                       JOIN Teaches ON Class.class_ID = Teaches.class_ID
                       WHERE Teaches.teacher_ID = ? 
                            AND Class.beginning_time >= ? 
                            AND Class.ending_time <= ?
                        ''', (teacher_ID, start_date, end_date)) 
        classes = cursor.fetchall()
        if not classes:
            return {"success": False, "error": "No classes found"}
        return {
            "success": True,
            "classes": [
                {
                    "class_ID": row[0],
                    "subject": row[1],
                    "grade": row[2],
                    "beginning_time": row[3],
                    "ending_time": row[4],
                    "room": row[5]
                }
                for row in classes
            ]
        }
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()
