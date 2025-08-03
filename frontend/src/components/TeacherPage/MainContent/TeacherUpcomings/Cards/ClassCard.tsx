import { Panel, TagProps,Tag } from "rsuite";
import styles from "../../../../../scss_stylings/card.module.scss"
import { Job } from "../teacherUpcomings";



type TagColour = NonNullable<TagProps['color']>

const statusColour:  Record<Job['status'], TagColour> = {
    Pending: 'gray',
    Searching: 'cyan',
    Accepted: 'green',
    Revoked: 'red'
}

const statusGradient: Record<Job['status'], string> = {
    Pending: styles.g0,
    Searching: styles.g1,
    Accepted: styles.g2,
    Revoked: styles.g3
}
type ClassCardProps = { job: Job };

export default function ClassCard({ job }: ClassCardProps) {
    return(
        <Panel
            bordered
            bodyFill
            className={`${styles.card} ${statusGradient[job.status]}`}
        >
            <div className={styles.inner}>
                <h5 className={styles.title}>{job.date}</h5>
                <h5 className={styles.title}>{job.beginning_time} - {job.ending_time}</h5>
                <span className={styles.smallertext}>{job.subject}</span>
                <span className={styles.smallertext}>{job.grade}</span>
                <Tag
                    size="sm"
                    className={styles.status}
                    color={statusColour[job.status]}
                >
                    {job.status}
                </Tag>
            </div>
        </Panel>
    )
}
