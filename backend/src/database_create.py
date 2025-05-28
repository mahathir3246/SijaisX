import sqlite3
from .db import get_db_connection

def create_database():
    conn = None
    try: 
        conn = get_db_connection()  # this connects to the database
        cursor = conn.cursor()      # allows interactions with code
        cursor.executescript('''
    CREATE TABLE Teacher (
        teacher_ID TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number TEXT,
        school_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );


    CREATE TABLE SubstituteCoordinator (
        teacher_ID TEXT PRIMARY KEY,
        authority_level INTEGER NOT NULL CHECK (authority_level >= 0 AND authority_level < 10),
        FOREIGN KEY (teacher_ID) REFERENCES Teacher(teacher_ID) ON DELETE CASCADE
    );


    CREATE TABLE Substitute (
        substitute_ID TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        experience INTEGER,
        profile BLOB,
        picture BLOB
    );

    CREATE TABLE FeedbackToSub (
        feedback_ID TEXT PRIMARY KEY,
        date TEXT NOT NULL,
        rating INTEGER,
        comments TEXT,
        teacher_ID TEXT,
        substitute_ID TEXT,
        FOREIGN KEY (teacher_ID) REFERENCES Teacher(teacher_ID),
        FOREIGN KEY (substitute_ID) REFERENCES Substitute(substitute_ID)
    );

    CREATE TABLE FeedbackToTeacher (
        feedback_tunnus TEXT PRIMARY KEY,
        date TEXT NOT NULL,
        comments TEXT NOT NULL,
        teacher_ID TEXT,
        substitute_ID TEXT,
        FOREIGN KEY (teacher_ID) REFERENCES Teacher(teacher_ID),
        FOREIGN KEY (substitute_ID) REFERENCES Substitute(substitute_ID)
    );

    CREATE TABLE Availability (
        availability_ID TEXT PRIMARY KEY,
        beginning_date TEXT,
        ending_date TEXT,
        location TEXT,
        substitute_ID TEXT,
        FOREIGN KEY (substitute_ID) REFERENCES Substitute(substitute_ID)
    );

    CREATE TABLE SubstitutePreference (
        preference_ID TEXT PRIMARY KEY,
        grade TEXT CHECK (grade IN ('Yläkoulu', 'Alakoulu', 'Lukio')),
        subject TEXT,
        school TEXT,
        location TEXT,
        substitute_ID TEXT,
        FOREIGN KEY (substitute_ID) REFERENCES Substitute(substitute_ID)
    );

    CREATE TABLE Class (
        class_ID TEXT PRIMARY KEY,
        subject TEXT NOT NULL,
        grade TEXT NOT NULL,
        beginning_time TEXT NOT NULL,
        ending_time TEXT NOT NULL,
        duration INTEGER,
        room TEXT NOT NULL
    );

    CREATE TABLE Assignment (
        assignment_ID TEXT PRIMARY KEY,
        date TEXT NOT NULL,
        notes TEXT,
        status TEXT NOT NULL CHECK (status IN ('accepted', 'pending', 'searching', 'revoked')), 
        class_ID TEXT,
        teacher_ID TEXT,
        substitute_ID TEXT,
        FOREIGN KEY (class_ID) REFERENCES Class(class_ID),
        FOREIGN KEY (teacher_ID) REFERENCES Teacher(teacher_ID),
        FOREIGN KEY (substitute_ID) REFERENCES Substitute(substitute_ID)
    );

    CREATE TABLE Teaches (
        teacher_ID TEXT,
        class_ID TEXT,
        PRIMARY KEY (teacher_ID, class_ID),
        FOREIGN KEY (teacher_ID) REFERENCES Teacher(teacher_ID),
        FOREIGN KEY (class_ID) REFERENCES Class(class_ID)
    );

    CREATE TABLE Volunteers (
        substitute_ID TEXT,
        class_ID TEXT,
        PRIMARY KEY (substitute_ID, class_ID),
        FOREIGN KEY (substitute_ID) REFERENCES Substitute(substitute_ID),
        FOREIGN KEY (class_ID) REFERENCES Class(class_ID)
    );


                            ''')
    except sqlite3.Error as e:
        print("Error while creating database: ", e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()
