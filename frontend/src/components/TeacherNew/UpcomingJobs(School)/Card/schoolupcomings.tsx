import { useState } from 'react';
import styles from '../../../../scss_stylings/card.module.scss';
import SchoolAssignmentDetailsModal from '../Details';
import SchoolJobsCard from './SchoolJobsCard';
import { useSchoolJobs, matchJobToAssignment, SchoolJob } from '../SchoolJobHook';

const SchoolUpcomings = () => {
  const { assignments, jobs, loading, error } = useSchoolJobs();
  const [selectedAssignment, setSelectedAssignment] =
    useState<ReturnType<typeof matchJobToAssignment>>(null);
  const [modalOpen, setModalOpen] = useState(false);

  const handleCardClick = (job: SchoolJob) => {
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
          {jobs.map((job, index) => (
            <div
              key={`${job.date}-${job.beginning_time}-${job.subject}-${index}`}
              className={styles.cardWrapper}
            >
              <SchoolJobsCard job={job} onClick={() => handleCardClick(job)} />
            </div>
          ))}
        </div>
      </div>

      <SchoolAssignmentDetailsModal
        open={modalOpen}
        onClose={handleCloseModal}
        assignment={selectedAssignment}
      />
    </div>
  );
};

export default SchoolUpcomings;