import { useEffect, useState } from 'react';
import { get_all_assignments_of_teacher } from '../../../functions/api_calls';
import { getUserID } from '../../../functions/auth';

export interface Assignment {
  date: string;
  batch_ID?: string;
  classes: {
    assignment_ID: string;
    subject: string;
    grade: string;
    notes?: string;
    beginning_time: string;
    ending_time: string;
    room: string;
    school_name: string;
    substitute_name: string | null;
  }[];
  status: 'accepted' | 'pending' | 'searching' | 'revoked';
}

export interface Job {
  date: string;
  beginning_time: string;
  ending_time: string;
  grade: string;
  subject: string;
  status: string;
  classCount: number;
  substitute_name: string;
}

const statusTokens: Record<string, string> = {
  searching: 'searching',
  pending: 'pending',
  accepted: 'accepted',
  revoked: 'revoked',
};

export const getStatusColor = (status: string) =>
  statusTokens[status.toLowerCase()] ?? 'pending';

export const mapAssignmentsToJobs = (assignments: Assignment[]): Job[] =>
  assignments
    .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime())
    .map((assignment) => {
      const grades = [...new Set(assignment.classes.map((c) => c.grade))].join(',');
      const subjects = [...new Set(assignment.classes.map((c) => c.subject))].join(',');
      const dateObj = new Date(assignment.date);
      const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
      const formattedDate = dateObj.toLocaleDateString('fi-FI');
      const substitute = assignment.classes[0]?.substitute_name?.trim() || '-';

      return {
        date: `${formattedDate} ${dayOfWeek}`,
        beginning_time: assignment.classes[0].beginning_time.slice(11, 16),
        ending_time: assignment.classes[assignment.classes.length - 1].ending_time.slice(11, 16),
        grade: grades,
        subject: subjects,
        status: assignment.status.charAt(0).toUpperCase() + assignment.status.slice(1),
        classCount: assignment.classes.length,
        substitute_name: substitute,
      };
    });

export const matchJobToAssignment = (assignments: Assignment[], job: Job) =>
  assignments.find((assignment) => {
    const dateObj = new Date(assignment.date);
    const formattedDate = dateObj.toLocaleDateString('fi-FI');
    const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
    const composed = `${formattedDate} ${dayOfWeek}`;
    const start = assignment.classes[0].beginning_time.slice(11, 16);
    return composed === job.date && start === job.beginning_time;
  }) ?? null;

export function useTeacherJobs() {
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchAssignments = async () => {
      try {
        const teacherId = getUserID();
        if (!teacherId) {
          setError('No teacher ID found');
          return;
        }

        const response = await get_all_assignments_of_teacher(teacherId);
        if (response?.success) {
          setAssignments(response.assignments);
          setJobs(mapAssignmentsToJobs(response.assignments));
        } else {
          setError('Failed to fetch assignments');
        }
      } catch (err) {
        console.error(err);
        setError('Error');
      } finally {
        setLoading(false);
      }
    };

    fetchAssignments();
  }, []);

  return { assignments, jobs, loading, error };
}