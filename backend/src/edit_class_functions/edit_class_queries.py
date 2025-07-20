from ..db import get_db_connection

def edit_class_info(class_ID, teacher_ID, subject=None, grade=None,
                    beginning_time=None, ending_time=None, duration=None,
                    room=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # check if teacher teaches this class
        cursor.execute('''
                       SELECT class_ID
                       FROM Teaches
                       WHERE teacher_ID = ?
                       ''', (teacher_ID,))
        result = cursor.fetchone()
        if result is None or result[0] != class_ID:
            return {"success": False, "error": "Unauthorized"}
        
        # fetch current class data
        cursor.execute('''
                       SELECT subject, grade, beginning_time, ending_time, duration, room
                       FROM Class
                       WHERE class_ID = ?
                       ''', (class_ID,))
        existing_data = cursor.fetchone()
        if existing_data is None:
            return {"success": False, "error": "Class info not found"}
        subject = existing_data[0]
        grade = existing_data[1]
        beginning_time = existing_data[2]
        ending_time = existing_data[3]
        duration = existing_data[4]
        room = existing_data[5]

        # edit class info
        cursor.execute('''
                       UPDATE Class
                       SET subject = ?, grade = ?, beginning_time = ?, ending_time = ?, duration = ?, room = ?)
                       WHERE class_ID = ?
                       ''', (subject, grade, beginning_time, ending_time, duration, room, class_ID))
        conn.commit()
        return {"success": True}
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()