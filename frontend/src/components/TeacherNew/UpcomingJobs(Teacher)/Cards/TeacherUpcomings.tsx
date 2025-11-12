import { useState } from 'react';
import styles from '../../../../scss_stylings/card.module.scss';
import AssignmentDetailsModal from '../Details';
import ClassCard from './ClassCard';
import { useTeacherJobs, matchJobToAssignment, Job } from '../TeacherJobsHook';

const TeacherUpcomings = () => {
  const { assignments, jobs, loading, error } = useTeacherJobs();
  const [selectedAssignment, setSelectedAssignment] = useState<typeof assignments[number] | null>(null);
  const [modalOpen, setModalOpen] = useState(false);

  const handleCardClick = (job: Job) => {
    const match = matchJobToAssignment(assignments, job);
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
              matchJobToAssignment(assignments, job)?.classes.map((c) => c.assignment_ID) ?? [];

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