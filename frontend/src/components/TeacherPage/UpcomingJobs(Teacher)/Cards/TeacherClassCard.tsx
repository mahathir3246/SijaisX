import { Button, Panel, Badge, TagProps } from 'rsuite';
import "../../TeacherDashboard.scss"
import { Job } from '../TeacherJobsHook';
import { getUserID } from '../../../../functions/auth';
import { delete_assignments } from '../../../../functions/api_calls';

type TagColour = NonNullable<TagProps['color']>;

const statusColour: Record<Job['status'], TagColour> = {
  Pending: 'blue',
  Searching: 'orange',
  Accepted: 'green',
  Revoked: 'red',
};

const statusClass: Record<Job['status'], string> = {
  Pending: 'job-card job-card--pending',
  Searching: 'job-card job-card--searching',
  Accepted: 'job-card job-card--accepted',
  Revoked: 'job-card job-card--revoked',
};

type ClassCardProps = {
  job: Job;
  onClick: () => void;
  assignmentIds?: string[];
};

export default function TeacherClassCard({ job, onClick, assignmentIds }: ClassCardProps) {
  const handleDelete = async (e: React.MouseEvent) => {
    e.stopPropagation();
    if (!assignmentIds?.length) return;

    const teacherID = getUserID();
    if (!teacherID) return;

    if (confirm(`Delete assignment on ${job.date}?`)) {
      await delete_assignments(teacherID, assignmentIds);
    }
  };

  return (
    <Panel bordered bodyFill className={statusClass[job.status]} onClick={onClick}>
      <div className="job-card__header">
        <Badge content={job.status} color={statusColour[job.status]} />
      </div>

      <span className="job-card__date">{job.date}</span>


      <h6>{job.beginning_time} – {job.ending_time}</h6>

      <h6>{job.classCount} classes</h6>

      <div className="job-card__meta">
        <span>Grades: {job.grade}</span>
      </div>

      <h6
        title={job.subject}
        style={{
            width: '100%',
            overflow: 'hidden',
            textOverflow: 'ellipsis',
            whiteSpace: 'nowrap',
        }}
        >
        {job.subject}
        </h6>

      <div className="job-card__applicants">
        <strong>3 Applicants</strong>
      </div>

      {job.status === 'Searching' && (
        <Button appearance="primary" block>
          View Details
        </Button>
      )}
      {job.status === 'Pending' && (
        <Button appearance="primary" block>
          View Details and Applicants
        </Button>
      )}
      {job.status === 'Accepted' && (
        <Button appearance="primary" block>
          View Details and Assignee
        </Button>
      )}

    <Button style={{backgroundColor: '#cb0d0d', color: 'white'}} block onClick={handleDelete}>
        Delete Assignment
    </Button>
    </Panel>
  );
}