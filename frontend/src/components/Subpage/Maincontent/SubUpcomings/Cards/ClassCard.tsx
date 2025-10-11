import { Panel } from "rsuite";
import styles from "../../../../../scss_stylings/card.module.scss";
import { SubstitutionFE } from '../subUpcomings';

interface ClassCardProps {
    substitution: SubstitutionFE;
}

const ClassCard = ({ substitution }: ClassCardProps) => (
    <Panel
        bordered
        bodyFill
        className={`${styles.card} ${styles.g0}`} // Always gray (g0)
    >
        <div className={styles.inner}>
            <h5 className={styles.title}>{substitution.school_name}</h5>
            <h5 className={styles.title}>{substitution.teacher_name}</h5>
            <span className={styles.title}>{substitution.date}</span>
            <span className={styles.title}>{substitution.beginning_time} - {substitution.ending_time}</span>
            <span className={styles.title}>{substitution.amount_of_hours}</span>
            <span className={styles.smallertext}>{substitution.subject}</span>
            <span className={styles.smallertext}>{substitution.grade}</span>

            <button className={styles.applyButton}>Apply</button>
        </div>
    </Panel>

    
);

export default ClassCard;