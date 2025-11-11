import { useEffect, useState } from 'react';
import styles from '../../../../scss_stylings/card.module.scss';
import AssignmentDetailsModal from './CardPopup';
import { get_all_assignments_of_teacher } from '../../../../functions/api_calls';
import { getUserID } from '../../../../functions/auth';
import ClassCard from './ClassCard';


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
  date: string,
  beginning_time : string,
  ending_time: string,
  grade: string,
  subject: string,
  status: string,
  classCount: number
}


export function cardContentfetcher(assignmentList:Assignment[]): Job[]{
  return assignmentList
  .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime()).
  map(assignment =>{
    const grades = [...new Set(assignment.classes.map(c=> c.grade))].join(",")
    const subjects = [...new Set(assignment.classes.map(c=> c.subject))].join(",")
    const dateObj = new Date(assignment.date);
    const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' }); // Gets "Monday", "Tuesday", etc.
    const formattedDate = dateObj.toLocaleDateString('fi-FI'); // Gets "DD.MM.YYYY"
    const date = `${formattedDate} ${dayOfWeek}`;
    const status = assignment.status.charAt(0).toUpperCase() + assignment.status.slice(1)
    const beginning_time = assignment.classes[0].beginning_time.slice(11,16)
    const ending_time= assignment.classes[assignment.classes.length-1].ending_time.slice(11,16)
    return{
      date:date,
      beginning_time:beginning_time,
      ending_time:ending_time,
      grade: grades,
      subject: subjects,
      status:status,
      classCount: assignment.classes.length
    }

  })
}


const TeacherUpcomings = () => {
    const [jobs, setJobs] = useState<Job[]>([]);
    const [assignments, setAssignments] = useState<Assignment[]>([]);
    const [selectedAssignment, setSelectedAssignment] = useState<Assignment | null>(null);
    const [modalOpen, setModalOpen] = useState(false);
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
          const response = await get_all_assignments_of_teacher(teacherID);
          if (response && response.success) {
            setAssignments(response.assignments);
            setJobs(cardContentfetcher(response.assignments));
          } else {
            setError('Failed to fetch assignments');
          }
        } catch (err) {
          setError('Error');
        } finally {
          setLoading(false);
        }
      };
      fetchAssignments();
    }, []);
  
    const handleCardClick = (job: Job) => {
      const match = assignments.find((assignment) => {
        const dateObj = new Date(assignment.date);
        const formattedDate = dateObj.toLocaleDateString('fi-FI');
        const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
        const date = `${formattedDate} ${dayOfWeek}`;
        const beginning_time = assignment.classes[0].beginning_time.slice(11, 16);
        return date === job.date && beginning_time === job.beginning_time;
      });
      if (match) {
        setSelectedAssignment(match);
        setModalOpen(true);
      }
    };
  
    const handleCloseModal = () => {
      setModalOpen(false);
      setSelectedAssignment(null);
    };
  
    if (loading) return <div>Loading assignments...</div>;
    if (error) return <div>Error: {error}</div>;
  
    return (
        <div className={styles.galleryWrapper}>
          <div className={styles.cardRail}>
            <div className={styles.cardContainer}>
              {jobs.map((job, index) => {
                const assignmentIds =
                  assignments
                    .find((assignment) => {
                      const dateObj = new Date(assignment.date);
                      const formattedDate = dateObj.toLocaleDateString('fi-FI');
                      const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
                      const composed = `${formattedDate} ${dayOfWeek}`;
                      const start = assignment.classes[0].beginning_time.slice(11, 16);
                      return composed === job.date && start === job.beginning_time;
                    })
                    ?.classes.map((c) => c.assignment_ID) ?? [];
    
                return (
                  <div key={`${job.date}-${job.beginning_time}-${job.subject}-${index}`} className={styles.cardWrapper}>
                    <ClassCard
                      job={job}
                      onClick={() => handleCardClick(job)}
                      assignmentIds={assignmentIds}
                    />
                  </div>
                );
              })}
            </div>
          </div>
    
          <AssignmentDetailsModal
            open={modalOpen}
            onClose={handleCloseModal}
            assignment={selectedAssignment}
          />
        </div>
      );
    };
    
    export default TeacherUpcomings;