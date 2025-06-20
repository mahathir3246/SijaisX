// src/data/jobsData.ts
export type Job = {
  class: string;
  subject: string;
  date: string;
  status: 'Pending' | 'Searching' | 'Accepted' | 'Revoked';
};

export const jobs: Job[] = [
  { class: '7C', subject: 'Biology',   date: '27.01.2025 8.15-9.00',  status: 'Pending'   },
  { class: '8B', subject: 'Chemistry', date: '27.01.2025 9.00-9.45',  status: 'Searching' },
  { class: '9A', subject: 'Physics',   date: '27.01.2025 10.15-11.00',status: 'Accepted'  },
  { class: '9C', subject: 'Math',      date: '27.02.2025 11.00-11.45',status: 'Revoked'   },
  { class: '9C', subject: 'Math',      date: '27.02.2025 11.00-11.45',status: 'Revoked'   }
];
