import { Panel, Button } from "rsuite";
import styles from "../../../../../scss_stylings/card.module.scss";
import { SubstitutionFE } from '../SubstituteJobLists';
import { add_substitute_to_batch } from '../../../../../functions/api_calls';
import { getUserID } from '../../../../../functions/auth';
import { useState } from 'react';

interface ClassCardProps {
    substitution: SubstitutionFE;
    onApply?: () => void;  // Callback to refresh the list after applying
}

const statusGradient = {
    searching: styles.g1, // Blue gradient for available jobs
    pending: styles.g3,
    accepted: styles.g2   // Green gradient for accepted jobs
}

const ClassCard = ({ substitution, onApply }: ClassCardProps) => {
    const [isApplying, setIsApplying] = useState(false);
    const [applied, setApplied] = useState(false);
    
    const handleApply = async () => {
        const substituteID = getUserID();
        if (!substituteID) {
            alert('You must be logged in to apply');
            return;
        }

        setIsApplying(true);
        try {
            const result = await add_substitute_to_batch(substituteID, substitution.batch_ID);
            
            if (result && result.success) {
                setApplied(true);
                alert('Successfully applied for this job!');
                if (onApply) {
                    onApply();  // Refresh the list
                }
            } else {
                alert(result?.error || 'Failed to apply for this job');
            }
        } catch (error) {
            console.error('Error applying for job:', error);
            alert('An error occurred while applying');
        } finally {
            setIsApplying(false);
        }
    };

    return (
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
                
                {/* Only show Apply button for jobs with 'searching' status */}
                {substitution.status === 'searching' && !applied && (
                    <Button 
                        appearance="primary" 
                        onClick={handleApply}
                        loading={isApplying}
                        disabled={isApplying}
                        style={{ marginTop: '10px', width: '100%' }}
                    >
                        {isApplying ? 'Applying...' : 'Apply'}
                    </Button>
                )}
                
                {applied && (
                    <Button 
                        appearance="ghost" 
                        disabled
                        style={{ marginTop: '10px', width: '100%' }}
                    >
                        Applied ✓
                    </Button>
                )}
            </div>
        </Panel>
    );
};

export default ClassCard;