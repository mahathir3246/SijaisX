import { Panel, TagProps,Tag } from "rsuite";
import styles from "../../../../scss_stylings/card.module.scss"
import { Job } from "../teacherUpcomings";



type TagColour = NonNullable<TagProps['color']>

const statusColour:  Record<Job['status'], TagColour> = {
    Pending: 'blue',
    Searching: 'orange',
    Accepted: 'green',
    Revoked: 'red'
}

const statusGradient: Record<Job['status'], string> = {
    Pending: styles.g0,
    Searching: styles.g1,
    Accepted: styles.g2,
    Revoked: styles.g3
}
type ClassCardProps = { 
    job: Job;
    onClick: () => void };

export default function ClassCard({ job, onClick }: ClassCardProps) {
    return(
        <Panel
            bordered
            bodyFill
            className={`${styles.card} ${statusGradient[job.status]}`}
            onClick={onClick}
        >
            <div className={styles.inner}>
                <h5 className={styles.title}>{job.date}</h5>
                <h5 className={styles.title}>{job.beginning_time} - {job.ending_time}</h5>
                <span></span>
                <span className={styles.smallertext}>{job.subject}</span>
                <span className={styles.smallertext}>{job.grade}</span>
                <span className={styles.smallertext}>
                    {job.classCount} classes
                </span>
                <Tag
                    size="sm"
                    className={styles.status}
                    color={statusColour[job.status]}
                >
                    {job.status}
                </Tag>
                {job.status === 'Pending' && (
                    <div style={{ 
                        marginTop: '8px', 
                        fontSize: '1rem', 
                        fontStyle: 'italic'
                    }}>
                        Click to see applicants
                    </div>
                )}
            </div>
        </Panel>
    )
}
