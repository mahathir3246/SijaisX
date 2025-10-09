from ..db import get_db_connection
from ..insert_data.add_data import add_assignment
from ..insert_data.ID_generator import generate_unique_batch_id

def volunteer_for_assignment(substitute_ID, assignment_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Get assignment info (status + school_ID through class_ID)
        cursor.execute('''
            SELECT A.status, C.school_ID
            FROM Assignment A
            JOIN Class C ON A.class_ID = C.class_ID
            WHERE A.assignment_ID = ?
        ''', (assignment_ID,))
        result = cursor.fetchone()

        if not result:
            return {"success": False, "error": "Assignment not found"}

        status, school_ID = result

        if status not in ('searching', 'pending'):
            return {"success": False, "error": "Assignment not open for volunteers"}

        # Check if sub is allowed to volunteer at this school
        cursor.execute('''
            SELECT 1 FROM VolunteersInSchool
            WHERE substitute_ID = ? AND school_ID = ?
        ''', (substitute_ID, school_ID))
        if not cursor.fetchone():
            return {"success": False, "error": "Substitute not approved for this school"}

        # Check if already volunteered for this assignment
        cursor.execute('''
            SELECT 1 FROM AssignmentVolunteers
            WHERE assignment_ID = ? AND substitute_ID = ?
        ''', (assignment_ID, substitute_ID))
        if cursor.fetchone():
            return {"success": False, "error": "Already volunteered"}

        # Add to volunteers list
        cursor.execute('''
            INSERT INTO AssignmentVolunteers (assignment_ID, substitute_ID)
            VALUES (?, ?)
        ''', (assignment_ID, substitute_ID))

        # Count volunteers
        cursor.execute('''
            SELECT COUNT(*) FROM AssignmentVolunteers
            WHERE assignment_ID = ?
        ''', (assignment_ID,))
        total_volunteers = cursor.fetchone()[0]

        # Update status if needed
        new_status = 'pending' if (total_volunteers > 0 and status == 'searching') else status
        if new_status != status:
            cursor.execute('''
                UPDATE Assignment SET status = ?
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
        # Validate teacher ownership
        cursor.execute('''
            SELECT teacher_ID FROM Assignment WHERE assignment_ID = ?
        ''', (assignment_ID,))
        result = cursor.fetchone()
        if not result:
            return {"success": False, "error": "Assignment not found"}

        assignment_teacher_ID = result[0]
        if assignment_teacher_ID != teacher_ID:
            return {"success": False, "error": "Unauthorized"}

        if new_status == "accepted":
            if not substitute_ID:
                return {"success": False, "error": "No substitute specified"}

            # Confirm sub actually applied
            cursor.execute('''
                SELECT 1 FROM AssignmentVolunteers
                WHERE assignment_ID = ? AND substitute_ID = ?
            ''', (assignment_ID, substitute_ID))
            if not cursor.fetchone():
                return {"success": False, "error": "Substitute did not apply for this assignment"}

            # Accept sub
            cursor.execute('''
                UPDATE Assignment
                SET status = ?, substitute_ID = ?
                WHERE assignment_ID = ?
            ''', (new_status, substitute_ID, assignment_ID))

            # Clear volunteer list after accepting
            cursor.execute('''
                DELETE FROM AssignmentVolunteers
                WHERE assignment_ID = ?
            ''', (assignment_ID,))

        elif new_status == "revoked":
            # Revoke previously accepted sub
            cursor.execute('''
                UPDATE Assignment
                SET status = ?, substitute_ID = NULL
                WHERE assignment_ID = ?
            ''', (new_status, assignment_ID))

            # Clear volunteer list after revoking
            cursor.execute('''
                DELETE FROM AssignmentVolunteers
                WHERE assignment_ID = ?
            ''', (assignment_ID,))

        else:
            return {"success": False, "error": "Invalid status change"}

        conn.commit()
        return {"success": True}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()



# Get assignment volunteers
def get_assignment_volunteers(assignment_ID):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT Substitute.substitute_ID, Substitute.name, Substitute.email
            FROM AssignmentVolunteers
            JOIN Substitute ON AssignmentVolunteers.substitute_ID = Substitute.substitute_ID
            WHERE AssignmentVolunteers.assignment_ID = ?
        ''', (assignment_ID,))
        
        volunteers = cursor.fetchall()
        return {
            "success": True,
            "volunteers": [
                {"substitute_ID": row[0], "name": row[1], "email": row[2]}
                for row in volunteers
            ]
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()



def create_batch_assignment(teacher_ID, assignment_data):
    
    conn = get_db_connection()
    cursor = conn.cursor()
    created_assignments = []
    batch_ID = generate_unique_batch_id(teacher_ID)
    try:
        cursor.execute('''
                        INSERT INTO Batch (batch_ID, teacher_ID)
                        VALUES (?, ?)
                        ''', (batch_ID, teacher_ID)
                        )
        # iterate through each assignment
        for assignment in assignment_data:
            class_ID = assignment.get("class_ID")
            date = assignment.get("date")
            notes = assignment.get("notes", "")
            status = assignment.get("status", "searching")

            # check if the teacher is ok
            cursor.execute('''
                           SELECT 1 
                           FROM Teaches
                           WHERE teacher_ID = ? AND class_ID = ?
                           ''', (teacher_ID, class_ID))
            
            if cursor.fetchone() is None:
                conn.rollback()
                return {"success": False, "error": f"Unauthorized for class {class_ID}"}
            
            # insert assignment
            result = add_assignment(
                date=date,
                status=status,
                class_ID=class_ID,
                teacher_ID=teacher_ID,
                substitute_ID=None,
                notes=notes,
                batch_ID=batch_ID,
                conn=conn  # pass shared connection
            )
            if not result["success"]:
                conn.rollback()
                return {"success": False, "error": result.get("error", f"Failed to add assignment for class {class_ID}")}
            created_assignments.append(result["assignment_ID"])
        

        conn.commit()
        return {"success": True, "message": f"{len(assignment_data)} assignments created.",
                "batch_ID": batch_ID,
                "assignments": created_assignments}
        
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    
    finally: 
        conn.close()

def volunteer_for_batch_assignment(substitute_ID, batch_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 1. Check if the batch exists and get its assignments and status
        cursor.execute('''
            SELECT status
            FROM Batch
            WHERE batch_ID = ?
        ''', (batch_ID,))
        batch_info = cursor.fetchone()
        if not batch_info:
            return {"success": False, "error": f"Batch {batch_ID} not found"}
        
        batch_status = batch_info[0]
        if batch_status not in ('searching', 'pending'):
            return {"success": False, "error": f"Batch {batch_ID} is not open for volunteers"}

        # 2. Check if substitute already volunteered for this batch
        cursor.execute('''
            SELECT 1
            FROM BatchVolunteers
            WHERE batch_ID = ? AND substitute_ID = ?
        ''', (batch_ID, substitute_ID))
        if cursor.fetchone():
            return {"success": False, "error": "Already volunteered for this batch"}

        # 3. Check that substitute is allowed for all schools in this batch
        cursor.execute('''
            SELECT DISTINCT C.school_ID
            FROM Assignment AS A
            JOIN Class AS C ON A.class_ID = C.class_ID
            WHERE A.batch_ID = ?
        ''', (batch_ID,))
        schools = [row[0] for row in cursor.fetchall()]

        for school_ID in schools:
            cursor.execute('''
                SELECT 1
                FROM VolunteersInSchool
                WHERE substitute_ID = ? AND school_ID = ?
            ''', (substitute_ID, school_ID))
            if not cursor.fetchone():
                return {"success": False, "error": f"Substitute not approved for school {school_ID}"}

        # 4. Add substitute to BatchVolunteers
        cursor.execute('''
            INSERT INTO BatchVolunteers (batch_ID, substitute_ID)
            VALUES (?, ?)
        ''', (batch_ID, substitute_ID))

        # 5. Update status of all assignments in this batch if needed
        cursor.execute('''
            UPDATE Assignment
            SET status = 'pending'
            WHERE batch_ID = ? AND status = 'searching'
        ''', (batch_ID,))

        conn.commit()
        return {"success": True, "message": "Applied to batch successfully", "batch_ID": batch_ID}

    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}

    finally:
        conn.close()