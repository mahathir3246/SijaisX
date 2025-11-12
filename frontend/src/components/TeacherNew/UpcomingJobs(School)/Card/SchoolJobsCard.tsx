import { SchoolJob } from "../SchoolJobHook";
import { Button, Panel, Badge, TagProps } from 'rsuite';
import "../../TeacherDashboard.scss";
type TagColour = NonNullable<TagProps['color']>;

const statusColour: Record<SchoolJob['status'], TagColour> = {
  Pending: 'blue',
  Searching: 'orange',
  Accepted: 'green',
  Revoked: 'red',
};

const statusClass: Record<SchoolJob['status'], string> = {
  Pending: 'job-card job-card--pending',
  Searching: 'job-card job-card--searching',
  Accepted: 'job-card job-card--accepted',
  Revoked: 'job-card job-card--revoked',
};

type SchoolJobCardProps = {
  job: SchoolJob;
  onClick: () => void;
};

export default function SchoolJobCard({ job, onClick }: SchoolJobCardProps) {
    return (
        <Panel bordered bodyFill className={statusClass[job.status]} onClick={onClick}>
      <div className="job-card__header">
        <Badge content={job.status} color={statusColour[job.status]} />
      </div>

      <span className="job-card__date">{job.date}</span>

      <h6>{job.beginning_time} – {job.ending_time}</h6>

      <h6>{job.classCount} classes</h6>

      <h6>{job.teacher_name}</h6>

      <h6>{job.substitute_name}</h6>
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


      <div className="job-card__meta">
        <span>Grades: {job.grade}</span>
      </div>

      <Button appearance="primary" block>
          View Details
        </Button>

    </Panel>
  );
}