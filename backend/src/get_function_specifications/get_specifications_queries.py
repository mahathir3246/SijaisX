from collections import defaultdict
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
        
        grouped = defaultdict(list)
        for row in classes:
            date_key = str(row[3]).split(" ")[0]  # Extract the date
            grouped[date_key].append({
                "class_ID": row[0],
                "subject": row[1],
                "grade": row[2],
                "beginning_time": row[3],
                "ending_time": row[4],
                "room": row[5]
            })
        
        return {
            "success": True,
            "classes": dict(grouped)
        }
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()


def get_all_assignment_of_teacher(teacher_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       SELECT A.assignment_ID, A.date, A.notes,
                              C.subject, C.grade, C.beginning_time, 
                              C.ending_time, C.room, S.school_name, SUB.name AS substitute_name,
                              A.status, A.batch_ID
                              FROM Assignment AS A
                              JOIN Class AS C ON A.class_ID = C.class_ID
                              JOIN School AS S ON C.school_ID = S.school_ID
                              LEFT JOIN Substitute AS SUB ON A.substitute_ID = SUB.substitute_ID
                              WHERE A.teacher_ID = ?
                              ORDER BY A.date DESC, C.beginning_time
                       ''', (teacher_ID,))
        result = cursor.fetchall()
        if not result:
            return {"success": False, "error": "Assignments not found for teacher"}
        
        # create a result list
        grouped_result = {}
        priority = {"searching": 4, "revoked": 3, "pending": 2, "accepted": 1, "completed": 0}

        for row in result:
            date = row[1]
            if date not in grouped_result: # check if this already added
                grouped_result[date] = {
                    "date": date,
                    "classes": [],
                    "status": "accepted",    # use for priority list overlap
                    "batch_ID": row[11]  # Make sure this line is added

                    
                }

            grouped_result[date]["classes"].append({  # add the info for the date
                "assignment_ID": row[0],
                "notes": row[2],
                "subject": row[3],
                "grade": row[4],
                "beginning_time": row[5],
                "ending_time": row[6],
                "room": row[7],
                "school_name": row[8],
                "substitute_name": row[9]
            })

            current_status = grouped_result[date]["status"]
            new_status = row[10]
            if priority[new_status] > priority[current_status]:
                # this applies if ANY of the assignments has a higher priority
                grouped_result[date]["status"] = new_status  # fix the status based on priority
        
        return {
            "success": True,
            "assignments": list(grouped_result.values())
        }

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()

# get all assignments of a school
def get_all_assignments_of_school(school_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       SELECT A.assignment_ID, A.date, A.notes,
                              C.subject, C.grade, C.beginning_time, 
                              C.ending_time, C.room, S.school_name,
                              SUB.name AS substitute_name, T.name AS teacher_name, 
                              A.status
                              FROM Assignment AS A
                              JOIN Class AS C ON A.class_ID = C.class_ID
                              JOIN School AS S ON C.school_ID = S.school_ID
                              JOIN Teacher AS T ON A.teacher_ID = T.teacher_ID
                              LEFT JOIN Substitute AS SUB ON A.substitute_ID = SUB.substitute_ID
                              WHERE S.school_ID = ?
                              ORDER BY A.date DESC, C.beginning_time
                       ''', (school_ID,))
        result = cursor.fetchall()
        if not result:
            return {"success": False, "error": "Assignments not found for school"}
        
        # create result list
        grouped_result = {}
        priority = {"searching": 4, "revoked": 3, "pending": 2, "accepted": 1, "completed": 0}

        for row in result:
            date = row[1]
            if date not in grouped_result: # check if this already added
                grouped_result[date] = {
                    "date": date,
                    "classes": [],
                    "status": "accepted"    # use for priority list overlap
                }

            grouped_result[date]["classes"].append({  # add the info for the date
                "assignment_ID": row[0],
                "subject": row[3],
                "grade": row[4],
                "beginning_time": row[5],
                "ending_time": row[6],
                "room": row[7],
                "school_name": row[8],
                "substitute_name": row[9],
                "teacher_name": row[10]
            })

            current_status = grouped_result[date]["status"]
            new_status = row[11]
            if priority[new_status] > priority[current_status]:
                # this applies if ANY of the assignments has a higher priority
                grouped_result[date]["status"] = new_status  # fix the status based on priority
        
        return {
            "success": True,
            "assignments": list(grouped_result.values())
        }
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()

