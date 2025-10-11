import { Panel } from "rsuite";
import styles from "../../../../../scss_stylings/card.module.scss";
import { SubstitutionFE } from '../SubstituteJobLists';

interface ClassCardProps {
    substitution: SubstitutionFE;
}

const statusGradient = {
    searching: styles.g1, // Blue gradient for available jobs
    pending: styles.g3,
    accepted: styles.g2   // Green gradient for accepted jobs
}

const ClassCard = ({ substitution }: ClassCardProps) => (
    <Panel
        bordered
        bodyFill
        className={`${styles.card} ${statusGradient[substitution.status]}`} 
    >
        <div className={styles.inner}>
            <h5 className={styles.title}>{substitution.school_name}</h5>
            <h5 className={styles.title}>{substitution.teacher_name}</h5>
            <span className={styles.title}>{substitution.date}</span>
            <span className={styles.title}>{substitution.beginning_time} - {substitution.ending_time}</span>
            <span className={styles.title}>{substitution.amount_of_hours}</span>
            <span className={styles.smallertext}>{substitution.subject}</span>
            <span className={styles.smallertext}>{substitution.grade}</span>
        </div>
    </Panel>

    
);

export default ClassCard;