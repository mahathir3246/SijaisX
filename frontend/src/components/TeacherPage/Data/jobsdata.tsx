// src/data/jobsData.ts
export type Job = {
  class: string;
  subject: string;
  date: string;
  status: 'Pending' | 'Searching' | 'Accepted' | 'Revoked';
};
export interface ClassCardProps {
    job:Job;
}



export const jobs: Job[] = [
  { class: '7C', subject: 'Biology',   date: '27.01.2025 8.15-9.00',  status: 'Pending'   },
  { class: '8B', subject: 'Chemistry', date: '27.01.2025 9.00-9.45',  status: 'Searching' },
  { class: '9A', subject: 'Physics',   date: '27.01.2025 10.15-11.00',status: 'Accepted'  },
  { class: '9C', subject: 'Math',      date: '27.02.2025 11.00-11.45',status: 'Revoked'   },
  { class: '9C', subject: 'Math',      date: '27.02.2025 11.00-11.45',status: 'Revoked'   }
];


export interface Assignment {
  subject: string;
  grade: string;
  start: string;
  end: string;
  duration: string;
  room:string;
  school:string;
  notes:string;
}

type DateKey = `${number}-${number}-${number}`;

export const lessonsBydate: Record <DateKey, Assignment[]> ={
  "2025-06-25": [
    { subject: "Math",      grade: "8C", start: "08:15", end: "09:00", duration: "45 min", room: "A101", school: "Jokiniemen koulu", notes:"" },
    { subject: "Biology",   grade: "9B", start: "09:15", end: "10:00", duration: "45 min", room: "B204", school: "Jokiniemen koulu", notes:"" },
    { subject: "English",   grade: "7A", start: "10:15", end: "11:00", duration: "45 min", room: "C105", school: "Jokiniemen koulu", notes:"" },
    { subject: "Physics",   grade: "9A", start: "12:00", end: "12:45", duration: "45 min", room: "Lab 1", school: "Jokiniemen koulu" , notes:""},
    { subject: "Art",       grade: "8B", start: "13:00", end: "13:45", duration: "45 min", room: "Art-2", school: "Jokiniemen koulu" , notes:""}
  ],

  "2025-06-26": [
    { subject: "History",   grade: "8A", start: "08:15", end: "09:00", duration: "45 min", room: "H201", school: "Ruusu­vuoren koulu", notes:"" },
    { subject: "Chemistry", grade: "9C", start: "09:15", end: "10:00", duration: "45 min", room: "Lab 3", school: "Ruusu­vuoren koulu", notes:"" },
    { subject: "PE",        grade: "7C", start: "10:15", end: "11:00", duration: "45 min", room: "Gym-1", school: "Ruusu­vuoren koulu", notes:"" },
    { subject: "Math",      grade: "9A", start: "12:00", end: "12:45", duration: "45 min", room: "A302", school: "Ruusu­vuoren koulu" , notes:""},
    { subject: "Music",     grade: "7B", start: "13:00", end: "13:45", duration: "45 min", room: "Music-1", school: "Ruusu­vuoren koulu", notes:"" }
  ],

  "2025-06-27": [
    { subject: "Geography", grade: "7A", start: "08:15", end: "09:00", duration: "45 min", room: "G101", school: "Hakunilan koulu", notes:"" },
    { subject: "Finnish",   grade: "8B", start: "09:15", end: "10:00", duration: "45 min", room: "F203", school: "Hakunilan koulu", notes:"" },
    { subject: "IT",        grade: "9B", start: "10:15", end: "11:00", duration: "45 min", room: "ICT-2", school: "Hakunilan koulu", notes:"" },
    { subject: "Physics",   grade: "8C", start: "12:00", end: "12:45", duration: "45 min", room: "Lab 2", school: "Hakunilan koulu" , notes:""},
    { subject: "English",   grade: "9C", start: "13:00", end: "13:45", duration: "45 min", room: "E104", school: "Hakunilan koulu", notes:"" }
  ],

  /* ————————————————— July ————————————————— */
  "2025-07-01": [
    { subject: "Math",      grade: "7B", start: "08:15", end: "09:00", duration: "45 min", room: "M105", school: "Simon­kylän koulu", notes:"" },
    { subject: "Biology",   grade: "8C", start: "09:15", end: "10:00", duration: "45 min", room: "Bio-1", school: "Simon­kylän koulu" , notes:""},
    { subject: "History",   grade: "9A", start: "10:15", end: "11:00", duration: "45 min", room: "H102", school: "Simon­kylän koulu", notes:"" },
    { subject: "Art",       grade: "7A", start: "12:00", end: "12:45", duration: "45 min", room: "Art-3", school: "Simon­kylän koulu" , notes:""},
    { subject: "PE",        grade: "8A", start: "13:00", end: "13:45", duration: "45 min", room: "Gym-2", school: "Simon­kylän koulu", notes:"" }
  ],

  "2025-07-02": [
    { subject: "Chemistry", grade: "8B", start: "08:15", end: "09:00", duration: "45 min", room: "Lab 4", school: "Vesikon koulu", notes:"" },
    { subject: "Finnish",   grade: "9C", start: "09:15", end: "10:00", duration: "45 min", room: "F101", school: "Vesikon koulu", notes:"" },
    { subject: "Music",     grade: "7C", start: "10:15", end: "11:00", duration: "45 min", room: "Music-2", school: "Vesikon koulu", notes:"" },
    { subject: "Geography", grade: "8A", start: "12:00", end: "12:45", duration: "45 min", room: "G202", school: "Vesikon koulu", notes:"" },
    { subject: "English",   grade: "9B", start: "13:00", end: "13:45", duration: "45 min", room: "E205", school: "Vesikon koulu", notes:"" }
  ],

  "2025-07-03": [
    { subject: "Physics",   grade: "9A", start: "08:15", end: "09:00", duration: "45 min", room: "Lab 2", school: "Ilolan koulu", notes:"" },
    { subject: "Math",      grade: "8C", start: "09:15", end: "10:00", duration: "45 min", room: "A205", school: "Ilolan koulu" , notes:""},
    { subject: "Biology",   grade: "7B", start: "10:15", end: "11:00", duration: "45 min", room: "Bio-2", school: "Ilolan koulu", notes:"" },
    { subject: "History",   grade: "8B", start: "12:00", end: "12:45", duration: "45 min", room: "H203", school: "Ilolan koulu", notes:"" },
    { subject: "PE",        grade: "7A", start: "13:00", end: "13:45", duration: "45 min", room: "Gym-1", school: "Ilolan koulu" , notes:""}
  ],

  /* ————————————————— August ————————————————— */
  "2025-08-19": [
    { subject: "English",   grade: "9C", start: "08:15", end: "09:00", duration: "45 min", room: "E101", school: "Hämeenkylän koulu" , notes:""},
    { subject: "Chemistry", grade: "8A", start: "09:15", end: "10:00", duration: "45 min", room: "Lab 1", school: "Hämeenkylän koulu", notes:"" },
    { subject: "Math",      grade: "7C", start: "10:15", end: "11:00", duration: "45 min", room: "A103", school: "Hämeenkylän koulu", notes:"" },
    { subject: "Music",     grade: "8B", start: "12:00", end: "12:45", duration: "45 min", room: "Music-1", school: "Hämeenkylän koulu", notes:"" },
    { subject: "Biology",   grade: "9B", start: "13:00", end: "13:45", duration: "45 min", room: "Bio-1", school: "Hämeenkylän koulu", notes:"" }
  ],

  "2025-08-20": [
    { subject: "Geography", grade: "8C", start: "08:15", end: "09:00", duration: "45 min", room: "G101", school: "Rajatorpan koulu", notes:"" },
    { subject: "Finnish",   grade: "7A", start: "09:15", end: "10:00", duration: "45 min", room: "F202", school: "Rajatorpan koulu", notes:"" },
    { subject: "History",   grade: "9A", start: "10:15", end: "11:00", duration: "45 min", room: "H201", school: "Rajatorpan koulu", notes:"" },
    { subject: "Physics",   grade: "8B", start: "12:00", end: "12:45", duration: "45 min", room: "Lab 3", school: "Rajatorpan koulu", notes:"" },
    { subject: "PE",        grade: "9C", start: "13:00", end: "13:45", duration: "45 min", room: "Gym-2", school: "Rajatorpan koulu", notes:"" }
  ],

  /* ————————————————— September ————————————————— */
  "2025-09-02": [
    { subject: "Math",      grade: "7B", start: "08:15", end: "09:00", duration: "45 min", room: "A106", school: "Lehti­mäen koulu", notes:"" },
    { subject: "English",   grade: "8A", start: "09:15", end: "10:00", duration: "45 min", room: "E202", school: "Lehti­mäen koulu", notes:"" },
    { subject: "Biology",   grade: "9B", start: "10:15", end: "11:00", duration: "45 min", room: "Bio-3", school: "Lehti­mäen koulu", notes:"" },
    { subject: "Chemistry", grade: "8C", start: "12:00", end: "12:45", duration: "45 min", room: "Lab 2", school: "Lehti­mäen koulu", notes:"" },
    { subject: "Art",       grade: "9C", start: "13:00", end: "13:45", duration: "45 min", room: "Art-1", school: "Lehti­mäen koulu", notes:"" }
  ]
}