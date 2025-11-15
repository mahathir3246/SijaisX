import { useState } from 'react';
import AssignmentDetailsModal from '../Details';
import TeacherClassCard from './TeacherClassCard';
import { useTeacherJobs, matchJobToAssignment, Job } from '../TeacherJobsHook';

const TeacherCardGallery = () => {
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
    <div className="galleryWrapper">
      <div className="cardRail">
        <div className="cardContainer">
          {jobs.map((job, index) => {
            const assignmentIds =
              matchJobToAssignment(assignments, job)?.classes.map((c) => c.assignment_ID) ?? [];

            return (
              <div key={`${job.date}-${job.beginning_time}-${job.subject}-${index}`} className="cardWrapper">
                <TeacherClassCard
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

export default TeacherCardGallery;