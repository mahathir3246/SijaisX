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


def get_all_assignment_of_teacher(teacher_ID):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       SELECT A.assignment_ID, A.date, A.notes,
                              C.subject, C.grade, C.beginning_time, 
                              C.ending_time, C.room, S.school_name, SUB.name AS substitute_name,
                              A.status
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
        priority = {"searching": 3, "revoked": 2, "pending": 1, "accepted": 0}

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
        priority = {"searching": 3, "revoked": 2, "pending": 1, "accepted": 0}

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
            key = (row["date"], row["school_name"])
            if key not in batches:
                batches[key] = {
                    "date": row["date"],
                    "school_name": row["school_name"],
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
                "teacher_name": row["teacher_name"],
                "teacher_email": row["teacher_email"]
            })
        
        #Convert dict to list for JSON
        result_list = list(batches.values())

        return {"success": True, "batches": result_list}

    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()
