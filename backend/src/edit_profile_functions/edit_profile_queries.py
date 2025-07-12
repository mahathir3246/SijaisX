from ..db import get_db_connection

def update_substitute_profile(substitute_ID, name=None, phone_number=None, email=None,
                               password=None, experience=None, highest_education=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Fetch current profile data
        cursor.execute('SELECT name, phone_number, email, password, experience, highest_education FROM Substitute WHERE substitute_ID = ?', (substitute_ID,))
        existing_data = cursor.fetchone()

        if not existing_data:
            return {"success": False, "error": "Substitute not found"}

        # Use current values if new ones are not provided
        name = name if name is not None else existing_data[0]
        phone_number = phone_number if phone_number is not None else existing_data[1]
        email = email if email is not None else existing_data[2]
        password = password if password is not None else existing_data[3]
        experience = experience if experience is not None else existing_data[4]
        highest_education = highest_education if highest_education is not None else existing_data[5]

        # Update with merged data
        cursor.execute('''
            UPDATE Substitute
            SET name = ?, phone_number = ?, email = ?, password = ?, experience = ?, highest_education = ?
            WHERE substitute_ID = ?
        ''', (name, phone_number, email, password, experience, highest_education, substitute_ID))

        conn.commit()
        return {"success": True}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()

def update_teacher_profile(teacher_ID, name=None, phone_number=None, email=None,
                           password=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Fetch current teacher data
        cursor.execute(' SELECT name, phone_number, email, password FROM Teacher WHERE teacher_ID = ?', (teacher_ID,))
        existing_data = cursor.fetchone()
        
        if not existing_data:
            return {"success" : False, "error" : "Teacher not found"}
        
        # Use current values if new ones are not provided
        name = name if name is not None else existing_data[0]
        phone_number = phone_number if phone_number is not None else existing_data[1]
        email = email if email is not None else existing_data[2]
        password = password if password is not None else existing_data[3]

        # Update with merged data
        cursor.execute('''
                    UPDATE Teacher
                    SET name = ?, phone_number = ?, email = ?, password = ?
                    WHERE teacher_ID = ?
                    ''', (name, phone_number, email, password, teacher_ID))
        
        conn.commit()
        return {"success" : True}
    
    except Exception as e:
        return {"success" : False, "error" : str(e)}
    
    finally:
        conn.close()

        
