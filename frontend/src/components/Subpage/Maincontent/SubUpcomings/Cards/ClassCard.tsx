import { Panel, Button } from "rsuite";
import styles from "../../../../../scss_stylings/card.module.scss";
import { SubstitutionFE, SubstitutionBE } from '../SubstituteJobLists';
import { add_substitute_to_batch, cancel_application_for_batch } from '../../../../../functions/api_calls';
import { getUserID } from '../../../../../functions/auth';
import { useState } from 'react';
import SubstitutionDetailsModal from './SubPopup';

interface ClassCardProps {
    substitution: SubstitutionFE;
    originalData: SubstitutionBE;
    onApply?: () => void;  // Callback to refresh the list after applying
}

const statusGradient = {
    searching: styles.g1, // Blue gradient for available jobs
    pending: styles.g3,
    accepted: styles.g2   // Green gradient for accepted jobs
}

const ClassCard = ({ substitution, originalData, onApply }: ClassCardProps) => {
    const [isApplying, setIsApplying] = useState(false);
    const [showPopup, setShowPopup] = useState(false);
    const [isWithdrawing, setIsWithdrawing] = useState(false);
    
    const handleApply = async (e: React.MouseEvent) => {
        e.stopPropagation();
        const substituteID = getUserID();
        if (!substituteID) {
            alert('You must be logged in to apply');
            return;
        }

        setIsApplying(true);
        try {
            const result = await add_substitute_to_batch(substituteID, substitution.batch_ID);
            
            if (result && result.success) {
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

    const handleWithdraw = async (e: React.MouseEvent) => {
        e.stopPropagation();
        const substituteID = getUserID();
        if (!substituteID) {
            alert('You must be logged in to withdraw');
            return;
        }
        try{
            console.log('withdraw', { substituteID, batchID: substitution.batch_ID });
            const result = await cancel_application_for_batch(substituteID, substitution.batch_ID);
            if (result && result.success) {
                alert('Successfully withdrawn from this job!');

            } else {
                alert(result?.error || 'Failed to withdraw from this job');
            }
        } catch (error) {
            console.error('Error withdrawing from job:', error);
            alert('An error occurred while withdrawing');
        } finally {
            setIsWithdrawing(false);
        }
    };

    return (
        <Panel
            bordered
            bodyFill
            className={`${styles.card} ${statusGradient[substitution.status]}`}
            onClick={() => setShowPopup(true)}
            style={{ cursor: 'pointer' }}
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
                {substitution.status === 'searching' && (
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
                
                {substitution.status === 'pending' && (
                    <Button 
                        appearance="primary" 
                        disabled
                        style={{ marginTop: '10px', width: '100%' }}
                    >
                        Applied
                    </Button>
                )}

                {substitution.status === 'accepted' && (
                    <Button 
                        appearance="primary" 
                        style={{ marginTop: '10px', width: '100%' }}
                        onClick={handleWithdraw}
                        loading={isWithdrawing}
                        disabled={isWithdrawing}
                    >
                        Withdraw Application
                    </Button>
                )}
            </div>
            <SubstitutionDetailsModal
                open={showPopup}
                onClose={() => setShowPopup(false)}
                substitution={originalData}
                status={substitution.status}
            />
        </Panel>
    );
};

export default ClassCard;