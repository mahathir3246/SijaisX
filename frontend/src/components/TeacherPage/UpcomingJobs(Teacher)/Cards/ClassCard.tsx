import { Panel, TagProps,Tag } from "rsuite";
import styles from "../../../../scss_stylings/card.module.scss"
import { Job } from "../teacherUpcomings";
import { getUserID } from "../../../../functions/auth";
import { delete_assignments } from "../../../../functions/api_calls";



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
    onClick: () => void;
    assignmentIds?: string[]; };
    

export default function ClassCard({ job, onClick, assignmentIds }: ClassCardProps) {
    const handleDelete = async(e: React.MouseEvent) => {   
        e.stopPropagation(); // Prevent card click  
        if (!assignmentIds || assignmentIds.length === 0) return;
        
        const teacherID = getUserID();
        if (!teacherID) return;
        
        if (confirm(`Delete assignment on ${job.date}?`)) {
            await delete_assignments(teacherID, assignmentIds);
        }
    };
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
                <Tag
                    size="sm"
                    className={styles.delete}
                    onClick={handleDelete}
                >
                    Delete Assignment?
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
