import { Panel, TagProps,Tag } from "rsuite";
import {Job } from "../../../Data/jobsdata";
import styles from "../../../../../scss_stylings/card.module.scss"
import { ClassCardProps } from "../../../Data/jobsdata";



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

const ClassCard = ({ job }: ClassCardProps) => (
    <Panel
        bordered
        bodyFill
        className={`${styles.card} ${statusGradient[job.status]}`}
    >
        <div className={styles.inner}>
            <h5 className={styles.title}>{job.subject} {job.class}</h5>
            <span className={styles.smallertext}>{job.date}</span>
            <span className={styles.smallertext}>Riikka Ruusuvuori</span>
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

export default ClassCard;