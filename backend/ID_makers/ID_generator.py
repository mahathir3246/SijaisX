import sqlite3
import re
from src.db import get_db_connection

# This generates unique IDs based on the name and possible school name.
# It ensures that the generated ID is unique by checking against existing IDs in the database.
# It uses slugify and make_unique_id as helpers.
def slugify(text):
    # Simple slugify: remove non-alphanumeric, make lowercase
    return re.sub(r'[^a-zA-Z0-9]', '', text.lower())

def make_unique_id(table: str, column: str, base_id: str) -> str:
    conn = get_db_connection()
    cursor = conn.cursor()
    unique_id = base_id
    counter = 1
    while True:
        cursor.execute(f"SELECT 1 FROM {table} WHERE {column} = ?", (unique_id,))
        if cursor.fetchone() is None:
            conn.close()
            return unique_id
        unique_id = f"{base_id}{counter}"
        counter += 1


def generate_unique_teacher_id(name: str, school_name: str) -> str:
    base = f"t_{slugify(name)}_{slugify(school_name)}"
    return make_unique_id("Teacher", "teacher_ID", base)


def generate_unique_substitute_id(name: str) -> str:
    base = f"sub_{slugify(name)}"
    return make_unique_id("Substitute", "substitute_ID", base)


def generate_unique_feedback_to_sub_id(teacher_id: str, substitute_id: str, date: str) -> str:
    base = (
        "fs_" +
        slugify(teacher_id)[2:4] + "_" +
        slugify(substitute_id)[4:6] + "_" +
        slugify(date)
    )
    return make_unique_id("FeedbackToSub", "feedback_ID", base)


def generate_unique_feedback_to_teacher_id(teacher_id: str, substitute_id: str, date: str) -> str:
    base = (
        "ft_" +
        slugify(teacher_id)[2:4] + "_" +
        slugify(substitute_id)[4:6] + "_" +
        slugify(date)
    )
    return make_unique_id("FeedbackToTeacher", "feedback_tunnus", base)


def generate_unique_availability_id(
    substitute_id: str,
    beginning_date: str | None,
    ending_date: str | None,
    location: str | None
) -> str:
    parts: list[str] = ["av", slugify(substitute_id)[4:6]]
    if beginning_date:
        parts.append("b")
        parts.append(slugify(beginning_date))
    if ending_date:
        parts.append("e")
        parts.append(slugify(ending_date))
    if location:
        parts.append("l")
        parts.append(slugify(location))

    base = "_".join(filter(None, parts))
    return make_unique_id("Availability", "availability_ID", base)

def generate_unique_substitute_preference(
        substitute_id: str,
        grade: str | None,
        subject: str | None,
        school: str | None,
        location: str | None
) -> str :
    parts: list[str] = ["pr", slugify(substitute_id)[4:6]]
    if grade:
        parts.append("gr")
        parts.append(slugify(grade))
    if subject:
        parts.append("sub")
        parts.append(slugify(subject)[0:2])
    if school:
        parts.append("sch")
        parts.append(slugify(school))
    if location:
        parts.append("l")
        parts.append(slugify(location))
        
    base = "_".join(None, parts)
    return make_unique_id("Preference", "preference_ID", base)
