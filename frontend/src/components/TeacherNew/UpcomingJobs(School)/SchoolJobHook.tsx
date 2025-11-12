import { useEffect, useState } from 'react';
import { get_all_assignments_of_school, get_teacher_info } from '../../../functions/api_calls';
import { getUserID } from '../../../functions/auth';
import { TeacherData } from '../TeacherProfile/TeacherProfile';

export interface SchoolAssignment {
  date: string;
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
    teacher_name: string;
  }[];
  status: 'accepted' | 'pending' | 'searching' | 'revoked';
}

export interface SchoolJob {
  teacher_name: string;
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

export const mapAssignmentsToJobs = (assignments: SchoolAssignment[]): SchoolJob[] =>
  assignments
    .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime())
    .map((assignment) => {
      const teacherName = [...new Set(assignment.classes.map((cls) => cls.teacher_name))].join(', ');
      const grades = [...new Set(assignment.classes.map((c) => c.grade))].join(',');
      const subjects = [...new Set(assignment.classes.map((c) => c.subject))].join(',');
      const substitute = assignment.classes[0]?.substitute_name?.trim() || 'No substitute yet';
      const dateObj = new Date(assignment.date);
      const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
      const formattedDate = dateObj.toLocaleDateString('fi-FI');

      return {
        teacher_name: teacherName,
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

export const matchJobToAssignment = (assignments: SchoolAssignment[], job: SchoolJob) =>
  assignments.find((assignment) => {
    const dateObj = new Date(assignment.date);
    const formattedDate = dateObj.toLocaleDateString('fi-FI');
    const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
    const composed = `${formattedDate} ${dayOfWeek}`;
    const start = assignment.classes[0].beginning_time.slice(11, 16);
    return composed === job.date && start === job.beginning_time;
  }) ?? null;

export function useSchoolJobs() {
  const [assignments, setAssignments] = useState<SchoolAssignment[]>([]);
  const [jobs, setJobs] = useState<SchoolJob[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchAssignments = async () => {
      try {
        const teacherID = getUserID();
        if (!teacherID) {
          setError('No teacher ID found');
          return;
        }

        const teacherInfo = (await get_teacher_info(teacherID)) as TeacherData | null;
        if (!teacherInfo?.school_ID) {
          setError('No school ID found for teacher');
          return;
        }

        const response = await get_all_assignments_of_school(teacherInfo.school_ID);
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