# get all assignments available to a sub
def get_all_assignments_available_to_sub(substitute_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # first get all the schools
        cursor.execute('''
                       SELECT school_ID
                       FROM VolunteersInSchool
                       WHERE substitute_ID = ?
                       ''', (substitute_ID,))
        school_IDs= cursor.fetchall()
        if not school_IDs:
            return {"success": False, "error": "No schools found "}
        
        list_of_all_assignments = []
        for (school_ID,) in school_IDs:
            cursor.execute('''
                            SELECT A.assignment_ID, A.date, A.notes,
                              C.subject, C.grade, C.beginning_time, 
                              C.ending_time, C.room, S.school_name,
                              T.name AS teacher_name, A.status
                            FROM Assignment AS A
                            JOIN Class AS C ON A.class_ID = C.class_ID
                            JOIN Teacher AS T ON A.teacher_ID = T.teacher_ID
                            WHERE C.school_ID = ? AND A.status IN ("searching", "pending")
                            ORDER BY A.date DESC
                           ''', (school_ID,))
            result = cursor.fetchall()
            list_of_all_assignments.extend(result)
        if not list_of_all_assignments:
            return {"success": False, "error": "No assignments found"}
        return {
            "success": True,
            "assignments": [dict(row) for row in list_of_all_assignments]
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()

# get all schools a sub is in
def get_all_schools_of_sub(substitute_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # get all the schools
        cursor.execute('''
                       SELECT S.school_ID, S.school_name
                       FROM VolunteersInSchool AS V
                       JOIN School AS S ON V.school_ID = S.school_ID
                       WHERE substitute_ID = ?
                       ''', (substitute_ID,))
        school_rows= cursor.fetchall()
        if not school_rows:
            return {"success": False, "error": "No schools found "}
        return {"success": True,
                "schools": [dict(row) for row in school_rows]}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def get_assignments_accepted_by_sub_as_batch(substitute_ID):
    
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        #get all the assignments of a sub and arrange them based on date and school
        cursor.execute('''
                       SELECT S.school_name, A.date, C.subject, C.grade, 
                       C.beginning_time, C.ending_time, C.duration, C.room,
                       A.notes, T.name AS teacher_name, T.email AS teacher_email
                       FROM Assignment AS A
                       JOIN Teacher AS T ON T.teacher_ID = A.teacher_ID
                       JOIN Class AS C ON C.class_ID = A.class_ID
                       JOIN School AS S ON S.school_ID = C.school_ID
                       WHERE A.status = 'accepted' AND A.substitute_ID = ?
                       ORDER BY A.date ASC, S.school_name, C.beginning_time
                       ''', (substitute_ID, ))
        result = cursor.fetchall()
       
        if not result:
            return {"success": False, "error": "No assignments found"}
        
        batches = {}

        for row in result:
            key = (row["date"], row["school_name"],row["teacher_name"])
            if key not in batches:
                batches[key] = {
                    "date": row["date"],
                    "school_name": row["school_name"],
                    "teacher_name": row["teacher_name"],
                    "teacher_email": row["teacher_email"],
                    "batch_ID": row["batch_ID"] if "batch_ID" in row.keys() else None,
                    "classes": []
                }
            batches[key]["classes"].append({
                "subject": row["subject"],
                "grade": row["grade"],
                "beginning_time": row["beginning_time"],
                "ending_time": row["ending_time"],
                "duration": row["duration"],
                "room": row["room"],
                "notes": row["notes"],
            })
        
        #Convert dict to list for JSON
        result_list = list(batches.values())

        return {"success": True, "batches": result_list}

    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

# get all assignments availble to sub as a batch
def get_available_assignments_of_sub_as_batch(substitute_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # first get all the schools
        cursor.execute('''
                       SELECT school_ID
                       FROM VolunteersInSchool
                       WHERE substitute_ID = ?
                       ''', (substitute_ID,))
        school_IDs = cursor.fetchall()

        if not school_IDs:
            return {"success": False, "error": "No schools found for substitute"}

        # get all assignments available and arrange them based on date and school
        batches = {}
        for (school_ID,) in school_IDs:
            cursor.execute('''
                           SELECT S.school_name, A.date, A.batch_ID, C.subject, C.grade, 
                           C.beginning_time, C.ending_time, C.duration, C.room,
                           A.notes, T.name AS teacher_name, T.email AS teacher_email
                           FROM Assignment AS A
                           JOIN Teacher AS T ON T.teacher_ID = A.teacher_ID
                           JOIN Class AS C ON C.class_ID = A.class_ID
                           JOIN School AS S ON S.school_ID = C.school_ID
                           WHERE C.school_ID = ? 
                            AND A.status IN ('searching', 'pending')
                            AND A.batch_ID NOT IN (
                                SELECT DISTINCT batch_ID
                                FROM BatchVolunteers
                                WHERE substitute_ID = ?
                           )
                           ORDER BY A.date ASC, S.school_name, C.beginning_time
                           ''', (school_ID, substitute_ID))
            result = cursor.fetchall()

            if not result:
                continue # ie no assignments found for this school

            for row in result:
                key = (row["date"], row["school_name"], row["teacher_name"])
                if key not in batches:
                    batches[key] = {
                        "date": row["date"],
                        "school_name": row["school_name"],
                        "teacher_name": row["teacher_name"],
                        "teacher_email": row["teacher_email"],
                        "batch_ID": row["batch_ID"],
                        "classes": []
                    }
                batches[key]["classes"].append({
                    "subject": row["subject"],
                    "grade": row["grade"],
                    "beginning_time": row["beginning_time"],
                    "ending_time": row["ending_time"],
                    "duration": row["duration"],
                    "room": row["room"],
                    "notes": row["notes"],
                })

        # convert dict to list for json
        result_list = list(batches.values())

        if not result_list:
            return {"success": False, "error": "No assignments found"}
        
        return {"success": True, "batches": result_list}
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()

def get_all_applied_batches_of_sub(substitute_ID):
    conn = get_db_connection()
    cursor = conn.cursor()


    try:
        cursor.execute('''
                       SELECT DISTINCT BV.batch_ID, S.school_name, A.date, C.subject, C.grade, 
                           C.beginning_time, C.ending_time, C.duration, C.room,
                           A.notes, T.name AS teacher_name, T.email AS teacher_email
                       FROM BatchVolunteers AS BV
                       JOIN Assignment AS A ON A.batch_ID = BV.batch_ID
                       JOIN Teacher AS T ON T.teacher_ID = A.teacher_ID
                       JOIN Class AS C ON C.class_ID = A.class_ID
                       JOIN School AS S ON S.school_ID = C.school_ID
                       WHERE BV.substitute_ID = ?
                       ORDER BY A.date ASC, S.school_name, C.beginning_time
                       ''', (substitute_ID,))
        result = cursor.fetchall()

        if not result:
            return {"success": False, "error": "No applied batches found"}
        
        batches = {}
        for row in result:
                key = (row["date"], row["school_name"], row["teacher_name"])
                if key not in batches:
                    batches[key] = {
                        "date": row["date"],
                        "school_name": row["school_name"],
                        "teacher_name": row["teacher_name"],
                        "teacher_email": row["teacher_email"],
                        "batch_ID": row["batch_ID"],
                        "classes": []
                    }
                batches[key]["classes"].append({
                    "subject": row["subject"],
                    "grade": row["grade"],
                    "beginning_time": row["beginning_time"],
                    "ending_time": row["ending_time"],
                    "duration": row["duration"],
                    "room": row["room"],
                    "notes": row["notes"],
                })
        # convert dict to list for json
        result_list = list(batches.values())
        
        return {"success": True, "batches": result_list}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()



def get_batch_volunteers(batch_ID: str, requester_ID: str):
    if not batch_ID:
        return {"success": False, "error": "No batch ID provided"}

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT DISTINCT teacher_ID FROM Assignment WHERE batch_ID = ?', (batch_ID,))
        rows = cursor.fetchall()
        if not rows:
            return {"success": False, "error": "No assignments found for this batch"}

        batch_teacher_IDs = [r[0] for r in rows]

        cursor.execute('SELECT 1 FROM SubstituteCoordinator WHERE teacher_ID = ?', (requester_ID,))
        is_subcoord = cursor.fetchone() is not None

        if requester_ID not in batch_teacher_IDs and not is_subcoord:
            return {"success": False, "error": "Access denied"}

        cursor.execute('''
            SELECT Sub.substitute_ID, Sub.name, Sub.email
            FROM BatchVolunteers AS BV
            JOIN Substitute AS Sub ON BV.substitute_ID = Sub.substitute_ID
            WHERE BV.batch_ID = ?
        ''', (batch_ID,))

        result = cursor.fetchall()
        if not result:
            return {"success": False, "error": "No volunteers found for the given batch"}

        return {
            "success": True,
            "volunteers": [
                {"substitute_ID": r[0], "name": r[1], "email": r[2]}
                for r in result
            ]
        }
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def get_batch_of_completed_and_after_current_time(teacher_ID, current_datetime = None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT batch_ID
            FROM Batch
            WHERE teacher_ID = ? 
                AND status = 'completed'
        ''', (teacher_ID,))
        completed_batches = [row['batch_ID'] for row in cursor.fetchall()]
        
        if current_datetime:
            cursor.execute('''
                SELECT b.batch_ID
                FROM Batch AS b
                JOIN Assignment AS a ON b.batch_ID = a.batch_ID
                JOIN Class AS c ON a.class_ID = c.class_ID
                WHERE b.teacher_ID = ?
                    AND b.status != 'completed'
                GROUP BY b.batch_ID
                HAVING MAX(datetime(c.ending_time)) <= datetime(?)
            ''', (teacher_ID, current_datetime))
            by_time_completed = [row['batch_ID'] for row in cursor.fetchall()]
        else:
            by_time_completed = []

        all_batch_ids = list(set(completed_batches + by_time_completed))
        if not all_batch_ids:
            return {"success": True, "batches": []}
        else:
            # fetch the assignment infos for each batch id
            placeholders = ','.join(['?'] * len(all_batch_ids))
            cursor.execute(f'''
                SELECT A.batch_ID, S.school_name, A.date, C.subject, C.grade,
                    C.beginning_time, C.ending_time, C.duration, C.room,
                    A.notes, T.name AS teacher_name, T.email AS teacher_email
                FROM Assignment AS A
                JOIN Teacher AS T ON T.teacher_ID = A.teacher_ID
                JOIN Class AS C ON C.class_ID = A.class_ID
                JOIN School AS S ON S.school_ID = C.school_ID
                WHERE A.batch_ID IN ({placeholders})
                ORDER BY A.date ASC, S.school_name, C.beginning_time
            ''', all_batch_ids)
            
            result = cursor.fetchall()
            batches = {}
            for row in result:
                key = (row["date"], row["school_name"], row["teacher_name"])
                if key not in batches:
                    batches[key] = {
                        "date": row["date"],
                        "school_name": row["school_name"],
                        "teacher_name": row["teacher_name"],
                        "teacher_email": row["teacher_email"],
                        "batch_ID": row["batch_ID"],
                        "classes": []
                    }
                batches[key]["classes"].append({
                    "subject": row["subject"],
                    "grade": row["grade"],
                    "beginning_time": row["beginning_time"],
                    "ending_time": row["ending_time"],
                    "duration": row["duration"],
                    "room": row["room"],
                    "notes": row["notes"],
                })
            return {"success": True, "batches": list(batches.values())}
    
    except Exception as e:
        print("Error in get_batch_of_completed_and_after_current_time", e)
        return {"success": False, "error": str(e)}
    
    finally:
        conn.close()