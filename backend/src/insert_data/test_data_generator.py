from .ID_generator import generate_unique_teacher_id, generate_unique_school_id, generate_unique_class_id
from datetime import date, timedelta


teacher1= generate_unique_teacher_id("Tuomas Salovaara", "Jokiniemen Koulu")
teacher2 = generate_unique_teacher_id("Mario Pirinen", "Jokiniemen Koulu")
teacher3= generate_unique_teacher_id("Mika Vanhamäki", "Jokiniemen Koulu")
teacher4= generate_unique_teacher_id("Anna Kaisa", "Jokiniemen Koulu")
teacher5= generate_unique_teacher_id("Katja Halonen", "Jokiniemen Koulu" )



school1= generate_unique_school_id("Jokiniemen Koulu")

print(generate_unique_class_id("Mathematics", "7A", "2025-07-21 08:15", "2025-07-21 09:00", "45", "A101"))
 
#Mika Vanhamäki Schedule
#5 classes a day
timesFive    = (
    ("08:15", "09:00"),
    ("09:00", "09:45"),
    ("10:00", "10:45"),
    ("11:00", "11:45"),
    ("12:30", "13:15"),
)

#4 classes a day
timesFour    = (
    ("08:15", "09:00"),
    ("09:00", "09:45"),
    ("10:00", "10:45"),
    ("11:00", "11:45"),
)

#Mika Vanhamäki Schedule
# Monday
subjectsMonday = ["Mathematics", "Chemistry", "Mathematics", "Chemistry", "Math"]
gradesMonday   = ["7A", "8B", "7B", "9A", "8C"]
roomsMonday    = ["A101", "B204", "A102", "B205", "A103"]

#
# Tuesday
subjectsTuesday = ["Physics", "Physics", "Physics", "Mathematics"]
gradesTuesday   = ["7C",      "8A",      "9B",      "7A"]
roomsTuesday    = ["A104",    "A105",    "Gym1",    "A101"]

#Wednesday 
subjectsWednesday = ["Mathematics", "Mathematics", "Chemistry", "Chemistry", "Physics"]
gradesWednesday   = ["8C",          "7B",          "8B",        "9A",        "8A"]
roomsWednesday    = ["A103",        "A102",        "B204",      "B205",      "A105"]

#Thursday
subjectsThursday = ["Physics", "Physics", "Mathematics", "Mathematics", "Mathematics"]
gradesThursday   = ["9B",      "7C",      "7A",          "8C",          "7B"]
roomsThursday    = ["Gym1",    "A104",    "A101",        "A103",        "A102"]

#Friday
subjectsFriday = ["Physics", "Chemistry", "Chemistry", "Physics"]
gradesFriday   = ["8A",      "8B",        "9A",        "7C"]
roomsFriday    = ["A105",    "B204",      "B205",      "A104"]



Weekday = int  # 0 = Mon ; 1= Tue;  2 = Wed;  3 = Thu; 4 = Fri, 5= Sat, 6 = Sun

def dump_day(
    weekday:   Weekday,
    how_many:  int,
    subjects:  list[str],
    grades:    list[str],
    rooms:     list[str],
    times:     tuple[tuple[str, str], ...],
    school_id: str,
    teacher_id: str
) -> None:
    """
    Print  INSERT-style rows for `how_many` consecutive occurrences
    of the chosen weekday (0 = Monday … 6 = Sunday).
    """
    today = date.today()
    delta = (weekday - today.weekday()) % 7
    current = today + timedelta(days=delta)

    for _ in range(how_many):
        for i in range(len(subjects)):
            start_ts = f"{current} {times[i][0]}"
            end_ts   = f"{current} {times[i][1]}"
            class_id = generate_unique_class_id(
                subjects[i], grades[i], start_ts, end_ts, "45", rooms[i]
            )

            print(
                f'INSERT INTO Class VALUES'
                f'("{class_id}", '
                f'"{subjects[i]}", "{grades[i]}", '
                f'"{start_ts}", "{end_ts}", '
                f'"45", "{rooms[i]}", "{school_id}")'
            )

            print(
                f'INSERT INTO Teaches Values'
                f'("{teacher_id}" , "{class_id}")'

            )
        current += timedelta(days=7)
        print()   



dump_day(0, 20, subjectsMonday, gradesMonday, roomsMonday, timesFive, school1, teacher3)  # Mondays
dump_day(1, 20, subjectsTuesday, gradesTuesday, roomsTuesday, timesFour, school1, teacher3)  # Tuesdays
dump_day(2, 20, subjectsWednesday, gradesWednesday, roomsWednesday, timesFive, school1, teacher3)  # Wednesday
dump_day(3, 20, subjectsThursday, gradesThursday, roomsThursday, timesFive, school1, teacher3)  # Thursday
dump_day(4, 20, subjectsFriday, gradesFriday, roomsFriday, timesFour, school1, teacher3)  # Friday